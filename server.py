from python_banyan.banyan_base import BanyanBase
from gui.server.interface import ServerInterface
from classes.user_server import UserServer
from classes.item import Item
from threading import Thread
from time import sleep
import msgpack
import zmq


class Server(BanyanBase):
    def __init__(self, ):
        super(Server, self).__init__(process_name="Server")
        
        self.set_subscriber_topic('server')
                
        self.interface = ServerInterface()
        self.interface.set_send_message_function(function=self.publish_payload)
        self.interface.bind("<Destroy>", self.on_destroy)
        self.interface.after(5, self.get_message)   
        self.interface.mainloop()
        
    def get_message(self):
        try:
            data = self.subscriber.recv_multipart(zmq.NOBLOCK)
            self.incoming_message_processing(data[0].decode(), msgpack.unpackb(data[1]))
            sleep(.001)
            self.interface.after(1, self.get_message)

        except zmq.error.Again:
            sleep(.001)
            self.interface.after(1, self.get_message)
                        
    def incoming_message_processing(self, topic, payload):
        if payload['message'] == 'user_creation':
            new_user = UserServer(name=payload['user'])
            
            # Assign ID to newly created user
            payload['message'] = 'assign_id'
            payload['user_id'] = new_user.get_id()
            self.publish_payload(payload, 'user')
            
            # display on GUI
            self.interface.window.insert(message=f"{payload['user']} is ready...")
            
        if payload['message'] == 'sell':
            item_name = payload['name']
            price = payload['price']
                
            seller = self.match_user(payload['user_id'])
                
            Item(name=item_name, price=price, seller=seller)
            payload['message'] = 'new_item'
            self.publish_payload(payload, 'user')

            # display on GUI
            self.interface.window.insert(message=f"Selling: {item_name} PHP {price: ,.2f} [{payload['user']}]")
            
        if payload['message'] == 'bid':
            # assigning variables
            bidder_name = payload['user']
            bidder = self.match_user(payload['user_id'])
            item_name = payload['name']
            item = self.match_item(item_name=item_name)
            bid_amount = payload['bid_amount']
            
            if not item.get_highest_bidder():
                if bid_amount > item.get_price():
                    item.add_bidder(bidder=bidder, bid_amount=payload['bid_amount'])

                    payload['message'] = 'bidders' 
                    self.publish_payload(payload, 'user')
                    
                    # display on GUI
                    self.interface.window.insert(message=f"Bidding: {item_name} PHP {bid_amount: ,.2f} [{bidder_name}]")
                
            if item.get_highest_bidder():
                highest_bidder, highest_bid = item.get_highest_bidder()
                
                if bid_amount > highest_bid:    
                    item.add_bidder(bidder=bidder, bid_amount=payload['bid_amount'])

                    payload['message'] = 'bidders' 
                    self.publish_payload(payload, 'user')
                    
                    # display on GUI
                    self.interface.window.insert(message=f"Bidding: {item_name} PHP {bid_amount: ,.2f} [{bidder_name}]")
                    
                

            
        if payload['message'] == 'timer':
            self.interface.window.insert(message='-- WINNERS:')
            
            payload = {}
            payload['message'] = 'winner'
            payload['items'] = []
            payload['winners'] = []
            payload['bids'] = []
            
            for data in Item.ITEMS_LIST:
                if data.get_highest_bidder() == None:
                    continue
                
                item = data.get_name()
                winner, bid = data.get_highest_bidder()
                payload['items'].append(item)
                payload['winners'].append(winner)
                payload['bids'].append(bid)
                
                message = f'{item}: {winner} - PHP{bid: ,.2f} ** WINNER **'
                self.interface.window.insert(message)
        
            self.publish_payload(payload=payload, topic='user')
                                
    def on_destroy(self, event):
        if event.widget != self.interface:
            return
        
        self.clean_up()
          
    def match_user(self, id):
        for user in UserServer.USERS_LIST:
            if id == user.get_id():
                return user  
            
    def match_item(self, item_name):
        for item in Item.ITEMS_LIST:
            if item_name == item.get_name():
                return item
        
        
if __name__ == '__main__':
    Server()
    