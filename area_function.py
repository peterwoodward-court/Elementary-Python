#For a given radius (r), calculates the volume of a sphere
import math

def sphere_volume(r):
	"""Returns sphere volume"""
	v = (4.0/3.0) * math.pi * r**3
	return v

user_radius = int(input("Enter sphere radius: "))
result = sphere_volume(user_radius)

print(result)
