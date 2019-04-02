#!/usr/bin/env python3

class Polynomial:
    """
    Class that represents polynom.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Polynom initialization with args kwargs and args[0]=List
        """  
        if args and isinstance(args[0], list): # if input is arg0-array: Polynomial([-5,1,0,-1,4,-2,0,1,3,0])
            self.polynom = args[0]    
        elif args: # if input is only args: Polynomial(0,1,0,-1,4,-2,0,1,3,0)
            self.polynom = args
        else:  # if input Polynomial(x2=0...)
            self.polynom = [kwargs.get(x, 0) for x in ['x' + str(i) for i in range(len(kwargs)+1)]]
    
    def __str__(self):
        """
        str method  definition:
        input: self
        output: string form of the polynom
        """
        PolList =  ['{:+d}'.format(self.polynom[i])+     #'+/-d'
                    ('x^' + str(i) if i > 1              #'+/-dx^i'
                    else 'x' if i==1                     #'+/-dx'
                    else '')                             #'+/-d'
                    for i in range(0, len(self.polynom)) if self.polynom[i] != 0] #if == 0 => "0"
        #PolList output format = ['+1x', '-1x^3', '+4x^4', '-2x^5', '+1x^7', '+3x^8'] needed reversed " +/- (z>1) x"
        if len(PolList) == 0:
             return "0"    
        return (''.join(PolList[::-1])[1:].replace('+', ' + ').replace('-', ' - ').replace('1x', 'x'))
    
    def __eq__(self, other):
        """
        == method  definition:
        input: two polynoms (self, other)
        output: True/False of all elemets
        """
        for i in range(0, len(self.polynom)):
            return self.polynom[i] == other.polynom[i]
        
    
    def __add__(self, other):
        """
        + method  definition:
        input: two polynoms (self, other)
        output: one polynom (elements additing)
        """
        PolList =  [0]*max(len(self.polynom), len(other.polynom))
        for i in range(len(self.polynom)):
            PolList[i] = self.polynom[i]
        for i in range(len(other.polynom)):
            PolList[i] = PolList[i] + other.polynom[i]   
        return Polynomial(PolList)
    
    def __pow__(self, power):
        """
        ** method  definition:
        input: one polynom (self) and pow step
        output: one polynom (self*self*...), num or error
        """
        if power < 0:
            raise ValueError("Power must be a non-negative integer.")
        elif power == 0:
            return Polynomial(1)
        elif power == 1:
            return self
        else:
            result = self
            for i in range(2, power + 1):
                result = result * self  
        return result
            
    def __mul__(self, other):
        """
        * method definition (additional for pow):
        input: two polynoms (self, other)
        output: one polynom (elements multiplied)
        """
        PolList = [0] * (len(self.polynom) + len(other.polynom) + 1)
        for i in range(0, len(self.polynom)):
            for j in range(0, len(other.polynom)):
                PolList[i + j] += self.polynom[i] * other.polynom[j]
        return Polynomial(PolList)
    
    def derivative(self):
        """
        derivative. method definition:
        input: one polynom (self)
        output: one polynom (derivated)
        """
        PolList = []
        for i in range(1, len(self.polynom)):
            PolList.append(self.polynom[i] * i)  #2X^2 => 4X, 2X => 2, 2 => 0 
        return Polynomial(PolList)
    
    def at_value(self, x, y=None):
        """
        at_value. method definition:
        input: one polynom, X, Y (optional)
        output: numerical result at value X or Y-X
        """
        result=0
        if not y:
            for i in range(0, len(self.polynom)):
                result=result+self.polynom[i]*(x**i)
            return result
        for i in range(0, len(self.polynom)):
            result=result-self.polynom[i]*(x**i)+self.polynom[i]*(y**i)
        return result

def test():
    assert str(Polynomial(0,1,0,-1,4,-2,0,1,3,0)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial([-5,1,0,-1,4,-2,0,1,3,0])) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x - 5"
    assert str(Polynomial(x7=1, x4=4, x8=3, x9=0, x0=0, x5=-2, x3= -1, x1=1)) == "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
    assert str(Polynomial(x2=0)) == "0"
    assert str(Polynomial(x0=0)) == "0"
    assert Polynomial(x0=2, x1=0, x3=0, x2=3) == Polynomial(2,0,3)
    assert Polynomial(x2=0) == Polynomial(x0=0)
    assert str(Polynomial(x0=1)+Polynomial(x1=1)) == "x + 1"
    assert str(Polynomial([-1,1,1,0])+Polynomial(1,-1,1)) == "2x^2"
    pol1 = Polynomial(x2=3, x0=1)
    pol2 = Polynomial(x1=1, x3=0)
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(pol1+pol2) == "3x^2 + x + 1"
    assert str(Polynomial(x0=-1,x1=1)**1) == "x - 1"
    assert str(Polynomial(x0=-1,x1=1)**2) == "x^2 - 2x + 1"
    pol3 = Polynomial(x0=-1,x1=1)
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(pol3**4) == "x^4 - 4x^3 + 6x^2 - 4x + 1"
    assert str(Polynomial(x0=2).derivative()) == "0"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative()) == "6x^2 + 3"
    assert str(Polynomial(x3=2,x1=3,x0=2).derivative().derivative()) == "12x"
    pol4 = Polynomial(x3=2,x1=3,x0=2)
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert str(pol4.derivative()) == "6x^2 + 3"
    assert Polynomial(-2,3,4,-5).at_value(0) == -2
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3) == 20
    assert Polynomial(x2=3, x0=-1, x1=-2).at_value(3,5) == 44
    pol5 = Polynomial([1,0,-2])
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-2.4) == -10.52
    assert pol5.at_value(-1,3.6) == -23.92
    assert pol5.at_value(-1,3.6) == -23.92

if __name__ == '__main__':
    test()
