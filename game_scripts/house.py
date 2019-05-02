def return_bg(url,width,height,pygame):
	bg = pygame.image.load(url)
	size = bg.get_size()
	print(size)
	if(width > size[0]):
		bigger = pygame.transform.scale(bg,(int((width/size[0])*size[0]),int((height/size[1])*size[1])))
		print(bigger.get_size())
		return bigger
	else:
		return bg
def return_2x(url,times,pygame):
	img = pygame.image.load(url)
	size = img.get_size()
	bigger = pygame.transform.scale(img,(int(size[0]*times),int(size[1]*times)))
	return bigger
class background:
	def __init__(self,pygame,win,screenwidth,screenheight,user):
		self.pygame = pygame
		self.win = win
		self.user = user
		self.screenwidth = screenwidth
		self.screenheight = screenheight
		self.position_x = [0,350]
		self.position_y = [0,320]
		self.room_limit_x = [200,900]
		self.room_limit_y = [150,450]
		self.casa = "./scenarios/casa_1.png"
		self.porta = "./scenarios/door_1.png"
		self.door_size = (120,250)
		self.door_hitbox = (self.position_x[1],self.position_y[1],150,20)
	def draw(self,camera):
		self.bgs = []
		#self.bgs.append(return_bg(self.sky,self.screenwidth,self.screenheight,self.pygame))
		self.bgs.append(return_bg(self.casa,self.screenwidth,self.screenheight,self.pygame))

		self.update(camera)
		h = 0 
		for item in self.bgs:
			print(self.position_x,self.position_y)
			self.win.blit(item,(self.position_x[h],self.position_y[h]))
			h+=1
	def draw_door(self,win,pygame,hero,camera,keys,level,debug=False):
		self.door_hitbox = (self.position_x[1]+self.door_size[0],self.position_y[1]+self.door_size[1],150,20)
		porta = return_2x(self.porta,4,self.pygame)
		deltaT = hero.get_rect(pygame,camera)
		new_rect = pygame.Rect(self.door_hitbox)
		win.blit(porta,(self.position_x[1],self.position_y[1]))
		if new_rect.colliderect(deltaT):
			if keys[pygame.K_q]:
				level.is_inside = False
				return level.is_inside
	

		if debug == True:
			pygame.draw.rect(win, (255,0,0), self.door_hitbox,2)
	def update(self,hero):
		self.position_y[1] -= hero.y
		self.position_y[0] -= hero.y
		self.position_x[0] -= hero.x
		self.position_x[1] -= hero.x
