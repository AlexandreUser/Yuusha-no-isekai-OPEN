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
import time
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,pygame,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.Font("./fonts/Pixel_miners.otf",12)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
class npc:
	def __init__(self,x,y,name,pygame):
		self.width = 40
		self.height = 20
		self.variance = 80
		self.x = x
		self.y = y
		self.name = name
		self.font = render_font(pygame,"./fonts/Pixel_miners.otf",12,self.x,self.y)
		self.idle = [
			return_2x("./npc/"+self.name+"/idle/0.png",2,pygame),
			return_2x("./npc/"+self.name+"/idle/1.png",2,pygame),
			return_2x("./npc/"+self.name+"/idle/2.png",2,pygame),
			return_2x("./npc/"+self.name+"/idle/3.png",2,pygame),
			return_2x("./npc/"+self.name+"/idle/4.png",2,pygame)]
		self.idle_frames = len(self.idle)*2
		self.actual_frame = 0
		self.dialogue_box = return_2x("./characters/dialogue_box_0",3,pygame)
		self.ballon_box = return_2x("./misc/ballon_shape.png",2,pygame)
		self.hitbox = (self.x+self.width,self.y+self.height*6,self.width,self.height)
		self.is_talking = False
		self.times = 0
		self.font_text = render_font(pygame,"./fonts/Pixel_miners.otf",10,self.x,self.y)
		self.dialogues_text = ["Ola, pelo visto você também é um heroi.","que azar...","Fui jogada nesse mundo ","ja faz uma semana","E ainda não sai do nivel 10"]
		self.j = 0
		self.wait = 0 
		self.begun = False
	def draw(self,win,pygame,camera):
		if self.variance >= 80:
			self.begun = True
		elif self.variance < 60:
			self.begun = False
		if self.begun == True:
			self.variance -= 1
		else:
			self.variance += 1
			self.variance += 1
		if self.actual_frame >= self.idle_frames-1:
			self.actual_frame = 0
		else:
			self.actual_frame += 1
		self.font.update(self.x+self.width-camera.x,self.y-10-camera.y)
		win.blit(self.ballon_box,(self.x+self.width/1.4-camera.x,self.y-self.variance-camera.y))
		self.font.text(self.name,win)
		surface = pygame.Surface((50, 50), pygame.SRCALPHA, 32)
		pygame.draw.ellipse(
			    surface, 
			    (0, 0, 0, 50), 
			    [0,0,50,20])
		win.blit(surface, ((self.x+self.width*1.1)-camera.x, (self.y+self.height*5.5)-camera.y))
		win.blit(self.idle[self.actual_frame//2],(self.x-camera.x,self.y-camera.y))
		#pygame.draw.rect(win, (0,0,0), ((self.x-self.width)-camera.x,(self.y+self.height*6)-camera.y,self.width*4,self.height*2),0)
	def get_rect(self,pygame,camera):
		return pygame.Rect((self.x-self.width)-camera.x,(self.y+self.height*6)-camera.y,self.width*4,self.height*2)
	def dialogue(self,hero,win,pygame,camera,keys,options):

		hero_rect = hero.get_rect(pygame,camera)
		new_rect = self.get_rect(pygame,camera)
		btn = button((109, 40, 0),options[0]+250,options[1]+100-20,80,20,"proximo")
		pos = pygame.mouse.get_pos()
		if not self.is_talking:
			if hero_rect.colliderect(new_rect):
				if keys[pygame.K_q]:
					self.j = 0
					self.times = 0
					self.is_talking = True
		else:
			if hero_rect.colliderect(new_rect):
				self.dialogue_box = return_sc("./characters/dialogue_box_0",pygame,32*self.times,64,2)
				win.blit(self.dialogue_box,(options[0],options[1]))
				if self.times >= 6:
					self.times = 6
					self.font_text.update(options[0]+50,options[1]+50)
					win.blit(self.dialogue_box,(options[0],options[1]))
					self.font_text.text(self.dialogues_text[self.j],win)
					btn.draw(win,pygame)

				else:
					self.times +=1
				if btn.isOver(pos) and pygame.mouse.get_pressed()[0]:
					time.sleep(.100)
					if self.j <= len(self.dialogues_text)-2:
						self.j +=1 
					else:
						self.j = 0
						self.is_talking = False
						self.times = 0
			else:
				self.is_talking = False
				self.times = 0
				self.j = 0 
