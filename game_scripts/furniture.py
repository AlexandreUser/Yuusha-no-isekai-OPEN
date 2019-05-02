def return_2x(url,times,pygame):
	img = pygame.image.load(url)
	size = img.get_size()
	bigger = pygame.transform.scale(img,(int(size[0]*times),int(size[1]*times)))
	return bigger
class furniture:
	def __init__(self,x,reduce_x,y,reduce_y,width,height,name,pygame):
		self.x = x
		self.y = y
		self.reduce_x = reduce_x
		self.reduce_y = reduce_y
		self.width = width
		self.height = height
		self.name = name+".png"
		self.size = 3
		self.image = return_2x("./furniture/"+self.name,self.size,pygame)
	def render(self,camera,win,pygame):
		if self.name == "mesa_1.png":
			self.img_size = self.image.get_size()
			self.hitbox = (self.x+35*2 , self.y+35*2, self.img_size[0]-70*2, self.img_size[1]-35*2)
			pygame.draw.rect(win,  (48, 29, 19, 50), self.hitbox)
			self.hitbox = (self.x+40 , self.y+35, self.img_size[0]-100, self.img_size[1]-35)
		
		win.blit(self.image,(self.x,self.y))