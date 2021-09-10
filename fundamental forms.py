from Curves import curve
from vector import vector
import sympy as sym

u, v = sym.symbols("u v")
class fundamental_form:

    def __init__(self,sigma_uv: vector):

        self.functions = curve(sigma_uv)
        self.first_fundamental_form = 0
        self.second_fundamental_form = 0

    #need multivar derivative for o(u,v).

    def compute_first_fundamental_form(self):
        sigma_u = curve.multi_derivative(u)
        sigma_v = curve.compute_derivative(v)
        sigma_uv = vector(sigma_u).dot_product(vector(sigma_v))
