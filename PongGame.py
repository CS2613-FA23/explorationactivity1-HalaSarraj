#Pong game implementation
import turtle

class PongGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title('Pong Game')
        self.screen.bgcolor('black')
        self.screen.setup(width=1000, height=600)
        self.left_paddle, self.right_paddle, self.ball, self.score_board = self.setup_game()
        self.left_score = 0
        self.right_score = 0

    def setup_game(self):
        # Create and position the paddles
        left_paddle = self.create_paddle(-400, 0, 'red')
        right_paddle = self.create_paddle(400, 0, 'blue')

        # Create and position the ball
        ball = turtle.Turtle()
        ball.speed(40)
        ball.shape('circle')
        ball.color('white')
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 5
        ball.dy = -5

        # Create and position the score display
        score_board = turtle.Turtle()
        score_board.speed(0)
        score_board.color('green')
        score_board.penup()
        score_board.hideturtle()
        score_board.goto(0, 260)
        score_board.write('Left Player: 0 \t Right Player: 0',
                          align='center', font=('Times New Roman', 30, 'normal'))

        return left_paddle, right_paddle, ball, score_board

    def create_paddle(self, x, y, color):
        paddle = turtle.Turtle()
        paddle.speed(0)
        paddle.shape('square')
        paddle.color(color)
        paddle.shapesize(stretch_wid=6, stretch_len=1)
        paddle.penup()
        paddle.goto(x, y)
        return paddle

    def left_paddle_up(self):
        y = self.left_paddle.ycor()
        if y < 240:
            self.left_paddle.sety(y + 20)

    def left_paddle_down(self):
        y = self.left_paddle.ycor()
        if y > -235:
            self.left_paddle.sety(y - 20)

    def right_paddle_up(self):
        y = self.right_paddle.ycor()
        if y < 240:
            self.right_paddle.sety(y + 20)

    def right_paddle_down(self):
        y = self.right_paddle.ycor()
        if y > -235:
            self.right_paddle.sety(y - 20)

    def keep_score(self, player):
        if player == 'left':
            self.left_score += 1
        elif player == 'right':
            self.right_score += 1

        self.score_board.clear()
        self.score_board.penup()
        self.score_board.goto(0, 260)
        self.score_board.write('Left Player: {} \t Right Player: {}'.format(
            self.left_score, self.right_score), align='center', font=('Times New Roman', 30, 'normal'))

    def run_game(self):
        self.screen.listen()
        self.screen.onkeypress(self.left_paddle_up, 'w')
        self.screen.onkeypress(self.left_paddle_down, 's')
        self.screen.onkeypress(self.right_paddle_up, 'Up')
        self.screen.onkeypress(self.right_paddle_down, 'Down')

        while True:
            self.screen.update()
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            if self.ball.ycor() > 280:
                self.ball.sety(280)
                self.ball.dy *= -1

            if self.ball.ycor() < -280:
                self.ball.sety(-280)
                self.ball.dy *= -1

            if ((self.ball.xcor() > 360) and
               (self.ball.xcor() < 370) and
               (self.ball.ycor() < self.right_paddle.ycor() + 40) and
               (self.ball.ycor() > self.right_paddle.ycor() - 40)):
                self.ball.setx(360)
                self.ball.dx *= -1

            if ((self.ball.xcor() < -360) and
               (self.ball.xcor() > -370) and
               (self.ball.ycor() < self.left_paddle.ycor() + 40) and
               (self.ball.ycor() > self.left_paddle.ycor() - 40)):
                self.ball.setx(-360)
                self.ball.dx *= -1

            if self.ball.xcor() > 500:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.keep_score('left')

            elif self.ball.xcor() < -500:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.keep_score('right')

            if self.left_score >= 5 or self.right_score >= 5:
                winner_message = turtle.Turtle()
                winner_message.speed(0)
                if self.left_score >= 5:
                    winner_message.color('red')
                    winner_message_message = "Left Player wins! Game Over"
                else:
                    winner_message.color('blue')
                    winner_message_message = "Right Player wins! Game Over"
                winner_message.penup()
                winner_message.hideturtle()
                winner_message.goto(0, 0)
                winner_message.write(winner_message_message,
                                    align='center', font=('Arial', 30, 'bold'))
                self.screen.update()
                turtle.done()

if __name__ == '__main__':
    game = PongGame()
    game.run_game()
