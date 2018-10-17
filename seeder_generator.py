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

	if (facebook == 'Nulo' or (type(facebook) == type(1.1) and np.isnan(facebook))):
		facebook = ""

	facebook.replace("https://www.facebook.com/", "")
	facebook.replace("http://www.facebook.com/", "")

	if (linkedin == 'Nulo' or (type(linkedin) == type(1.1) and np.isnan(linkedin))):
		linkedin = ""

	linkedin.replace("https://www.linkedin.com/in/", "")
	linkedin.replace("http://www.linkedin.com/in/", "")

	email = row['Email']
	telefone = row['Telefone']
	foto = row['Foto']

	output.write(seed.format(nome, diretoria, cargo, facebook, linkedin, email, telefone, foto).replace('nan', '')+"\n")
