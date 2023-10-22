Problem – Find the vertex, focus and directrix of a parabola when the coefficients of its equation are given.
A set of points on a plain surface that forms a curve such that any point on that curve is equidistant from the focus is a parabola. 
Vertex of a parabola is the coordinate from which it takes the sharpest turn whereas a is the straight line used to generate the curve. 
 

The standard form of a parabola equation is y=ax^2+bx+c. 
Given the values of a, b and c; our task is to find the coordinates of vertex, focus and the equation of the directrix. 
Example – 
 
Input : 5 3 2
Output : Vertex:(-0.3, 1.55)
         Focus: (-0.3, 1.6)
         Directrix: y=-198
Consult the formula below for explanation.
 


This problem is a simple example of implementations of formulae. Given below are the required set of formulae which will help us tackle the problem. 
 

For a parabola in the form y=ax^2+bx+cVertex: (-b/2a, 4ac-b^2/4a)Focus: (-b/2a, 4ac-b^2+1/4a)Directrix: y=c-(b^2+1)4a

  #Function to calculate Vertex,Focus and Directrix
    
def parabola(a, b, c):

	print("Vertex: (" , (-b / (2 * a)),
		", ", (((4 * a * c) - (b * b)) 
			/ (4 * a)), ")", sep = "")
			
	print("Focus: (" , (-b / (2 * a)),
	", ", (((4 * a * c) - (b * b) + 1)
			/ (4 * a)), ")", sep = "")
				
	print("Directrix: y=", c - ((b * b)
				+ 1) * 4 * a, sep = "")

# Driver Function
a = 5
b = 3
c = 2
parabola(a, b, c)
