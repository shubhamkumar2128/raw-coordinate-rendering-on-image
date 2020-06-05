import glob
import cv2
import os
import random

class Coord:

	img = []
	coordlist=[]
	imagelist=[]
	count=0

	def readCoord(self):
		f = open("coord.txt", "r")
		for x in f:
		    if "*" in x:
			try:
				self.draw(self.imagelist[self.count],self.coordlist)
				self.count+=1
				self.coordlist=[]
			except Exception as ex:
				print("No more images.")
		    else:
			self.coordlist.append(x.split())

	def draw(self,image,coord):
		color = (255, 0, 0) 
		path = 'output/'
		for i in range(len(coord)):
			x1=int(coord[i][0])
			y1=int(coord[i][1])
			x2=int(coord[i][2])
			y2=int(coord[i][3])
			self.out = cv2.rectangle(image, (x1,y1), (x2,y2), color, 2)
			cv2.imshow("Image", self.out)
			cv2.waitKey(300)
			print(x1,y1,x2,y2)
		status = cv2.imwrite(os.path.join(path , str(random.randint(1,22))+".jpg"),self.out)
		print(status)	
	
	def imageRead(self):
		for img in glob.glob("images/*.jpg"):
		  self.imagelist.append(cv2.imread(img))
		
   		 
o=Coord()
o.imageRead()
o.readCoord()
