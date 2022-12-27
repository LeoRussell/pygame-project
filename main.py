import pygame


# -----------------------------------
#   ___ _      _   ___ ___ ___ ___  
#  / __| |    /_\ / __/ __| __/ __| 
# | (__| |__ / _ \\__ \__ \ _|\__ \ 
#  \___|____/_/ \_\___/___/___|___/ 
#
# -----------------------------------


# класс персонажа (игрока).
class Character(pygame.sprite.Sprite):
    hero_image = pygame.image.load("data/hero.png")
    hero_image = pygame.transform.scale(hero_image, (140, 170))


    def __init__(self, group):
        super().__init__(group)
        self.image = self.hero_image
        self.rect = self.image.get_rect()
        self.rect.x = 201
        self.rect.y = 100
        
        # статы героя.
        self.health_points = 100
        self.weapon_points = 50
    
    def move(self, direction):
        index = [item for sublist in field.tiles for item in sublist].index(hero)
        row, col = index // 3, index % 3
        if direction == "LEFT":
            try:
                assert col - 1 >= 0
                field.tiles[row][col - 1] = hero
                field.tiles[row][col] = None
                hero.rect.x -= 125
            except IndexError:
                pass
            except AssertionError:
                pass
        if direction == "RIGHT":
            try:
                field.tiles[row][col + 1] = hero
                field.tiles[row][col] = None
                hero.rect.x += 125
            except IndexError:
                pass
        if direction == "UP":
            try:
                assert row - 1 >= 0
                field.tiles[row - 1][col] = hero
                field.tiles[row][col] = None
                hero.rect.y -= 125
            except IndexError:
                pass
            except AssertionError:
                pass
        if direction == "DOWN":
            try:    
                field.tiles[row + 1][col] = hero
                field.tiles[row][col] = None
                hero.rect.y += 125
            except IndexError:
                pass


# класс поля.
class Field(pygame.sprite.Sprite):
    field_image = pygame.image.load("data/field.png")
    field_image = pygame.transform.scale(field_image, (500, 500))


    def __init__(self, group):
        super().__init__(group)
        self.image = self.field_image
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 50
        self.tiles = [
                    [None, None, None],
                    [None, None, None],
                    [None, None, None]
                    ]


# материнский класс пикапов.
class Pickup(pygame.sprite.Sprite):
    def __init__(self, image, group):
        super().__init__(group)
        pickup_image = pygame.image.load(f"data/{image}")
        pickup_image = pygame.transform.scale(pickup_image, (140, 170))
        self.image = self.pickup_image
        self.rect = self.image.get_rect()
        self.rect.x = None
        self.rect.y = None
        
        # "вместимость" пикапа.
        self.value = 0
    

    # функция получения пикапа
    def pickup_get(self):
        # self.hero_pickup_value += self.value
        index = [item for sublist in field.tiles for item in sublist].index(hero)
        row, col = index // 3, index % 3
        field.tiles[row][col] == None
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
size = width, height = 800, 650
screen = pygame.display.set_mode(size)

# создание поля и его спрайта. 
field_sprite = pygame.sprite.Group()
field = Field(field_sprite)

# создание героя.
hero_sprite = pygame.sprite.Group()
hero = Character(hero_sprite)
field.tiles[0][0] = hero

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

    screen.fill((255, 255, 255))

    # прорисовка спрайтов.
    field_sprite.draw(screen)
    hero_sprite.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

