import pygame
import time
from game_scripts.Better_logic import character,prop,path,camera,render_font,HUD,event_holder
from game_scripts.npc import npc
from game_scripts.Better_logic import background
class options:
	def __init__(self,width,height):
		self.width = width
		self.height = height
	def resolution_lowScaled(self):
		return (int(self.width/1.5),int(self.height/1.5))
	def resolution_medScaled(self):
		return (self.width,self.height)
	def mid_place(self,hero):
		return (-(self.width/2-hero.width),-(self.height/2-hero.height))
	def menu_placement(self):
		return (self.width/3,self.height-130)
pygame.init()
screenwidth = 1280
screenheight = 680
gaming = options(screenwidth,screenheight)
class phases:
	def __init__(self,level):
		self.phase = level
		self.houses = []
		self.paths = []
		self.is_inside = False
	def init(self,pygame):
		self.houses = []
		self.houses.append(prop(400,100,500,500,80,pygame,0,"house"))
		self.houses.append(prop(-280,150,500,500,80,pygame,1,"not"))
		self.houses.append(prop(-780,150,500,500,80,pygame,0,"not"))
		self.houses.append(prop(-1380,150,500,500,80,pygame,2,"not"))
		self.houses.append(prop(-280,600,500,500,80,pygame,2,"not"))
		self.houses.append(prop(-1380,600,500,500,80,pygame,1,"not"))
		self.paths = []
		self.paths.append(path(560,500,12))
		self.paths.append(path(530,550,20))
		self.paths.append(path(530,1000,20))
		self.npcs = []
		self.npcs.append(npc(420,380,"leona",pygame))
		#self.npcs.append(npc(-300,440,"lucio",pygame))
		#self.npcs[1].dialogues_text = ["Olha só, você é um novato","Boa sorte daqui pra frente"]
		self.Sobreposto = []
		self.npc_sobreposto = []
		self.__version = render_font(pygame,"./fonts/Pixel_miners.otf",24,0,20)
	def display(self,camera,pygame,win,hero,keys,cutScene_inside):
		self.paths[2].Inverted_L_path(win, pygame,camera)
		self.paths[1].Inverted_L_path(win, pygame,camera)
		self.paths[0].I_path(win,pygame,camera)


		for i in range(0,len(self.houses)):
			if keys[pygame.K_q] and cutScene_inside > 190:
				self.houses[i].is_inside = self.houses[i].collided_door(pygame,win,hero,camera,keys)
				if self.houses[i].is_inside:
					self.is_inside = True
			if self.houses[i].y+self.houses[i].height/3 > hero.y:
				self.Sobreposto.append(self.houses[i])
			else:
				self.houses[i].draw(win,pygame,camera,hero,keys,cutScene_inside)
		for i in range(0,len(self.npcs)):
			if self.npcs[i].y+self.npcs[i].height/2 > hero.y:
				self.npc_sobreposto.append(self.npcs[i])
			else:
				self.npcs[i].draw(win,pygame,camera)
		self.__version.color = (255,255,255)
		self.__version.text("Alpha v.0.0.5",win)
	def display_sobreposto(self,camera,pygame,win,hero,keys):
			#if self.is_sobrepost == False:
				#self.enemies[h].draw(win,pygame,camera,hero)
		for i in range(0,len(self.Sobreposto)):
			self.Sobreposto[i].draw(win,pygame,camera,hero,keys,cutScene_inside)

		for i in range(0,len(self.npc_sobreposto)):
			self.npc_sobreposto[i].draw(win,pygame,camera)
		self.npc_sobreposto = []
		self.Sobreposto = []
hero = character("Naofumi",pygame)
hero.x = 500
hero.y = 500
camera = camera(hero.x,hero.y)
win = pygame.display.set_mode((gaming.resolution_medScaled()))
pygame.display.set_caption("Yuusha no isekai")
run = True
level = phases(1)
level.init(pygame)
newhud = HUD(-100,screenheight-200,"./scenarios/huds/0.png",pygame)
not_trigger = False

def level_1(keys,level,hero,pygame,win,camera,cutScene,cutScene_inside,not_trigger,run):
	if level.is_inside == False:
		if cutScene_inside < 200:
			cutScene = 200
			cutScene_inside += 10
			win.fill((cutScene_inside,cutScene_inside,cutScene_inside))
		else:
			level.display(camera,pygame,win,hero,keys,cutScene_inside)	
			hero.draw(keys,win,pygame,camera)
			level.display_sobreposto(camera,pygame,win,hero,keys)

			hero.collision(level.houses,pygame,camera)
			level.npcs[0].dialogue(hero,win,pygame,camera,keys,gaming.menu_placement())
			#level.npcs[1].dialogue(hero,win,pygame,camera,keys,gaming.menu_placement())
			camera.update(gaming.mid_place(hero)[0]+hero.x,gaming.mid_place(hero)[1]+hero.y)	
	else:
		cutScene_inside = 0 
	return cutScene, cutScene_inside,level.is_inside
cutScene = 200
cutScene_inside = 0
while run:
	win.fill((103, 140, 51))
	keys = pygame.key.get_pressed()
	cutScene,cutScene_inside,level.is_inside = level_1(keys,level,hero,pygame,win,camera,cutScene,cutScene_inside,not_trigger,run)
	if level.is_inside != False:
		if cutScene > 10:
			win.fill((cutScene, cutScene, cutScene))
			cutScene-=10
		else:
			level,run = event_holder(keys,win,pygame,hero,run,camera,level)
	else:
		level.is_inside = False
	newhud.render(win,pygame,hero)
	pygame.time.delay(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()
