"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel

FRAME_RATE = 1000 / 120     # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add animation loop here!
    graphics.click_to_start()
    while True:
        pause(FRAME_RATE)
        if graphics.switch:                     # Switch on.
            graphics.ball_on_thing()            # Check if ball hit on objects.
            graphics.ball_move()                # Ball bounce back if it hits wall.
            if graphics.get_score() == graphics.get_brick_number():      # If scores are the same as brick numbers.
                graphics.stop_win()                                      # Stop ball and print "You Win!"
                break
            if graphics.ball.y >= graphics.window.height:                # If ball falls out of window, lives minus one.
                graphics.switch = False
                lives -= 1
                if lives > 0:
                    graphics.reset_ball()                                # Reset ball.
                else:
                    graphics.game_over()                                 # Break if there are no more lives.
                    break


if __name__ == '__main__':
    main()