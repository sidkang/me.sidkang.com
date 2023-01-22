# %%
from plantuml import PlantUML
from IPython.display import Image

uml = """@startuml
skinparam defaultTextAlignment center
participant Consumer as con
participant Corp as corp
group Period 1
 [-> con: <latex>L, k_0</latex>
 con -> corp: <math>L,k_0</math>
 corp -> con: <math>w_1L,(1+r_1)k_0</math>
 [<- con: <math>c_1</math>
end
group Period 2
[-> con: <math>L, k_1</math>
con -> corp: <math>L,k_1</math>
corp -> con: <math>w_2L,(1+r_2)k_1</math>
[<- con: <math>c_2</math>
end
@enduml"""

puml = PlantUML('http://www.plantuml.com/plantuml/png/')
Image(url=puml.get_url(uml))
# %%
from scipy import optimize

def func(x):
    return [x[0] + x[2] - 2,
            x[1] - x[2] - x[2]**0.5,
            (x[1]/x[0])**2 - 0.98 * (0.5 * x[2]**0.5 + 1)]
solve = optimize.root(func, [0.1, 0.1, 0.1], method='df-sane')
print(solve.x)
print(0.5 * solve.x[2] ** -0.5)
# %%

from scipy import optimize

def func(x):
    return [x[0] + x[2] - 2,
            x[1] - x[2] - x[2]**0.4,
            (x[1]/x[0])**2 - 0.98 * (0.4 * x[2]**0.6 + 1)]
solve = optimize.root(func, [0.1, 0.1, 0.1], method='hybr')
print(solve.x)
print(0.4 * solve.x[2] ** -0.6)

# %%

from scipy import optimize

def func(x):
    return [(((x[0]**0.4 + x[0])/(2-x[0]))**2 - 0.98 * (0.4 * x[0]**0.6 + 1))**2]
solve = optimize.root(func, [0.1], method='hybr')
print(solve.x)
# print(0.4 * solve.x[2] ** -0.6)
# %%

from scipy.optimize import root

def func(x):
    return (( (x**0.5 + x)/(x-2) )**2 - 0.98 * (0.5 * (x**-0.5) + 1))**2

sol = root(func, 1)
k = sol.x
c1 = 2 - k
c2 = k**0.4 + k

# %%

from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
solve( ((x**0.5+x)/(2-x))**2 - 0.98 * (x**-0.5*0.5 + 1), x)
# %%
