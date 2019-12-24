from sympy import *
x,y,a,b=symbols('x y a b')
init_printing(use_unicode=True)
M = Matrix([[x, -2,  4, -2], [5,  3, -3, -2], [5, -2,  2, -2], [5, -2, -3,  3]])
M1 = Matrix([[x, a],[y,  b]])
print('Matrice M :')
pprint(M1,use_unicode=False)
print('Eigenvalue for M :')
pprint(M1.eigenvals())
print('Eigenvectors for M :')
pprint(M1.eigenvects())