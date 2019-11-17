import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
import time

# This project has been implemented and tested on Python 3.8.0
# by Taha Yasin for the course Ceng445 in semester 20191

class User:
    """ User class creates, modifies and observing Board & Shape classes. """
    user_count = 0
    user_name = "Unknown"
    def __init__(self, user_name="Player"):
        User.user_count += 1
        self.user_name = user_name
        print("A user has been created with the name", self.user_name, "and current user count is:", User.user_count)
    
    def get(self):
        return self.name
    
    def rename(self, newname="Player++"):
        oldname = self.name
        self.user_name = newname
        print("Player  \'", oldname, "\' has been renamed to  \'", self.name, "\'")

class Board:
    board_count = 0
    board_name = "Unknown"    
    
    def __init__(self, x=1280, y= 720, board_name ="Board#0"):
        Board.board_count += 1
        self.board_name = board_name
        self.board_space = pymunk.Space()
        self.board_space.gravity = 0, -100
        print("A board has been created with the name", self.board_name, "and current board count is:", self.board_count)
    
    def addShape(self, shape, x, y):
        shape.setPosition(x, y)
        self.board_space.add(shape.getBody())
        self.board_space.add(shape.getShape())
    
    def removeShape(self, shape):
        self.board_space.remove(shape.getBody())
        self.board_space.remove(shape.getShape())
    
    def moveShape(self, shape, x, y):
        shape.position = x, y


class Shape:
    """ Shape class is a base class for other sorts of shapes. """
    # Following attributes are shared among all shapes.
    def __init__(self, body, shape):
        self.__body = body
        self.__shape = shape
        print("Following shape created: ", self.__shape)

    def getBody(self):
        return self.__body
    def getShape(self):
        return self.__shape
    def setPosition(self, x, y):
        self.__body.position = x, y


class Ball(Shape):
    """ Ball class consists of Bowling, Tennis and Marble objects.
        Could use multiple inheritance, but looked unintuitive.  """
    
    def __init__(self, ball_type="Marble"):
        if ball_type == "Bowling":
            self.ball_moment = pymunk.moment_for_circle(30, 0, 30)
            self.ball_body = pymunk.Body(30, self.ball_moment)
            self.ball_shape = pymunk.Circle(self.ball_body, 30)
            self.ball_shape.elasticity = 0.65
            self.ball_shape.friction = 0.94
            
        elif ball_type == "Tennis":
            self.ball_moment = pymunk.moment_for_circle(8, 0, 8)
            self.ball_body = pymunk.Body(8, self.ball_moment)
            self.ball_shape = pymunk.Circle(self.ball_body, 8)
            self.ball_shape.elasticity = 0.728
            self.ball_shape.friction = 0.51
        else:
            self.ball_moment = pymunk.moment_for_circle(5, 0, 5)
            self.ball_body = pymunk.Body(1, self.ball_moment)
            self.ball_shape = pymunk.Circle(self.ball_body, 5)
            self.ball_shape.elasticity = 0.1
            self.ball_shape.friction = 0.94
        super().__init__(self.ball_body, self.ball_shape)


# Init tests.
window = pyglet.window.Window(1280, 720, "Pymunk Tester", resizable=False)
options = DrawOptions()
# Create a user.
user1 = User("Taha")
user2 = User("Artun")
# Create a board.
board1 = Board(1280, 720, "TestBoard")
# Create 2 marbles.
marble1 = Ball('Bowling')
marble2 = Ball('Bowling')
# Add marbles into the board.
board1.addShape(shape=marble1, x=50, y=100)
board1.addShape(shape=marble2, x=250, y=350)

# View the board using Pyglet
@window.event
def on_draw():
    window.clear()
    board1.board_space.debug_draw(options)

def update(dt):
    board1.board_space.step(dt)
    for shape in board1.board_space.shapes:
        if shape.body.position.y < -100:
            board1.board_space.remove(shape.body, shape)
            print(shape, "has been removed to save resources.")
            print("Current shapes in the board:", board1.board_space.shapes)

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()

