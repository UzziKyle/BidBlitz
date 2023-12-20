from typing import Optional, Tuple, Union
from customtkinter import *
from threading import Thread, Event
from time import sleep


class Utility(CTkFrame):
    def __init__(self, master: any, 
                 font,
                 width: int = 250, height: int = 250, 
                 corner_radius: int | str | None = 0, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = "transparent", 
                 border_color: str | Tuple[str, str] | None = None, 
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
        
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        
        self.font_heading = CTkFont(family='Monospac821 BT', size=18, weight='bold')
        self.font_general, self.font_buttons = font
                
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.button_holder = CTkFrame(master=self, fg_color="transparent")
        self.button_holder.grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.button_holder.grid_rowconfigure(0, weight=1)
        
        self.bid_button = CTkButton(master=self.button_holder, width=64, text="Bid", state="disabled", font=self.font_buttons)
        self.bid_button.grid(row=0, column=0, padx=0)
        
        self.sell_button = CTkButton(master=self.button_holder, width=64, text="Sell", state="disabled", font=self.font_buttons)
        self.sell_button.grid(row=0, column=1, padx=(8, 0))
        
        self.app_name = CTkLabel(master=self, text=f"BidBlitz", anchor="center", font=self.font_heading)
        self.app_name.grid(row=0, column=1, pady=8, sticky="ew")  
              
        self.timer = CTkLabel(master=self, text=f"Time Left: 00:00:00", font=self.font_general)
        self.timer.grid(row=0, column=2, padx=8, pady=8, sticky="e")
        
        self.timer_is_on = Event()
        
    def set_bid_button_command(self, function):
        self.bid_button.configure(command=lambda: function())
        
    def set_sell_button_command(self, function):
        self.sell_button.configure(command=lambda: function())
        
    def set_send_message_function(self, function) -> None:
        self.send_message = function
        
    def activate(self) -> None:
        self.bid_button.configure(state="normal")
        self.sell_button.configure(state="normal")
        
    def deactivate(self) -> None:
        self.bid_button.configure(state="disabled")
        self.sell_button.configure(state="disabled") 
                 
    def start_countdown(self, temp: int) -> None:
        self.timer_is_on.set()
        self.activate() 

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
        self.deactivate()
                        
    def stop_countdown(self):
        self.timer_is_on.clear()
        self.deactivate()
        self.timer.configure(text=f"Time Left: 00:00:00")
                       


if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.utility = Utility(master=self)
            self.utility.grid(row=0, column=0, padx=10, pady=10)
        
        
    app = Tester()
    
    app.mainloop()
    