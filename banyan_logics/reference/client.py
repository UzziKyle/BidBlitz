import sys
import argparse
import signal
from python_banyan.banyan_base import BanyanBase
from classes.user_client import UserClient
from threading import Thread
# from classes.item import Item


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
        
        # initialize the parent
        super(Client, self).__init__(back_plane_ip_address=kwargs['back_plane_ip_address'],
                                            subscriber_port=kwargs['subscriber_port'],
                                            publisher_port=kwargs['publisher_port'],
                                            process_name=kwargs['process_name'],
                                            loop_time=kwargs['loop_time'])
        
        self.set_subscriber_topic('user')
        
        self.user = UserClient(name=kwargs['user'])
        print(self.user.get_name())
        # self.sell = kwargs['sell']
        
        self.publish_payload({'message': 'user_creation', 'user': self.user.get_name()}, 'echo')

        self.items_sold = []
        self.items_for_bidding = []
        
        
        try: 
            self.receive_loop()
            
        except KeyboardInterrupt:
            self.clean_up()
            sys.exit(0)
            
    
    def incoming_message_processing(self, topic, payload):
        
        if payload['message'] == 'assign_id':
            if self.user.get_id() == None:
                self.user.set_id(payload['user_id'])
                print(f"User ID: {self.user.get_id()}")
                
                Thread(target=self.prompt).start()
        
        if payload['message'] == 'new_item':
            print('new item received')
            if payload['user_id'] != self.user.get_id():
                self.items_for_bidding.append({'item': payload['name'], 'bid_amount': 0})
                # add to bidding 
                
        if payload['message'] == 'bidders':
            print(f'{payload['name']}: {payload['user']} bidded ${payload['bid_amount']: 0.2f}')
        
    def prompt(self):
        while True:
            print("Enter [1] to sell, [2] to bid, [3] to exit: ")
            response = input()
            
            if response == '1':
                item_name = input("Enter item to sell: ")
                item_price = float(input("Enter the item's price: "))
                
                
                self.publish_payload({'message': 'sell', 'name': item_name, 'price': item_price, 'user': self.user.get_name(), 'user_id': self.user.get_id()}, 'echo')
                print(f"Selling {item_name}.")
                
                self.items_sold.append({'name': item_name, 'price': item_price})
                print(f"ID:{self.user.get_id()}")
                for item in self.items_sold:
                    print(item['name'])
                
            if response == '2':
                print("Items for bidding")
                for idx, item in enumerate(self.items_for_bidding):
                    print(f"{idx + 1}. {item['item']}")
                    
                index = int(input("Enter the corresponding number: "))
                chosen_item = self.items_for_bidding[index - 1]
                bid_amount = float(input("Enter the bidding amount: "))
                chosen_item['bid_amount'] = bid_amount
                
                self.publish_payload({'message': 'bid', 'name': chosen_item['item'], 'bid_amount': bid_amount, 'user': self.user.get_name(), 'user_id': self.user.get_id()}, 'echo')
        
            if response == '3':
                break     
            

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
    parser.add_argument("-u", dest="user", default='', 
                        help='User')
    
    args = parser.parse_args()
    
    if args.back_plane_ip_address == 'None':
        args.back_plane_ip_address = None
        
    if not args.user:
        args.user = input("Enter the name of the client: ")
        
    kw_options= {'back_plane_ip_address': args.back_plane_ip_address,
                    'user': args.user,
                    'publisher_port': args.publisher_port,
                    'subscriber_port': args.subscriber_port,
                    'process_name': args.process_name,
                    'loop_time': float(args.loop_time),
                    'sell': None,
                    'bid': None}

    Client(**kw_options)
    

def signal_handler(sig, frame):
    raise KeyboardInterrupt


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
    

if __name__ == '__main__':
    cmd_client()
            