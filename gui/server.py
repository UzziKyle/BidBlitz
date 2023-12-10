from typing import Optional, Tuple, Union
from .server_components.countdown_setter import CountdownSetter
from .server_components.window import Window
from customtkinter import *
from time import sleep
from threading import Thread

        
class ServerInterface(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.title('SERVER')
        self.geometry('375x500')
        self.minsize(width=375, height=250)
        set_appearance_mode('System')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.timer = CTkLabel(master=self, text=f"Time Left: 00:00:00")
        self.timer.grid(row=0, column=0, padx=8, pady=8, sticky="e")
        
        self.timer_is_on = False
                
        self.window = Window(self, corner_radius=8)
        self.window.grid(row=1, column=0, padx=8, sticky="nsew")
        
        # TODO center position this
        self.countdown_setter = CountdownSetter(self)
        self.countdown_setter.grid(row=2, column=0, padx=8, sticky="ew")
        
        self.countdown_setter.start_button.configure(command=lambda: Thread(target=self.start_countdown).start())
        self.countdown_setter.stop_button.configure(command=lambda: self.stop_countdown())
        
    def start_countdown(self) -> None:
        temp = self.countdown_setter.get()
        self.timer_is_on = True
                
        while temp >-1:
            if self.timer_is_on == False:
                break
                        
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins, secs = divmod(temp,60) 
            hours = 0
            
            if mins > 60:
                # divmod(firstvalue = temp//60, secondvalue 
                # = temp%60)
                hours, mins = divmod(mins, 60)
            
            self.timer.configure(text=f'Countdown: {hours:02d}:{mins:02d}:{secs:02d}')
                            
            # after every one sec the value of temp will be decremented
            # by one
            sleep(1)
            temp -= 1        
            
    def stop_countdown(self):
        self.timer_is_on = False
        self.timer.configure(text=f"Time Left: 00:00:00")
                       
        
if __name__ == '__main__':
    server_interface = ServerInterface()
    server_interface.mainloop()
    