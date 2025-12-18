import pygame

WIDTH  = 1900
HEIGHT = 1000

levelBtns = []
buttonNo = []

startX = WIDTH / 2 - 545
x = startX
y = HEIGHT / 2 - 25
l = (-65*10)*1.5
gap = 65

for i in range(10):
    btn = Actor('level-buttons')
    startX = startX + gap
    btn.pos = (startX, HEIGHT / 2 - 125)
    levelBtns.append(btn)
    buttonNo.append(str(i + 1))

fs = False
parrot = Actor('parrot-3')
bgSky = Actor('sky-bg')
play = Actor('blue-play')
shop = Actor('blue-shop')
quitb = Actor('blue-quit')
play.pos = (WIDTH/2 - 175, HEIGHT/2)
shop.pos = (WIDTH/2 - 175, HEIGHT/2 + 100)
quitb.pos = (WIDTH/2 - 175, HEIGHT/2 + 200)
gameTxt = "PARROT"
stat = "Start"

def on_key_down(key):
    global fs

    if key == keys.F11 and not fs:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        fs = True


    elif key == keys.F11 and fs:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        fs = False

def draw():
    global stat

    if stat == "Start":
        screen.clear()
        bgSky.draw()
        shop.draw()
        play.draw()
        quitb.draw()
        screen.draw.text(gameTxt, midbottom = (WIDTH/2 - 175, HEIGHT/2 - 200), fontname = "daydream", fontsize = 96, color = "Yellow", gcolor = "Orange", owidth=1.5, ocolor= "Black")
    for i, btn in enumerate(levelBtns):
                btn.draw()
                screen.draw.text(buttonNo[i], center=btn.pos, fontname="daydream", fontsize=16, color="black")

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        if play.collidepoint(pos):
            play.image = 'blue-play1'
        if shop.collidepoint(pos):
            shop.image = 'blue-shop1'
        if quitb.collidepoint(pos):
            quitb.image = 'blue-quit1'
        for btn in levelBtns:
            if btn.collidepoint(pos):
                btn.image = 'level-buttons1'

def on_mouse_up(pos, button):
    if button == mouse.LEFT:
        play.image = 'blue-play'
        shop.image = 'blue-shop'
        quitb.image = 'blue-quit'
        if quitb.collidepoint(pos):
            exit()
        for btn in levelBtns:
            btn.image = 'level-buttons'
