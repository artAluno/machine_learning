#Passo1: tabela inicial de classificacao
# vetor [é gordinho? ; tem perna curta? ; faz auauau?]
porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [0,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,0,1]

#Passo2: agrupando os dados
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
 
#Passo3: Marcação para indicar o que cada um dos elementos da lista dados é:
# considere que porco -> 1 e cachorr -> -1
marcacao = [1,1,1,-1,-1,-1]

#Passo4: Elemento misterioso. Qual será a classificação dele?
misterioso = [1,1,1]

#Passo5: Será que esse elemento misterioso é um porco (1) ou um cachorro (0)?
# Para responder a essa pergunta, temos que usar um algoritmo de classificação, 
# baseado nos dados (tabela de classificação) que classifique o misterioso
# a partir de sua experiência anterior.

# Multinomial é o algoritmo que usaremos para treinar nosso modelo

from sklearn.naive_bayes import MultinomialNB

#criação de um modelo para treinar os dados e marcações
modelo = MultinomialNB()

#necessitamos de algo para treinar o modelo e associar dados a marcacoes no estilo
#modelo.treinar(dados,marcacao). Para isso usamos o método fit
modelo.fit(dados, marcacao)

#após o treinamento, devemos prever (predict) se o misterioso é cachorro ou porco.
print(modelo.predict([misterioso]))

#Resultado: Misterioso é um cachorro.
