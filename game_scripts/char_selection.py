from game_scripts.Better_logic import return_2x,render_font,return_sc

class select_hero:
	def __init__(self,x,y,pygame):
		self.selected = False
		self.heroes = []
		self.x = x
		self.old_x = x
		self.old_y = y
		self.y = y
		self.hero_size = 2
		self.moldur_img_size = 3
		self.heroes = [
		return_2x("./char_selection/tank_grass/1.png",self.hero_size,pygame),
		return_2x("./char_selection/tank_grass/2.png",self.hero_size,pygame),
		return_2x("./char_selection/tank_grass/3.png",self.hero_size,pygame),
		return_2x("./char_selection/tank_grass/4.png",self.hero_size,pygame),
		return_2x("./char_selection/tank_grass/5.png",self.hero_size,pygame),
		return_2x("./char_selection/tank_grass/6.png",self.hero_size,pygame)
		]
		self.moldura = return_2x("./char_selection/tank_grass/moldura.png",self.moldur_img_size,pygame)
		self.background = return_2x("./char_selection/tank_grass/fundo_replace.png",self.moldur_img_size,pygame)

		self.image_size = self.heroes[0].get_size()
		self.moldura_size = self.moldura.get_size()
		self.width = self.moldura_size[0]
		self.height = self.moldura_size[1]
		self.frames = len(self.heroes)*3
		self.actual_frame = 0
		print(self.image_size)
	def draw(self,win,pygame):
		if self.actual_frame >= self.frames - 1:
			self.actual_frame = 0
		else:
			self.actual_frame +=1
		pos = pygame.mouse.get_pos()
		self.hover(pos,pygame)
		win.blit(self.background,(self.x-60,self.y-100))
		win.blit(self.heroes[self.actual_frame//3],(self.x,self.y))
		win.blit(self.moldura,(self.x-60,self.y-100))
	def isOver(self, pos):
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		return False
	def hover(self,pos,pygame):
		if self.isOver(pos):
			if pygame.mouse.get_pressed()[0]:
				self.selected = True

			self.hero_size = 2.2
		
			self.x = self.old_x - 20
			self.y = self.old_y - 50
			self.moldur_img_size = 3.3
			self.heroes = [
			return_2x("./char_selection/tank_grass/1.png",self.hero_size,pygame),
			return_2x("./char_selection/tank_grass/2.png",self.hero_size,pygame),
			return_2x("./char_selection/tank_grass/3.png",self.hero_size,pygame),
			return_2x("./char_selection/tank_grass/4.png",self.hero_size,pygame),
			return_2x("./char_selection/tank_grass/5.png",self.hero_size,pygame),
			return_2x("./char_selection/tank_grass/6.png",self.hero_size,pygame)
			]
			self.moldura = return_2x("./char_selection/tank_grass/moldura.png",self.moldur_img_size,pygame)
			self.background = return_2x("./char_selection/tank_grass/fundo_replace.png",self.moldur_img_size,pygame)
		else:
			self.x = self.old_x
			self.y = self.old_y
			self.hero_size = 2
			self.moldur_img_size = 3
			self.heroes = [
			return_2x("./char_selection/tank_grass/1.png",self.hero_size,pygame),
			return_2x("./char_selection/tank_grass/2.png",self.hero_size,pygame),
			return_2x("./char_selection/tank_grass/3.png",self.hero_size,pygame),
			return_2x("./char_selection/tank_grass/4.png",self.hero_size,pygame),
			return_2x("./char_selection/tank_grass/5.png",self.hero_size,pygame),
			return_2x("./char_selection/tank_grass/6.png",self.hero_size,pygame)
			]
			self.moldura = return_2x("./char_selection/tank_grass/moldura.png",self.moldur_img_size,pygame)
			self.background = return_2x("./char_selection/tank_grass/fundo_replace.png",self.moldur_img_size,pygame)
