import pymunk
import time

# This project has been implemented and tested on Python 3.8.0
# by Taha Yasin for the course Ceng445 in semester 20191

class User:
    """
    User class is responsible for creating, modifying and observing Board & Shape classes.
    """
    def __init__(self, name="Player"):
        self.name = name
        print("A user has been created with the name \'", self.name, "\'")
    
    def get(self):
        return self.name
    
    def rename(self, newname="Player++"):
        oldname = self.name
        self.name = newname
        print("Player  \'", oldname, "\' has been renamed to  \'", self.name, "\'")


space = pymunk.Space()
space.gravity = 0, -1000

body = pymunk.Body(1, 1666)
body.position = 50, 1000
space.add(body)

# Init tests.

while True:
    space.step(0.02) # 50 fps
    print(body.position)
    time.sleep(0.5)