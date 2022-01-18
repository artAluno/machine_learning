porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [0,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,0,1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
 
marcacao = [1,1,1,-1,-1,-1]

#Agora vamos inserir mais animais misteriosos e tentar realizar as novas predições baseados
#nas experiências passadas

'''misterioso1 = [1,1,1]
misterioso2 = [0,0,1]
misterioso3 = [1,0,1]
misterioso4 = [1,1,0]
misterioso5 = [0,0,0]
misterioso6 = [0,0,1]

base_teste = [misterioso1,misterioso2,misterioso3,misterioso4,misterioso5,misterioso6]'''
misterioso1=[1,1,1]
misterioso2=[1,0,0]
misterioso3=[0,0,1]

teste = [misterioso1, misterioso2, misterioso3]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

modelo.fit(dados, marcacao)
resultado = modelo.predict(teste)
print(resultado)

#Resultado: [-1 -1 -1  1 -1 -1]


# A partir de agora, vamos nos preocupar com os erros de classificação
# Resultados que sejam falsos positivos ou falsos negativos

# é necessário saber a taxa de erro e qual é a taxa aceitável em nosso algoritmo

# verificar se a taxa de erro é boa e qual a margem de erro, além de verificar se a margem de erro está 
# melhorando ou não, erros são aceitáveis?

# as métricas envolvendo o calculo de erros são importantes para fornecer feedbacks
# de quanto foi nossa taxa de erro?
# a taxa melhora ou piora com o passar do tempo?
# a taxa de erro é aceitável?
# como calcular a taxa de erros?


# iniciamos criando nossos cenários de teste
# [é gordinho?, tem perninha curta?, faz auauau?]



# qual o cenário esperado?
marcacao_teste = [-1,1,1]

# após esses passos, rodar novamente nosso algoritmo e comparar com o esperado (marcacoes_teste)

# Neste exemplo é tranquilo, porém em uma bas de dados gigante é impossível verificar a olho nu.
# é preciso então comparar o resultado esperado com o resultado obtido

#podemos subrair os vetores
#print(resultado-marcacao_teste)

# se a diferença for igual a 0, 100% de acerto
# se a diferença for diferente de 0, podemos calcular a taxa de erros

diferencas = resultado-marcacao_teste

# diferencas eh um vetor

#acertos = for d in diferencas if d == 0
acertos = [d for d in diferencas if d == 0]

print(acertos)

total_acertos = len(acertos)
total_elementos = len(teste)

taxa_acerto = 100 * total_acertos/total_elementos

print(resultado)
print(diferencas)
print(taxa_acerto)


















