import random
import sys, pygame
pygame.init()
# Screen
icon = pygame.image.load("assets/snake_icon2.png")
pygame.display.set_icon(icon)
size = height, width = 600,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
grid_size = 30
grid=[]
for i in range(0,height,30):
    for j in range(0,width,30):
        grid.append((j,i))

#Snake

class body_part:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dirX = 1
        self.dirY = 0

    def move(self):
        if self.x == width - grid_size and self.dirX == 1:
            self.x = 0
        elif self.x == 0 and self.dirX == -1:
            self.x = width - grid_size
        elif self.y == 0 and self.dirY == -1:
            self.y = height - grid_size
        elif self.y == height - grid_size and self.dirY == 1:
            self.y = 0
        else:
            self.x = self.x + self.dirX * grid_size
            self.y = self.y + self.dirY * grid_size


class Snake:
    body = []
    turns = {}

    def grow(self):
        if self.body[-1].dirX == 1 and self.body[-1].dirY == 0:
            tail = body_part(self.body[-1].x-1*grid_size, self.body[-1].y)
            self.body.append(tail)

        elif self.body[-1].dirX == -1 and self.body[-1].dirY == 0:
            tail = body_part(self.body[-1].x+1*grid_size, self.body[-1].y)
            self.body.append(tail)

        elif self.body[-1].dirX == 0 and self.body[-1].dirY == -1:
            tail = body_part(self.body[-1].x, self.body[-1].y+1*grid_size)
            self.body.append(tail)

        elif self.body[-1].dirX == 0 and self.body[-1].dirY == 1:
            tail = body_part(self.body[-1].x, self.body[-1].y-1*grid_size)
            self.body.append(tail)

        self.body[-1].dirX = self.body[-2].dirX
        self.body[-1].dirY = self.body[-2].dirY



    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.body[0].dirY != 1 and self.body[0].dirY != -1:
            self.body[0].dirY = -1
            self.body[0].dirX = 0
            self.turns[(self.body[0].x, self.body[0].y)] = (self.body[0].dirX, self.body[0].dirY)

        elif keys[pygame.K_DOWN] and self.body[0].dirY != -1 and self.body[0].dirY != 1:
            self.body[0].dirY = 1
            self.body[0].dirX = 0
            self.turns[(self.body[0].x, self.body[0].y)] = (self.body[0].dirX, self.body[0].dirY)

        elif keys[pygame.K_RIGHT] and self.body[0].dirX != -1 and self.body[0].dirX != 1:
            self.body[0].dirY = 0
            self.body[0].dirX = 1
            self.turns[(self.body[0].x, self.body[0].y)] = (self.body[0].dirX, self.body[0].dirY)

        elif keys[pygame.K_LEFT] and self.body[0].dirX != 1 and self.body[0].dirX != -1:
            self.body[0].dirY = 0
            self.body[0].dirX = -1
            self.turns[(self.body[0].x, self.body[0].y)] = (self.body[0].dirX, self.body[0].dirY)


        for i, part in enumerate(self.body):
            if i > 0:
                pos = part.x, part.y
                if pos in self.turns:
                    part.dirX = self.turns[pos][0]
                    part.dirY = self.turns[pos][1]
                    if i == len(self.body)-1:
                        self.turns.pop(pos)
                part.move()
            else:
                part.move()

    def draw(self):
        for i, part in enumerate(self.body):
            if i == 0:
                if part.dirX == 1:
                    screen.blit(snake_head_right, (part.x, part.y))
                elif part.dirX == -1:
                    screen.blit(snake_head_left, (part.x, part.y))
                elif part.dirY == -1:
                    screen.blit(snake_head_up, (part.x, part.y))
                elif part.dirY == 1:
                    screen.blit(snake_head_down, (part.x, part.y))
            if 0 < i < len(self.body)-1:
                pos = part.x, part.y
                if pos in self.turns:
                    if part.dirX == 1:
                        if self.body[i-1].dirY == 1:
                            screen.blit(snake_turn3, (part.x, part.y))
                        else:
                            screen.blit(snake_turn2, (part.x, part.y))

                    elif part.dirX == -1:
                        if self.body[i-1].dirY == 1:
                            screen.blit(snake_turn4, (part.x, part.y))
                        else:
                            screen.blit(snake_turn1, (part.x, part.y))

                    elif part.dirY == -1:
                        if self.body[i-1].dirX == 1:
                            screen.blit(snake_turn4, (part.x, part.y))
                        else:
                            screen.blit(snake_turn3, (part.x, part.y))

                    elif part.dirY == 1:
                        if self.body[i-1].dirX == 1:
                            screen.blit(snake_turn1, (part.x, part.y))
                        else:
                            screen.blit(snake_turn2, (part.x, part.y))

                elif part.dirX == 1:
                    screen.blit(snake_body, (part.x, part.y))
                elif part.dirX == -1:
                    screen.blit(snake_body, (part.x, part.y))
                elif part.dirY == -1:
                    screen.blit(snake_body_up, (part.x, part.y))
                elif part.dirY == 1:
                    screen.blit(snake_body_up, (part.x, part.y))
            if i == len(self.body) - 1:
                    if part.dirX == 1:
                        if self.body[i-1].dirY == 1:
                            screen.blit(snake_tail_down, (part.x, part.y))
                        elif self.body[i-1].dirY == -1:
                            screen.blit(snake_tail_up, (part.x, part.y))
                        else:
                            screen.blit(snake_tail_right, (part.x, part.y))
                    elif part.dirX == -1:
                        if self.body[i-1].dirY == 1:
                            screen.blit(snake_tail_down, (part.x, part.y))
                        elif self.body[i-1].dirY == -1:
                            screen.blit(snake_tail_up, (part.x, part.y))
                        else:
                            screen.blit(snake_tail_left, (part.x, part.y))
                    elif part.dirY == -1:
                        if self.body[i-1].dirX == 1:
                            screen.blit(snake_tail_right, (part.x, part.y))
                        elif self.body[i-1].dirX == -1:
                            screen.blit(snake_tail_left, (part.x, part.y))
                        else:
                            screen.blit(snake_tail_up, (part.x, part.y))
                    elif part.dirY == 1:
                        if self.body[i-1].dirX == 1:
                            screen.blit(snake_tail_right, (part.x, part.y))
                        elif self.body[i-1].dirX == -1:
                            screen.blit(snake_tail_left, (part.x, part.y))
                        else:
                            screen.blit(snake_tail_down, (part.x, part.y))

    def position(self):
        position = []
        for part in self.body:
            position.append([part.x, part.y])
        return position

    def dead(self):
        pos = [self.body[0].x, self.body[0].y]
        position = self.position()[1:]
        if pos in position:
            return True
        return False

    def reset(self):
        self.body = []
        self.turns = {}
        h = body_part(300, 300)
        self.body.append(h)
        self.grow()
        self.grow()
        self.grow()
        self.grow()


