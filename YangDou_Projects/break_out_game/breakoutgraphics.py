"""
File: breakoutgraphics.py
Name: Doris
----------------------
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

In this game, the player moves a paddle from side-to-side to hit a ball.
The game’s objective is to eliminate all of the bricks at the top of
the screen by hitting them with the ball.
But, if the ball falls to the bottom of the ground,
the player loses lives, and when there is no lives, the game ends!

To win the game, all the bricks must be eliminated.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = 'True'
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.switch = False  # A switch that control the ball for bouncing
        onmouseclicked(self.drop_ball)
        onmousemoved(self.paddle_move)

        # Brick's rows, cols
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        # Draw bricks
        self.brick_y = brick_offset
        for i in range(self.brick_rows):
            self.brick_x = 0
            for j in range(self.brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = 'red'
                self.brick.color = 'red'
                self.window.add(self.brick, x=self.brick_x, y=self.brick_y)
                self.brick_x = self.brick_x + self.brick.width + brick_spacing
                if 1 < i <= 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif 3 < i <= 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif 5 < i <= 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                elif 7 < i <= 9:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
            self.brick_y = self.brick_y + self.brick.height + brick_spacing

    def paddle_move(self, event):
        """
        Use the mouse position to control the movement of the paddle.
        """
        # The x-coordinate of the middle of the paddle will be the same as the x-coordinate of the mouse
        self.paddle.x = event.x - self.paddle.width/2
        # To prevent the paddle from extending beyond the left and right sides of the game window
        if event.x - self.paddle.width/2 <= 0:
            self.paddle.x = 0
        elif event.x + self.paddle.width/2 >= self.window.width:
            self.paddle.x = self.window.width-self.paddle.width

    def drop_ball(self, event):
        """
        Use mouse click to turn on the switch.
        """
        # Switch reassign True(turn on the switch)
        self.switch = True
        # Velocity of the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_dx(self):
        """
        :return: int, the random horizontal velocity of the ball
        """
        return self.__dx

    def get_dy(self):
        """
        :return: int, the vertical velocity of the ball
        """
        return self.__dy
