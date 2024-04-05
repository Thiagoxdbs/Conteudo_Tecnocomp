import importlib

import aaula98_m

print(aaula98_m.variavel)

for i in range(10):
    importlib.reload(aaula98_m)
    print(i)

print('Fim')