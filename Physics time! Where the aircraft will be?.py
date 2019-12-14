import math

class flight():
	time = 0
	def __init__(self,latitude,longitude,vh,vv,height,heading):
		#converting to radian
		heading = math.radians(heading)
		
		#position
		self.latitude = latitude
		self.longitude = longitude
		self.height=height

		#velocity
		self.vv = vv
		self.vx = vh*math.cos(heading)
		self.vy = vh*math.sin(heading)
	
	def calc(self,time):
		self.time = time
		self.height += self.vv*time
		self.latitude += self.vx*time
		self.longitude += self.vy*time
	
	def __str__(self):
		return (" the flight is at (" + str(self.latitude) + "," + str(self.longitude) + ") \n Height : " + str(self.height) + " meters ")

latitude = float(input("Enter latitude (m) :  "))
longitude = float(input("Enter longitude (m) :  "))
heading = float(input("Enter Heading (degrees) :  "))
vh = float(input("Enter horizontal speed (m/s) :  "))
vv = float(input("Enter vertical speed (m/s) :  "))
height = float(input("Enter height (m) :  "))
f = flight(latitude=latitude,longitude=longitude,height=height,vv=vv,vh=vh,heading=heading)
print("\n Currently" + str(f))
time = int(input("\n Now, Enter time delay (s) : "))
f.calc(time)
print("\n After time delay," +str(f))

