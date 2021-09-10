import vector
from vector import vector
import typing
from typing import List
import sympy as sym
u,v = sym.symbols("u,v")
class curve:

    def __init__(self, gamma_eq_vec: List
                 ):
        self.gamma_equations = gamma_eq_vec
        #define
        self.gamma_equations_symbols = self.find_symbols()
        # might need to make a function for it
        self.domain_symbols = self.find_dim_domain()
        self.dim_domain = len(self.domain_symbols)
        self.dim_codomain = len(gamma_eq_vec)
        self.d_one_gamma_equations = self.compute_derivative()
        self.d_two_gamma_equations = self.compute_second_derivative()
        self.sigma_u = self.compute_partial_vectors(u,self.gamma_equations)
        self.sigma_v = self.compute_partial_vectors(v,self.gamma_equations)
        self.sigma_uu = self.compute_partial_vectors(u,self.sigma_u.vec)
        self.sigma_vv = self.compute_partial_vectors(v,self.sigma_v.vec)
        #below is equivalent to sigma_vu
        self.sigma_uv = self.compute_partial_vectors(v,self.sigma_u.vec)
        self.sigma_vu = self.sigma_uv
        self.uv_norma = self.sigma_u.cross(self.sigma_v)
        self.first_fundamental_form_coefficients = self.fff_symbols()
        self.second_fundamental_form_coefficients = self.sff_symbols()



        #self.fff_coeff = self.fff_symbols()


    def find_symbols(self) -> int:
        free_sym = []
        for eq in self.gamma_equations:
            eq_sym = eq.free_symbols
            free_sym.append(eq_sym)
        return free_sym

    def find_dim_domain(self)->int:
        free_sym = []
        for eq in self.gamma_equations:
            eq_sym = eq.free_symbols
            for element in eq_sym:
                if element not in free_sym:
                    free_sym.append(element)
        return free_sym

    #kind of correct but not completely. Only for one variable atm.
    def compute_derivative(self):
        dg_eq = []
        for index,eq in enumerate(self.gamma_equations):
            dg_eq.append(sym.diff(eq,self.domain_symbols[0]))
        return dg_eq

    def compute_second_derivative(self):
        second_dg_eq = []
        for index, eq in enumerate(self.d_one_gamma_equations):
            second_dg_eq.append(sym.diff(eq, self.domain_symbols[0]))
        return second_dg_eq

    def multi_derivative(self,variable: sym.symbols):
        dg_eq = []
        for index, eq in enumerate(self.gamma_equations):
            dg_eq.append(sym.diff(eq, variable))
        return dg_eq
    '''
    work on 
    def is_regular(self):
        t_vals = []
        for eq in self.d_one_gamma_equations:
            t_vals.append(sym.solve(eq,self.domain_symbols[0]))
        return t_vals
    '''
    def eq_eval(self,eq,eq_val):
        eq1 = eq.subs(eq_val)
        return eq1

    def compute_curvature_kappa(self,t_val=None):
        mod_1 = self.eq_eval()
        numerator = vector.vector(self.d_one_gamma_equations).cross(vector.vector(self.d_two_gamma_equations))
        denominator = vector.vector(self.d_one_gamma_equations).magnitude()
        return numerator/denominator

    def compute_partial_vectors(self,var: sym.symbols, equations):
        sigma_var = []
        for eq in equations:
            sigma_var.append(sym.diff(eq, var))
        return vector(sigma_var)


    def fff_symbols(self):
        fff_E = self.sigma_u.dot_product(self.sigma_u)
        fff_F = self.sigma_u.dot_product(self.sigma_v)
        fff_G = self.sigma_v.dot_product(self.sigma_v)
        return [fff_E,fff_F,fff_G]

    def sff_symbols(self):
        normal_uv = self.sigma_u.cross(self.sigma_v)
        normal_uv.scale_vec(normal_uv.magnitude())
        sff_L = self.sigma_uu.dot_product(normal_uv)
        sff_M = self.sigma_uv.dot_product(normal_uv)
        sff_N = self.sigma_vv.dot_product(normal_uv)
        return [sff_L,sff_M,sff_N]

    #Need to figure out how to make eq
    def print_fff(self):
        print("(" + str(self.first_fundamental_form_coefficients[0]) + ")dudu  +  ("+ str(self.first_fundamental_form_coefficients[1]) + ")dudv  +  (" + str(self.first_fundamental_form_coefficients[2]) + ")dvdv" )

    def print_sff(self):
        print("(" + str(self.second_fundamental_form_coefficients[0]) + ")dudu  +  ("+ str(self.second_fundamental_form_coefficients[1]) + ")dudv  +  (" + str(self.second_fundamental_form_coefficients[2]) + ")dvdv" )
'''
    def first_fundamental_form(self):
        mag_E = vector(self.gamma_equations)
    '''
"""
COMPUTING ARC-LENGTH
COMPUTING GRADIENT 
COMPUTING TORSION
COMPUTING DERIVATIVE MATRIX 

"""

"""
BOOL :
        (1) Regular 
        (2) unit speed 
        
t = sym.symbols("t")

f = [sym.exp(t),t,sym.exp(-t)]
a = curve(f)
print(a.gamma_equations)
print(a.d_one_gamma_equations)
print(a.d_two_gamma_equations)
#a = vector.vector(a.gamma_equations).magnitude()
"""


f = [u,v,u*v]
a = curve(f)
print(a.fff_symbols())
print(a.sff_symbols())
a.print_fff()
a.print_sff()
