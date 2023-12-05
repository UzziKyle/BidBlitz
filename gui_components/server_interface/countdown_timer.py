from typing import Optional, Tuple, Union
from customtkinter import *


class CountdownTimer(CTkFrame):
    def __init__(self, master: any, 
                 width: int = 200, height: int = 200, 
                 corner_radius: int | str | None = 0, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = "transparent", 
                 border_color: str | Tuple[str, str] | None = None, 
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
        
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
                
        # self.grid_columnconfigure(list(range(6)), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.hour = StringVar( value="00")
        self.minute = StringVar(value="00")
        self.second = StringVar(value="00")
        
        self.timer_label = CTkLabel(master=self, text=f"Countdown:")
        self.timer_label.grid(row=0, column=0, padx=(8, 0), pady=8, sticky="ew")
        
        self.hour_entry = CTkEntry(master=self, width=32, textvariable=self.hour, justify="center")
        self.hour_entry.grid(row=0, column=1, padx=(8, 0), pady=8, sticky="ew")
        
        self.colon1_label = CTkLabel(master=self, text=f":")
        self.colon1_label.grid(row=0, column=2, padx=(4,0), pady=8, sticky="ew")
        
        self.minute_entry = CTkEntry(master=self, width=32, textvariable=self.minute, justify="center")
        self.minute_entry.grid(row=0, column=3, padx=(4, 0), pady=8, sticky="ew")
        
        self.colon2_label = CTkLabel(master=self, text=f":")
        self.colon2_label.grid(row=0, column=4, padx=(4, 0), pady=8, sticky="ew")
        
        self.second_entry = CTkEntry(master=self, width=32, textvariable=self.second, justify="center")
        self.second_entry.grid(row=0, column=5, padx=(4, 0), pady=8, sticky="ew")
        
        self.submit_button = CTkButton(master=self, width=32, text="Submit")
        self.submit_button.grid(row=0, column=6, padx=(16, 8), pady=8, sticky="ew")
        
    def get(self):
        # the input provided by the user is
        # stored in here: temp
        hour = self.hour.get()
        minute = self.minute.get()
        second = self.second.get()
        temp = int(hour)*3600 + int(minute)*60 + int(second)
        
        return temp
        
        
    # def countdown(self):
    #     try:
    #         # the input provided by the user is
    #         # stored in here :temp
    #         hour = self.hour.get()
    #         minute = self.minute.get()
    #         second = self.second.get()
    #         temp = int(hour)*3600 + int(minute)*60 + int(second)
            
    #     except:
    #         print("Please input the right value")
            
    #     while temp >-1:
            
    #         # divmod(firstvalue = temp//60, secondvalue = temp%60)
    #         mins,secs = divmod(temp,60) 
    
    #         # Converting the input entered in mins or secs to hours,
    #         # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
    #         # 50min: 0sec)
    #         hours=0
    #         if mins >60:
                
    #             # divmod(firstvalue = temp//60, secondvalue 
    #             # = temp%60)
    #             hours, mins = divmod(mins, 60)
            
    #         # using format () method to store the value up to 
    #         # two decimal places
            
    #         self.timer_label.configure(text=f'Countdown: {hours:02d}:{mins:02d}:{secs:02d}')
    
    #         # updating the GUI window after decrementing the
    #         # temp value every time

    #         self.master.update()
    #         time.sleep(1)
            
    #         # after every one sec the value of temp will be decremented
    #         # by one
    #         temp -= 1    


if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.countdown_timer = CountdownTimer(master=self)
            self.countdown_timer.grid(row=0, column=0, padx=10, pady=10)
        
        
    app = Tester()
    
    app.mainloop()
    