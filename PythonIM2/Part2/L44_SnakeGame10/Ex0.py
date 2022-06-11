import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake with Pygame")
food_color = ['red', 'purple', 'yellow', 'cyan', 'orange', 'pink']

class Snake():
    def __init__(self):
        self.x = 400
        self.y = 300
        self.x_move = 0
        self.y_move = 0
        self.body = []
        self.speed = 3
        self.head_rect = pygame.draw.circle(screen, 'blue', (self.x, self.y), 10)

    def get_direction(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP] == True:
            self.x_move = 0
            self.y_move = -self.speed
        if key_pressed[pygame.K_DOWN] == True:
            self.x_move = 0
            self.y_move = self.speed
        if key_pressed[pygame.K_LEFT] == True:
            self.x_move = -self.speed
            self.y_move = 0
        if key_pressed[pygame.K_RIGHT] == True:
            self.x_move = self.speed
            self.y_move = 0

    def update(self):
        # Set first element of body to be head position
        if len(self.body) >= 1:
            # Move body of snake
            for i in range(len(self.body)-1, 0, -1):
                self.body[i] = self.body[i-1]
            self.body[0] = {"x": self.x, "y": self.y}

        if self.x_move != 0:
            self.x += self.x_move
        if self.y_move != 0:
            self.y += self.y_move

    def drawSnake(self):
        self.head_rect = pygame.draw.circle(screen, 'blue', (self.x, self.y), 10)
        for body in self.body:
            pygame.draw.circle(screen, 'red', (body['x'], body['y']), 10)

    def level_up(self):
        self.speed += 1

    def check_end_game(self):
        if (self.x <= 10 or self.x >= 790) or (self.y <= 10 or self.y >= 590):
            return True

class Food():
    def __init__(self):
        self.x = random.randint(10, 790)
        self.y = random.randint(10, 590)
        self.color = random.choice(food_color)
        #với lớp Food
        self.rect = pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

    def update(self):
        self.rect = pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

class Wall():
    def __init__(self):
        self.x = random.randint(0, 750)
        self.y = random.randint(0, 550)
        self.height = random.randint(50, 200)
        self.direction = random.randint(0, 1) # 0: vertical, 1: horizontal
        if self.direction == 0:
            self.rect = pygame.draw.rect(screen, '#0e7819', (self.x, self.y, 20, self.height))
        else:
            self.rect = pygame.draw.rect(screen, '#0e7819', (self.x, self.y, self.height, 20))

    def update(self):
        if self.direction == 0:
            self.rect = pygame.draw.rect(screen, '#0e7819', (self.x, self.y, 20, self.height))
        else:
            self.rect = pygame.draw.rect(screen, '#0e7819', (self.x, self.y, self.height, 20))

def create_wall():
    global wall_list
    numWall = random.randint(5, 15)
    wall_list = []
    for i in range(numWall):
        wall_temp = Wall()
        while wall_temp.rect.colliderect(snake.head_rect):
            wall_temp = Wall()
        for food in food_list:
            while wall_temp.rect.colliderect(food.rect):
                wall_temp = Wall()

        wall_list.append(wall_temp)

def create_food(level):
    global food_list
    numFood = random.randint(5*level, 5*level*2)
    food_list = []
    for i in range(numFood):
        food_list.append(Food())

def pause_game(text):
    global pause
    snake.drawSnake()
    for food in food_list:
        food.update()
    for wall in wall_list:
        wall.update()
    screen.blit(text, (350, 300))
    if pygame.time.get_ticks() > (freeze_time + 3000):
        pause = 0

def collide(snake, food_list):
    global score, freeze_text, freeze_time, pause
    for food in food_list:
        distance = math.sqrt((snake.x - food.x) ** 2 + (snake.y - food.y) ** 2)
        if distance <= 20:
            if food.color == 'red':
                score += 1
            elif food.color == 'pink':
                score += 2
            elif food.color == 'purple':
                score -= 2
            elif food.color == 'yellow':
                if snake.speed > 2:
                    snake.speed -= 2
                else:
                    snake.speed = 1
            elif food.color == 'orange':
                snake.speed += 2
            elif food.color == 'cyan':
                freeze_text = font.render("Freezing...", True, 'black')
                freeze_time = pygame.time.get_ticks()
                pause = 1

            if len(snake.body) == 0:
                snake.body.append({'x': snake.x, 'y': snake.y})
            else:
                snake.body.append(snake.body[-1])
            food_list.remove(food)
            break

def update_wall_food(food_list, wall_list):
    for food in food_list:
        food.update()
    for wall in wall_list:
        wall.update()

running = True
FPS = 60
clock = pygame.time.Clock()

font = pygame.font.SysFont("couriernew", 28, bold=True)
score = 0
level = 1

snake = Snake()
create_food(level)
create_wall()
is_end = False

bg = pygame.image.load('bg_Snake.png')
pause = 0 # 0: no pause, 1: frezzing, 2: level up

while running:
    clock.tick(FPS)
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    for wall in wall_list:
        if wall.rect.colliderect(snake.head_rect):
            is_end = True
            break

    is_end = is_end or snake.check_end_game()
    if is_end:
        game_over_text = font.render("GAME OVER!", True, 'black')
        replay_text = font.render("(Press Space to play again)", True, 'black')
        screen.blit(game_over_text, (320, 230))
        screen.blit(replay_text, (180, 280))
        #reset
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE] == True:
            score = 0
            level = 1
            is_end = False
            snake.__init__()
            create_food(level)
            create_wall()
            update_wall_food(food_list, wall_list)
    elif level == 4:
        win_text = font.render("YOU WIN!!!", True, 'black')
        screen.blit(win_text, (320, 230))

    elif pause > 0:
        if pause == 1:
            pause_game(freeze_text)
        else:
            pause_game(lv_up_text)
    else:
        #update
        snake.get_direction()
        snake.update()
        snake.drawSnake()
        update_wall_food(food_list, wall_list)
        #check collide
        collide(snake, food_list)
        #check level up
        if len(food_list) == 0:
            lv_up_text = font.render("Level up!", True, 'black')
            freeze_time = pygame.time.get_ticks()
            level += 1
            snake.level_up()
            pause = 2
            create_food(level)
            create_wall()

    score_text = font.render("Score: " + str(score) + ' - Level: ' + str(level), True, 'black')
    screen.blit(score_text, (0, 0))

    print(snake.body)
    pygame.display.flip()

pygame.quit()