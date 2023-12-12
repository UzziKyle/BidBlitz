from python_banyan.banyan_base import BanyanBase
from gui.client.interface import ClientInterface
from gui.client.components.username_input_dialog import UsernameInputDialog
from threading import Thread
from time import sleep
import msgpack
import zmq


class Client(BanyanBase):
    def __init__(self, ):
        super(Client, self).__init__(process_name="Client")
        
        self.set_subscriber_topic('timer')
        self.set_subscriber_topic('bidding')
        self.set_subscriber_topic('bidder')
        
        self.username: str | None = None
        
        self.interface = ClientInterface()
        self.username_input_dialog = UsernameInputDialog()
        self.username_input_dialog.accept_button.configure(command=lambda: self.set_username())
        
        self.interface.bind("<Destroy>", self.on_destroy)
                
        self.interface.withdraw()
        self.interface.after(5, self.get_message)
        self.interface.mainloop()
            
    def set_username(self):
        self.username = self.username_input_dialog.name_entry.get()
        self.username_input_dialog.destroy()
        self.interface.deiconify()
        self.interface.title(f'CLIENT: {self.username}')
        self.publish_payload(payload={'username': self.username}, topic='users')
        
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
        if topic == 'timer':
            timer = Thread(target=self.interface.utility.start_countdown, args=(payload['temp'], ))
            
            timer.start()
            
        # if topic == 'selling':
        #     print(f'Items you are SELLING: {payload["items"]}')
                
        # if topic == 'bidding':
        #     print(f'Items for BIDDING: {payload["items"]}')
            
        # if topic == 'bidder':
        #     print(f'{payload["bidder"]} is me!')
            
    def on_destroy(self, event):
        if event.widget != self.interface:
            return
        
        self.clean_up()
            
        
if __name__ == '__main__':
    Client()
    