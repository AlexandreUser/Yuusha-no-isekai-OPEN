from game_scripts.Better_logic import return_2x,render_font,return_sc

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