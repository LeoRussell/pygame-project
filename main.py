import pygame
import random


#     ██╗███████╗████████╗██████╗ ██╗   ██╗ ██████╗████████╗██╗   ██╗██████╗ ███████╗
#    ██╔╝██╔════╝╚══██╔══╝██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
#   ██╔╝ ███████╗   ██║   ██████╔╝██║   ██║██║        ██║   ██║   ██║██████╔╝█████╗  
#  ██╔╝  ╚════██║   ██║   ██╔══██╗██║   ██║██║        ██║   ██║   ██║██╔══██╗██╔══╝  
# ██╔╝   ███████║   ██║   ██║  ██║╚██████╔╝╚██████╗   ██║   ╚██████╔╝██║  ██║███████╗
# ╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝                                                                           


# координаты ячеек поля.
coords = [
        [(10, 160), (170, 160), (330, 160)],
        [(10, 320), (170, 320), (330, 320)],
        [(10, 480), (170, 480), (330, 480)]
        ]

class Blank_Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(tiles)
        self.type = "tile"

        tile_image = pygame.image.load(f"data/tile.png")
        tile_image = pygame.transform.scale(tile_image, (150, 150))
        self.image = tile_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

# класс индикатора монеток.
class Indicator_Coins(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.type = "indicator"

        coin_indicator_image = pygame.image.load(f"data/indicator/gold/0.png")
        coin_indicator_image = pygame.transform.scale(coin_indicator_image, (150, 150))
        self.image = coin_indicator_image
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

    
    def show_up(self, coins):
        coin_indicator_image = pygame.image.load(f"data/indicator/gold/{coins}.png")
        coin_indicator_image = pygame.transform.scale(coin_indicator_image, (150, 150))
        self.image = coin_indicator_image


# класс индикатора жизней.
class Indicator_Health(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.type = "indicator"

        health_indicator_image = pygame.image.load(f"data/indicator/health/0.png")
        health_indicator_image = pygame.transform.scale(health_indicator_image, (150, 150))
        self.image = health_indicator_image
        self.rect = self.image.get_rect()
        self.rect.x = 165
        self.rect.y = 10

    
    def show_up(self, health):
        health_indicator_image = pygame.image.load(f"data/indicator/health/{health}.png")
        health_indicator_image = pygame.transform.scale(health_indicator_image, (150, 150))
        self.image = health_indicator_image


# класс индикатора оружия.
class Indicator_Weapon(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.type = "indicator"

        weapon_indicator_image = pygame.image.load(f"data/indicator/weapon/0.png")
        weapon_indicator_image = pygame.transform.scale(weapon_indicator_image, (150, 150))
        self.image = weapon_indicator_image
        self.rect = self.image.get_rect()
        self.rect.x = 325
        self.rect.y = 10

    
    def show_up(self, weapon):
        weapon_indicator_image = pygame.image.load(f"data/indicator/weapon/{weapon}.png")
        weapon_indicator_image = pygame.transform.scale(weapon_indicator_image, (150, 150))
        self.image = weapon_indicator_image


# класс персонажа (игрока).
class Character(pygame.sprite.Sprite):
    hero_image = pygame.image.load("data/character/alex.png")
    hero_image = pygame.transform.scale(hero_image, (150, 150))


    def __init__(self):
        super().__init__(hero_sprite)
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


        if direction == "LEFT":
            try:
                assert col - 1 >= 0
                if (FIELD[row][col - 1]).type == "active":
                            (FIELD[row][col - 1]).activate()
                elif (FIELD[row][col - 1]).type != "enemy":
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
                        FIELD[row][col - 1].deal_damage(self.weapon, True)
                    elif self.health > FIELD[row][col - 1].health:
                        FIELD[row][col - 1].deal_damage(self.health, False)
                    else:
                        if FIELD[row][col - 1].health - self.health == 0:
                            FIELD[row][col - 1].die(row, col - 1)
                        else:
                            FIELD[row][col - 1].health -= self.health
                            FIELD[row][col - 1].show_health()
                        self.health = 0
                        self.kill()
                        FIELD[row][col] = None
            
            except IndexError:
                pass
            except AssertionError:
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
                if (FIELD[row][col + 1]).type == "active":
                            (FIELD[row][col + 1]).activate()
                elif (FIELD[row][col + 1]).type != "enemy":
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
                        if FIELD[row][col + 1].health - self.health == 0:
                            FIELD[row][col + 1].die(row, col + 1)
                        else:
                            FIELD[row][col + 1].health -= self.health
                            FIELD[row][col + 1].show_health()
                        self.health = 0
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
                assert row - 1 >= 0
                if (FIELD[row - 1][col]).type == "active":
                            (FIELD[row - 1][col]).activate()
                elif (FIELD[row - 1][col]).type != "enemy":
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
                        if FIELD[row - 1][col].health - self.health == 0:
                            FIELD[row - 1][col].die(row - 1, col)
                        else:
                            FIELD[row - 1][col].health -= self.health
                            FIELD[row - 1][col].show_health()
                        self.health = 0
                        self.kill()
                        FIELD[row][col] = None

            except IndexError:
                pass
            except AssertionError:
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
                if (FIELD[row + 1][col]).type == "active":
                            (FIELD[row + 1][col]).activate()
                elif (FIELD[row + 1][col]).type != "enemy":
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
                        if FIELD[row + 1][col].health - self.health == 0:
                            FIELD[row + 1][col].die(row + 1, col)
                        else:
                            FIELD[row + 1][col].health -= self.health
                            FIELD[row + 1][col].show_health()
                        self.health = 0
                        self.kill()
                        FIELD[row][col] = None
            
            except IndexError:
                pass
            except AttributeError:
                FIELD[row + 1][col] = hero
                FIELD[row][col] = None
                hero.rect.y = coords[row + 1][col][1]

        if hero.weapon < 0:
            hero.weapon = 0


# матрица ячеек поля.
FIELD = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
            ]


# класс пикапа-леченья (зелье).
class Potion_Heal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(pickup_group)
        self.type = "pickup"

        heal_image = pygame.image.load(f"data/pickup/heal_potion.png")
        heal_image = pygame.transform.scale(heal_image, (150, 150))
        self.image = heal_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

    
    def pick_up(self):
        if hero.health + 3 > 10:
            hero.health = 10
        else:
            hero.health += 3
        self.kill()

# класс пикапа-монетки.
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(pickup_group)
        self.type = "pickup"

        coin_image = pygame.image.load(f"data/pickup/gold.png")
        coin_image = pygame.transform.scale(coin_image, (150, 150))
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

    
    def pick_up(self):
        if hero.coins + 1 > 99:
            hero.coins == 99
        else:
            hero.coins += 1
        self.kill()


# класс активного предмета сундук.
class Chest(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(activate_group)
        self.type = "active"
        self.chest_image = pygame.image.load(f"data/activate/chest.png")
        self.chest_image = pygame.transform.scale(self.chest_image, (150, 150))
        self.image = self.chest_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]
    

    def activate(self):
        index = [item for sublist in FIELD for item in sublist].index(self)
        row, col = index // 3, index % 3
        chest_image = pygame.transform.scale(self.chest_image, (160, 160))
        chest_image = pygame.transform.scale(self.chest_image, (150, 150))
        self.kill()
        object = (["Coin", "Sword_Iron", "Sword_Diamond", "Potion_Heal"])[random.randint(0, 2)]
        FIELD[row][col] = eval(f'{object}(col, row)')
                

# класс пикапа-меча (железный).
class Sword_Iron(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(pickup_group)
        self.type = "pickup"

        weapon_image = pygame.image.load(f"data/pickup/iron_sword.png")
        weapon_image = pygame.transform.scale(weapon_image, (150, 150))
        self.image = weapon_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

    
    def pick_up(self):
        if hero.weapon + 5 > 15:
            hero.weapon = 15
        else:
            hero.weapon += 5
        self.kill()


# класс пикапа-меча (алмазный).
class Sword_Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(pickup_group)
        self.type = "pickup"

        weapon_image = pygame.image.load(f"data/pickup/diamond_sword.png")
        weapon_image = pygame.transform.scale(weapon_image, (150, 150))
        self.image = weapon_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

    
    def pick_up(self):
        if hero.weapon + 8 > 15:
            hero.weapon = 15
        else:
            hero.weapon += 8
        self.kill()


# класс врага-зомби.
class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemy_group)
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
                self.die(row, col)
                hero.weapon = hero.weapon - self.health
            else:
                self.health -= damage_dealt
                self.show_health()
                hero.weapon = 0
        else:
            if self.health - damage_dealt <= 0:
                index = [item for sublist in FIELD for item in sublist].index(self)
                row, col = index // 3, index % 3
                hero.health -= self.health
                self.die(row, col)
                
            else:
                self.health -= damage_dealt
                self.show_health()
                
    
    def die(self, row, col):
        self.kill()
        FIELD[row][col] = Coin(col, row)
    
    def show_health(self):
        zombie_image = pygame.image.load(f"data/enemy/zombie/{self.health}.png")
        zombie_image = pygame.transform.scale(zombie_image, (150, 150))
        self.image = zombie_image


# класс врага зомби в шлеме.
class Helmet_Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemy_group)
        self.type = "enemy"

        zombie_image = pygame.image.load(f"data/enemy/helmet_zombie/7.png")
        zombie_image = pygame.transform.scale(zombie_image, (150, 150))
        self.image = zombie_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

        # статы зомби.
        self.health = 7
    
    def deal_damage(self, damage_dealt, weapon):
        if weapon == True:
            if self.health - damage_dealt <= 0:
                index = [item for sublist in FIELD for item in sublist].index(self)
                row, col = index // 3, index % 3
                self.die(row, col)
                hero.weapon = hero.weapon - self.health
            else:
                self.health -= damage_dealt
                self.show_health()
                hero.weapon = 0
        else:
            if self.health - damage_dealt <= 0:
                index = [item for sublist in FIELD for item in sublist].index(self)
                row, col = index // 3, index % 3
                hero.health -= self.health
                self.die(row, col)
                
            else:
                self.health -= damage_dealt
                self.show_health()
                
    
    def die(self, row, col):
        self.kill()
        FIELD[row][col] = Coin(col, row)
    
    def show_health(self):
        zombie_image = pygame.image.load(f"data/enemy/zombie/{self.health}.png")
        zombie_image = pygame.transform.scale(zombie_image, (150, 150))
        self.image = zombie_image

objects = ["Coin", "Sword_Iron", "Sword_Diamond", "Potion_Heal", "Zombie", "Helmet_Zombie", "Chest"]

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

# создание индикаторов.
indicators_group = pygame.sprite.Group()
coin_indicator = Indicator_Coins(indicators_group)
health_indicator = Indicator_Health(indicators_group)
weapon_indicator = Indicator_Weapon(indicators_group)

# создание пустых тайлов.
tiles = pygame.sprite.Group()
for row in range(len(FIELD)):
    for col in range(len(FIELD[row])):
        Blank_Tile(col, row)

# создание героя.
hero_sprite = pygame.sprite.Group()
hero = Character()
FIELD[1][1] = hero

# создание групп спрайтов.
pickup_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
activate_group = pygame.sprite.Group()

# фиксирование кадров в секунду.
clock = pygame.time.Clock()
fps = 15

# запуск программы.
running = True
while running:
    for row in range(len(FIELD)):
        for col in range(len(FIELD[row])):
            if FIELD[row][col] == None:
                object = random.choice(objects)
                FIELD[row][col] = eval(f'{object}(col, row)')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                try:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        hero.do("LEFT")
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        hero.do("RIGHT")
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        hero.do("DOWN")
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        hero.do("UP")
                except ValueError:
                    print("Вы погибли и не можете двигаться.", random.randint(1, 8))

    screen.fill((50, 50, 50))
    
    # прорисовка спрайтов.
    tiles.draw(screen)
    pickup_group.draw(screen)
    enemy_group.draw(screen)
    indicators_group.draw(screen)
    activate_group.draw(screen)
    hero_sprite.draw(screen)

    # отображение индикаторов.
    coin_indicator.show_up(hero.coins)
    health_indicator.show_up(hero.health)
    weapon_indicator.show_up(hero.weapon)
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

