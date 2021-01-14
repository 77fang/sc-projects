"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.
SCORE = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, dy=INITIAL_Y_SPEED,  dx=MAX_X_SPEED,
                 score=SCORE,
                 title='Breakout'):

        self.__dx = 0
        self.__dy = 0
        self.ball_radius = ball_radius
        self.start = False
        self.score = SCORE
        self.brick_numbers = brick_rows * brick_cols

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'steelblue'
        self.paddle.color = 'steelblue'
        self.window.add(self.paddle, self.window_width/2-paddle_width/2, self.window_height-paddle_offset)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'gold'
        self.ball.color = 'gold'
        self.window.add(self.ball, (self.window_width-self.ball.width) / 2, self.window_height/2)

        # Default initial velocity for the ball.
        # self.set_ball_velocity()

        # Initialize our mouse listeners.
        self.switch = False
        onmousemoved(self.paddle_position)
        onmouseclicked(self.start_ball)

        # Draw bricks.
        run = 0
        self.brick_numbers = 0
        for i in range(0, (brick_rows * (brick_height + brick_spacing) - brick_spacing), brick_spacing+brick_height):
            run += 1
            for j in range(0, self.window_width, brick_spacing+brick_width):
                self.brick_numbers += 1
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if run % 3 == 0:
                    self.brick.fill_color = 'lightpink'
                    self.brick.color = 'lightpink'
                if run % 3 == 1:
                    self.brick.fill_color = 'indianred'
                    self.brick.color = 'indianred'
                if run % 3 == 2:
                    self.brick.fill_color = 'lightcoral'
                    self.brick.color = 'lightcoral'
                self.window.add(self.brick, x=j, y=brick_offset+i)

        # Add score label.
        self.score_label = GLabel('Score: ' + str(self.score), x=0, y=self.window_height)
        self.score_label.font = 'Courier-20'
        self.window.add(self.score_label)

    # Click to start ball moving.
    def start_ball(self, event):
        self.switch = True
        if self.__dx == 0 and self.__dy == 0:
            self.set_ball_velocity()

    # Place paddle where mouse is.
    def paddle_position(self, event):
        if event.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif event.x >= self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width/2

    # Give ball a speed.
    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    # Check if ball hits on object.
    def ball_on_thing(self):
        # Check four points of ball.
        touch1 = self.window.get_object_at(self.ball.x, self.ball.y)
        touch2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        touch3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        touch4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if touch1 is not None and touch1 is not self.score_label:
            if touch1.y is self.paddle.y:
                self.ball.y = self.paddle.y - self.ball.height
                self.__dy = -self.__dy
            else:
                self.window.remove(touch1)
                self.score += 1
                self.__dy = -self.__dy
                self.score_label.text = 'Score: ' + str(self.score)
        elif touch2 is not None and touch2 is not self.score_label:
            if touch2.y is self.paddle.y:
                self.ball.y = self.paddle.y - self.ball.height
                self.__dy = -self.__dy
            else:
                self.window.remove(touch2)
                self.score += 1
                self.__dy = -self.__dy
                self.score_label.text = 'Score: ' + str(self.score)
        elif touch3 is not None and touch3 is not self.score_label:
            if touch3.y is self.paddle.y:
                self.ball.y = self.paddle.y - self.ball.height
                self.__dy = -self.__dy
            else:
                self.window.remove(touch3)
                self.score += 1
                self.__dy = -self.__dy
                self.score_label.text = 'Score: ' + str(self.score)
        elif touch4 is not None and touch4 is not self.score_label:
            if touch4.y is self.paddle.y:
                self.ball.y = self.paddle.y - self.ball.height
                self.__dy = -self.__dy
            else:
                self.window.remove(touch4)
                self.score += 1
                self.__dy = -self.__dy
                self.score_label.text = 'Score: ' + str(self.score)

    # Reset ball to its original position.
    def reset_ball(self):
        self.window.add(self.ball, (self.window_width-self.ball.width) / 2, self.window_height/2)

    # Make the ball bounces back if it hits wall.
    def ball_move(self):
        self.ball.move(self.__dx, self.__dy)
        if self.ball.x <= 0:
            self.__dx = -self.__dx
        elif self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dy = -self.__dy

    # Return score.
    def get_score(self):
        return self.score

    # Return brick numbers.
    def get_brick_number(self):
        return self.brick_numbers

    # Print "You Wint!"
    def stop_win(self):
        self.__dx = 0
        self.__dy = 0
        win = GLabel('You Win!')
        win.font = 'Courier-20'
        self.window.add(win, x=(self.window_width-win.width) / 2, y=self.window_height / 2)

    # Print "Game Over!"
    def game_over(self):
        game_over = GLabel('Game Over!')
        game_over.font = 'Courier-20'
        self.window.add(game_over, x=(self.window_width - game_over.width) / 2, y=self.window_height / 2)

    def click_to_start(self):
        click_to_start = GLabel('Click to Start!')
        click_to_start.font = 'Courier-20'
        self.window.add(click_to_start, x=(self.window_width - click_to_start.width) / 2, y=self.window_height / 2)

