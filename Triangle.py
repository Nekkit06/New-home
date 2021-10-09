class TriangleChecker:  
    def __init__(self, a, b, c):  
        self.a, self.b, self.c = a, b, c  
      
    def is_triangle(self):  
        if self.a <= 0 or self.b <= 0 or self.c <= 0:  
            print("What did you expect to get with negative numbers")  
        else:  
            sides = sorted((self.a, self.b, self.c), key = lambda x : -x)  
            print("Hurray, you can build a triangle (at last)!") if sides[0] < sides[1] + sides[2] else print("Sorry, but building a triangle is impossible") 

a=int(input("Check triangle number ")) 
tri1 = TriangleChecker(-1, 4, 5)  
tri2 = TriangleChecker(17, 2, 2) 
tri3 = TriangleChecker(2, 3, 4)   
if a==1: 
    tri1.is_triangle() 
  
elif a==2: 
    tri2.is_triangle() 
  
elif a==3: 
    tri3.is_triangle()
