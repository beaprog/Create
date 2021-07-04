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
screen = pygame.display.set_mode((600,500))
FSD=32
    #setting background image and cars (main and enimes_cars)
background = pygame.image.load("F:\python\shivam_car_racing/black_bg.jpg")
road_Strips = pygame.image.load("F:\python\shivam_car_racing/strips.png")
car_1 = pygame.image.load("F:\python\shivam_car_racing/car_1.jpg")
car_2 = pygame.image.load("F:\python\shivam_car_racing/car_2.jpg")
car_3 = pygame.image.load("F:\python\shivam_car_racing/car_3.jpg")
maincar_2 = pygame.image.load("F:\python\shivam_car_racing/maincar_2.jpeg")
pygame.mixer.music.load("F:\python\shivam_car_racing/BackgroundMusic.mp3")
pygame.mixer.music.play()
crash_sound= pygame.mixer.Sound("F:\python\shivam_car_racing/car_crash.wav")
def welcome_screen():
  while True:
   
        for event in pygame.event.get(): 
            if event.type == QUIT or (event.type==KEYDOWN and event.key ==K_ESCAPE): 
                pygame.quit()
                sys.exit()
            # if the user presses space or up key , start the game for them.
            elif event.type ==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                return # welcome screen ko return kr do means game started.
            else:
                font_2 = pygame.font.Font("F:\python\shivam_car_racing/freesansbold.ttf",30)
                created= font_2.render("Created", True,(130,210,150))
                by= font_2.render("by", True,(130,210,150))
                Creator_name= font_2.render("Shivam Bhardwaj", True,(130,210,150))
                screen.blit(created,(250,100))
                screen.blit(by,(295,150))
                screen.blit(Creator_name,(170,200))
                pygame.display.update()
welcome_screen()
def countdown():
    
    font_2 = pygame.font.Font("F:\python\shivam_car_racing/freesansbold.ttf",50)
    countdown_b_g= pygame.image.load("F:\python\shivam_car_racing/black_bg.jpg")
    three = font_2.render("3",True,(200,170,220))
    two = font_2.render("2",True,(200,170,220))
    one = font_2.render("1",True,(200,170,220))
    go = font_2.render("GO!!!",True,(200,170,220))
    #display time
    screen.blit(countdown_b_g,(131,0))
    pygame.display.update()
     #display for 3
    screen.blit(three,(298,250))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdown_b_g,(131,0))
    pygame.display.update()
     #display for 2
    screen.blit(two,(298,250))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdown_b_g,(131,0))
    pygame.display.update()
     #display for 1
    screen.blit(one,(298,250))
    pygame.display.update()
    time.sleep(1)

    screen.blit(countdown_b_g,(131,0))
    pygame.display.update()
    #  display for Go!!
    screen.blit(go,(260,250))
    pygame.display.update()
    time.sleep(1)
