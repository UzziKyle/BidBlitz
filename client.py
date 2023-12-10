from python_banyan.banyan_base import BanyanBase
from gui.client import ClientInterface
from threading import Thread


class Client(BanyanBase):
    def __init__(self, ):
        super(Client, self).__init__(process_name="Client")
        
        self.username = 'Kyle'
        
        self.set_subscriber_topic('timer')
        self.set_subscriber_topic('bidding')
        self.set_subscriber_topic('bidder')
        
        self.interface = ClientInterface()
        self.interface.bind("<Destroy>", self.on_destroy)
        self.interface.mainloop()
        
        self.receive_loop()
            
    def incoming_message_processing(self, topic, payload):
        # if topic == 'timer':
        #     print('Received')
        #     timer_thread = Thread(target=self.interface.utility.start_countdown, args=(payload["temp"], ))
            
        #     timer_thread.start()
            
        if topic == 'selling':
            print(f'Items you are SELLING: {payload["items"]}')
                
        if topic == 'bidding':
            print(f'Items for BIDDING: {payload["items"]}')
            
        if topic == 'bidder':
            print(f'{payload["bidder"]} is me!')
            
    def on_destroy(self, event):
        if event.widget != self.interface:
            return
        
        self.clean_up()
        exit()
            
        
if __name__ == '__main__':
    Client()
    