snake_head_right = pygame.image.load("assets/snake_head_right.png")
snake_head_left = pygame.image.load("assets/snake_head_left.png")
snake_head_up = pygame.image.load("assets/snake_head_up.png")
snake_head_down = pygame.image.load("assets/snake_head_down.png")
snake_body = pygame.image.load("assets/snake_body.png")
snake_body_up = pygame.image.load("assets/snake_body_up.png")
snake_tail_right = pygame.image.load("assets/snake_tail_right.png")
snake_tail_left = pygame.image.load("assets/snake_tail_left.png")
snake_tail_up = pygame.image.load("assets/snake_tail_up.png")
snake_tail_down = pygame.image.load("assets/snake_tail_down.png")
snake_turn1 = pygame.image.load("assets/snake_turn_LUDR.png")
snake_turn2 = pygame.image.load("assets/snake_turn_RUDL.png")
snake_turn3 = pygame.image.load("assets/snake_turn_ULRD.png")
snake_turn4 = pygame.image.load("assets/snake_turn_URLD.png")
apple_image = pygame.image.load("assets/apple.png")


class Apple:
    pos = 0, 0

    def spawn(self, position):
        game_grid = grid.copy()
        for x in position:
            try:
                game_grid.remove(x)
            except ValueError:
                pass
        self.pos = random.choice(game_grid)

    def draw(self):
        screen.blit(apple_image, self.pos)

    def eaten(self, head):
        head_pos = head.x, head.y
        if head_pos == self.pos:
            return True
        return False

snake = Snake()
head = body_part(300, 300)
snake.body.append(head)
snake.grow()
snake.grow()
snake.grow()
snake.grow()

apple = Apple()
apple.spawn(snake.position())

clock = pygame.time.Clock()






while 1:
    pygame.time.delay(100)
    clock.tick(23)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if snake.dead():
        snake.reset()
    screen.fill([255, 255, 255])
    snake.move()
    if apple.eaten(snake.body[0]):
        snake.grow()
        apple.spawn(snake.position())
        apple.draw()
    else:
        apple.draw()



    snake.draw()



    pygame.display.flip()
