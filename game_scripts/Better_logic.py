import random
from game_scripts.house import background
from game_scripts.tiles import path
from game_scripts.furniture import furniture
from game_scripts.camera import camera

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
class HUD:
	def __init__(self,x,y,url,pygame):
		self.x = x
		self.y = y
		self.url = url
		self.hud = return_2x(self.url,4,pygame)
	def render(self,win,pygame,hero):
		win.blit(self.hud,(self.x,self.y))


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



def detect_colision(room_limit_x,room_limit_y,user):
	statement = False
	if user.x < room_limit_x[0]:
		user.colided_x_down = 1
		statement = True
	else:
		user.colided_x_down = 0
	
	if user.x > room_limit_x[1]:
		statement = True
		
		user.colided_x_up = 1
	else:

		user.colided_x_up = 0

	if user.y < room_limit_y[0]:
		statement = True

		user.colided_y_down = 1
	else:

		user.colided_y_down = 0
	if user.y > room_limit_y[1]:
		statement = True

		user.colided_y_up = 1
	else:

		user.colided_y_up = 0
	return statement 


def event_holder(local,keys,win,pygame,user,run,camera,level):
	if local == "loja_de_armas":
		color = (0,0,0)
		win.fill(color)
		new_back = background(pygame,win,1280,720,user)
		furnitures = []
		furnitures.append(furniture(680,300,200,50,128,64,"mesa_1",pygame))

		new_back.draw(camera)
		for block in furnitures:
			block.render(camera,win,pygame)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		limited = detect_colision(new_back.room_limit_x,new_back.room_limit_y,user)
		if not limited:
			user.collision(furnitures,pygame,camera)

		user.draw(keys,win,pygame,camera)
		level.is_inside = new_back.draw_door(win,pygame,user,camera,keys,level)
		return level,run