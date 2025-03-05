import pandas as pd
import matplotlib.pyplot as plt

# Description: Dicionário com informações sobre gatos
gatos = {
    'nomes': ['Tina', 'Bolinha', 'Garfield', 'Bella', 'Nina'],
    'cores': ['branco', 'preto', 'cinza', 'amarelo', 'marrom'],
    'fofura': [3, 4, 5, 6, 7],
}

# Description: Criando um DataFrame com as informações dos gatos
df = pd.DataFrame(gatos)

# Description: Adicionando dois novos gatos ao DataFrame
novo = ['Mia', 'branco', 4]
novo2 = ['Reinaldo', 'preto', 5]
df.loc[len(df)] = novo 
df.loc[len(df)] = novo2

# Description: Adicionando uma nova coluna ao DataFrame
sexo = ['femea', 'macho', 'macho', 'femea', 'femea', 'femea', 'macho']
df['sexo'] = sexo

#Mostrando o DataFrame no console
print(df)

# Description: Gráfico de barras com a quantidade de patas dos gatos
cores = {
    'Tina': 'pink',
    'Bolinha': 'black',
    'Garfield': 'yellow',
    'Bella': 'orange',
    'Nina': 'brown',
    'Mia': 'gray',
    'Reinaldo': 'black'
}
cor = [cores.get(name, 'gray') for name in df['nomes']]
print("Cores atribuídas:", cor)
plt.bar(df['nomes'], df['fofura'], color= cor)
plt.title('Fofura dos gatos')
plt.xlabel('Nome')
plt.ylabel('Fofura')
plt.show()

#Description: Gráfico de pizza com a quantidade de gatos por sexo
sexo = df['sexo'].value_counts() #conta a quantidade de gatos por sexo
plt.pie(sexo, labels=sexo.index, autopct='%1.1f%%', colors=['hotpink', 'blue'])
plt.title('Sexo dos gatos')
plt.show()


