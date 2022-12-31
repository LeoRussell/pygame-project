import pygame
import random


# Чтобы узнать больше информации об игре, ознакомьтесь с файлом readme.txt


#  ██████╗ ██████╗ ██████╗ ███████╗
# ██╔════╝██╔═══██╗██╔══██╗██╔════╝
# ██║     ██║   ██║██████╔╝█████╗  
# ██║     ██║   ██║██╔══██╗██╔══╝  
# ╚██████╗╚██████╔╝██║  ██║███████╗
#  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝                                                                    


# координаты ячеек поля.
coords = [
        [(10, 160), (170, 160), (330, 160)],
        [(10, 320), (170, 320), (330, 320)],
        [(10, 480), (170, 480), (330, 480)]
        ]

# матрица ячеек поля.
FIELD = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
            ]

# список всех возможных объектов на карте.
objects = ["Coin", "Sword_Iron", "Sword_Diamond", "Potion_Heal", "Zombie", "Helmet_Zombie", "Chest", "Diamond", "Tnt", "Creeper", "Endermite", "Enderman", "Bad_Chest", "Skeleton", "Golem"]


# статистика.
statistic = [0, 0, 0]


# проверка шагов и связанных с ней событий.
def steps_check():
    hero.steps += 1
    for row in range(len(FIELD)):
        for col in range(len(FIELD[row])): 
            try:
                FIELD[row][col].special_ability()
            except AttributeError:
                pass


# класс стартового меню.
class Start_Menu(pygame.sprite.Sprite):
    def __init__(self, width=490, height=800):
        super().__init__(menu_group)
        self.type = "menu"

        menu_image = pygame.image.load(f"data/menu/menu.png")
        menu_image = pygame.transform.scale(menu_image, (490, 800))
        self.image = menu_image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.on = True


# класс меню смерти.
class Death_Menu(pygame.sprite.Sprite):
    def __init__(self, width=490, height=800):
        super().__init__(death_menu_group)
        self.type = "menu"

        death_menu_image = pygame.image.load(f"data/menu/death_menu.png")
        death_menu_image = pygame.transform.scale(death_menu_image, (490, 800))
        self.image = death_menu_image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.on = False


# класс пустой клетки.
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


#     ██╗██╗███╗   ██╗██████╗ ██╗ ██████╗ █████╗ ████████╗ ██████╗ ██████╗ ███████╗
#    ██╔╝██║████╗  ██║██╔══██╗██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
#   ██╔╝ ██║██╔██╗ ██║██║  ██║██║██║     ███████║   ██║   ██║   ██║██████╔╝███████╗
#  ██╔╝  ██║██║╚██╗██║██║  ██║██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗╚════██║
# ██╔╝   ██║██║ ╚████║██████╔╝██║╚██████╗██║  ██║   ██║   ╚██████╔╝██║  ██║███████║
# ╚═╝    ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝


