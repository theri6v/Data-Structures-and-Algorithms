#add(A[0..m-1], B[0..n01])
#1) Create a sum array sum[] of size equal to maximum of 'm' and 'n'
#2) Copy A[] to sum[].
#3) Traverse array B[] and do following for every element B[i]
          #sum[i] = sum[i] + B[i]
#4) Return sum[].
#The following is the implementation of the above algorithm. 




 # Simple Python 3 program to add two
# polynomials
 
# A utility function to return maximum 
# of two integers
 
# A[] represents coefficients of first polynomial
# B[] represents coefficients of second polynomial
# m and n are sizes of A[] and B[] respectively
def add(A, B, m, n):
 
    size = max(m, n);
    sum = [0 for i in range(size)]
 
    # Initialize the product polynomial
     
    for i in range(0, m, 1):
        sum[i] = A[i]
 
    # Take ever term of first polynomial
    for i in range(n):
        sum[i] += B[i]
 
    return sum
 
# A utility function to print a polynomial
def printPoly(poly, n):
    for i in range(n):
        print(poly[i], end = "")
        if (i != 0):
            print("x^", i, end = "")
        if (i != n - 1):
            print(" + ", end = "")
 
# Driver Code
if __name__ == '__main__':
     
    # The following array represents
    # polynomial 5 + 10x^2 + 6x^3
    A = [5, 0, 10, 6]
 
    # The following array represents
    # polynomial 1 + 2x + 4x^2
    B = [1, 2, 4]
    m = len(A)
    n = len(B)
 
    print("First polynomial is")
    printPoly(A, m)
    print("\n", end = "")
    print("Second polynomial is")
    printPoly(B, n)
    print("\n", end = "")
    sum = add(A, B, m, n)
    size = max(m, n)
 
    print("sum polynomial is")
    printPoly(sum, size)


----------------------------------------------------------------------------------------------------------------------------------------------------------

'''Polynomial addition using Linked List'''

 # Program to add two polynomials represented
# in linkedlist using recursion
class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None
         
# Function to add polynomials
def add_polynomials(head1, head2):
    if not head1 and not head2:
        return
    elif head1.power == head2.power:
        print(f' {head1.coeff + head2.coeff}x^{head1.power}', end='')
        add_polynomials(head1.next, head2.next)
    elif head1.power > head2.power:
        print(f' {head1.coeff}x^{head1.power}', end='')
        add_polynomials(head1.next, head2)
    else:
        print(f' {head2.coeff}x^{head2.power}', end='')
        add_polynomials(head1, head2.next)
 
def insert(head, coeff, power):
    new_node = Node(coeff, power)
    while head.next:
        head = head.next
    head.next = new_node
 
def print_list(head):
    print('Linked List')
    while head:
        print(f' {head.coeff}x^{head.power}', end='')
        head = head.next
 
if __name__ == '__main__':
    head = Node(5, 2)
    insert(head, 4, 1)
    head2 = Node(6, 2)
    insert(head2, 4, 1)
    print_list(head)
    print()
    print_list(head2)
    print('\nAddition:')
    add_polynomials(head, head2)

----------------------------------------------------------------------------------------------------------------------------------------------------------


'''Implementation of a function that adds two polynomials represented as lists'''

Approach

This implementation takes two arguments p1 and p2, which are lists representing the coefficients of two polynomials. The function returns a new list representing the sum of the two input polynomials.

The function first checks the lengths of the two input lists and pads the shorter list with zeros so that both lists have the same length. We then use the zip function to create pairs of corresponding coefficients from the two input lists, and the sum function to add the pairs together. The resulting sum is appended to a new list, which is returned at the end.

 def add_polynomials(p1, p2):
    len1, len2 = len(p1), len(p2)
    if len1 < len2:
        p1 += [0] * (len2 - len1)
    else:
        p2 += [0] * (len1 - len2)
    return [sum(x) for x in zip(p1, p2)]
 
p1 = [2, 0, 4, 6, 8]
p2 = [0, 0, 1, 2]
print(add_polynomials(p1, p2))


