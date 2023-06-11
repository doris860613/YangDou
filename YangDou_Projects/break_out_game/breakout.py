"""
File: breakout.py
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

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    brick_byebye = 0  # To count the number of bricks hit
    # If the player doesn't have any lives or all bricks are hit, then game over
    while 0 < lives <= NUM_LIVES or brick_byebye == graphics.brick_rows * graphics.brick_cols:
        pause(FRAME_RATE)
        # A switch that let the ball start bouncing
        if graphics.switch:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            # Ball's bouncing range
            while graphics.ball.y < graphics.window.height:

                # Game over
                if brick_byebye == graphics.brick_rows * graphics.brick_cols:
                    break

                # Ball's move
                graphics.ball.move(dx, dy)

                # To check if is a wall or not
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    dx = -dx
                if graphics.ball.y <= 0:
                    dy = -dy

                # The upper left detection point of the ball
                obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                # The upper right detection point of the ball
                obj2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
                # The lower left detection point of the ball
                obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
                # The lower right detection point of the ball
                obj4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                     graphics.ball.y + graphics.ball.height)

                # Check what object the ball hit
                if obj1 is not None:
                    if obj1 is not graphics.paddle:
                        graphics.window.remove(obj1)
                        brick_byebye += 1
                        dy = -dy  # Rebound
                    else:
                        dy = -abs(dy)  # To prevent the ball from rebounding infinity inside the paddle
                elif obj2 is not None:
                    if obj2 is not graphics.paddle:
                        graphics.window.remove(obj2)
                        brick_byebye += 1
                        dy = -dy  # Rebound
                    else:
                        dy = -abs(dy)  # To prevent the ball from rebounding infinity inside the paddle
                elif obj3 is not None:
                    if obj3 is not graphics.paddle:
                        graphics.window.remove(obj3)
                        brick_byebye += 1
                    dy = -abs(dy)  # Rebound
                elif obj4 is not None:
                    if obj4 is not graphics.paddle:
                        graphics.window.remove(obj4)
                        brick_byebye += 1
                    dy = -abs(dy)  # Rebound

                # Pause
                pause(FRAME_RATE)

            # Switch reassign False(turn off the switch)
            graphics.switch = False
            # If the ball falls to the bottom border of the window, then lose one lives
            lives -= 1
            # Add a ball for the next round
            graphics.window.add(graphics.ball, x=(graphics.window.width-graphics.ball.width)/2,
                                y=(graphics.window.height-graphics.ball.height)/2)
    # If game over or win the game, remove the ball from screen
    graphics.window.remove(graphics.ball)


if __name__ == '__main__':
    main()
