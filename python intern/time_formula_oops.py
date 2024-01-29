class Time:
    def __init__(self,distance,speed):
        self.distance = distance
        self.speed = speed
    def measure(self):
        return self.distance/self.speed
    
distance = int(input("Enter the distance: "))
speed = int(input("Enter the speed: "))
obj1 = Time(distance,speed)
print("Time required to cover distance",distance,"km is",obj1.measure())