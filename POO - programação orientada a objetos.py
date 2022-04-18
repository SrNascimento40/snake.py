#Classe = grupo com características em comum - ex cachorro
#atributos de uma classe = características em comum  - todo cachorro tem fucinho e rabo
#metodo da classe = o que ela faz - todo cachorro late
#objetos = criado com base no molde da classe - cada cão é um objeto da classe cachorro

class Cachorros:
    def __init__(self, nome, cor_de_pelo, idade, tamanho):
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho
    def latir(self):
        print('Au au')
    def correr(self):
        print(f'{self.nome} está correndo')

cachorro_1 = Cachorros('Toby', 'Branco', 17, 'Colosssal')

print(cachorro_1.nome)
cachorro_1.correr()

cachorro_2 = Cachorros('Max', 'preto', 3, 'Pequeno')
print(cachorro_2.tamanho)
