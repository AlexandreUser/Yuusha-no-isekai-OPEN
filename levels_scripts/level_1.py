from game_scripts.Better_logic import render_font,HUD,event_holder
from game_scripts.house import background
from game_scripts.tiles import path
from game_scripts.character import character
from game_scripts.prop import prop
from game_scripts.furniture import furniture
from game_scripts.camera import camera
from game_scripts.npc import npc
cutScene = 200
cutScene_inside = 0

class phases:
	def __init__(self,level):
		self.phase = level
		self.houses = []
		self.paths = []
		self.is_inside = False
	def init(self,pygame):
		self.houses = []
		self.houses.append(prop(400,100,500,500,80,pygame,0,"house"))
		self.houses.append(prop(-280,150,500,500,80,pygame,1,"house"))
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
		self.__version.text("Alpha v.0.0.7",win)
	def display_sobreposto(self,camera,pygame,win,hero,keys):
			#if self.is_sobrepost == False:
				#self.enemies[h].draw(win,pygame,camera,hero)
		for i in range(0,len(self.Sobreposto)):
			self.Sobreposto[i].draw(win,pygame,camera,hero,keys,cutScene_inside)

		for i in range(0,len(self.npc_sobreposto)):
			self.npc_sobreposto[i].draw(win,pygame,camera)
		self.npc_sobreposto = []
		self.Sobreposto = []