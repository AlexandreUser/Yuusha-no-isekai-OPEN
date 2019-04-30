import random


class render_font:
	def __init__(self,pygame,url,size,x,y):
		self.font = pygame.font.Font(url, size)
		self.x = x
		self.y = y
		self.color = (0,0,0)
	def text(self,text,win):
		text = self.font.render(text, True,self.color)
		win.blit(text,(self.x , self.y ))
	def update(self,x,y):
		self.x = x
		self.y = y
class tiles:
	def __init__(self, pygame):
		self.grass_tile = return_2x("./scenarios/grass_tile/0.png",4,pygame)
		self.x = 0
		self.y = 0
		
class HUD:
	def __init__(self,x,y,url,pygame):
		self.x = x
		self.y = y
		self.url = url
		self.hud = return_2x(self.url,4,pygame)
	def render(self,win,pygame,hero):
		win.blit(self.hud,(self.x,self.y))


class camera:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def update(self,mov_x,mov_y):
		self.x = mov_x
		self.y = mov_y
def return_2x(url,times,pygame):
	img = pygame.image.load(url)
	size = img.get_size()
	bigger = pygame.transform.scale(img,(int(size[0]*times),int(size[1]*times)))
	return bigger
def return_sc(url,pygame,x,y,sizing):
	img = pygame.image.load(url)
	size = img.get_size()
	bigger = pygame.transform.scale(img,(int(x*sizing),int(y*sizing)))
	return bigger
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
shadown = (93, 105, 38,20)
class path:
	def __init__(self,x,y,size):
		self.x = x
		self.y = y
		self.old_y = y
		self.old_x = x
		self.size = size
		self.width = 64*2
		self.height = 64*2
		self.h = 0
		self.path_dirt_I = ["./scenarios/dirt_end.png","./scenarios/dirt_fix.png"]
		self.path_dirt_L = ["./scenarios/dirt_end_L1.png","./scenarios/dirt_end_L2.png"]

	def I_path(self,win,pygame,camera):
		for i in range(0,self.size):
			
			tile = return_2x(self.path_dirt_I[self.h],2,pygame)
			win.blit(tile,(self.x-camera.x,self.y-camera.y))
			self.y += self.height
			self.h +=1
			if self.h >= 1:
				self.h = 1
		self.h = 0
		self.y = self.old_y
	def Inverted_L_path(self,win,pygame,camera):
		self.h = 1
		for i in range(0,self.size):
			if i == self.size-1:
				self.h = 0 
			tile = return_2x(self.path_dirt_L[self.h],2,pygame)
			win.blit(tile,(self.x-camera.x,self.y-camera.y))
			self.x -= self.width
			self.h +=1
			if self.h >= 1:
				self.h = 1
		self.h = 0
		self.x = self.old_x




class prop:
	def __init__(self,x,y,width,height,reduction,pygame,types=0,instance="house"):
		self.x = x 
		self.y = y 
		self.instance = instance
		self.width = width
		self.height = height
		self.is_inside = False
		self.type = types
		self.reduction = reduction
		self.prop_file = ["./scenarios/houses/1.png","./scenarios/houses/2.png","./scenarios/houses/3.png"]
		self.prop_blit = return_bg(self.prop_file[self.type],self.width,self.height,pygame)
		self.hitbox = (self.x , self.y , self.width-self.reduction, self.height-self.reduction)
	def draw(self,win,pygame,camera,hero,keys,cutScene_inside):
		self.hitbox = (self.x-camera.x , self.y-camera.y , self.width-self.reduction, self.height-self.reduction)

		if self.type == 1:
			self.placement_door = (self.x+self.width/3-camera.x,self.y*2.7-camera.y,self.width/4,self.height/3)

			self.hitbox = (self.x+self.width/10-camera.x , self.y+self.reduction-camera.y , self.width-self.reduction/2, self.height-self.reduction*2)
		elif self.type == 2:
			self.placement_door = (self.x+self.width/3-camera.x,self.y*2.7-camera.y,self.width/3.5,self.height/3)
			self.hitbox = (self.x-camera.x , self.y+self.reduction-camera.y , self.width, self.height-self.reduction*2)
		else:
			self.placement_door = (self.hitbox[0]+self.width/3,self.hitbox[1]+self.height/2,self.width/3.5,self.height/3)
			self.hitbox = ((self.x+self.reduction/2)-camera.x , self.y+self.reduction-camera.y , self.width - self.reduction*1.5, self.height-self.reduction*2)
		if self.type == 1:
			pygame.draw.rect(win, shadown, (self.hitbox[0],(self.y-camera.y)+self.height/1.9,self.width-self.reduction/2,self.height/4))
			win.blit(self.prop_blit,((self.hitbox[0]),((self.y-camera.y)-self.reduction/2)))
		elif self.type == 2:

			pygame.draw.rect(win, shadown, (self.hitbox[0],(self.y-camera.y)+self.height/1.9,self.width,self.height/4))
			win.blit(self.prop_blit,((self.hitbox[0]+self.reduction/8),((self.y-camera.y)-self.reduction/2)))

		else:
			pygame.draw.rect(win, shadown, (self.hitbox[0],(self.y-camera.y)+self.height/1.9,self.width-self.reduction*1.5,self.height/4))
			win.blit(self.prop_blit,((self.x-camera.x)-self.reduction/2,((self.y-camera.y)-self.reduction/2)))
		#ONLY FOR DEBUG PORPOSES
		#pygame.draw.rect(win, (255,0,0), self.hitbox,2)
		if self.instance == "house":
			if keys[pygame.K_q] and cutScene_inside > 190:
				self.is_inside = self.collided_door(pygame,win,hero,camera,keys)


	def collided_door(self,pygame,win,hero,camera,keys):
		deltaT = hero.get_rect(pygame,camera)
		new_rect = pygame.Rect(self.placement_door)
		if new_rect.colliderect(deltaT):
			return True
		else: 
			return False
