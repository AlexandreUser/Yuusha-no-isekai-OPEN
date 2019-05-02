def return_2x(url,times,pygame):
	img = pygame.image.load(url)
	size = img.get_size()
	bigger = pygame.transform.scale(img,(int(size[0]*times),int(size[1]*times)))
	return bigger
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

