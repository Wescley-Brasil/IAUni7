from copy import deepcopy
import matplotlib.pyplot as plt

class Perceptron():

    pesos = (0.75,0.5,-0.6)
    #pesos = [-1.6100000000000017, 0.25999999999999845, 6.200000000000001]
    vies = 1
    aprendizagem = 0.2
    erro = 0
    registro_validados =[]
    fim_perceptron = False
    conti = 0

    def soma_registros(self,registros):
        resultado = 0
        indice = 0
        for registro in registros[0:(len(registros)-1)]:
            resultado += registro * self.pesos[indice]
            indice+=1
        resultado += self.vies * self.pesos[indice]
        if resultado >= 0:
            resultado = 1
        else:
            resultado = -1
        return resultado

    def ativacao(self,resultado,classe):
        if resultado == classe:
            return True
        return False

    def calculo_erro(self,resultado,classe):
        self.erro = classe - resultado

    def recalcular_pesos(self,registros):
        resultado = self.erro * self.aprendizagem
        registros.pop(2)
        registros.append(self.vies)
        resultado_mult_lista = [valor * resultado for valor in registros]
        novos_pesos =[]
        for indice in range(len(resultado_mult_lista)):
            novos_pesos.append(round(self.pesos[indice] + resultado_mult_lista[indice],4) )
        self.pesos = novos_pesos


    def gerar_perceptron(self,conjunto_registros):
        for contador in range(len(conjunto_registros)):
            self.registro_validados.append(True)
        while len(self.registro_validados) > 0:
            for registro in conjunto_registros:
                registro_classificado = False
                while registro_classificado is False:
                    self.conti +=1
                    resultado = self.soma_registros(registro)
                    if self.ativacao(resultado,registro[2]) is True:
                        self.registro_validados.pop(0)
                        registro_classificado = True
                    else:
                        self.calculo_erro(resultado,registro[2])
                        self.recalcular_pesos(deepcopy(registro))
                        self.registro_validados.clear()
                        return False
        print('Pesos: ',self.pesos)
        self.fim_perceptron = True

    def reiniciar_perceptron(self):
        self.pesos = (0.75,0.5,-0.6)
        self.vies = 1
        self.aprendizagem = 0.2
        self.erro = 0
        self.registro_validados = []
        self.fim_perceptron = False

    def induzir_novo_registro(self,registro):
        resultado = self.soma_registros(registro)
        print('Classificacao: ',resultado)


    def iniciar_perceptron(self,conjunto_registros):
        while self.fim_perceptron is False:
            self.gerar_perceptron(conjunto_registros)


if __name__ == '__main__':


    registros_treinamento = [
        ('Registro', 'Registro', 'Classe')
        , [1, 1, 1]
        , [9.4, 6.4, -1]
        , [2.5, 2.1, 1]
        , [8, 7.7, -1]
        , [0.5, 2.2, 1]
        , [7.9, 8.4, -1]
        , [7, 7, -1]
        , [2.8, 0.8, 1]
        , [1.2, 3, 1]
        , [7.8, 6.8, -1]
    ]


    per = Perceptron();
    per.iniciar_perceptron(registros_treinamento[1:])
    per.induzir_novo_registro([2,2,1])



