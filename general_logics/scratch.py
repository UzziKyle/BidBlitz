
"""
3 tasks

1. Add clients
2. Clients can do selling, and it will appear to other clients' bidding list
3. Clients can bid within a specified time, and each bid must be displayed.
4. Clients with highest biddings for each sold items must be displayed after the time limit.
"""

import time

def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
        
countdown_timer(15)
