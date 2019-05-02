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

class prop:
	def __init__(self,x,y,width,height,reduction,pygame,types=0,instance="default"):
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
			pass

	def collided_door(self,pygame,win,hero,camera,keys):
		if self.instance == "house":
			deltaT = hero.get_rect(pygame,camera)
			new_rect = pygame.Rect(self.placement_door)
			if new_rect.colliderect(deltaT):
				return True
			else: 
				return False
		else:
			return False