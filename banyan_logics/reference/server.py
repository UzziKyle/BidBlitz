import sys
from python_banyan.banyan_base import BanyanBase
from classes.user_server import UserServer
from classes.item import Item

class EchoServer(BanyanBase):
    """A simple Banyan echo server"""
    
    def __init__(self):
        super(EchoServer, self).__init__(process_name='Server')
        
        # subscribe to receive 'echo' messages from the client
        self.set_subscriber_topic('echo')     
        
        try:
            self.receive_loop()
        
        except KeyboardInterrupt:
            self.clean_up()
            sys.exit(0)
            
    def incoming_message_processing(self, topic, payload):
        """
        Process incoming messages from client
        :param topic: message topic
        :param payload: message payload
        :return:
        """

        if payload['message'] == 'user_creation':
            user_name = payload['user']
            new_user = UserServer(name=payload['user'])
            print(f"Added user {user_name}..")
            print(UserServer.USERS_LIST)
            payload['message'] = 'assign_id'
            payload['user_id'] = new_user.get_id()
            self.publish_payload(payload, 'user')
                    
        if payload['message'] == 'sell':
            item = payload['name']
            price = payload['price']
                
            seller = self.match_user(payload['user_id'])
                
            Item(name=item, price=price, seller=seller)
            payload['message'] = 'new_item'
            self.publish_payload(payload, 'user')

            print(UserServer.USERS_LIST)
            print(Item.ITEMS_LIST)
            
        if payload['message'] == 'bid':
            bidder = self.match_user(payload['user_id'])
            item = self.match_item(payload['name'])
            print(bidder, item)
            print(type(bidder), type(item))
            
            item.add_bidder(bidder=bidder, bid_amount=payload['bid_amount'])
            print(item.get_bidders())
            payload['message'] = 'bidders'
            
            self.publish_payload(payload, 'user')
            # print(item.get_highest_bidder())
                 
    def match_user(self, id):
        for user in UserServer.USERS_LIST:
            if id == user.get_id():
                return user  
            
    def match_item(self, item_name):
        for item in Item.ITEMS_LIST:
            if item_name == item.get_name():
                return item
        

def echo_server():
    EchoServer()
        
if __name__ == '__main__':
    echo_server()
