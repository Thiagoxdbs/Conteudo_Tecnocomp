import copy
from Aula_resolucao_160 import produtos

novos_produtos = [
    {**p, 'preco': round(p['preco']*1.1 , 2)}
    for p in copy.deepcopy(produtos)
]

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

print()
print(*produtos_ordenados_por_nome, sep='\n')

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

print()
print(*produtos_ordenados_por_preco, sep='\n')