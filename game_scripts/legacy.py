class enemy:
	def __init__(self,name,pygame,x,y,sizing):
		self.name = name
		self.width = 40
		self.height = 20
		self.speed = 10
		self.x = x
		self.y = y
		self.sizing = sizing
		self.moving = True
		self.font = render_font(pygame,"./fonts/Pixel_miners.otf",12,self.x,self.y)
		self.direction = "R"
		self.walking_left = [
				return_2x("./enemies/lobo/walk_right/0.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_right/1.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_right/2.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_right/3.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_right/4.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_right/5.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_right/6.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_right/7.png",sizing,pygame)]
		self.walking_right = [
				return_2x("./enemies/lobo/walk_left/0.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_left/1.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_left/2.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_left/3.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_left/4.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_left/5.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_left/6.png",sizing,pygame),
				return_2x("./enemies/lobo/walk_left/7.png",sizing,pygame)]
		self.actual_frame = 0
		self.walking_left_frames = len(self.walking_left)*2
		self.walking_right_frames = len(self.walking_right)*2
		self.colided_x_up = 0
		self.colided_x_down = 0
		self.colided_y_up = 0
		self.colided_y_down = 0
		self.hitbox = (self.x+self.width,self.y+self.height*6,self.width,self.height)
		self.state = 0
		self.path = "L"
	def move(self,side,win,camera):
		if side == "R" and self.colided_x_up == 0:
			self.x += self.speed
			self.direction = "R"
		elif side == "L" and self.colided_x_down == 0 :
			self.x -= self.speed
			self.direction = "L"
		elif side == "U" and self.colided_y_up == 0 :
			self.y += self.speed
		elif side == "D" and self.colided_y_down == 0 :
			self.y -= self.speed
		else:
			self.moving = False
		self.hitbox = ((self.x+self.width)-camera.x,(self.y+self.height*6)-camera.y,self.width,self.height)
	def get_rect(self,pygame,camera):
		return pygame.Rect((self.x+self.width)-camera.x,(self.y+self.height*6)-camera.y,self.width,self.height)
	def animate(self,win,camera):
		if self.moving == True:
			if self.direction == 'R':
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
			elif self.direction == "U":
				if self.actual_frame >= self.walking_left_frames-1:
					self.actual_frame = 0
				else:
					self.actual_frame +=1
				win.blit(self.walking_left[self.actual_frame//2],(self.x-camera.x,self.y-camera.y))
			elif self.direction == "D":
				if self.actual_frame >= self.walking_right_frames-1:
					self.actual_frame = 0
				else:
					self.actual_frame +=1
				win.blit(self.walking_right[self.actual_frame//2],(self.x-camera.x,self.y-camera.y))

		else:
			if self.direction == "R" :
				win.blit(self.walking_right[0],(self.x-camera.x,self.y-camera.y))
			elif self.direction == "L":
				win.blit(self.walking_left[0],(self.x-camera.x,self.y-camera.y))
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
	def draw(self,win,pygame,camera,hero):
	
		shadown = (104, 104, 104,20)
		self.font.update(self.x+self.width*self.sizing-camera.x,self.y+self.sizing*10-camera.y)
		self.font.text(self.name,win)
		self.state +=1
		surface = pygame.Surface((50*self.sizing, 25*self.sizing), pygame.SRCALPHA, 32)
		pygame.draw.ellipse(
		    surface, 
		    (0, 0, 0, 50), 
		    [0,0,50*self.sizing,15*self.sizing])

		win.blit(surface, ((self.x)-camera.x, (self.y+self.height*2.7*self.sizing)-camera.y))
		self.animate(win,camera)