from python_banyan.banyan_base import BanyanBase
from gui.server import ServerInterface


class Server(BanyanBase):
    def __init__(self, ):
        super(Server, self).__init__(process_name="Server")
        
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
        
        self.interface = ServerInterface()
        self.interface.bind("<Destroy>", self.on_destroy)
        self.interface.mainloop()
        
        self.receive_loop()
                
    def incoming_message_processing(self, topic, payload):
        print('New Item: ', payload['item'])
        self.items.append(payload['item'])
        self.publish_payload(payload={'items': self.items}, topic='selling')
        
    def on_destroy(self, event):
        if event.widget != self.interface:
            return
        
        self.clean_up()
        exit()
        
        
if __name__ == '__main__':
    Server()
    