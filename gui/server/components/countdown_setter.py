from typing import Optional, Tuple, Union
from customtkinter import *


class CountdownSetter(CTkFrame):
    def __init__(self, master: any, font: any, 
                 width: int = 200, height: int = 200, 
                 corner_radius: int | str | None = 0, 
                 border_width: int | str | None = 0, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = "transparent", 
                 border_color: str | Tuple[str, str] | None = None, 
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
        
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
                
        # self.grid_columnconfigure(list(range(6)), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        
        self.font_general, self.font_buttons = font

        self.hour = StringVar( value="00")
        self.minute = StringVar(value="00")
        self.second = StringVar(value="00")
        
        self.timer_label = CTkLabel(master=self, text=f"Countdown:", font=self.font_general)
        self.timer_label.grid(row=0, column=0, padx=(8, 0), pady=8, sticky="e")
        
        self.hour_entry = CTkEntry(master=self, width=32, textvariable=self.hour, justify="center", font=self.font_general)
        self.hour_entry.grid(row=0, column=1, padx=(8, 0), pady=8, sticky="ew")
        
        self.colon1_label = CTkLabel(master=self, text=f":", font=self.font_general)
        self.colon1_label.grid(row=0, column=2, padx=(4,0), pady=8, sticky="ew")
        
        self.minute_entry = CTkEntry(master=self, width=32, textvariable=self.minute, justify="center", font=self.font_general)
        self.minute_entry.grid(row=0, column=3, padx=(4, 0), pady=8, sticky="ew")
        
        self.colon2_label = CTkLabel(master=self, text=f":", font=self.font_general)
        self.colon2_label.grid(row=0, column=4, padx=(4, 0), pady=8, sticky="ew")
        
        self.second_entry = CTkEntry(master=self, width=32, textvariable=self.second, justify="center", font=self.font_general)
        self.second_entry.grid(row=0, column=5, padx=(4, 0), pady=8, sticky="ew")
        
        self.start_button = CTkButton(master=self, width=64, height=32, text="Start", font=self.font_buttons)
        self.start_button.grid(row=0, column=6, padx=(16, 0), pady=8, sticky="ew")
        
        # self.stop_button = CTkButton(master=self, width=64, text="Stop")
        # self.stop_button.grid(row=0, column=7, padx=(4, 16), pady=8, sticky="ew")
        
    def get(self):
        # the input provided by the user is
        # stored in here: temp
        hour = self.hour.get()
        minute = self.minute.get()
        second = self.second.get()
        temp = int(hour)*3600 + int(minute)*60 + int(second)
        
        return temp


if __name__ == '__main__':
    class Tester(CTk):
        def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
            super().__init__(fg_color, **kwargs)
                    
            self.grid_columnconfigure(0, weight=1)
            
            self.countdown_timer = CountdownSetter(master=self)
            self.countdown_timer.grid(row=0, column=0, padx=10, pady=10)
        
        
    app = Tester()
    
    app.mainloop()
    