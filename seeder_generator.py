import pandas as pd
import numpy as np

df = pd.read_csv("membros.csv")

#print(df)

output = open("out", "w+")

seed = "Membro::create(['nome' => '{0}', 'diretoria' => '{1}', 'cargo' => '{2}', 'facebook' => '{3}', 'linkedin' => '{4}', 'email' => '{5}', 'telefone' => '{6}', 'foto' => '{7}']);"

for index, row in df.iterrows():
	nome = row['Nome']
	diretoria = row['Diretoria']
	cargo = row['Cargo']
	facebook = row['Facebook']
	linkedin = row['LinkedIn']

	if (facebook == 'Nulo'):
		facebook = ""

	if (linkedin == 'Nulo'):
		linkedin = ""

	email = row['Email']
	telefone = row['Telefone']
	#foto = row['Foto']
	foto = "criar coluna maneira luiz!!"

	output.write(seed.format(nome, diretoria, cargo, facebook, linkedin, email, telefone, foto).replace('nan', '')+"\n")
