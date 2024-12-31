# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:00:54 2020

@author: cesar Garay
"""
#########----- Importamos librerias -------#############
import pygame, sys
import random
import math

########----- Inicializamos las librerias -------##########
pygame.init()
pygame.mixer.init() #iniciar sonidos

#######----- Variables de pantalla y color ----------##########
ANCHO = 1300
ALTO = 690 
PANTALLA = pygame.display.set_mode((ANCHO,ALTO))

BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)

##-----puntero -------##
target = pygame.image.load('img/target.png')
rect_target = target.get_rect()


#######----- Reloj de FPS por segundo del juego -------#########
FPS = 60
RELOJ = pygame.time.Clock()

######----- Imagen de Fondo titulo e icono del juego ------#########
fondo = pygame.image.load('img/espacio.png').convert()
moveX = 0
varX = 1

icono = pygame.image.load('img/icono.png')
pygame.display.set_icon(icono)

pygame.display.set_caption('Asteroids')


 
######----- Metodos de pintar encima del juego --------#########
corazon = pygame.image.load('img/vida.png').convert_alpha()
def vida(surface,x,y, porcentaje):
    barra = 100
    barra_alto = 15
    fill = (porcentaje / 100) * barra
    borde = pygame.Rect(x,y, barra, barra_alto)
    fill = pygame.Rect(x,y,fill,barra_alto)
    pygame.draw.rect(surface, RED , fill)
    
    pygame.draw.rect(surface, WHITE, borde, 2)

#####------ Clase del Personaje metodos de movimiento etc... -----########
class Personaje1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/nave/nave0.png')
        self.grados = 0
        
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        
        self.rect.center =(ANCHO //2, ALTO //2)
        self.original_image = self.image
        
        self.vida = 100  #vida

      
#######----- Movimiento, Rotacion y Delimitacion de la pantalla del personaje ----####     
    def update(self):
        
        self.move = pygame.key.get_pressed()
        
        if self.move[pygame.K_w]:
            self.rect.y -=5
            
        if self.move[pygame.K_s]:
            self.rect.y +=5
        if self.move[pygame.K_a]:
            self.rect.x -=5
        if self.move[pygame.K_d]:
            self.rect.x +=5
            
            
        if self.rect.left < 0:
            self.rect.left = 0
            
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
            
        if self.rect.top < 0:
            self.rect.top = 0
            
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
                   
        self.x, self.y = pygame.mouse.get_pos()
        self.rotacio = math.atan2((self.rect.center[0] - self.x), (self.rect.center[1] - self.y))
        
        self.grados = math.degrees(self.rotacio)
        
        self.image = pygame.transform.rotate(self.original_image, int(self.grados))
    
#######---- metodo de disparo laser -----####### 
    def disparo(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_esprites.add(bullet)
        bullets.add(bullet)
        
        self.sound = random.choice(laser)
        self.sound.play()
        
#########------ Clase Sprite de la bala laser -------##########
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("img/laser1.png")
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.rect.centerx = x
        
        self.vx = 0
        self.vy = 0
        
######----- Rotacion de salida de la bala (dirreccion) ----########      
        self.original_image = self.image
        
        self.x, self.y = pygame.mouse.get_pos()
        
        self.rotacio = math.atan2((self.rect.center[0] - self.x), (self.rect.center[1] - self.y))
        
        self.grados = math.degrees(self.rotacio)
        self.image = pygame.transform.rotate(self.original_image, int(self.grados))
        
        
#####----- Validacion de cuadrante y dirreciion (X,Y) PROYECTIL -----#########
        self.x_pos = False
        self.y_pos = False
        
        if self.grados <0:
            self.x_pos = True
        if abs(self.grados) >90:
            self.y_pos = True
        
        
        if self.y_pos == False and self.x_pos == True:
            self.grados = abs(self.grados)
            
            if self.grados == 90:
                self.vx = 10
                self.vy = 0
                
            elif self.grados >= 81:
                self.vx = 9
                self.vy = -1
            elif self.grados >= 72:
                self.vx = 8
                self.vy = -2
            elif self.grados >= 63:
                self.vx = 7
                self.vy = -3
            elif self.grados >= 54:
                self.vx = 6
                self.vy = -4
            elif self.grados >= 45:
                self.vx = 5
                self.vy = -5
            elif self.grados >= 48:
                self.vx = 4
                self.vy = -6
            elif self.grados >= 36:
                self.vx = 3
                self.vy = -7
            elif self.grados >= 27:
                self.vx = 2
                self.vy = -8
            elif self.grados >= 18:
                self.vx = 1
                self.vy = -9
            elif self.grados >= 9:
                self.vx = 0
                self.vy = -10
            elif self.grados >= 0:
                self.vx = 0
                self.vy = -10
        
        if self.y_pos == True and self.x_pos == True:
            self.grados = abs(self.grados)
            
            if self.grados == 180:
                self.vx = 0
                self.vy = 10
                
            elif self.grados >= 171:
                self.vx = 1
                self.vy = 9
            elif self.grados >= 162:
                self.vx = 2
                self.vy = 8
            elif self.grados >= 153:
                self.vx = 3
                self.vy = 7
            elif self.grados >= 144:
                self.vx = 4
                self.vy = 6
            elif self.grados >= 135:
                self.vx = 5
                self.vy = 5
            elif self.grados >= 126:
                self.vx = 6
                self.vy = 5
            elif self.grados >= 117:
                self.vx = 7
                self.vy = 4
            elif self.grados >=108 :
                self.vx = 8
                self.vy = 2
            elif self.grados >= 99:
                self.vx = 9
                self.vy = 1
               
                #### cuadrante 1
            elif self.grados >=90:
                self.vx = 10
                self.vy = 0
        
        if self.y_pos == True and self.x_pos == False:
            self.grados = abs(self.grados)
            
            if self.grados == 180:
                self.vx = 0
                self.vy = 10
                
            elif self.grados >= 171:
                self.vx = -1
                self.vy = 9
            elif self.grados >= 162:
                self.vx = -2
                self.vy = 8
            elif self.grados >= 153:
                self.vx = -3
                self.vy = 7
            elif self.grados >= 144:
                self.vx = -4
                self.vy = 6
            elif self.grados >= 135:
                self.vx = -5
                self.vy = 5
            elif self.grados >= 126:
                self.vx = -6
                self.vy = 5
            elif self.grados >= 117:
                self.vx = -7
                self.vy = 4
            elif self.grados >=108 :
                self.vx = -8
                self.vy = 2
            elif self.grados >= 99:
                self.vx = -9
                self.vy = 1
               
            elif self.grados >=90:
                self.vx = -10
                self.vy = 0
        
        if self.y_pos == False and self.x_pos == False:            
            self.grados = abs(self.grados)
            
            if self.grados == 90:
                self.vx = -10
                self.vy = 0
                
            elif self.grados >= 81:
                self.vx = -9
                self.vy = -1
            elif self.grados >= 72:
                self.vx = -8
                self.vy = -2
            elif self.grados >= 63:
                self.vx = -7
                self.vy = -3
            elif self.grados >= 54:
                self.vx = -6
                self.vy = -4
            elif self.grados >= 45:
                self.vx = -5
                self.vy = -5
            elif self.grados >= 48:
                self.vx = -4
                self.vy = -6
            elif self.grados >= 36:
                self.vx = -3
                self.vy = -7
            elif self.grados >= 27:
                self.vx = -2
                self.vy = -8
            elif self.grados >= 18:
                self.vx = -1
                self.vy = -9
            elif self.grados >= 9:
                self.vx = 0
                self.vy = -10
            elif self.grados >= 0:
                self.vx = 0
                self.vy = -10
            
        
        
#######---- Metodo de aplicacion de direccion de proyectil PS ------######
    def update(self):
        
        self.rect.y += self.vy
        self.rect.x += self.vx
            
        if self.rect.bottom <0:
            self.kill()


######------- Clase de meteoros Sprites etc... --------#########
class Meteoro(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = random.choice(meteoro_img)
        self.image.set_colorkey(BLACK) 
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(ANCHO - self.rect.width) #una punto de incio en x
        self.rect.y = random.randrange(-140,-50)#un punto de inicio en y

        self.velocidad = random.randrange(1,3) #una velocidad variable
        self.velocidadX = random.randrange(-5,5)


    def update(self):
        self.rect.y += self.velocidad
        self.rect.x += self.velocidadX # agregamos velocidad a las

        #cuando el metiorito salga se respawnea
        if self.rect.top > ALTO + 10 or self.rect.left < -40 or self.rect.right > ANCHO + 40:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


######------- Clase de meteoros Sprites etc... --------#########
class Meteoro2(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = random.choice(meteoro_img)
        self.image.set_colorkey(BLACK) 
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(ANCHO -self.rect.width)
        self.rect.y = random.randrange(ALTO+40,ALTO+100)
        
        self.velocidad = random.randrange(1,3) #una velocidad variable
        self.velocidadX = random.randrange(-2,2)
    def update(self):
        self.rect.y -=self.velocidad
        self.rect.x += self.velocidadX
        
        if self.rect.top < -40 or self.rect.left < -40 or self.rect.right > ANCHO + 40:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = random.randrange(ALTO+40,ALTO+100)
            self.speedy = random.randrange(1, 8)


##########---------- Clase Explosion animacion de explosion -------######
class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
				self.kill() 
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center
                
                




#######-------- Cargar Sprites De meteoro ----------###########
meteoro_img = []
meteoro_list = ['img/asteroids/sprite_7.png', 
                'img/asteroids/sprite_8.png',
                'img/asteroids/sprite_9.png',
                'img/asteroids/sprite_10.png',
                'img/asteroids/sprite_11.png',
                'img/asteroids/sprite_12.png',
                'img/asteroids/sprite_13.png',
                'img/asteroids/sprite_14.png',
                'img/asteroids/sprite_15.png']

for img in meteoro_list:
    meteoro_img.append(pygame.image.load(img).convert())


########------- Sonido del Laser --------########
laser = []
laser_list =["sonidos/laser5.ogg"]
disparos = 0
dispaT = False

for i in laser_list:
    laser.append(pygame.mixer.Sound(i))


########------- Sonido de explosion --------########
explosion_sound = pygame.mixer.Sound('sonidos/explo.ogg')
explosion_sound.set_volume(0.07) #volumen del sonido




######------------ CARGAR IMAGENES EXPLOSIÓN -------------------#####
explosion_anim = []
for i in range(9):
	file = "img/explosiones/regularExplosion0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(BLACK)
	img_scale = pygame.transform.scale(img, (70, 70))
	explosion_anim.append(img_scale)

##-------------- cargar imagenes de transicion -----------##
transicion = []
for i in range(12):
    file = "img/transicion/f{}.png".format(i)
    img = pygame.image.load(file).convert_alpha()
    transicion.append(img)
##--------------------------------------------------------##

              
########------- Sonido de Choque meteorito vs Nave --------########
choque = pygame.mixer.Sound('sonidos/metal.ogg')
choque.set_volume(1)   


    
######------ Metodo de crear meteoros destruidos ------#####
def back():
    meteoro2 = Meteoro2()
    
    all_esprites.add(meteoro2)
    metioritos.add(meteoro2)
          
def back1():
    meteoro = Meteoro()
    all_esprites.add(meteoro)
    metioritos.add(meteoro)


Extreme_option =False
estado = [1]
MeteorMax = 0
def song():
    
    pygame.mixer.music.load('music/music_game.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

puntaje = 0
eliminacion = 0
Home = []
reiniciarL = []



def texto(PANTALLA, text, size, x, y):
	font = pygame.font.Font('fonts/Bun.ttf', size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	PANTALLA.blit(text_surface, text_rect)

tablero = pygame.image.load('img/tablero.png')
rectT = tablero.get_rect()
rectT.center = (ANCHO - 245, 20)

####--------------------- Pausa del juego -------------###
pausa = pygame.image.load('img/pausa.png').convert_alpha()
rectP = pausa.get_rect()
rectP.center = (ANCHO -20, 15)

def pausaG(x):
    
    
    pygame.mouse.set_visible(1)
    if x == 1:
        ajuste = -100
        menu = pygame.image.load('img/game_over_menu.png').convert_alpha()
    else:
        ajuste = 0
        menu = pygame.image.load('img/pausa_menu.png').convert_alpha()
    
    pausa = True
    
    
    
    salir = pygame.image.load('img/no_menu.png').convert_alpha()
    rectS = salir.get_rect()
    rectS.center = (ANCHO /1.25, 45)
    
    home = pygame.image.load('img/home_si.png').convert_alpha()
    rectH = home.get_rect()
    rectH.center = (ANCHO // 2 + ajuste, ALTO - 200)
    
    
    resume = pygame.image.load('img/resume_no.png').convert_alpha()
    rectR = resume.get_rect()
    rectR.center = (ANCHO // 2 -200, ALTO - 200)
    
    reiniciar = pygame.image.load('img/re.png').convert_alpha()
    rectI = reiniciar.get_rect()
    rectI.center = (ANCHO // 2 +200 + ajuste, ALTO - 200)
    
    PANTALLA.blit(menu,(0,0))
    
    
    texto(PANTALLA, str(puntaje), 35, ANCHO /2 -120,220)
    texto(PANTALLA, str(eliminacion), 35, ANCHO -400,220)
    while pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mousex, Mousey = event.pos
                if event.button == 1:
                    
                    
                    if rectH.collidepoint(Mousex,Mousey):
                        Home.append(True)
                        pausa = False        
                    
                    if rectI.collidepoint(Mousex,Mousey):
                        reiniciarL.append(True)
                        Home.append(True)
                        pausa = False
                    if x == 0:
                        if rectR.collidepoint(Mousex,Mousey):
                            pausa = False
                        
                        if rectS.collidepoint(Mousex,Mousey):
                            pausa = False
                        
        
        
        
        
        Mousex, Mousey = pygame.mouse.get_pos()  
        if rectS.collidepoint(Mousex,Mousey):
            salir = pygame.image.load('img/si_menu.png').convert_alpha()
        else:
            salir = pygame.image.load('img/no_menu.png').convert_alpha()
        
        if rectR.collidepoint(Mousex,Mousey):
            resume = pygame.image.load('img/resume_si.png').convert_alpha()
        else:
            resume = pygame.image.load('img/resume_no.png').convert_alpha()
        
        if rectI.collidepoint(Mousex,Mousey):
            reiniciar = pygame.image.load('img/re_si.png').convert_alpha()
        else:
            reiniciar = pygame.image.load('img/re.png').convert_alpha()
        
        if rectH.collidepoint(Mousex,Mousey):
            home = pygame.image.load('img/home_no.png').convert_alpha()
        else:
            home = pygame.image.load('img/home_si.png').convert_alpha()
        
        if x == 1:
            pass
        else:
            PANTALLA.blit(resume,rectR)
            
            PANTALLA.blit(salir,rectS)
            
        PANTALLA.blit(reiniciar,rectI)
        PANTALLA.blit(home,rectH)
        
        
        RELOJ.tick(60)
        pygame.display.flip()
        

def pantalla():
    
    waiting = True
##--------------- veriables de movimiento (X,Y)--------------------------##
    x=0
    y=0
##--------------- Movimiento (ARRIBA - ABAJO) de la capa ----------------##
    naveM = pygame.image.load('img/capas/nave.png').convert_alpha()
    rectM = naveM.get_rect()
    yM = 1
##------------------------ Titulo de entrada ----------------------------##  
    tituloM = pygame.image.load('img/capas/asteroids.png').convert_alpha()
    
##----------------------- Fondo de meteoros volando ---------------------##
    fondoM = pygame.image.load('img/capas/meteoros.png').convert_alpha()
    
##-------------------- Fondo de espacio direccion -----------------------##
    espacioM = pygame.image.load('img/capas/espacio.png').convert_alpha()


##--------------opciones de jugar --------------------##
    option_play = pygame.image.load('img/si.png').convert_alpha()
    rect_play   = option_play.get_rect()
    
    rect_play.center = (ANCHO // 2, ALTO / 1.5)
    
    option_extreme = pygame.image.load('img/EXTREME_si.png').convert_alpha()
    rect_playE   = option_extreme.get_rect()
    
    rect_playE.center = (ANCHO // 2 -200 , ALTO /1.3)
    
##------------ Animacion de transicio -----------------##
    animacioF = transicion[0]
    frame = 0
    frame_rate = 50 
    transicioT = False
    
    
##---------- Musica de inicio ----------------------##
    
    pygame.mixer.music.load('music/music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    
##--------------controles del juego --------------------##
    control = pygame.image.load('img/control.png').convert_alpha()
    rectQ = control.get_rect()
    rectQ.center = (ANCHO // 2 +200 , ALTO - 150)
    
    
    control_menu_I = pygame.image.load('img/menu_control.png')
    control_M = False
    
    salirQ = pygame.image.load('img/no_menu.png').convert_alpha()
    rect_salirQ = salirQ.get_rect()
    rect_salirQ.center = (ANCHO /1.25, 45)
    
##---------------- Bucle de espera -------------##    
    while waiting:
        RELOJ.tick(60)
        pygame.display.update()
        
        
##-----------------------------------------------------------##
        y_relativa = y % espacioM.get_rect().width 
    
        PANTALLA.blit(espacioM,(y_relativa - espacioM.get_rect().width  ,0))
    
        if y_relativa < ANCHO:
            PANTALLA.blit(espacioM,(y_relativa,0))
        y+=3
##-----------------------------------------------------------##

#####-----Asteroides de fondo con movimiento --------------###
        
        x_relativa = x % fondoM.get_rect().width 
    
        PANTALLA.blit(fondoM,(x_relativa - fondoM.get_rect().width  ,0))
    
        if x_relativa < ANCHO:
            PANTALLA.blit(fondoM,(x_relativa,0))
        x-=2
##-----------------------------------------------------------##
        PANTALLA.blit(naveM,(0,rectM.y))
        rectM.y += yM
        if rectM.y == 100:
            yM = -1
        elif rectM.y == 0:
            yM = +1
##-----------------------------------------------------------##      
        PANTALLA.blit(tituloM,(0,0))

##------------opciones del juego-----------------------------##
        PANTALLA.blit(option_play,rect_play)
        
        
        
        Mx, My = pygame.mouse.get_pos()
        
        if rect_play.collidepoint(Mx,My):
            option_play = pygame.image.load('img/no.png')
        else:
            option_play = pygame.image.load('img/si.png')
        
        
        
        if rect_playE.collidepoint(Mx,My):
            option_extreme = pygame.image.load('img/EXTREME_no.png')
        else:
            option_extreme = pygame.image.load('img/EXTREME_si.png')
        
        PANTALLA.blit(option_extreme,rect_playE)
##...........................................................## 
        
##------------------controles -----------------------------##
        if rectQ.collidepoint(Mx,My):
            control = pygame.image.load('img/control_no.png')
        else:
            control = pygame.image.load('img/control.png')
            
        PANTALLA.blit(control,rectQ)
        
        if control_M :
            
            PANTALLA.blit(control_menu_I,(0,0))
            
            if rect_salirQ .collidepoint(Mx,My):
                salirQ = pygame.image.load('img/si_menu.png')
            else:
                salirQ = pygame.image.load('img/no_menu.png')
            
            PANTALLA.blit(salirQ,rect_salirQ )
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
###-------- boton de play presionado -------------###                                
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mx,My = event.pos
                if event.button == 1:
                    if control_M :
                         if rect_salirQ .collidepoint(Mx,My):
                             control_M = False
                    
                    else:
                        if rect_play.collidepoint(Mx,My):
                            #transicion()
                            last_update = pygame.time.get_ticks()
                            pygame.mixer.music.fadeout(1500)
                            transicioT = True
                            estado[0] = False
                            
                            
                        if rect_playE.collidepoint(Mx,My):
                            #transicion()
                            last_update = pygame.time.get_ticks()
                            pygame.mixer.music.fadeout(1500)
                            transicioT = True
                            estado[0] = True
                            
                        if rectQ.collidepoint(Mx,My):
                            control_M = True
                                   
##------------------------------------------------##
        if transicioT:
            now = pygame.time.get_ticks()
            
            if now - last_update >frame_rate:
                last_update = now
                frame +=1
                if frame == len(transicion):
                    waiting = False
                else:
                    animacioF = transicion[frame]
        
        
            
        PANTALLA.blit(animacioF,(0,0))      
                
        pygame.display.flip()
        
        
    
######----------- game over ------------###########
game_over = True

#####-----variable Bucle --------###########
run = True


#---------------------------------------------------------------------------#
while run:
    if game_over:
        MeteorMax = 0
        puntaje = 0 
        eliminacion = 0
        Home = []
        pygame.mouse.set_visible(1)
        
        if len(reiniciarL) == 1:
            reiniciarL = []    
        else:
            pantalla()
        
        reiniciar = []
        game_over = False       
        
        song()
        ########----Listas de Sprites y Asignacion de sprites ------######
        bullets = pygame.sprite.Group() 
        metioritos = pygame.sprite.Group() 
        all_esprites = pygame.sprite.Group()
 
        Personaje = Personaje1()
        all_esprites.add(Personaje)
        
        ##########----- Crear meteoritos Iniciales --------#########
        for i in range(8): 
            meteoro = Meteoro()
        
            all_esprites.add(meteoro)
            metioritos.add(meteoro)
        
        
        for i in range(8):
            
            meteoro2 = Meteoro2()
            
            all_esprites.add(meteoro2)
            metioritos.add(meteoro2)
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #disparo
        if event.type == pygame.MOUSEBUTTONDOWN:
            Mousex, Mousey = event.pos
            if event.button == 1:
                Personaje.disparo()
                disparos += 1
                dispaT = True
            if rectP.collidepoint(Mousex,Mousey):
                pausaG(0)

##-------------opcion Home Para ir al menu principal--------------------------## 
    if len(Home) ==1:
        game_over = Home[0]
##--------------------sonido del juego en esta play -------------##
    
    
######-----Agrega sonido aleatorio cada 20 disparos -------######
    if dispaT == True:
        if disparos % 20 == 0:
            laser.append(pygame.mixer.Sound("sonidos/Cuack.ogg"))
        else:
            if len(laser) == 2:
                laser.pop(1)
                
    dispaT = False
    
#####---------------- FONDO DE ESTRELLAS ----------------------#####
    moveF = pygame.key.get_pressed()
    
    if moveF[pygame.K_a]:
        varX = -1
    if moveF[pygame.K_d]:
        varX = 1
    
    x_relativa = moveX % fondo.get_rect().width
    PANTALLA.blit(fondo,(x_relativa - fondo.get_rect().width ,0))
    
    if x_relativa < ANCHO:
        PANTALLA.blit(fondo,(x_relativa,0))
    moveX -= varX
####----------------- ESTADO DEL JUEGO ------------------------#####
    Extreme_option = estado[0]
    
    
    
####------ Validar colisiones entre disparos y Asteroides -------####    
    hits = pygame.sprite.groupcollide(metioritos, bullets, True, True)
    
    for hit in hits:
        
        explosion_sound.play()
        explosion = Explosion(hit.rect.center) ###iniciar la animacion###
        all_esprites.add(explosion)
        
#####----- Evalua de que tipo son para rehacerlo ------#######
        if str(hit) == '<Meteoro sprite(in 0 groups)>':
            back1()
            
        else:
            back()
####--------- Modo de juego dificil ----------####     
        MeteorMax += 1
        if MeteorMax < 30:
            if Extreme_option:
                back()
                back1()
        
        puntaje += 25
        eliminacion += 1
    
    
####------ Validar colisiones entre nave y Asteroides -------####    
    golpe = pygame.sprite.spritecollide(Personaje,metioritos,True)
    for i in golpe:
        Personaje.vida -= 25
        
        choque.play()
        explosion = Explosion(i.rect.center) ###iniciar la animacion###
        all_esprites.add(explosion)
        
#####----- Evalua de que tipo son para rehacerlo ------#######
        if str(i) == '<Meteoro sprite(in 0 groups)>':
            back1()
            
        else:
            back()
        
        
####--------- Modo de juego dificil ----------####       
        if Extreme_option:
            back()
            back1()
####----------- Pantalla de Game Over o Inicio -------------####
        if Personaje.vida <=0:
            pausaG(1)
            
    
    
##---------- Acceder a metodo update de todos los sprites ----------#####    
    all_esprites.update()  

##--------- Pinta todos los objetos Sprite --------#########
    all_esprites.draw(PANTALLA)

##--------- Pinta la barra de vida sobre todo ------------##########
    vida(PANTALLA,22,5,Personaje.vida)
    PANTALLA.blit(corazon,(1,5))
    
    
    PANTALLA.blit(tablero,rectT)
    texto(PANTALLA, str(puntaje), 25, ANCHO - 200, 5)
    
##------------- mause tiempo real ----------------------#####
    Mousex, Mousey = pygame.mouse.get_pos()
    
    if rectP.collidepoint(Mousex,Mousey):
        pausa = pygame.image.load('img/pausa_si.png').convert_alpha()
    else:
        pausa = pygame.image.load('img/pausa.png').convert_alpha()
        
    PANTALLA.blit(pausa, rectP)
    
    rect_target.center = (Mousex,Mousey)
    PANTALLA.blit(target, rect_target)   
    
    pygame.mouse.set_visible(0)
###----------- FPS del juego y refrescar la PANTALLA -----------########
    RELOJ.tick(FPS)
    pygame.display.update()