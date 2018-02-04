import pygame as pg
import random as rn
import time as t
import sys
pg.init()
pg.mixer.music.load("great.wav")
display_height = 700
display_width = 1366
direction = "up"
ultra_width = 64
gameDisp = pg.display.set_mode((display_width,display_height))
clock = pg.time.Clock()

pg.display.set_caption("ultraman rumble")
crashed = False

imgdisp = pg.image.load('ultra.png')
rect = imgdisp.get_rect()
rect = imgdisp.get_rect(x = (display_width * 0.45),y = (display_height * 0.6))
def car(rect):
	gameDisp.blit(imgdisp,rect)
def reward1(rectn,rect,e):
	if rect.colliderect(rectn):
		e += 1
		point(e)
		return e
	return e	
def point(er):
	message_disp('got an energy ore',er)
def message_disp(text,ern):
	pt = pg.font.Font('freesansbold.ttf',20)
	TextSurf,TextRect = text_objects(text,pt)
	TextRect.center = (600,600)
	gameDisp.blit(TextSurf, TextRect)
	pt2 = pg.font.Font('freesansbold.ttf',20)
	TextSurf2,TextRect2 = text_objects(str(ern),pt2)
	TextRect2.center = (100,100)
	gameDisp.blit(TextSurf2, TextRect2)
	pg.display.update()
def message_display(text,etr):
	largeText = pg.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisp.blit(TextSurf, TextRect)
	large = pg.font.Font('freesansbold.ttf',20)
	TextSurf2, TextRect2 = text_objects(etr, large)
	TextRect2.center = (300,500)
	gameDisp.blit(TextSurf2, TextRect2)
	pg.display.update()
	t.sleep(2)
	game_intro()
def crash(eer): 
	exr = "score :"+ str(eer)                                         
	message_display('ultraman dead',exr)
	pg.mixer.music.stop()              
def shot(rectn,rect,ear):
	if rect.colliderect(rectn):
		crash(ear)
		crashed = True         
def text_objects(text, font):                         
	white = (225,205,85)                               
	textSurface = font.render(text, True, white)  
	return textSurface, textSurface.get_rect()         
def game_intro():#welcome page of the game

	intro = True
	white = (255,255,255)
	black = (0,2,2)
	red = (255,0,0)
	brightred = (230,100,20)          #experimental RGB values 
	blue = (15,30,200)
	green = (0,255,0)
	brightgreen = (100,230,20)
	while intro:
		for event in pg.event.get():#this is used to get the cordinates,ascii values,events from i/o devices
			if event.type == pg.QUIT:
				pg.quit()
				quit()
                
		gameDisp.fill(black)
		largeText = pg.font.Font('freesansbold.ttf',115)
		TextSurf,TextRect = text_objects("ultraman rumble", largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisp.blit(TextSurf, TextRect)
		devlopers = pg.font.Font('freesansbold.ttf',15)
		TextSurf,TextRect = text_objects("devloped by swayam and ritik",devlopers)#yes we are the devlopers believe it
		TextRect.center = (1100,660)
		gameDisp.blit(TextSurf, TextRect)
		arg1 = "play"
		arg2 = "exit"
		button("go",350,450,150,50,green,brightgreen,arg1)
		button("give up",950,450,150,50,red,brightred,arg2)
		pg.display.update()
		clock.tick(15)
def button(msg,x,y,w,h,ic,ac,action=""):#ha ha these are not real buttons just rectangles but looks like buttons
	mouse = pg.mouse.get_pos()
	click = pg.mouse.get_pressed()
	arg1 = "play"
	arg2 = "exit"
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pg.draw.rect(gameDisp, ac,(x,y,w,h))
	else:
		pg.draw.rect(gameDisp, ic,(x,y,w,h))#this code is literaly topsy truvy
		if click[0] == 1 and action != "":#i don`t know how this code working like normal
#but this is working so don`t try to mess up with it
			if action == arg1:

				pg.quit()
				quit()
			elif action == arg2:
				game_start(crashed,direction,rect)				
	pg.draw.rect(gameDisp,ic,(x,y,w,h))
	smallText = pg.font.Font("freesansbold.ttf",20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)),(y+(h/2)) )
	gameDisp.blit(textSurf,textRect)
		
		
