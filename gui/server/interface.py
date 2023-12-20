from typing import Optional, Tuple, Union
from .components.utility import Utility
from .components.window import Window
from customtkinter import *
from time import sleep
from threading import Thread, Event
        
class ServerInterface(CTk):
    def __init__(self):
        super().__init__()
        
        self.title('SERVER')
        self.geometry('375x500')
        self.minsize(width=375, height=250)
        
        self.iconbitmap('assets/img/bidblitz.ico')
        
        self.font_heading = CTkFont(family='Monospac821 BT', size=18, weight='bold')
        self.font_general = CTkFont(family='Monospac821 BT', size=14)
        self.font_buttons = CTkFont(family='Monospac821 BT', size=14, weight='bold')
        
        self.font = (self.font_general, self.font_buttons)
        
        set_appearance_mode('System')
        set_default_color_theme('assets/themes/coffee.json')                
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.send_message = None
        
        self.app_name = CTkLabel(master=self, text=f"BidBlitz", font=self.font_heading)
        self.app_name.grid(row=0, column=0, padx=16, pady=8, sticky="w")
        
        self.timer = CTkLabel(master=self, text=f"Time Left: 00:00:00", font=self.font_general)
        self.timer.grid(row=0, column=1, padx=8, pady=8, sticky="e")
        
        self.timer_is_on = Event()
                
        self.window = Window(self, font=self.font, corner_radius=8)
        self.window.grid(row=1, column=0, columnspan=2,  padx=8, sticky="nsew")
        
        self.utility = Utility(master=self, font=self.font, func=self.start_button_functions)
        self.utility.grid(row=2, column=0, columnspan=2, pady=8, sticky='ew')
        
        
    def start_button_functions(self):
        self.window.insert(message=f'Server started...')
        
        self.send_message(payload={"message": "timer", "temp": self.utility.countdown_setter.get()}, topic="user")  # Sends signal to clients
        
        Thread(target=self.start_countdown).start()
        
    def start_countdown(self) -> None:
        temp = self.utility.countdown_setter.get()
        self.utility.countdown_setter.start_button.configure(state='disabled')
        self.timer_is_on.set()
                
        while temp >-1:
            if not self.timer_is_on.is_set():
                break
                        
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins, secs = divmod(temp,60) 
            hours = 0
            
            if mins > 60:
                # divmod(firstvalue = temp//60, secondvalue 
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            self.timer.configure(text=f'Time Left: {hours:02d}:{mins:02d}:{secs:02d}')
                            
            # after every one sec the value of temp will be decremented
            # by one
            sleep(1)
            temp -= 1     
            
        self.timer_is_on.clear()
        self.utility.countdown_setter.start_button.configure(state='active')
        self.send_message(payload={'message': 'timer'}, topic='server')
    
    def set_send_message_function(self, function) -> None:
        self.send_message = function
                       
        
if __name__ == '__main__':
    server_interface = ServerInterface()
    server_interface.mainloop()
    