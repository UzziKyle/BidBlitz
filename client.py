from python_banyan.banyan_base import BanyanBase
from gui.client.interface import ClientInterface
from gui.client.dialogs.username_input_dialog import UsernameInputDialog
from gui.client.dialogs.selling_input_dialog import SellingInputDialog
from gui.client.dialogs.bidding_input_dialog import BiddingInputDialog
from classes.user_client import UserClient
from threading import Thread
from time import sleep
import msgpack
import zmq


class Client(BanyanBase):
    def __init__(self, ):
        super(Client, self).__init__(process_name="Client")
        
        self.set_subscriber_topic('user')
        
        self.user: UserClient | None = None
        
        self.items_sold = []
        self.items_for_bidding = []
        
        self.interface = ClientInterface()
        self.username_input_dialog = UsernameInputDialog()
        self.username_input_dialog.accept_button.configure(command=lambda: self.set_user())
        
        self.interface.bind("<Destroy>", self.on_destroy)
        
        self.interface.utility.set_sell_button_command(function=self.sell)
        self.interface.utility.set_bid_button_command(function=self.bid)
        
        self.interface.utility.set_send_message_function(function=self.publish_payload)
                
        self.interface.withdraw()
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
        if payload['message'] == 'timer':
            timer = Thread(target=self.interface.utility.start_countdown, args=(payload['temp'], ))
            
            timer.start()
            
        if payload['message'] == 'assign_id':
            if self.user:
                if self.user.get_id() == None:
                    self.user.set_id(payload['user_id'])
                
        if payload['message'] == 'new_item':
            if payload['user_id'] != self.user.get_id():
                self.items_for_bidding.append({'item': payload['name'], 'bid_amount': 0})
                self.interface.bidding_window.insert(message=f"{payload['name']} [{payload['user']}]")
                # add to bidding 
                
            else: 
                self.items_sold.append({'item': payload['name'], 'bid_amount': 0})
                self.interface.selling_window.insert(payload=payload)
                
        if payload['message'] == 'bidders':
            self.interface.bidder_window.insert(message=f"{payload['name']}: {payload['user']} bidded PHP{payload['bid_amount']: 0.2f}")
            
        if payload['message'] == 'winner':
            self.interface.bidder_window.insert(message=f"{payload['name']}: {payload['winner']} - PHP{payload['bid_amount']: 0.2f} ** WINNER **")
            
                                            
    def set_user(self):
        # assign user to this client
        self.user = UserClient(name=self.username_input_dialog.name_entry.get())
        
        self.username_input_dialog.destroy()
        
        self.interface.deiconify()
        self.interface.title(f'CLIENT: {self.user}')
        
        # add user to server
        self.publish_payload(payload={'message': 'user_creation', 'user': self.user.get_name()}, topic='server')
        
    def sell(self):
        SellingInputDialog(title="SELLING...", payload={'message': 'sell', 'name': '', 'price': 0, 'user': self.user.get_name(), 'user_id': self.user.get_id()}, topic='server', send_message=self.publish_payload) 
        
    def bid(self):
        try:
            item_idx = self.interface.bidding_window.get_item_index()
            
            item = self.items_for_bidding[item_idx]
            
            BiddingInputDialog(title='BIDDING', payload={'message': 'bid', 'name': item['item'], 'bid_amount': 0, 'user': self.user.get_name(), 'user_id': self.user.get_id()}, topic='server', send_message=self.publish_payload)
            
        except:
            pass
            
    def on_destroy(self, event):
        if event.widget != self.interface:
            return
        
        self.clean_up()
            
        
if __name__ == '__main__':
    Client()
    