def game_start(crashed,direction,rect):
	pg.mixer.music.play(-3)
	black = (0,7,4)
	white = (255,255,255)
	red = (255,0,0)
	blue = (15,30,200)
	green = (0,255,0)
	ultra_width = 64
	ultra_height = 210
	earn=0
	imgdisp2 = pg.image.load('img/fire4.png')
	rect2 = imgdisp2.get_rect()
	rect2 = imgdisp2.get_rect(x=300, y= -10)
	imgdisp3 = pg.image.load('img/fire2.png')
	rect3 = imgdisp3.get_rect()
	rect3 = imgdisp3.get_rect(x=500, y= -100)
	imgdisp4 = pg.image.load('img/fire1.png')
	rect4 = imgdisp4.get_rect()
	rect4 = imgdisp4.get_rect(x=400, y= -1000)
	imgdisp5 = pg.image.load('img/fire5.png')
	rect5 = imgdisp5.get_rect()
	rect5 = imgdisp5.get_rect(x=900, y= -1048)
			                                     #these are all images 
	imgdisp6 = pg.image.load('img/fire6.png')
	rect6 = imgdisp6.get_rect()
	rect6 = imgdisp6.get_rect(x=700, y= -700)
	imgdisp7 = pg.image.load('img/fire3.png')
	rect7 = imgdisp7.get_rect()
	rect7 = imgdisp7.get_rect(x=150, y= -1090)
	imgdisp8 = pg.image.load('img/fire7.png')
	rect8 = imgdisp8.get_rect()
	rect8 = imgdisp8.get_rect(x=150, y= -1024)
	imgdisp9 = pg.image.load('img/fire5.png')
	rect9 = imgdisp9.get_rect()
	rect9 = imgdisp9.get_rect(x=900, y= -1036)
	imgdisp10 = pg.image.load('e1.png')
	rect10 = imgdisp10.get_rect()
	rect10 = imgdisp10.get_rect(x=700, y= -750)
	imgdisp11 = pg.image.load('e2.png')
	rect11 = imgdisp11.get_rect()
	rect11 = imgdisp11.get_rect(x=900, y= -1050)
	imgdisp12 = pg.image.load('e3.png')
	rect12 = imgdisp12.get_rect()
	rect12 = imgdisp12.get_rect(x=700, y= -750)
	
	while not crashed:# the so called game loop starts here
		for ev in pg.event.get():
			if ev.type == pg.QUIT:
				crashed = True

			if ev.type == pg.KEYDOWN:#entering the arrow key events
				if ev.key == pg.K_LEFT:
					rect.x -= 55
				if ev.key == pg.K_RIGHT:
					rect.x += 55
				if ev.key == pg.K_UP:
					rect.y -= 50
				if ev.key == pg.K_DOWN:
					rect.y += 50
			if ev.type == pg.KEYUP:
				if ev.key == pg.K_LEFT or ev.key == pg.K_RIGHT:
					rect.x += 0
		
		if rect2.y != 812:
			rect2.y += 2
		else:
			rect2.y = -10
		if rect3.y != 800:
			rect3.y += 4
		else:                              #just to move the fireballs verticaly
			rect3.y = -100
		if rect4.y != 800:
			rect4.y += 3
		else:
			rect4.y = -1000
		if rect5.y != 800:
			rect5.y += 3
		else:
			rect5.y = -1048
		if rect6.y != 800:
			rect6.y += 2
		else:
			rect6.y = -700
		if rect7.y != 800:
			rect7.y += 5
		else:
			rect7.y = -1090
		if rect8.y != 800:
			rect8.y += 3
		else:
			rect8.y = -1024
		if rect9.y != 800:
			rect9.y += 3
		else:
			rect9.y = -1036
		if rect10.y != 800:
			rect10.y += 2
		else:
			rect10.y = -700
		if rect11.y != 801:
			rect11.y += 3
		else:
			rect11.y = -1260
		if rect12.y != 800:
			rect12.y += 2
		else:
			rect12.y = -700
		if rect2.y == -10:
			rect2.x = rn.randint(50,400)
		if rect3.y == -100:
			rect3.x = rn.randint(400,800)
			
		if rect4.y == -1000:
			rect4.x = rn.randint(800,1350)
			
		if rect5.y == -1048:
			rect5.x = rn.randint(60,1360)
			
		if rect6.y == -700:
			rect6.x = rn.randint(700,1350)
			
		if rect7.y == -1090:
			rect7.x = rn.randint(50,1360)
			
		if rect8.y == -1024:
			rect8.x = rn.randint(50,500)
			                         # moves the fireball horizontaly with random origin
		if rect9.y == -1036:
			rect9.x = rn.randint(500,680)
		if rect10.y == -700:
			rect10.x = rn.randint(100,1200)
			
		if rect11.y == -1260:
			rect11.x = rn.randint(200,1000)
		if rect12.y == -700:
			rect12.x = rn.randint(100,1200)			
		if rect.x > display_width - ultra_width or rect.x < 0:
			rect.x = 585
		gameDisp.fill(black)
		gameDisp.blit(imgdisp2,rect2)
		gameDisp.blit(imgdisp3,rect3)
		gameDisp.blit(imgdisp4,rect4)
		gameDisp.blit(imgdisp5,rect5)
		gameDisp.blit(imgdisp6,rect6)
		gameDisp.blit(imgdisp7,rect7)
		gameDisp.blit(imgdisp8,rect8)
		gameDisp.blit(imgdisp9,rect9)
		gameDisp.blit(imgdisp10,rect10)
		gameDisp.blit(imgdisp11,rect11)
		gameDisp.blit(imgdisp12,rect12)
		shot(rect2,rect,earn)
		shot(rect3,rect,earn)
		shot(rect4,rect,earn)
		shot(rect5,rect,earn)
		shot(rect6,rect,earn)
		shot(rect7,rect,earn)
		shot(rect8,rect,earn)
		shot(rect9,rect,earn)
		earn=reward1(rect10,rect,earn)
		earn=reward1(rect11,rect,earn)
		earn=reward1(rect12,rect,earn)
		car(rect)
		pg.display.update()
game_intro()
clock.tick(150)#it represents frame per second 60 fps is ok but we used 150
pg.quit()
quit()#finally quit the game