countdown()
def gameloop():
    # speed
    speed=.1
     #move the strip
    d2 =100
    d = random.randint(300,300)
    d3 =200
    d = random.randint(300,300)
    d4 =300
    d = random.randint(300,300)
    d5 =400
    d = random.randint(300,300)
    d6 =500
    
    # score
    font_1 = pygame.font.Font("F:\python\shivam_car_racing/freesansbold.ttf",25)
    def Show_score(x,y):
        score = font_1.render("SCORE:" +str(score_value),True,(250,235,200))
        screen.blit(score,(x,y))
        
    score_value =0
    # Highscore 
    with open("F:\python\shivam_car_racing/high_score.txt", "r") as f:
        high_score = f.read()
    def show_high_score(x,y):
        high_score_text = font_1.render("HIGHSCORE:"+str(high_score),True,(0,255,0))
        screen.blit(high_score_text,(x,y))
        pygame.display.update()
    

    #  Setting of the main_car
    maincar_2X = 370
    maincar_2Y = 400
    maincar_2X_change=370
    maincar_2Y_change=400
    maincar_2X_change = random.randint(140,425)

    
    # Enamies car set

    car_1X = random.randint(140,250) 
    car_1Y = 0
    car_1Ychange = .2

    car_2X = random.randint(285,295)
    car_2Y = 200
    car_2Ychange =.2
    car_3X = random.randint(395,425)
    car_3Y = 400
    car_3Ychange = .2


    run = True
    while True:
        # pygame.delay.time(10)
        for event in pygame.event.get():
         if event.type == pygame.QUIT :
            run = False 
        
            sys.exit()

        if event.type==pygame.KEYDOWN:
        
            if event.key ==K_RIGHT:
                maincar_2X_change += 1

            if event.key==K_LEFT:
                maincar_2X_change -= 1

            if event.key==K_UP:
                maincar_2Y_change -=1

            if event.key ==K_DOWN:
                maincar_2Y_change+=1



        # boundary condition of the main_car

        if maincar_2X < 140:
               maincar_2X = 140
        if maincar_2X > 425:
               maincar_2X = 425
        
        if maincar_2Y < 0:
               maincar_2Y = 0
        if maincar_2Y > 470:
               maincar_2Y = 470
            

        #CHANGING COLOR WITH RGB VALUE, RGB = RED, GREEN, BLUE 
        screen.fill((0,255,0))
        # display background
        screen.blit(background,(131,0))
        #strip blit
        screen.blit(road_Strips,(d,d2))
        screen.blit(road_Strips,(d,d3))
        screen.blit(road_Strips,(d,d4))
        screen.blit(road_Strips,(d,d5))
        screen.blit(road_Strips,(d,d6))
        
        if d2>500:
            d2=0
        d2=d2+speed
        if d3>500:
            d3=0
        d3=d3+speed
        if d4>500:
            d4=0
        d4=d4+speed
        if d5>500:
            d5=0
        d5=d5+speed
        if d6>500:
            d6=0
        d6=d6+speed

        # display maincar
        screen.blit(maincar_2,(maincar_2X,maincar_2Y))
        screen.blit(car_1,(car_1X,car_1Y))
        screen.blit(car_2,(car_2X,car_2Y))
        screen.blit(car_3,(car_3X,car_3Y))
        maincar_2X= maincar_2X_change
        maincar_2Y= maincar_2Y_change
        # movement of the enmies cars.
     
     #movement of the enemies
        car_1Y += .3
        car_2Y += .3
        car_3Y += .3
        maincar_2Y_change-=.1
        if maincar_2Y_change<0:
            maincar_2Y_change=600
            maincar_2X_change=random.randint(140,425)

        #moving enemies infinitely
        if car_1Y > 500:
            car_1Y = -100
            car_1X = random.randint(140,425)
            score_value+=1

        if car_2Y > 500:
            car_2Y =-100
            car_2X = random.randint(140,425)
            score_value+=1
        if car_3Y > 500:
            car_3Y = -100
            car_3X = random.randint(140,425)
            score_value+=1
        # compare score and hifh_score value
        if score_value> int(high_score):
            high_score = score_value
    
        # COLLISION BETWEEN CARS.
        # Collision between the car_1 and maincar_2.
        def iscollision(car_1X,car_1Y,maincar_2X,maincar_2Y):
            distance=math.sqrt(math.pow(car_1X-maincar_2X,2) +  math.pow(car_1Y-maincar_2Y,2))
            # if distancing between the cars and mainacr_2 is smalller than 50 then collosion occur.
            if distance< 30:
                return True
               
            else:
                return False

        def iscollision(car_2X,car_2Y,maincar_2X,maincar_2Y):
            distance=math.sqrt(math.pow(car_2X-maincar_2X,2) +  math.pow(car_2Y-maincar_2Y,2))
            # if distancing between the cars and mainacr_2 is smalller than 50 then collosion occur.
            if distance< 30:
                return True
            else:
                return False
        def iscollision(car_3X,car_3Y,maincar_2X,maincar_2Y):
            distance=math.sqrt(math.pow(car_3X-maincar_2X,2) +  math.pow(car_3Y-maincar_2Y,2))
            # if distancing between the cars and mainacr_2 is smalller than 50 then collosion occur.
            if distance<30:
               
                return True
            else:
                return False
           

    
        

        # give the collision variables.
        coll_1 = iscollision(car_1X,car_1Y,maincar_2X,maincar_2Y)
        coll_2 = iscollision(car_2X,car_2Y,maincar_2X,maincar_2Y)
        coll_3 = iscollision(car_3X,car_3Y,maincar_2X,maincar_2Y)
        # if collision occur 
        if coll_1:
            # screen.fill(230,200,225)
            car_1Y+= 0
            car_2Y+= 0
            car_3Y+= 0
            maincar_2X_change = 0
            maincar_2Y_change-=0
            pygame.mixer.music.stop()
            crash_sound.play()
            sys.exit()
        if coll_2:
            # screen.fill(230,200,225)
            car_1Y+= 0
            car_2Y+= 0
            car_3Y+= 0
            maincar_2X_change = 0
            maincar_2Y_change-=0
            pygame.mixer.music.stop()
            crash_sound.play()
            sys.exit()
            
        if coll_3:
            # screen.fill(230,200,225)
            car_2Y+= 0
            car_1Y+= 0
            car_3Y+= 0
            maincar_2X_change = 0
            maincar_2Y_change-=0
            pygame.mixer.music.stop()
            crash_sound.play()
            sys.exit()
        
        # display score   
        Show_score(270,280)
        # high_score.
        show_high_score(132,0)
        with open("F:\python\shivam_car_racing/high_score.txt","w") as f:
            f.write(str(high_score))
            pygame.display.update()
gameloop()

 


    
