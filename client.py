from python_banyan.banyan_base import BanyanBase
from gui.client.interface import ClientInterface
from gui.client.dialogs.username_input_dialog import UsernameInputDialog
from gui.client.dialogs.selling_input_dialog import SellingInputDialog
from gui.client.dialogs.bidding_input_dialog import BiddingInputDialog
from gui.client.dialogs.winner_dialog import WinnerDialog
from classes.user_client import UserClient
from threading import Thread
from time import sleep
import argparse
import signal
import msgpack
import zmq


class Client(BanyanBase):
    def __init__(self, **kwargs):
        """
        kwargs will contain the following keys:
        
        :param back_plane_ip_address:  banyan_base back_planeIP address
        :param subscriber_port: banyan_base back plane subscriber port
        :param publisher_port: banyan_base backplane
        :param client_name: name of bidder
        :param process_name: Component identifier
        :param loop_time: receive loop sleep time
        """
        
        super(Client, self).__init__(back_plane_ip_address=kwargs['back_plane_ip_address'],
                                            subscriber_port=kwargs['subscriber_port'],
                                            publisher_port=kwargs['publisher_port'],
                                            process_name=kwargs['process_name'],
                                            loop_time=kwargs['loop_time'])
        
        self.set_subscriber_topic('user')
        
        self.user: UserClient | None = None
        
        self.items_sold = []
        self.items_for_bidding = []
        
        self.interface = ClientInterface()
        
        self.interface.bind("<Destroy>", self.on_destroy)
        
        self.interface.utility.set_sell_button_command(function=self.sell)
        self.interface.utility.set_bid_button_command(function=self.bid)
        
        self.interface.utility.set_send_message_function(function=self.publish_payload)
                
        self.username_input_dialog = UsernameInputDialog()
        self.username_input_dialog.accept_button.configure(command=lambda: self.set_user())
        
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
                self.interface.bidding_window.insert(message=f"{payload['name']} [{payload['user']}] - PHP {payload['price']: ,.2f}")
                
            else: 
                self.items_sold.append({'item': payload['name'], 'bid_amount': 0})
                
                item = payload['name']
                price = payload['price']
                message = f'{item} PHP {price: ,.2f}'
                
                self.interface.selling_window.insert(message=message)
                
        if payload['message'] == 'bidders':
            self.interface.bidder_window.insert(message=f"{payload['name']}: {payload['user']} bidded PHP{payload['bid_amount']: ,.2f}")
            
        if payload['message'] == 'winner':
            WinnerDialog(payload=payload)
                                                  
    def set_user(self):
        # assign user to this client
        self.user = UserClient(name=self.username_input_dialog.name_entry.get())
        
        self.username_input_dialog.destroy()
        
        self.interface.deiconify()
        self.interface.title(f'CLIENT: {self.user}')
        
        # add user to server
        self.publish_payload(payload={'message': 'user_creation', 'user': self.user.get_name()}, topic='server')
        
    def sell(self) -> None:
        SellingInputDialog(title="SELLING...", payload={'message': 'sell', 'name': '', 'price': 0, 'user': self.user.get_name(), 'user_id': self.user.get_id()}, topic='server', send_message=self.publish_payload) 
        
    def bid(self) -> None:
        try:
            item_idx = self.interface.bidding_window.get_item_index()
            
            item = self.items_for_bidding[item_idx]
            
            BiddingInputDialog(title='BIDDING', payload={'message': 'bid', 'name': item['item'], 'bid_amount': 0, 'user': self.user.get_name(), 'user_id': self.user.get_id()}, topic='server', send_message=self.publish_payload)
            
        except:
            pass        
            
    def on_destroy(self, event) -> None:
        if event.widget != self.interface:
            return
        
        self.clean_up()
        

def cmd_client():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-b", dest="back_plane_ip_address", default='None', 
                        help='None or IP address used by Back Plane')    

    parser.add_argument("-n", dest="process_name", default='Client', 
                        help='Set process name in banner')
    parser.add_argument("-p", dest="publisher_port", default='43124', 
                        help='Publisher IP port')
    parser.add_argument("-s", dest="subscriber_port", default='43125', 
                        help='Subscriber IP port')
    parser.add_argument("-t", dest="loop_time", default='.1', 
                        help='Event Loop Timer in seconds')    
    
    args = parser.parse_args()
    
    if args.back_plane_ip_address == 'None':
        args.back_plane_ip_address = None
        
    kw_options= {'back_plane_ip_address': args.back_plane_ip_address,
                    'user': args.user,
                    'publisher_port': args.publisher_port,
                    'subscriber_port': args.subscriber_port,
                    'process_name': args.process_name,
                    'loop_time': float(args.loop_time)}

    Client(**kw_options)
              
def signal_handler(sig, frame):
    raise KeyboardInterrupt

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
    

if __name__ == '__main__':
    cmd_client()