#gopher mash
#written by Dr. Mo, 11/10/2020
import pygame
import math #needed for square root function



pygame.init()#initializes Pygame
pygame.display.set_caption("Cta Clicker")#sets the window title
CatPic = pygame.image.load("Popcat1.png")
CatRect = CatPic.get_rect(topleft=(100,100))
CatPic2 = pygame.image.load("Popcat2.png")
CatRect2 = CatPic.get_rect(topleft=(90,90))
screen = pygame.display.set_mode((400,400))#creates game screen
#SOUND
Click = pygame.mixer.Sound("TacoBell(LOUD).mp3")
#music pygame.mixer.music.load()
#pygame.mixer.music.set_volume(0.25)
#pygame.mixer.music.play(-1)
print(pygame.font.get_fonts())
#player variables
xpos = 200
ypos = 200
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
numClicks = 0
IsBig = False
#circle variables: circX and circY are the coordinates of the center (where it's drawn), and the radius is how big it is
circX = 200 
circY = 200
radius = 100

font = pygame.font.Font('freesansbold.ttf' , 32)
text1 = font.render('score:', False, (0,200,200))
text2 = font.render(str(int(numClicks)), 1, (0, 200,200))

#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()

    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN: #check if clicked
        mousePos = event.pos
        print("mouse position:(",mousePos[0],",",mousePos[1],")")
        if math.sqrt((circX-mousePos[0])**2+(circY-mousePos[1])**2)<radius:
            IsBig = True
            pygame.mixer.Sound.play(Click)
            numClicks+=1
            print("CLICK")
    else:
        IsBig  = False
        

    if event.type == pygame.MOUSEMOTION: #check if mouse moved
        mousePos = event.pos #refreshes mouse position
        print("mouse position: ",mousePos[0]," , ",mousePos[1])
 
#render section---------------------------------------------
    screen.fill((255, 255, 255)) #wipe screen (without this, things smear)
    #pygame.draw.circle(screen, (200, 0, 200), (circX,circY), radius)
    if IsBig == False:
        screen.blit(CatPic, CatRect)
    else:
        screen.blit(CatPic2,CatRect2)
    print("clicks:", numClicks) #uncomment this once collision is set up
    text2 = font.render(str(int(numClicks)), 1, (0, 200,200))
    screen.blit(text1,(10,10))
    screen.blit(text2,(110,10))
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()



