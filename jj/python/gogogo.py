import pygame
import random
from time import sleep

WHITE = (255, 255, 255)
RED = (255,0,0)
pad_width = 1024
pad_height = 512
background_width = 1024
aircraft_width = 90
aircraft_height = 55
bat_width = 110
bat_height = 67
fireball1_width = 140
fireball1_height = 60 
fireball2_width = 86
fireball2_height = 60



def drawScore(count):
    global gamepad

    font = pygame.font.SysFont(None,25)
    text = font.render('Bat Passed: ' + str(count),True,WHITE)
    gamepad.blit(text,(0,0))

def gameOver():
    global gamepad
    dispMessage('GameOver')

def textObj(text,font):
    textSurface = font.render(text,True,RED)
    return textSurface, textSurface.get_rect()

def dispMessage(text):
    global gamepad

    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = textObj(text, largeText)
    TextRect.center = ((pad_width/2),(pad_height/2))
    gamepad.blit(TextSurf, TextRect)
    pygame.display.update()
    sleep(2)
    runGame()

def crash():
    global gamepad, explosion_sound

    pygame.mixer.Sound.play(explosion_sound)
    dispMessage('Crashed!')
    



def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))

def runGame():
    global gamepad, aircraft, clock, background1, background2
    global bat,fires,bullet,boom, shot_sound



    
    isShotBat = False
    boom_count = 0

    bat_passed = 0
    

    bullet_xy = []
    
    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0

    background1_x = 0
    background2_x = background_width

    bat_x = pad_width
    bat_y = random.randrange(0, pad_height)

    fire_x = pad_width
    fire_y = random.randrange(0, pad_height)
    random.shuffle(fires)
    fire = fires[0]

    


    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                
                elif event.key == pygame.K_LCTRL:
                    bullet_x = x + aircraft_width
                    bullet_y = y + aircraft_height/2
                    bullet_xy.append([bullet_x, bullet_y])
                
                

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        # Clear gamepad
        gamepad.fill(WHITE)
        
        #Draw Background
        background1_x -= 2
        background2_x -= 2

        if background1_x == -background_width:
            background1_x = background_width
        
        if background2_x == -background_width:
            background2_x = background_width
        
        drawObject(background1, background1_x,0)
        drawObject(background2, background2_x,0)

        drawScore(bat_passed)

        #Check the number of BAT passed
        if bat_passed > 2:
            gameOver()

        
        #Aircraft Position
        y += y_change
        if y < 0:
            y=0
        elif y > pad_height - aircraft_height:
            y = pad_height - aircraft_height
        
        #Bat Position
        bat_x -= 7
        if bat_x <= 0:
            bat_passed += 1
            bat_x = pad_width
            bat_y = random.randrange(0, pad_height)
        
        #Firball Position
        if fire[1] == None:
            fire_x -= 30
        else:
            fire_x -= 15

        if fire_x <= 0:
            fire_x = pad_width
            fire_y = random.randrange(0, pad_height)
            random.shuffle(fires)
            fire = fires[0]

        #Bullet Position
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[0] += 15
                bullet_xy[i][0] = bxy[0]

                
                #Check if Bullet strike Bat
                if bxy[0] > bat_x:
                    if bxy[1] > bat_y and bxy[1] < bat_y + bat_height:
                        bullet_xy.remove(bxy)
                        isShotBat = True

                if bxy[0] >= pad_width:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass
        #Check aircraft crashed by Bat
        if x + aircraft_width > bat_x:
            if(y > bat_y and y < bat_y + bat_height) or\
             (y+aircraft_height > bat_y and y + aircraft_height < bat_y + bat_height):
                crash()

        #Check aircraft crashed by BAT       
        if fire[1] != None:
                if fire[0] == 0:
                        fireball_width = fireball1_width
                        fireball_height = fireball1_height
                elif fire[0] == 1:
                       fireball_width = fireball2_width
                       fireball_height = fireball2_height
                       
                if x + aircraft_width > fire_x:
                      if(y > fire_y and y < fire_y + fireball_height) or\
                      (y + aircraft_height > fire_y and y + aircraft_height < fire_y + fireball_height):
                           crash()

        drawObject(aircraft,x,y)
        
        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                drawObject(bat,bx,by)

        if not isShotBat:
            drawObject(bat,bat_x,bat_y)
        else:
            drawObject(bat,bat_x,bat_y)
            boom_count += 1
            if boom_count > 5:
                boom_count = 0
                bat_x = pad_width
                bat_y = random.randrange(0, pad_height-bat_height)
                isShotBat = False
       
        
        if fire[1] != None:
            drawObject(fire[1], fire_x, fire_y)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    
    quit()

def initGame():
    global gamepad, aircraft, clock, background1, background2
    global bat, fires, bullet, boom
    global shot_sound, explosion_sound

    

    fires = []

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PyFlying')
    aircraft = pygame.image.load('images/plane.png')
    background1 = pygame.image.load('images/background.png')
    background2 = background1.copy()
    bat = pygame.image.load('images/bat.png')
    fires.append((0,pygame.image.load('images/fireball.png')))
    fires.append((1,pygame.image.load('images/fireball2.png')))
    boom = pygame.image.load('images/boom.png')
    shot_sound = pygame.mixer.Sound('shot.wav')
    explosion_sound = pygame.mixer.pygame.mixer.Sound('explosion.wav')
    pygame.mixer.music.stop()
    pygame.mixer.music.pause()
    pygame.mixer.music.unpause()


    for i in range(3):
        fires.append((i+2,None))

    bullet = pygame.image.load('images/bullet.png')

    clock = pygame.time.Clock()
    runGame()

if __name__ == '__main__':
    initGame()







