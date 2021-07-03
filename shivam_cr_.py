import pygame 
pygame.init() #initializes the Pygame
from pygame.locals import* #import all modules from Pygame
import sys
import random
import math
import time 
# tittle of the game
pygame.display.set_caption('Car Racing')
# set a logo.
pygame.mixer.init()
screen = pygame.display.set_mode((798,600))
# coundown time.
def countdown():
    font_2 = pygame.font.Font("F:\python\shivam_cr_racing/freesansbold.ttf",100)
    countdown_b_g= pygame.image.load("F:\python\shivam_cr_racing/bg.png")
    three = font_2.render("3",True,(200,170,220))
    two = font_2.render("2",True,(200,170,220))
    one = font_2.render("1",True,(200,170,220))
    go = font_2.render("GO!!!",True,(200,170,220))
    #display time
    screen.blit(countdown_b_g,(0,0))
    pygame.display.update()
     #display for 3
    screen.blit(three,(350,400))
    pygame.display.update()

    screen.blit(countdown_b_g,(0,0))
    pygame.display.update()
     #display for 2
    screen.blit(two,(350,400))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdown_b_g,(0,0))
    pygame.display.update()
     #display for 1
    screen.blit(one,(350,400))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdown_b_g,(0,0))
    pygame.display.update()
     #display for Go!!
    screen.blit(go,(350,400))
    pygame.display.update()
    time.sleep(1)


def gameloop():
    
    # score
    font_1 = pygame.font.Font("F:\python\shivam_cr_racing/freesansbold.ttf",25)
    def Show_score(x,y):
        score = font_1.render("SCORE:" +str(score_value),True,(250,235,200))
        screen.blit(score,(x,y))
        
    score_value =0

    # Highscore
    with open("F:\python\shivam_cr_racing\high_score.txt","r") as f:
        high_score=f.read()
    def show_high_score(x,y):
        high_score_text= font_1.render("HIGHSCORE:"+str(high_score),True,(250,235,200))
        screen.blit(high_score_text,(x,y))
        pygame.display.update()


    #setting background image

    background = pygame.image.load("F:\python\shivam_cr_racing/bg.png")
    pygame.mixer.music.load("F:\python\shivam_cr_racing/BackgroundMusic.mp3")
    pygame.mixer.music.play()
    # crash_sound= pygame.mixer.sound("F:\python\shivam_cr_racing\car_crash.wav")

    #  Setting of the player
    maincar_2 = pygame.image.load("F:\python\shivam_cr_racing\maincar_2.png")
    maincar_2X = 370
    maincar_2Y = 460
    maincar_2X_change=0
    maincar_2Y_change=0

    # other cars
    car_1 = pygame.image.load("F:\python\shivam_cr_racing\car_1.jpg")
    car_1X = random.randint(100,490)
    car_1Y = 100
    car_2 = pygame.image.load("F:\python\shivam_cr_racing\car_2.jpg")
    car_2X = random.randint(100,490)
    car_2Y = 100


    car_3 = pygame.image.load("F:\python\shivam_cr_racing\car_3.jpg")
    car_3X = random.randint(100,490)
    car_3Y = 100


    run = True
    while True:
        for event in pygame.event.get():
         if event.type == pygame.QUIT :
            run = False 
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key ==K_RIGHT:
                maincar_2X_change += 5

            if event.key==K_LEFT:
                maincar_2X_change -= 5

            if event.key==K_UP:
                maincar_2Y_change -=5

            if event.key ==K_DOWN:
                maincar_2Y_change+=5


        if maincar_2X < 178:
               maincar_2X = 178
        if maincar_2X > 490:
               maincar_2X = 490
        
        if maincar_2Y < 0:
               maincar_2Y = 0
        if maincar_2Y > 495:
               maincar_2Y = 495
            
            
        # logo = pygame.image.load("F:\python\shivam_cr_racing/bird.png")
        # pygame.display.set_icon(logo)
        #CHANGING COLOR WITH RGB VALUE, RGB = RED, GREEN, BLUE 
        screen.fill((100,50,70))
        # display background
        screen.blit(background,(0,0))
        # display maincar
        screen.blit(maincar_2,(maincar_2X,maincar_2Y))
        screen.blit(car_1,(car_1X,car_1Y))
        screen.blit(car_2,(car_2X,car_2Y))
        screen.blit(car_3,(car_3X,car_3Y))
        maincar_2X= maincar_2X_change
        maincar_2Y= maincar_2Y_change
     #movement of the enemies
        car_1Y += 3
        car_2Y += 3
        car_3Y += 3

        #moving enemies infinitely
        if car_1Y > 670:
            car_1Y = -100
            score_value+=1

        if car_2Y > 670:
            car_2Y = -200
            score_value+=1
        if car_3Y > 670:
            car_3Y = -300
            score_value+=1
        
        # display high vs score

        if score_value>int(high_score):
            score_value = high_score
        
      
        # COLLISION BETWEEN CARS.
        # Collision between the car_1 and maincar_2.
        def iscollision(car_1X,car_1Y,maincar_2X,maincar_2Y):
            distance=math.sqrt(math.pow(car_1X-maincar_2X,2) +  math.pow(car_1Y-maincar_2Y,2))
            # if distancing between the cars and mainacr_2 is smalller than 50 then collosion occur.
            if distance< 50:
                return True
            else:
                return False
        def iscollision(car_1X,car_1Y,maincar_2X,maincar_2Y):
            distance=math.sqrt(math.pow(car_1X-maincar_2X,2) +  math.pow(car_1Y-maincar_2Y,2))
            # if distancing between the cars and mainacr_2 is smalller than 50 then collosion occur.
            if distance< 50:
                return True
            else:
                return False
        def iscollision(car_3X,car_3Y,maincar_2X,maincar_2Y):
            distance=math.sqrt(math.pow(car_3X-maincar_2X,2) +  math.pow(car_3Y-maincar_2Y,2))
            # if distancing between the cars and mainacr_2 is smalller than 50 then collosion occur.
            if distance< 50:
                return True
            else:
                return False
        

        # give the collision variables.
        coll_1 = iscollision(car_1X,car_1Y,maincar_2X,maincar_2Y)
        coll_2 = iscollision(car_2X,car_2Y,maincar_2X,maincar_2Y)
        coll_3 = iscollision(car_3X,car_3Y,maincar_2X,maincar_2Y)
        # if collision occur 
        if coll_1:
            screen.fill(230,200,225)
            car_1Ychange = 0
            car_2Ychange = 0
            car_3Ychange = 0
            maincar_2X_change = 0
            maincar_2Y_change =0
            pygame.mixer.music.stop()
            # crash_sound.play()
        if coll_2:
            screen.fill(230,200,225)
            car_1Ychange = 0
            car_2Ychange = 0
            car_3Ychange = 0
            maincar_2X_change = 0
            maincar_2Y_change =0
            pygame.mixer.music.stop()
            # crash_sound.play()
        if coll_3:
            screen.fill(230,200,225)
            car_1Ychange = 0
            car_2Ychange = 0
            car_3Ychange = 0
            maincar_2X_change = 0
            maincar_2Y_change =0 
            pygame.mixer.music.stop()
            # crash_sound.play()
            
        # display score   

        Show_score(270,280)
         #display high_score
        show_high_score(270,280)
      
        with open ("F:\python\shivam_cr_racing\high_score.txt","w") as f:
            f.write(str(high_score))

        pygame.display.update()

 


    
