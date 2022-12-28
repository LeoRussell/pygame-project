import pygame


# -----------------------------------
#   ___ _      _   ___ ___ ___ ___  
#  / __| |    /_\ / __/ __| __/ __| 
# | (__| |__ / _ \\__ \__ \ _|\__ \ 
#  \___|____/_/ \_\___/___/___|___/ 
#
# -----------------------------------


coords = [
        [(10, 160), (170, 160), (330, 160)],
        [(10, 320), (170, 320), (330, 320)],
        [(10, 480), (170, 480), (330, 480)]
        ]


# класс персонажа (игрока).
class Character(pygame.sprite.Sprite):
    hero_image = pygame.image.load("data/character/steve.png")
    hero_image = pygame.transform.scale(hero_image, (150, 150))


    def __init__(self, group):
        super().__init__(group)
        self.image = self.hero_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[1][1][0]
        self.rect.y = coords[1][1][1]
        
        # статы героя.
        self.coins = 0
        self.health_points = 10
        self.weapon_points = 3
    
    def move(self, direction):
        index = [item for sublist in FIELD for item in sublist].index(hero)
        row, col = index // 3, index % 3

        if direction == "LEFT":
            try:
                assert col - 1 >= 0
                if (FIELD[row][col - 1]).type == "pickup":
                    (FIELD[row][col - 1]).pick_up()
            except AttributeError:
                pass
            except IndexError:
                pass
            except AssertionError:
                pass

            try:
                assert col - 1 >= 0
                FIELD[row][col - 1] = hero
                FIELD[row][col] = None
                hero.rect.x = coords[row][col - 1][0]
                print(FIELD)
            except IndexError:
                pass
            except AssertionError:
                pass

        if direction == "RIGHT":
            try:
                if (FIELD[row][col + 1]).type == "pickup":
                    (FIELD[row][col + 1]).pick_up()
            except AttributeError:
                pass
            except IndexError:
                pass

            try:
                FIELD[row][col + 1] = hero
                FIELD[row][col] = None
                hero.rect.x = coords[row][col + 1][0]
                print(FIELD)
            except IndexError:
                pass

        if direction == "UP":
            try:
                assert row - 1 >= 0
                if (FIELD[row - 1][col]).type == "pickup":
                    (FIELD[row - 1][col]).pick_up()
            except AttributeError:
                pass
            except IndexError:
                pass
            except AssertionError:
                pass

            try:
                assert row - 1 >= 0
                FIELD[row - 1][col] = hero
                FIELD[row][col] = None
                hero.rect.y = coords[row - 1][col][1]
                print(FIELD)
            except IndexError:
                pass
            except AssertionError:
                pass

        if direction == "DOWN":
            try:
                if (FIELD[row + 1][col]).type == "pickup":
                    (FIELD[row + 1][col]).pick_up()
            except AttributeError:
                pass
            except IndexError:
                pass
            
            try:    
                FIELD[row + 1][col] = hero
                FIELD[row][col] = None
                hero.rect.y = coords[row + 1][col][1]
                print(FIELD)
            except IndexError:
                pass


# матрица ячеек поля.
FIELD = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
            ]


# материнский класс пикапов.
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        super().__init__(group)
        self.type = "pickup"

        coin_image = pygame.image.load(f"data/pickup/gold.png")
        coin_image = pygame.transform.scale(coin_image, (150, 150))
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

    
    def pick_up(self):
        hero.coins += 1
        self.kill()

# -----------------------
#   ___ _  _ ___ _____  
#  |_ _| \| |_ _|_   _| 
#   | || .` || |  | |   
#  |___|_|\_|___| |_|   
#
# -----------------------


# инициализация и наименование.
pygame.init()
pygame.display.set_caption('Игра?')

# создание окна по размеру.
size = width, height = 490, 650
screen = pygame.display.set_mode(size)

# создание героя.
hero_sprite = pygame.sprite.Group()
hero = Character(hero_sprite)
FIELD[1][1] = hero

# создание группы пикапов.
pickup_group = pygame.sprite.Group()

# создание пробной монетки.
x, y = 0, 2
FIELD[x][y] = Coin(y, x, pickup_group)

# фиксирование кадров в секунду на отметке в 60 или 30.
clock = pygame.time.Clock()
fps = 30

# запуск программы.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.move("LEFT")
            if event.key == pygame.K_RIGHT:
                hero.move("RIGHT")
            if event.key == pygame.K_DOWN:
                hero.move("DOWN")
            if event.key == pygame.K_UP:
                hero.move("UP")

    screen.fill((140, 110, 45))

    # прорисовка спрайтов.
    hero_sprite.draw(screen)
    pickup_group.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

