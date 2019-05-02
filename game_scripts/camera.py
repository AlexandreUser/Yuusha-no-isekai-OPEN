
class camera:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def update(self,mov_x,mov_y):
		self.x = mov_x
		self.y = mov_y