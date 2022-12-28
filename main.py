import pygame
import random


#     ██╗███████╗████████╗██████╗ ██╗   ██╗ ██████╗████████╗██╗   ██╗██████╗ ███████╗
#    ██╔╝██╔════╝╚══██╔══╝██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
#   ██╔╝ ███████╗   ██║   ██████╔╝██║   ██║██║        ██║   ██║   ██║██████╔╝█████╗  
#  ██╔╝  ╚════██║   ██║   ██╔══██╗██║   ██║██║        ██║   ██║   ██║██╔══██╗██╔══╝  
# ██╔╝   ███████║   ██║   ██║  ██║╚██████╔╝╚██████╗   ██║   ╚██████╔╝██║  ██║███████╗
# ╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝                                                                           


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
        self.health = 6
        self.weapon = 3

    
    def do(self, direction):
        index = [item for sublist in FIELD for item in sublist].index(hero)
        row, col = index // 3, index % 3
        print("health:", self.health, "money:", self.coins, "weapon:", self.weapon)
        if direction == "LEFT":
            try:
                if (FIELD[row][col - 1]).type != "enemy":
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

                    except IndexError:
                        pass
                    except AssertionError:
                        pass
                else:
                    if self.weapon > 0:
                        FIELD[row][col - 1].deal_damage(self.weapon)
                    elif self.health > FIELD[row][col + 1].health:
                        FIELD[row][col - 1].deal_damage(self.health, False)
                    else:
                        self.kill()
                        FIELD[row][col] = None
            
            except IndexError:
                pass
            except AttributeError:
                try:
                    assert col - 1 >= 0
                    FIELD[row][col - 1] = hero
                    FIELD[row][col] = None
                    hero.rect.x = coords[row][col - 1][0]
                except AssertionError:
                    pass

        if direction == "RIGHT":
            try:
                if (FIELD[row][col + 1]).type != "enemy":
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
                    except IndexError:
                        pass
                else:
                    if self.weapon > 0:
                        FIELD[row][col + 1].deal_damage(self.weapon, True)
                    elif self.health > FIELD[row][col + 1].health:
                        FIELD[row][col + 1].deal_damage(self.health, False)
                    else:
                        self.kill()
                        FIELD[row][col] = None

            except IndexError:
                pass
            except AttributeError:
                FIELD[row][col + 1] = hero
                FIELD[row][col] = None
                hero.rect.x = coords[row][col + 1][0]

        if direction == "UP":
            try:
                if (FIELD[row - 1][col]).type != "enemy":
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
                    except IndexError:
                        pass
                    except AssertionError:
                        pass
                else:
                    if self.weapon > 0:
                        FIELD[row - 1][col].deal_damage(self.weapon, True)
                    elif self.health > FIELD[row - 1][col].health:
                        FIELD[row - 1][col].deal_damage(self.health, False)
                    else:
                        self.kill()
                        FIELD[row][col] = None

            except IndexError:
                pass
            except AttributeError:
                try:
                    assert row - 1 >= 0
                    FIELD[row - 1][col] = hero
                    FIELD[row][col] = None
                    hero.rect.y = coords[row - 1][col][1]
                except AssertionError:
                    pass

        if direction == "DOWN":
            try:
                if (FIELD[row + 1][col]).type != "enemy":
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
                    except IndexError:
                        pass
                else:
                    if self.weapon > 0:
                        FIELD[row + 1][col].deal_damage(self.weapon, True)
                    elif self.health > FIELD[row + 1][col].health:
                        FIELD[row + 1][col].deal_damage(self.health, False)
                    else:
                        self.kill()
                        FIELD[row][col] = None
            
            #except IndexError:
                pass
            except AttributeError:
                FIELD[row + 1][col] = hero
                FIELD[row][col] = None
                hero.rect.y = coords[row + 1][col][1]


# матрица ячеек поля.
FIELD = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
            ]


# класс пикапа-монетки.
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


# класс врага-зомби.
class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        super().__init__(group)
        self.type = "enemy"

        zombie_image = pygame.image.load(f"data/enemy/zombie/6.png")
        zombie_image = pygame.transform.scale(zombie_image, (150, 150))
        self.image = zombie_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

        # статы зомби.
        self.health = 6
    
    def deal_damage(self, damage_dealt, weapon):
        if weapon == True:
            if self.health - damage_dealt <= 0:
                index = [item for sublist in FIELD for item in sublist].index(self)
                row, col = index // 3, index % 3
                self.kill()
                FIELD[row][col] = None
                hero.weapon = abs(self.health - damage_dealt)
            else:
                self.health -= damage_dealt
                zombie_image = pygame.image.load(f"data/enemy/zombie/{self.health}.png")
                zombie_image = pygame.transform.scale(zombie_image, (150, 150))
                self.image = zombie_image
                hero.weapon = self.health - damage_dealt
        else:
            if self.health - damage_dealt <= 0:
                index = [item for sublist in FIELD for item in sublist].index(self)
                row, col = index // 3, index % 3
                hero.health -= self.health
                self.kill()
                FIELD[row][col] = None
                
            else:
                self.health -= damage_dealt
                zombie_image = pygame.image.load(f"data/enemy/zombie/{self.health}.png")
                zombie_image = pygame.transform.scale(zombie_image, (150, 150))
                self.image = zombie_image
                hero.weapon = self.health - damage_dealt

            


#     ██╗██╗███╗   ██╗██╗████████╗██╗ █████╗ ██╗     ██╗███████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
#    ██╔╝██║████╗  ██║██║╚══██╔══╝██║██╔══██╗██║     ██║╚══███╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
#   ██╔╝ ██║██╔██╗ ██║██║   ██║   ██║███████║██║     ██║  ███╔╝ ███████║   ██║   ██║██║   ██║██╔██╗ ██║
#  ██╔╝  ██║██║╚██╗██║██║   ██║   ██║██╔══██║██║     ██║ ███╔╝  ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
# ██╔╝   ██║██║ ╚████║██║   ██║   ██║██║  ██║███████╗██║███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
# ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                     

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

# создание группы пикапов и группы врагов.
pickup_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# создание пробной монетки.
x, y = 0, 2
FIELD[x][y] = Coin(y, x, pickup_group)

# создание пробного зомби.
x, y = 2, 2
FIELD[x][y] = Zombie(y, x, pickup_group)

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
            try:
                if event.key == pygame.K_LEFT:
                    hero.do("LEFT")
                if event.key == pygame.K_RIGHT:
                    hero.do("RIGHT")
                if event.key == pygame.K_DOWN:
                    hero.do("DOWN")
                if event.key == pygame.K_UP:
                    hero.do("UP")
            except ValueError:
                print("Вы погибли и не можете двигаться.", random.randint(1, 8))

    screen.fill((140, 110, 45))

    # прорисовка спрайтов.
    hero_sprite.draw(screen)
    pickup_group.draw(screen)
    enemy_group.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

