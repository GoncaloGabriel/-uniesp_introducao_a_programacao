# Use um dicionário para armazenar os números favoritos de algumas pessoas.
# Escolha cinco colegas, e pergunte quais seus números favoritos.
# Use seus nomes para serem as chaves de cada número favorito. 
# Ao final, exiba o nome de cada pessoa e seu número favorito.

nprefer = {"João": 15, "José": 16, "José": 19, "Thiago": 27, "Renata": 30}

for t,g in nprefer.items():
    print(f'O número preferido de {t} é {g}.')
