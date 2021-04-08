"""
EM PYTHON TUDO É UM OBJETO: Incluindo classes 
Metaclasses são as "classes" que criam classes.
type é uma metaclasse (!!!???)
"""


A = type(
    'A',
    (),
    {
        'attr': 'Olá Mundo!'
    }
)

a = A()
print(a.attr)
print(type(a))