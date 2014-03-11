Horse-Racing-Animation
======================
The script horse_racing animation was created for for a Python 3.x study group. It works on Python 2.x, too.

I took a 1920's series of film slides and convered them into ASCII art.

The script also relies on modules: 

```python   

import time 
import os
import random

```

A clearScreen function was created with the os module to make it usable for different systems.

```python
# this is called after every frame needs to be cleared on the terminal

def clearScreen():
    if os.name == 'posix': 
        os.system('clear') 
    elif os.name == 'nt': 
        os.system('cls')

```
                                                                                                                    
                                                                                                                             
              
