import pygame

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


# инициализация и наименование.
pygame.init()
pygame.display.set_caption('Игра?')

# создание поля и его спрайта. 
field = pygame.sprite.Group()
Field(field)

# создание окна по размеру.
size = width, height = 800, 650
screen = pygame.display.set_mode(size)

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
    field.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

