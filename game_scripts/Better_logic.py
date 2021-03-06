import random
from game_scripts.house import background
from game_scripts.tiles import path
from game_scripts.furniture import furniture
from game_scripts.camera import camera
from game_scripts.npc import npc

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
	statement_y = ""
	statement_x = ""
	if user.x < room_limit_x[0]:
		user.colided_x_down = 1
		statement_x = "X_down"
	else:
		user.colided_x_down = 0
	
	if user.x > room_limit_x[1]:
		statement_x = "X_up"
		
		user.colided_x_up = 1
	else:

		user.colided_x_up = 0

	if user.y < room_limit_y[0]:
		statement_y = "Y_down"

		user.colided_y_down = 1
	else:

		user.colided_y_down = 0
	if user.y > room_limit_y[1]:
		statement_y = "Y_up"

		user.colided_y_up = 1
	else:

		user.colided_y_up = 0
	return [statement_x,statement_y]
def adjust_house_pos(camera,new_back,npcs,npcs_pos):
	new_back.position_x[0] = camera.x + 100
	new_back.position_x[1] = camera.x + 450
	new_back.position_y[0] = camera.y - 100
	new_back.position_y[1] = camera.y + 220
	new_back.room_limit_y[0] += camera.y - 100
	new_back.room_limit_y[1] += camera.y - 100
	new_back.room_limit_x[0] += camera.x + 100
	new_back.room_limit_x[1] += camera.x + 100
	for i in range(0,len(npcs)):
		npcs[i].x = camera.x + npcs_pos[i][0]
		npcs[i].y = camera.y + npcs_pos[i][1]
	return new_back,npcs
def render_inside(gaming,local,keys,win,pygame,user,run,camera,level):
	if local == "loja_de_armas":
		npcs_pos = [(400,120)]
		color = (0,0,0)
		win.fill(color)
		npcs = []
		new_back = background(pygame,win,1280,720,user)
		new_back,level.npcs_insides = adjust_house_pos(camera,new_back,level.npcs_insides,npcs_pos)
		furnitures = []
		furnitures.append(furniture(680,300,200,50,128,64,"mesa_1",pygame))
		furnitures.append(furniture(305,400,80,50,128,64,"balcao_1",pygame))

		new_back.draw(camera)
		vendor = level.npcs_insides[0]
		vendor.dialogues_text = ["Tem interesse em comprar alguma arma ?","posso lhe fazer um preço especial"]
		vendor.height = 30
		vendor.draw(win,pygame,camera)

		for block in furnitures:
			block.render(camera,win,pygame)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		statement = detect_colision(new_back.room_limit_x,new_back.room_limit_y,user)
		print(statement)
		user.collision(furnitures,pygame,camera,statement)

		user.draw(keys,win,pygame,camera)
		vendor.dialogue(user,win,pygame,camera,keys,gaming.menu_placement())
		level.is_inside = new_back.draw_door(win,pygame,user,camera,keys,level)
			
		return level,run