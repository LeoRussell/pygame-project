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
field = pygame.sprite.Group()
Field(field)

# создание героя.
hero = pygame.sprite.Group()
Character(hero)

# фиксирование кадров в секунду на отметке в 60 или 30.
clock = pygame.time.Clock()
fps = 30

# запуск программы.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # прорисовка спрайтов.
    field.draw(screen)
    hero.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

