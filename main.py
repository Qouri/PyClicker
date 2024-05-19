from pygame import *
from random import *
font.init()

WIN_WIDTH = 1000
WIN_HEIGHT = 600

FPS = 120

plus_coins = 1
coins = 0

plus_auto = 0
auto_clicer = 0

schot = 0
timerr = False
Tab = 1

font1 = font.SysFont('Arial', 80)

COINS_TXT = font1.render((':' + str(coins)), True, (140, 59, 32))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        super().__init__()
        self.player_image = player_image
        self.image = back = transform.scale(image.load(self.player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def click(self):
        global plus_coins
        global coins
        global timerr
        coins += plus_coins
        timerr = True
        self.image = back = transform.scale(image.load(self.player_image), (250, 250))
        self.rect.x = 175
        self.rect.y = 275
        print(coins)

class Button(GameSprite):
    def click(self, var1):
        var1 *= -1
        print(Tab)
        return var1

    def plus(self, var1, cost):
        global coins
        global plus_coins
        coins -= cost
        plus_coins += var1
        print(coins, plus_coins)
        
    def plus_auto(self, var1, cost):
        global coins
        global plus_auto
        coins -= cost
        plus_auto += var1
        print(coins, plus_auto)
        

window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))

coin = Player('coin.png', 150, 250, 300, 300)
menu = GameSprite('menu.png', 600, 0, 400, 600)

coins_otobroshenie = GameSprite('coin.png', 5, 5, 100, 100)

clock = time.Clock()

game = True

shop_button = Button('shop_dark.png', 600, 0, 200, 50)
boost_button = Button('boosts_dark.png', 800, 0, 200, 50)

button_plus_1 = Button('button_plus_1.png', 620, 70, 360, 80)
button_plus_5 = Button('button_plus_5.png', 620, 170, 360, 80)
button_plus_10 = Button('button_plus_10.png', 620, 270, 360, 80)
button_plus_25 = Button('button_plus_25.png', 620, 370, 360, 80)

button_plus_1_auto = Button('button_plus_auto_1.png', 620, 70, 360, 80)
button_plus_5_auto = Button('button_plus_auto_5.png', 620, 170, 360, 80)
button_plus_10_auto = Button('button_plus_auto_10.png', 620, 270, 360, 80)
button_plus_25_auto = Button('button_plus_auto_25.png', 620, 370, 360, 80)

while game:
    window.fill((247, 208, 195))
    for e in event.get():
        if e.type == QUIT:
            game = False 
        if e.type == MOUSEBUTTONDOWN:
            pos = e.pos
            if coin.rect.collidepoint(pos):
                coin.click()
            if shop_button.rect.collidepoint(pos):
                Tab = shop_button.click(Tab)
            elif boost_button.rect.collidepoint(pos):
                Tab = boost_button.click(Tab)
            
            if Tab == 1:
                if button_plus_1.rect.collidepoint(pos):
                    if coins >= 150:
                        button_plus_1.plus(1, 150)
                elif button_plus_5.rect.collidepoint(pos):
                    if coins >= 625:
                        button_plus_5.plus(5, 625)
                elif button_plus_10.rect.collidepoint(pos):
                    if coins >= 1000:
                        button_plus_10.plus(10, 1000)
                elif button_plus_25.rect.collidepoint(pos):
                    if coins >= 2000:
                        button_plus_25.plus(25, 2000)

            if Tab == -1:
                if button_plus_1.rect.collidepoint(pos):
                    if coins >= 250:
                        button_plus_1_auto.plus_auto(1, 250)
                elif button_plus_5.rect.collidepoint(pos):
                    if coins >= 1000:
                        button_plus_5_auto.plus_auto(5, 1000)
                elif button_plus_10.rect.collidepoint(pos):
                    if coins >= 1750:
                        button_plus_10_auto.plus_auto(10, 1750)
                elif button_plus_25.rect.collidepoint(pos):
                    if coins >= 3250:
                        button_plus_25_auto.plus_auto(25, 3250)

    auto_clicer += 1
    if auto_clicer >= FPS:
        auto_clicer = 0
        coins += plus_auto
        print(coins)

    if timerr:
        schot += 1

    if schot >= 10:
        schot = 0
        coin.image = back = transform.scale(image.load('coin.png'), (300, 300))
        coin.rect.x = 150
        coin.rect.y = 250
        timerr = False

    if Tab == 1:
        shop_button.image = back = transform.scale(image.load('shop_light.png'), (200, 50))
        boost_button.image = back = transform.scale(image.load('boosts_dark.png'), (200, 50))

    elif Tab == -1:
        boost_button.image = back = transform.scale(image.load('boosts_light.png'), (200, 50))
        shop_button.image = back = transform.scale(image.load('shop_dark.png'), (200, 50))

    coin.reset()
    menu.reset()
    boost_button.reset()
    shop_button.reset()
    coins_otobroshenie.reset()

    if Tab == 1:
        button_plus_1.reset()
        button_plus_5.reset()
        button_plus_10.reset()
        button_plus_25.reset()

    elif Tab == -1:
        button_plus_1_auto.reset()
        button_plus_5_auto.reset()
        button_plus_10_auto.reset()
        button_plus_25_auto.reset()
    
    elif Tab == -1:
        pass

    COINS_TXT = font1.render((':' + str(coins)), True, (140, 59, 32))
    window.blit(COINS_TXT,(110, 5))

    display.update()
    clock.tick(FPS)