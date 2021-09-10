import typing
import sympy as sym
from typing import List
from sympy import symbols,functions

class vector:

    def __init__(self, elements: List[symbols]):
        self.vec = elements
        self.dimension = len(elements)

    def add_vec(self,other)->List[symbols]:
        n_vec = []
        for x in range(0,self.dimension):
            n_vec.append(self.vec[x]+other.vec[x])
        return n_vec

    def scale_vec(self,scalar:symbols)->None:
        for element in self.vec:
            element *= scalar

    def magnitude(self)->symbols:
        sum = 0
        for x in self.vec:
            sum += x**2
        return sym.sqrt(sum)

    def dot_product(self, other)->symbols:
        dot_sum = 0
        for x in range(0,self.dimension):
            dot_sum += self.vec[x] * other.vec[x]
        return dot_sum

    def is_unit(self,other)->bool:
        if self.magnitude == 1:
            return True
        return False

    def cross(self, b):
        c = [self.vec[1] * b.vec[2] - self.vec[2] * b.vec[1],
        self.vec[2] * b.vec[0] - self.vec[0] * b.vec[2],
        self.vec[0] * b.vec[1] - self.vec[1] * b.vec[0]]

        return vector(c)

#a,b,c,d,e,f = symbols(a,b,c,d,e,f)