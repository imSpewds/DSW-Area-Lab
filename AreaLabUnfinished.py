import math #math library has pre-written math functions 
import unittest 

def circleArea(radius): 
    """Return the area of a circle"""
    return math.pi * radius * radius

def rectArea(base, height):
    """Return the area of a rectangle"""
    return base * height

def trapArea(base1, base2, height):
    """Return the area of a trapezoid"""
    return height * (base1 + base2) / 2

def triArea(base,height):
    """Return the area of a triangle"""
    return base * height / 2
    
	
class MyTest(unittest.TestCase):
    def testCircleArea(self):
        self.assertEqual(circleArea(5), 25 * math.pi)
    def testRectArea(self):
        self.assertEqual(rectArea(5, 5), 25)
    def testTrapArea(self):
        self.assertEqual(trapArea(5, 5, 2), 10)
    def testTriArea(self):
        self.assertEqual(triArea(5, 10), 25)