from python_banyan.banyan_base import BanyanBase
from gui.server.interface import ServerInterface
from threading import Thread
from time import sleep
import msgpack
import zmq


class Server(BanyanBase):
    def __init__(self, ):
        super(Server, self).__init__(process_name="Server")
        
        self.set_subscriber_topic('users')
        self.set_subscriber_topic('server')
        
        self.for_sale = {}
        self.items = []
        self.bidders = {}
        '''
            {
                "item": {
                    "bidders": {
                        "name": username,
                        "bid": amount,
                    },
                },
            }
        '''
        
        self.number_of_messages = 0
        
        self.interface = ServerInterface(publish_payload=self.publish_payload)
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
        if topic == 'users':
            self.interface.window.insert(message=f"{payload['username']} is ready...", row=self.number_of_messages)
            
        self.number_of_messages += 1
        
    def on_destroy(self, event):
        if event.widget != self.interface:
            return
        
        self.clean_up()
        
        
if __name__ == '__main__':
    Server()
    