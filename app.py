import pygame

#GLOBAL VARS
s_width = 600
s_height = 600
ball_size = 20
paddle_height = 100
paddle_width = 20
win = pygame.display.set_mode((s_width, s_height))

pygame.font.init()

class Ball(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 1.5
        self.dy = 1.5

    def draw(self, win):
        pygame.draw.rect(win, (255,255,255), (self.x, self.y, ball_size, ball_size), 0)

    def move(self, paddle_1, paddle_2):
        if self.x < 0:
            self.x = s_width/2
            self.y = s_height/2
            paddle_2.score += 1
        if self.x > s_width-ball_size:
            self.x = s_width/2
            self.y = s_height/2
            paddle_1.score += 1
        if self.x > paddle_2.x - ball_size and (self.y+ball_size >= paddle_2.y and self.y <= paddle_2.y + paddle_height):
            self.dx *= -1
        if self.x < paddle_1.x + ball_size and (self.y+ball_size >= paddle_1.y and self.y <= paddle_1.y + paddle_height):
            self.dx *= -1
        if self.y > s_height-ball_size:
            self.dy *= -1
        if self.y < 0:
            self.dy *= -1

        self.x += self.dx
        self.y += self.dy

class Paddle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3.5
        self.score = 0
    
    def draw(self, win):
        pygame.draw.rect(win, (255,255,255), (self.x, self.y, paddle_width, paddle_height), 0)

    def move(self, direction):
        new_pos = self.y + (direction * self.speed)
        if not(new_pos > (s_height - paddle_height) or new_pos < 0):
            self.y = new_pos

def draw_score(win, paddle_1, paddle_2):
    font = pygame.font.SysFont('comicsans', 50)
    score_1 = font.render(str(paddle_1.score), 1, (255,255,255))
    score_2 = font.render(str(paddle_2.score), 1, (255,255,255))

    win.blit(score_1, ((s_width/2) - 50,10))
    win.blit(score_2, ((s_width/2) + 50,10))

def main():
    run = True

    ball = Ball(s_width/2, s_height/2)
    paddle_1 = Paddle(10,(s_height/2) - paddle_height)
    paddle_2 = Paddle(s_width-10-paddle_width, (s_height/2) - paddle_height)
    
    while run:
        win.fill((0,0,0))
        ball.move(paddle_1, paddle_2)
        ball.draw(win)
        paddle_1.draw(win)
        paddle_2.draw(win)
        draw_score(win, paddle_1, paddle_2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            paddle_1.move(1)
        if keys[pygame.K_w]:
            paddle_1.move(-1)
        if keys[pygame.K_DOWN]:
            paddle_2.move(1)
        if keys[pygame.K_UP]:
            paddle_2.move(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    
    pygame.display.quit()

main()