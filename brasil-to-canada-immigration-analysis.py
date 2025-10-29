import pandas as pd

df = pd.read_csv('/canadian_immegration_data.csv')
df

df.info()

df.columns = ['País', 'Continente', 'Região', 'NomeDesenvolvedor'] + list(map(str, range(1980, 2014))) + ['Total']
df.head()

df.set_index('País', inplace=True)

anos = list(map(str, range(1980, 2014)))

brasil = df.loc['Brazil', anos]

brasil_dict = {'ano': brasil.index.tolist(), 'imigrantes': brasil.values.tolist()}
dados_brasil = pd.DataFrame((brasil_dict))

dados_brasil

import matplotlib.pyplot as plt

df_comparacao = df.loc[['Brazil', 'Argentina'], anos]

plt.plot(df_comparacao['Brazil'],label = 'Brasil')
plt.plot(df_comparacao['Argentina'],label ='Argentina')
plt.title('Imigração do Brasil e Argentina para o Canadá')
plt.xlabel('Ano')
plt.ylabel('Número de imigrantes')
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
plt.legend()
plt.show()