# класс индикатора следующей клетки.
class Next_Tile_Indicator(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.type = "indicator"

        next_tile_image = pygame.image.load(f"data/tile.png")
        next_tile_image = pygame.transform.scale(next_tile_image, (90, 90))
        self.image = next_tile_image
        self.rect = self.image.get_rect()
        self.rect.x = 65
        self.rect.y = 665


    def show_up(self, object):
        object = eval(f"{object}(0, 0)")
        image = pygame.transform.scale(object.image, (90, 90))
        object.kill()
        self.image = image 


# класс иконки индикатора следующей клетки.
class Next_Tile_Indicator_Icon(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.type = "indicator"

        self.image = pygame.transform.scale(pygame.image.load(f"data/indicator/next_tile/next.png"), (125, 125))
        self.rect = self.image.get_rect()
        self.rect.x = 5
        self.rect.y = 650


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
        if hero.coins > 99:
            hero.coins = 99
            coins = 99
        coin_indicator_image = pygame.image.load(f"data/indicator/gold/{coins}.png")
        coin_indicator_image = pygame.transform.scale(coin_indicator_image, (150, 150))
        self.image = coin_indicator_image
    


# класс индикатора убийств.
class Indicator_Kills(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.type = "indicator"

        kills_indicator_image = pygame.image.load(f"data/indicator/kill/0.png")
        kills_indicator_image = pygame.transform.scale(kills_indicator_image, (160, 150))
        self.image = kills_indicator_image
        self.rect = self.image.get_rect()
        self.rect.x = 330
        self.rect.y = 640

    
    def show_up(self, kills):
        if hero.enemies_killed > 99:
            hero.enemies_killed = 99
            kills = 99
        kills_indicator_image = pygame.image.load(f"data/indicator/kill/{kills}.png")
        kills_indicator_image = pygame.transform.scale(kills_indicator_image, (160, 150))
        self.image = kills_indicator_image


# класс индикатора шагов.
class Indicator_Steps(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.type = "indicator"

        steps_indicator_image = pygame.image.load(f"data/indicator/step/0.png")
        steps_indicator_image = pygame.transform.scale(steps_indicator_image, (150, 150))
        self.image = steps_indicator_image
        self.rect = self.image.get_rect()
        self.rect.x = 185
        self.rect.y = 640

    
    def show_up(self, steps):
        if hero.steps > 99:
            hero.steps = 99
            steps = 99
        steps_indicator_image = pygame.image.load(f"data/indicator/step/{steps}.png")
        steps_indicator_image = pygame.transform.scale(steps_indicator_image, (150, 150))
        self.image = steps_indicator_image


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

#     ██╗██╗  ██╗███████╗██████╗  ██████╗ 
#    ██╔╝██║  ██║██╔════╝██╔══██╗██╔═══██╗
#   ██╔╝ ███████║█████╗  ██████╔╝██║   ██║
#  ██╔╝  ██╔══██║██╔══╝  ██╔══██╗██║   ██║
# ██╔╝   ██║  ██║███████╗██║  ██║╚██████╔╝
# ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
                                        
# класс персонажа (игрока).
class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(hero_sprite)
        self.type = "hero"

        self.hero_image = pygame.image.load("data/character/steve.png")
        self.hero_image = pygame.transform.scale(self.hero_image, (150, 150))
        self.image = self.hero_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[1][1][0]
        self.rect.y = coords[1][1][1]
        
        self.coins = 0
        self.health = 6
        self.weapon = 3
        self.steps = 0
        self.enemies_killed = 0

    def do(self, direction):
        global statistic
        statistic = [self.coins, self.enemies_killed, self.steps]
        index = [item for sublist in FIELD for item in sublist].index(hero)
        row, col = index // 3, index % 3


        if direction == "LEFT":
            
            try:
                assert col - 1 >= 0
                if (FIELD[row][col - 1]).type == "active":
                    (FIELD[row][col - 1]).activate()
                elif (FIELD[row][col - 1]).type == "movable":
                    hero_reserve = FIELD[row][col]
                    (FIELD[row][col - 1]).move(row, col)
                    FIELD[row][col - 1] = hero_reserve
                    hero.rect.x = coords[row][col - 1][0]
                    
                elif (FIELD[row][col - 1]).type == "pickup":
                    try:
                        (FIELD[row][col - 1]).pick_up()

                    except AttributeError:
                        pass
                    except IndexError:
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
                elif (FIELD[row][col - 1]).type == "enemy":
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
                self.steps -= 1
            except AssertionError:
                self.steps -= 1
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
                elif (FIELD[row][col + 1]).type == "movable":
                    hero_reserve = FIELD[row][col]
                    (FIELD[row][col + 1]).move(row, col)
                    FIELD[row][col + 1] = hero_reserve
                    hero.rect.x = coords[row][col + 1][0]
                elif (FIELD[row][col + 1]).type == "pickup":
                    try:
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
                elif (FIELD[row][col + 1]).type == "enemy":
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
                self.steps -= 1
            except AttributeError:
                FIELD[row][col + 1] = hero
                FIELD[row][col] = None
                hero.rect.x = coords[row][col + 1][0]
            

        if direction == "UP":
            try:
                assert row - 1 >= 0
                if (FIELD[row - 1][col]).type == "active":
                            (FIELD[row - 1][col]).activate()
                elif (FIELD[row - 1][col]).type == "movable":
                    hero_reserve = FIELD[row][col]
                    (FIELD[row - 1][col]).move(row, col)
                    FIELD[row - 1][col] = hero_reserve
                    hero.rect.y = coords[row - 1][col][1]
                elif (FIELD[row - 1][col]).type == "pickup":
                    try:
                        (FIELD[row - 1][col]).pick_up()
                    except AttributeError:
                        pass
                    except IndexError:
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
                elif (FIELD[row - 1][col]).type == "enemy":
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
                self.steps -= 1
            except AssertionError:
                self.steps -= 1
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
                elif (FIELD[row + 1][col]).type == "movable":
                    hero_reserve = FIELD[row][col]
                    (FIELD[row + 1][col]).move(row, col)
                    FIELD[row + 1][col] = hero_reserve
                    hero.rect.y = coords[row + 1][col][1]
                elif (FIELD[row + 1][col]).type == "pickup":
                    try:
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
                elif (FIELD[row + 1][col]).type == "enemy":
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
                self.steps -= 1
            except AttributeError:
                FIELD[row + 1][col] = hero
                FIELD[row][col] = None
                hero.rect.y = coords[row + 1][col][1]

        if hero.weapon < 0:
            hero.weapon = 0

        
    def change(self, character):
        self.hero_image = pygame.image.load(f"data/character/{character}.png")
        self.hero_image = pygame.transform.scale(self.hero_image, (150, 150))
        self.image = self.hero_image


#     ██╗ █████╗  ██████╗████████╗██╗██╗   ██╗ █████╗ ████████╗███████╗
#    ██╔╝██╔══██╗██╔════╝╚══██╔══╝██║██║   ██║██╔══██╗╚══██╔══╝██╔════╝
#   ██╔╝ ███████║██║        ██║   ██║██║   ██║███████║   ██║   █████╗  
#  ██╔╝  ██╔══██║██║        ██║   ██║╚██╗ ██╔╝██╔══██║   ██║   ██╔══╝  
# ██╔╝   ██║  ██║╚██████╗   ██║   ██║ ╚████╔╝ ██║  ██║   ██║   ███████╗
# ╚═╝    ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝


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
        self.kill()
        object = (["Coin", "Sword_Iron", "Sword_Diamond", "Potion_Heal", "Diamond"])[random.randint(0, 2)]
        FIELD[row][col] = eval(f'{object}(col, row)')


# класс активного предмета "плохой" сундук.
class Bad_Chest(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(activate_group)
        self.type = "active"
        self.bad_chest_image = pygame.image.load(f"data/activate/bad_chest.png")
        self.bad_chest_image = pygame.transform.scale(self.bad_chest_image, (150, 150))
        self.image = self.bad_chest_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]
    

    def activate(self):
        index = [item for sublist in FIELD for item in sublist].index(self)
        row, col = index // 3, index % 3
        self.kill()
        object = (["Tnt", "Endermite", "Skeleton"])[random.randint(0, 2)]
        FIELD[row][col] = eval(f'{object}(col, row)')


#     ██╗███╗   ███╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ ██╗     ███████╗
#    ██╔╝████╗ ████║██╔═══██╗██║   ██║██╔══██╗██╔══██╗██║     ██╔════╝
#   ██╔╝ ██╔████╔██║██║   ██║██║   ██║███████║██████╔╝██║     █████╗  
#  ██╔╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══██║██╔══██╗██║     ██╔══╝  
# ██╔╝   ██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ██║  ██║██████╔╝███████╗███████╗
# ╚═╝    ╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝


# класс смещаемого предмета динамит.
class Tnt(pygame.sprite.Sprite):
    def __init__(self, x, y, timer=7):
        super().__init__(movable_group)
        self.type = "movable"

        self.timer = timer
        self.tnt_image = pygame.image.load(f"data/movable/tnt/{self.timer}.png")
        self.tnt_image = pygame.transform.scale(self.tnt_image, (150, 150))
        self.image = self.tnt_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]
    

    def special_ability(self):
        if self.timer > 1:
            self.timer -= 1
            self.tnt_image = pygame.image.load(f"data/movable/tnt/{self.timer}.png")
            self.tnt_image = pygame.transform.scale(self.tnt_image, (150, 150))
            self.image = self.tnt_image
        else:
            index = [item for sublist in FIELD for item in sublist].index(self)
            row, col = index // 3, index % 3
            self.kill()
            FIELD[row][col] = None

            try:
                if FIELD[row + 1][col].type != "hero":
                    FIELD[row + 1][col].kill()
                    FIELD[row + 1][col] = None
                else:
                    if FIELD[row + 1][col].health - 5 <= 0:
                        FIELD[row + 1][col].health = 0
                        FIELD[row + 1][col].kill()
                        FIELD[row + 1][col] = None
                    else:
                        FIELD[row + 1][col].health -= 5
            except IndexError:
                pass 
            
            try:
                assert row - 1 >= 0
                if FIELD[row - 1][col].type != "hero":
                    FIELD[row - 1][col].kill()
                    FIELD[row - 1][col] = None
                else:
                    if FIELD[row - 1][col].health - 5 <= 0:
                        FIELD[row - 1][col].health = 0
                        FIELD[row - 1][col].kill()
                        FIELD[row - 1][col] = None
                    else:
                        FIELD[row - 1][col].health -= 5
            except IndexError:
                pass 
            except AssertionError:
                pass

            try:
                assert col - 1 >= 0
                if FIELD[row][col - 1].type != "hero":
                    FIELD[row][col - 1].kill()
                    FIELD[row][col - 1] = None
                else:
                    if FIELD[row][col - 1].health - 5 <= 0:
                        FIELD[row][col - 1].health = 0
                        FIELD[row][col - 1].kill()
                        FIELD[row][col - 1] = None
                    else:
                        FIELD[row][col - 1].health -= 5
            except IndexError:
                pass
            except AssertionError:
                pass
            
            try:
                if FIELD[row][col + 1].type != "hero":
                    FIELD[row][col + 1].kill()
                    FIELD[row][col + 1] = None
                else:
                    if FIELD[row][col + 1].health - 5 <= 0:
                        FIELD[row][col + 1].health = 0
                        FIELD[row][col + 1].kill()
                        FIELD[row][col + 1] = None
                    else:
                        FIELD[row][col + 1].health -= 5
            except IndexError:
                pass 

            

    
    def move(self, row, col):
        FIELD[row][col] = self
        self.rect.x = coords[row][col][0]
        self.rect.y = coords[row][col][1]


#     ██╗██████╗ ██╗ ██████╗██╗  ██╗██╗   ██╗██████╗ 
#    ██╔╝██╔══██╗██║██╔════╝██║ ██╔╝██║   ██║██╔══██╗
#   ██╔╝ ██████╔╝██║██║     █████╔╝ ██║   ██║██████╔╝
#  ██╔╝  ██╔═══╝ ██║██║     ██╔═██╗ ██║   ██║██╔═══╝ 
# ██╔╝   ██║     ██║╚██████╗██║  ██╗╚██████╔╝██║     
# ╚═╝    ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  


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
        hero.coins += 1
        self.kill()


# класс пикапа-алмаза.
class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(pickup_group)
        self.type = "pickup"

        diamond_image = pygame.image.load(f"data/pickup/diamond.png")
        diamond_image = pygame.transform.scale(diamond_image, (150, 150))
        self.image = diamond_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

    
    def pick_up(self):
        hero.coins += 3
        self.kill()


# класс пикапа меча (железный).
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


# класс пикапа меча (алмазный).
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


#     ██╗███████╗███╗   ██╗███████╗███╗   ███╗██╗   ██╗
#    ██╔╝██╔════╝████╗  ██║██╔════╝████╗ ████║╚██╗ ██╔╝
#   ██╔╝ █████╗  ██╔██╗ ██║█████╗  ██╔████╔██║ ╚████╔╝ 
#  ██╔╝  ██╔══╝  ██║╚██╗██║██╔══╝  ██║╚██╔╝██║  ╚██╔╝  
# ██╔╝   ███████╗██║ ╚████║███████╗██║ ╚═╝ ██║   ██║   
# ╚═╝    ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝   ╚═╝                                                 
                                                               

# класс врага эндермит.
class Endermite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemy_group)
        self.type = "enemy"

        endermite_image = pygame.image.load(f"data/enemy/endermite/2.png")
        endermite_image = pygame.transform.scale(endermite_image, (150, 150))
        self.image = endermite_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

        self.health = 2
    
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
        hero.enemies_killed += 1

        row1, col1 = random.choice([(0, 0), (0, 2), (2, 0), (2, 2)])
        index = [item for sublist in FIELD for item in sublist].index(hero)
        x, y = index // 3, index % 3
        if x != row1 and col1 != y:
            FIELD[row1][col1].kill()
            FIELD[row1][col1] = FIELD[x][y]
            FIELD[x][y] = None
            hero.rect.x = coords[row1][col1][0]
            hero.rect.y = coords[row1][col1][1]
    
    def show_health(self):
        endermite_image = pygame.image.load(f"data/enemy/endermite/{self.health}.png")
        endermite_image = pygame.transform.scale(endermite_image, (150, 150))
        self.image = endermite_image
    
    def special_ability(self):
        pass


# класс врага скелет.
class Skeleton(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemy_group)
        self.type = "enemy"

        skeleton_image = pygame.image.load(f"data/enemy/skeleton/4.png")
        skeleton_image = pygame.transform.scale(skeleton_image, (150, 150))
        self.image = skeleton_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

        self.health = 4
    
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
        hero.enemies_killed += 1
    
    def show_health(self):
        skeleton_image = pygame.image.load(f"data/enemy/skeleton/{self.health}.png")
        skeleton_image = pygame.transform.scale(skeleton_image, (150, 150))
        self.image = skeleton_image


# класс врага эндермена.
class Enderman(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemy_group)
        self.type = "enemy"

        enderman_image = pygame.image.load(f"data/enemy/enderman/4.png")
        enderman_image = pygame.transform.scale(enderman_image, (150, 150))
        self.image = enderman_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

        self.health = 4
    
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
        hero.enemies_killed += 1
    
    def show_health(self):
        enderman_image = pygame.image.load(f"data/enemy/enderman/{self.health}.png")
        enderman_image = pygame.transform.scale(enderman_image, (150, 150))
        self.image = enderman_image
    
    def special_ability(self):
        index = [item for sublist in FIELD for item in sublist].index(self)
        row, col = index // 3, index % 3
        row_to_set, col_to_set = random.randint(0, 2), random.randint(0, 2)
        if FIELD[row_to_set][col_to_set].type != "hero":
            A = FIELD[row_to_set][col_to_set]
            FIELD[row_to_set][col_to_set] = FIELD[row][col]
            FIELD[row][col] = A

            FIELD[row][col].rect.x = coords[row][col][0]
            FIELD[row][col].rect.y = coords[row][col][1]

            self.rect.x = coords[row_to_set][col_to_set][0]
            self.rect.y = coords[row_to_set][col_to_set][1]


# класс врага крипера.
class Creeper(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemy_group)
        self.type = "enemy"

        creeper_image = pygame.image.load(f"data/enemy/creeper/4.png")
        creeper_image = pygame.transform.scale(creeper_image, (150, 150))
        self.image = creeper_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

        self.health = 4
    
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
        FIELD[row][col] = Tnt(col, row, 4)
        hero.enemies_killed += 1
    
    def show_health(self):
        creeper_image = pygame.image.load(f"data/enemy/creeper/{self.health}.png")
        creeper_image = pygame.transform.scale(creeper_image, (150, 150))
        self.image = creeper_image
    
    def special_ability(self):
        pass


# класс врага зомби.
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
        hero.enemies_killed += 1

    def show_health(self):
        zombie_image = pygame.image.load(f"data/enemy/zombie/{self.health}.png")
        zombie_image = pygame.transform.scale(zombie_image, (150, 150))
        self.image = zombie_image
    
    def special_ability(self):
        pass


# класс голема.
class Golem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(enemy_group)
        self.type = "enemy"

        golem_image = pygame.image.load(f"data/enemy/golem/8.png")
        golem_image = pygame.transform.scale(golem_image, (150, 150))
        self.image = golem_image
        self.rect = self.image.get_rect()
        self.rect.x = coords[y][x][0]
        self.rect.y = coords[y][x][1]

        self.health = 8
    
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
        FIELD[row][col] = Diamond(col, row)
        hero.enemies_killed += 1
    
    def show_health(self):
        golem_image = pygame.image.load(f"data/enemy/golem/{self.health}.png")
        golem_image = pygame.transform.scale(golem_image, (150, 150))
        self.image = golem_image
    
    def special_ability(self):
        pass

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
        hero.enemies_killed += 1
    
    def show_health(self):
        zombie_image = pygame.image.load(f"data/enemy/zombie/{self.health}.png")
        zombie_image = pygame.transform.scale(zombie_image, (150, 150))
        self.image = zombie_image
    
    def special_ability(self):
        pass


#     ██╗██╗███╗   ██╗██╗████████╗██╗ █████╗ ██╗     ██╗███████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗
#    ██╔╝██║████╗  ██║██║╚══██╔══╝██║██╔══██╗██║     ██║╚══███╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
#   ██╔╝ ██║██╔██╗ ██║██║   ██║   ██║███████║██║     ██║  ███╔╝ ███████║   ██║   ██║██║   ██║██╔██╗ ██║
#  ██╔╝  ██║██║╚██╗██║██║   ██║   ██║██╔══██║██║     ██║ ███╔╝  ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║
# ██╔╝   ██║██║ ╚████║██║   ██║   ██║██║  ██║███████╗██║███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
# ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                     

# инициализация и наименование.
pygame.init()
pygame.display.set_caption('Minicruft Dumgeons')

# создание окна по размеру.
size = width, height = 490, 800
screen = pygame.display.set_mode(size)

# создание меню.
menu_group = pygame.sprite.Group()
menu = Start_Menu()
death_menu_group = pygame.sprite.Group()
death_menu = Death_Menu()
indicator1 = Indicator_Coins(death_menu_group)
indicator1.rect.x = 20
indicator1.rect.y = 350
indicator2 = Indicator_Kills(death_menu_group)
indicator2.rect.x = 185
indicator2.rect.y = 350
indicator3 = Indicator_Steps(death_menu_group)
indicator3.rect.x = 350
indicator3.rect.y = 350

# создание индикаторов.
indicators_group = pygame.sprite.Group()
coin_indicator = Indicator_Coins(indicators_group)
health_indicator = Indicator_Health(indicators_group)
weapon_indicator = Indicator_Weapon(indicators_group)
next_tile_indicator = Next_Tile_Indicator(indicators_group)
next_tile_indicator_icon = Next_Tile_Indicator_Icon(indicators_group)
kills_indicator = Indicator_Kills(indicators_group)
steps_indicator = Indicator_Steps(indicators_group)

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
movable_group = pygame.sprite.Group()

# фиксирование кадров в секунду.
clock = pygame.time.Clock()
fps = 15

# первый устанавливаемый объект
object = random.choice(objects)

# запуск программы.
running = True
while running:
    screen.fill((50, 50, 50))
        
    # прорисовка спрайтов.
    tiles.draw(screen)
    pickup_group.draw(screen)
    enemy_group.draw(screen)
    movable_group.draw(screen)
    indicators_group.draw(screen)
    activate_group.draw(screen)
    hero_sprite.draw(screen)

    # отображение индикаторов.
    coin_indicator.show_up(hero.coins)
    health_indicator.show_up(hero.health)
    weapon_indicator.show_up(hero.weapon)
    steps_indicator.show_up(hero.steps)
    kills_indicator.show_up(hero.enemies_killed)

    # отображение стартового меню.
    if menu.on == True:
        menu_group.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.on = False
                else:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        hero.change("alex")
                        menu.on = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        hero.change("steve")
                        menu.on = False
    
    # отображение меню при смерти.
    elif death_menu.on == True:
        indicator1.show_up(statistic[0]) 
        indicator2.show_up(statistic[1])
        indicator3.show_up(statistic[-1])
        death_menu_group.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    if event.key == pygame.K_SPACE:
                        death_menu.on = False
                        menu.on = True
                        for row in range(len(FIELD)):
                            for col in range(len(FIELD[row])):
                                FIELD[row][col].kill()
                                FIELD[row][col] = eval(f'{object}(col, row)')
                                object = random.choice(objects)
                        FIELD[1][1].kill()
                        hero = Character()
                        FIELD[1][1] = hero

                        

    else:
        # основной процесс игры.
        for row in range(len(FIELD)):
            for col in range(len(FIELD[row])):
                if FIELD[row][col] == None:
                    FIELD[row][col] = eval(f'{object}(col, row)')
                    object = random.choice(objects)
                    next_tile_indicator.show_up(object)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.on = True
                else:
                    try:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            hero.do("LEFT")
                            steps_check()
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            hero.do("RIGHT")
                            steps_check()
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            hero.do("DOWN")
                            steps_check()
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            hero.do("UP")
                            steps_check()

                    except ValueError:
                        death_menu.on = True
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

