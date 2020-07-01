#CTI-110
#P3T1- Areas of Rectangles
#Eric Hudson
#29 June 2020
#
# Get the demensions of rectangle 1.
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

# Get the demensions of rectangle 2.
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

# Calculate the areas of rectangles.
area1 = length1* width1
area2 = length2* width2

# Determine which rectangle has the greater area.
if area1> area2:
	print('Rectangle 1 has the graeter area')
	
elif area2> area1:
		print('Rectangle 2 has the greater area')
		
else:
			print('Both rectangles are equal')
			

