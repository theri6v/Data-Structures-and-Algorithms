Formula : 
Perimeter of cylinder ( P ) = ( 2 * d ) + ( 2 * h )   
here d is the diameter of the cylinder 
h is the height of the cylinder
Examples : 
 

Input : diameter = 5, height = 10 
Output : Perimeter = 30

Input : diameter = 50, height = 150 
Output : Perimeter = 400



'''Function to calculate the perimeter of a cylinder'''

def perimeter( diameter, height ) : 
	return 2 * ( diameter + height ) 

# Driver function 
diameter = 5 ; 
height = 10 ; 
print ("Perimeter = ", 
			perimeter(diameter, height)) 