class character:
	
	def __init__(self,name,pygame):
		self.name = name
		self.width = 40
		self.height = 20
		self.speed = 10
		self.x = 0
		self.y = 0
		self.font = render_font(pygame,"./fonts/Pixel_miners.otf",12,self.x,self.y)
		self.walking_right = [
			return_2x("./characters/Naofumy/walking_right/0.png",2,pygame),
			return_2x("./characters/Naofumy/walking_right/1.png",2,pygame),
			return_2x("./characters/Naofumy/walking_right/2.png",2,pygame),
			return_2x("./characters/Naofumy/walking_right/3.png",2,pygame),
			return_2x("./characters/Naofumy/walking_right/4.png",2,pygame),
			return_2x("./characters/Naofumy/walking_right/5.png",2,pygame),
			return_2x("./characters/Naofumy/walking_right/6.png",2,pygame),
			return_2x("./characters/Naofumy/walking_right/7.png",2,pygame)]
		self.walking_left = [
			return_2x("./characters/Naofumy/walking_left/0.png",2,pygame),
			return_2x("./characters/Naofumy/walking_left/1.png",2,pygame),
			return_2x("./characters/Naofumy/walking_left/2.png",2,pygame),
			return_2x("./characters/Naofumy/walking_left/3.png",2,pygame),
			return_2x("./characters/Naofumy/walking_left/4.png",2,pygame),
			return_2x("./characters/Naofumy/walking_left/5.png",2,pygame),
			return_2x("./characters/Naofumy/walking_left/6.png",2,pygame),
			return_2x("./characters/Naofumy/walking_left/7.png",2,pygame)]
		self.walking_down = [
			return_2x("./characters/Naofumy/walking_down/0.png",2,pygame),
			return_2x("./characters/Naofumy/walking_down/1.png",2,pygame),
			return_2x("./characters/Naofumy/walking_down/2.png",2,pygame),
			return_2x("./characters/Naofumy/walking_down/3.png",2,pygame),
			return_2x("./characters/Naofumy/walking_down/4.png",2,pygame),
			return_2x("./characters/Naofumy/walking_down/5.png",2,pygame)]
		self.walking_top = [
			return_2x("./characters/Naofumy/walking_top/0.png",2,pygame),
			return_2x("./characters/Naofumy/walking_top/1.png",2,pygame),
			return_2x("./characters/Naofumy/walking_top/2.png",2,pygame),
			return_2x("./characters/Naofumy/walking_top/3.png",2,pygame),]
		self.actual_frame = 0
		self.walking_left_frames = len(self.walking_left)*2
		self.walking_right_frames = len(self.walking_right)*2
		self.walking_down_frames = len(self.walking_down)*2
		self.walking_top_frames = len(self.walking_top)*2
		self.colided_x_up = 0
		self.colided_x_down = 0
		self.colided_y_up = 0
		self.colided_y_down = 0

		self.moving = False
		self.hitbox = (self.x+self.width,self.y+self.height*6,self.width,self.height)
		self.direction = "L"
	def move(self,keys,pygame,camera,fake=False):
		self.moving = True
		if fake == True:
			self.y += self.speed
			self.direction = "D"
		else:
			if keys[pygame.K_s] and self.colided_y_up == 0:
				self.y += self.speed
				self.direction = "D"
			elif keys[pygame.K_w] and self.colided_y_down == 0:
				self.y -= self.speed
				self.direction = "U"
			elif keys[pygame.K_d] and self.colided_x_up == 0:
				self.x += self.speed
				self.direction = "R"
			elif keys[pygame.K_a] and self.colided_x_down == 0 :
				self.x -= self.speed
				self.direction = "L"
			else:
				self.moving = False
		self.hitbox = ((self.x+self.width)-camera.x,(self.y+self.height*6)-camera.y,self.width,self.height)
	def animate(self,win,camera):
		if self.moving == True:
			if self.direction == 'D':
				if self.actual_frame >= self.walking_down_frames-1:
					self.actual_frame = 0
				else:
					self.actual_frame +=1
				win.blit(self.walking_down[self.actual_frame//2],(self.x-camera.x,self.y-camera.y))
			elif self.direction == 'U':
				if self.actual_frame >= self.walking_top_frames-1:
					self.actual_frame = 0
				else:
					self.actual_frame +=1
				win.blit(self.walking_top[self.actual_frame//2],(self.x-camera.x,self.y-camera.y))
				
			elif self.direction == 'R':
				if self.actual_frame >= self.walking_right_frames-1:
					self.actual_frame = 0
				else:
					self.actual_frame +=1
				win.blit(self.walking_right[self.actual_frame//2],(self.x-camera.x,self.y-camera.y))
				
			elif self.direction == "L":
				if self.actual_frame >= self.walking_left_frames-1:
					self.actual_frame = 0
				else:
					self.actual_frame +=1
				win.blit(self.walking_left[self.actual_frame//2],(self.x-camera.x,self.y-camera.y))

		else:
			if self.direction == "R" :
				win.blit(self.walking_right[0],(self.x-camera.x,self.y-camera.y))
			elif self.direction == "L":
				win.blit(self.walking_left[0],(self.x-camera.x,self.y-camera.y))
			elif self.direction == "U" :
				win.blit(self.walking_top[0],(self.x-camera.x,self.y-camera.y))
			elif self.direction == "D" :
				win.blit(self.walking_down[0],(self.x-camera.x,self.y-camera.y))
	def get_rect(self,pygame,camera):
		return pygame.Rect((self.x+self.width)-camera.x,(self.y+self.height*6)-camera.y,self.width,self.height)
	def draw(self,keys,win,pygame,camera):
		self.move(keys,pygame,camera)
		shadown = (104, 104, 104,20)
		self.font.update(self.x+self.width-camera.x,self.y-10-camera.y)
		self.font.text(self.name,win)
		
		surface = pygame.Surface((50, 50), pygame.SRCALPHA, 32)
		pygame.draw.ellipse(
		    surface, 
		    (0, 0, 0, 50), 
		    [0,0,50,20])
		win.blit(surface, ((self.x+self.width*1.1)-camera.x, (self.y+self.height*5.5)-camera.y))
		#pygame.draw.ellipse(win, shadown, [self.x+self.width*1.1, self.y+self.height*5.5, 50, 20],1)
		
		self.animate(win,camera)
	def collision(self,rect1,pygame,camera):
		new_rect = []
		for i in range(0,len(rect1)):
			new_rect.append(pygame.Rect(rect1[i].hitbox))
		deltaT = self.get_rect(pygame,camera)
		self.colided_y_up = 0
		self.colided_y_down = 0 
		self.colided_x_down = 0
		self.colided_x_up = 0 
		for h in range(0,len(new_rect)):
			if new_rect[h].colliderect(deltaT):
				if new_rect[h][1] > deltaT[1]:
					self.colided_y_up = 1
				elif new_rect[h][1] < deltaT[1]:
					self.colided_y_down = 1
				if new_rect[h][0] > deltaT[0]:
					self.colided_x_up = 1
					self.colided_x_down = 0
				elif new_rect[h][0] < deltaT[0]:
					self.colided_x_down = 1
					self.colided_x_up = 0
def detect_colision(room_limit_x,room_limit_y,user):
	if user.x < room_limit_x[0]:
		user.colided_x_down = 1
	else:
		user.colided_x_down = 0
	if user.x > room_limit_x[1]:
		
		user.colided_x_up = 1
	else:
		user.colided_x_up = 0

	if user.y < room_limit_y[0]:
		user.colided_y_down = 1
	else:
		user.colided_y_down = 0
	if user.y > room_limit_y[1]:
		user.colided_y_up = 1
	else:
		user.colided_y_up = 0
class background:
	def __init__(self,pygame,win,screenwidth,screenheight,user):
		self.pygame = pygame
		self.win = win
		self.user = user
		self.screenwidth = screenwidth
		self.screenheight = screenheight
		self.position_x = [0,350]
		self.position_y = [0,400]
		self.room_limit_x = [200,900]
		self.room_limit_y = [150,450]
		self.casa = "./scenarios/casa_1.png"
		self.porta = "./scenarios/door_1.png"
		self.door_size = (120,250)
		self.door_hitbox = (self.position_x[1]+self.door_size[0],self.position_y[1]+self.door_size[1],150,20)
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
		self.update(camera)
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
	def update(self,camera):

		self.position_y[1] -= camera.y
		self.position_y[0] -= camera.y
		self.position_x[0] -= camera.x
		self.position_x[1] -= camera.x

def event_holder(keys,win,pygame,user,run,camera,level):
	color = (0,0,0)
	win.fill(color)
	new_back = background(pygame,win,1280,720,user)
	new_back.draw(camera)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	detect_colision(new_back.room_limit_x,new_back.room_limit_y,user)
	user.draw(keys,win,pygame,camera)
	level.is_inside = new_back.draw_door(win,pygame,user,camera,keys,level)
	return level,run