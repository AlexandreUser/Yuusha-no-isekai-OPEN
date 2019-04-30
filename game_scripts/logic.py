WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (45, 216, 108)
RED =       (255,   0,   0)
shadown =     (48, 29, 19)
TEXTCOLOR = (  0,   0,   0)
#self.room_limit_x = 
#self.room_limit_y = 
from math import pi
class prop:
	def __init__(self,x,y,width,height,pygame):
		self.x = x 
		self.y = y 
		self.width = width
		self.height = height
		self.prop_file = pygame.image.load("./scenarios/houses/1.png")
		self.hitbox = (self.x , self.y , self.width, self.height)

		#self.prop_file = pygame.transform.scale(bg
	def update(self,user,win,pygame):
		self.x -= user.x
		self.y -= user.y
		win.blit(self.prop_file,(self.x,self.y))
		self.hitbox = (self.x , self.y , self.width, self.height)
		pygame.draw.rect(win, (255,0,0), self.hitbox,2)
class background:
	def __init__(self,pygame,win,screenwidth,screenheight,user):
		self.pygame = pygame
		self.win = win
		self.user = user
		self.screenwidth = screenwidth
		self.screenheight = screenheight
		self.position_x = [550]
		self.position_y = [340]
		self.room_limit_x = [750,1480]
		self.room_limit_y = [500,800]
		self.casa = "./scenarios/casa_1.png"

	def draw(self):
		self.bgs = []
		#self.bgs.append(return_bg(self.sky,self.screenwidth,self.screenheight,self.pygame))
		self.bgs.append(return_bg(self.casa,self.screenwidth,self.screenheight,self.pygame))

		self.update(self.user)
		h = 0 
		for item in self.bgs:
			print(self.user.x,self.user.y)
			print(self.position_x,self.position_y)
			self.win.blit(item,(self.position_x[h],self.position_y[h]))
			h+=1
		


	def update(self,user):
		self.user = user
		for i in range(0,len(self.room_limit_x)):
			self.room_limit_x[i] -= self.user.x
		for i in range(0,len(self.room_limit_y)):
			self.room_limit_y[i] -= self.user.y 
		for i in range(0,len(self.position_x)):
			self.position_x[i] -= self.user.x 
		for i in range(0,len(self.position_y)):
			self.position_y[i] -= self.user.y 
class Hero:
	def __init__(self,name,pygame):
		self.pygame = pygame
		self.name = name
		self.speed = 10
		self.life = 100
		self.damage = 5
		self.click = 0
		self.x = 0
		self.y = 0
		self.golden_coins = 500
		self.emeralds = 10
		self.direction = "left"
		self.width = 50
		self.height = 20
		self.hitbox = (self.x + self.width, self.y + self.height, 50, 70)

		self.attacking = False
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.walking_right = [
			return_2x("./characters/Naofumy/walking_right/0.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_right/1.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_right/2.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_right/3.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_right/4.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_right/5.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_right/6.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_right/7.png",2,self.pygame)]
		self.walking_left = [
			return_2x("./characters/Naofumy/walking_left/0.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_left/1.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_left/2.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_left/3.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_left/4.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_left/5.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_left/6.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_left/7.png",2,self.pygame)]
		self.walking_down = [
			return_2x("./characters/Naofumy/walking_down/0.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_down/1.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_down/2.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_down/3.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_down/4.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_down/5.png",2,self.pygame)]
		self.walking_top = [
			return_2x("./characters/Naofumy/walking_top/0.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_top/1.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_top/2.png",2,self.pygame),
			return_2x("./characters/Naofumy/walking_top/3.png",2,self.pygame),]
		self.actual_frame = 0
		self.walking_left_frames = len(self.walking_left)*2
		self.walking_right_frames = len(self.walking_right)*2
		self.walking_down_frames = len(self.walking_down)*2
		self.walking_top_frames = len(self.walking_top)*2
		self.colided_x_up = 0
		self.colided_x_down = 0
		self.colided_y_up = 0
		self.colided_y_down = 0	
	def get_rect(self,pygame):
		return pygame.Rect(self.x, self.y, self.width, self.height)
		pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height),2) # To draw the hit box around the player

	def walk(self,direction):
		self.direction = direction
		if direction == "up" and self.colided_y_down == 0:
			self.y -= self.speed
		elif direction == "down" and self.colided_y_up == 0:
			self.y += self.speed
		elif direction == "right" and self.colided_x_up == 0:
			self.x += self.speed
		elif direction == "left" and self.colided_x_down == 0:
			self.x -= self.speed
		else:
			pass
	def moviment(self,keys,pygame,win,prop):
		self.hitbox = (self.x + self.width, self.y + self.height, 20, 70)
		pygame.draw.rect(win, (255,0,0), self.hitbox,2) # To draw the hit box around the player
		pygame.draw.ellipse(win, shadown, [self.x+self.width*1, self.y+self.height*5.5, 50, 20])
		new_rect = pygame.Rect(prop.hitbox)
		if new_rect.colliderect(self.get_rect(pygame)):
			print("COLIDIU AQUI PORRA AAAA ")
		if keys[pygame.K_s] and self.colided_y_up == 0:
			self.walk("down")
			if self.actual_frame >= self.walking_down_frames-1:
				self.actual_frame = 0
			else:
				self.actual_frame +=1
			win.blit(self.walking_down[self.actual_frame//2],(self.x,self.y))
		elif keys[pygame.K_d] and self.colided_x_up == 0:
			self.walk("right")
			if self.actual_frame >= self.walking_right_frames-1:
				self.actual_frame = 0
			else:
				self.actual_frame +=1
			win.blit(self.walking_right[self.actual_frame//2],(self.x,self.y))
		elif keys[pygame.K_a]  and self.colided_x_down == 0:
			if self.actual_frame >= self.walking_left_frames-1:
				self.actual_frame = 0
			else:
				self.actual_frame +=1
			win.blit(self.walking_left[self.actual_frame//2],(self.x,self.y))
			self.walk("left")
		elif keys[pygame.K_w] and self.colided_y_down == 0:
			if self.actual_frame >= self.walking_top_frames-1:
				self.actual_frame = 0
			else:
				self.actual_frame +=1
			win.blit(self.walking_top[self.actual_frame//2],(self.x,self.y))
			self.walk("up")
		else:
			if self.direction == "right" :
				win.blit(self.walking_right[0],(self.x,self.y))
			elif self.direction == "left":
				win.blit(self.walking_left[0],(self.x,self.y))
			elif self.direction == "up" :
				win.blit(self.walking_top[0],(self.x,self.y))
			elif self.direction == "down" :
				win.blit(self.walking_down[0],(self.x,self.y))


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

def event_holder(keys,win,pygame,user,run):
	color = (0,0,0)
	win.fill(color)
	new_back = background(pygame,win,1280,720,user)
	new_back.draw()
	item = prop(1200,700,100,100,pygame)
	item.update(user,win,pygame)
	
	pygame.time.delay(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	detect_colision(new_back.room_limit_x,new_back.room_limit_y,user)
	user.moviment(keys,pygame,win,item)
	pygame.display.update()
	return run

def return_2x(url,times,pygame):
	img = pygame.image.load(url)
	size = img.get_size()
	bigger = pygame.transform.scale(img,(int(size[0]*times),int(size[1]*times)))
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

