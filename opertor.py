class Multii:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __mul__(self,other):
        x= self.x+other.x
        y= self.y+other.y
        return Multii(x,y)
    def __str__(self):
        return "({0},{1}".format(self.x,self.y)
    
    

    
    
mul1 =Multii(3,2)
mul2 =Multii(5,3)

print(mul1*mul2)

    
        
           
