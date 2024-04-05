# nos caminhos de sys.path

import aaula97_m
from aaula97_m import soma, variavel_modulo

print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)
print(aaula97_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aaula97_m.soma(2, 3))