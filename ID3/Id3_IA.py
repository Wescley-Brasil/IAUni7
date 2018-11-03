from copy import deepcopy
from graphviz import Digraph
import os

class ArvoreInducao:
    #Comentar as 2 linhas abaixo caso não possua a biblioteca Graphivz
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
    grafico = Digraph(comment='Arvore inducao')

    #Variavel que armazenar os Nos da Arvore
    arvore_inducao = []
    #Variaveis usadas para mapear Pai e Filhos
    id_no= 1
    id_pai= 0


    def induzir(self,CE):
        PR = []
        for atributo in CE[0][2:]:
            PR.append(atributo)
        self.induzir_arvore(CE,PR)


    #Funcao que retornar a propriedade e remove da lista
    def selecao_propriedade(self,PR):
        return PR.pop(0)


    # Funcao usada para dividir a particao CE em uma nova Particao de acordo com a Propriedade passada
    def busca_particao(self,CE,propriedade):
        nova_particao =[]
        nova_particao.append(CE[0])
        for registro in CE:
            if registro.__contains__(propriedade):
                nova_particao.append(registro)
        return nova_particao


    #Funcao usada para retornar as Classes de forma Unica
    def coluna_propriedade(self,CE,Propriedade):
        coluna =0
        set_registros = set()
        for indice in range(len(CE[0])):
            if CE[0][indice] == Propriedade:
                coluna = indice
                indice = len(CE[0])
        for registro in CE:
            set_registros.add((registro[coluna]))
        set_registros.remove(Propriedade)
        return set_registros


    #Funcao usada para retornar as Classes de formar unica, usada na primeira comparacao da chamada de inducao
    def coluna_propriedade_classe(self,CE):
        coluna =0
        set_registros = set()
        for indice in range(len(CE[0])):
            if CE[0][indice] == 'RISCO':
                coluna = indice
                indice = len(CE[0])
        for registro in CE:
            set_registros.add((registro[coluna]))
        set_registros.remove('RISCO')
        return set_registros


    #funcao que contem as chamadas a arvore
    def induzir_arvore(self,CE,PR):
        if len(self.coluna_propriedade_classe(CE)) == 1:
            classe = (self.id_no,self.id_pai,CE[1][1])
            return classe
        elif not PR:
            valoresClasse = self.coluna_propriedade_classe(CE)
            classes = ""
            for indice in range(0,len(valoresClasse)):
                classes += valoresClasse.pop()
                if len(valoresClasse)== 0:
                   break
                else:
                    classes += " ou "
            classe=(self.id_no,self.id_pai,classes)
            return classe
        else:
            propriedade_atual = self.selecao_propriedade(PR)
            valores_propriedade = self.coluna_propriedade(deepcopy( CE ), propriedade_atual)
            self.arvore_inducao.append((self.id_no,self.id_pai,propriedade_atual))
            id_pr = self.id_no
            self.id_pai = self.id_no
            self.id_no += 1
            ramo_valor = []
            for propriedade in valores_propriedade:
                self.arvore_inducao.append((self.id_no,id_pr,propriedade))
                self.id_pai = self.id_no
                self.id_no += 1
                ce_propriedade = []
                ce_propriedade = self.busca_particao(CE,propriedade)
                classe =self.induzir_arvore(deepcopy(ce_propriedade),deepcopy(PR))
                if classe != None:
                    self.id_no += 1
                    self.arvore_inducao.append(classe)


    #funcao que gera a arvore em formato de gráfico
    #Caso não tenha a biblioteca Graphviz instalada essa funcao deve ser comentada pois retornara erro
    def result(self):
        for registro in self.arvore_inducao:
            self.grafico.node(str(registro[0]), str(registro[2]))
        for no in self.arvore_inducao:
            if no[1] != 0:
                pai = self.buscaPai(no)
                self.grafico.edge(str(pai), str(no[0]))
        self.grafico.render(filename="Arvore Inducao")


    #funcao que complementa a funcao que gera o grafico da arvore de inducao
    #Caso não tenha a biblioteca Graphviz instalada essa funcao deve ser comentada pois retornara erro
    def buscaPai(self,noFilho):
        for noPai in self.arvore_inducao:
            if noPai[0] == noFilho[1]:
                return noPai[0]
    
    
    def impressaoResultado(self):
        print(self.arvore_inducao)


        

if __name__ == '__main__':

    #Conjunto Exemplo
    CE =[]

    #Registros
    CE.append((0,  'RISCO',     'HISTORICO DE CREDITO',     'DIVIDA',   'GARANTIA',     'RENDA'))
    CE.append((1,  'ALTO',      'RUIM',                     'ALTA',     'NENHUMA',      '0 A 15MIL'))
    CE.append((2,  'ALTO',      'DESCONHECIDA',             'ALTA',     'NENHUMA',      '15 A 35MIL'))
    CE.append((3,  'MODERADO',  'DESCONHECIDA',             'BAIXA',    'NENHUMA',      '15 A 35MIL'))
    CE.append((4,  'ALTO',      'DESCONHECIDA',             'BAIXA',    'NENHUMA',      '0 A 15MIL'))
    CE.append((5,  'BAIXO',     'DESCONHECIDA',             'BAIXA',    'NENHUMA',      'ACIMA 35MIL'))
    CE.append((6,  'BAIXO',     'DESCONHECIDA',             'BAIXA',    'ADEQUADA',     'ACIMA 35MIL'))
    CE.append((7,  'ALTO',      'RUIM',                     'BAIXA',    'NENHUMA',      '0 A 15MIL'))
    CE.append((8,  'MODERADO',  'RUIM',                     'BAIXA',    'ADEQUADA',     'ACIMA 35MIL'))
    CE.append((9,  'BAIXO',     'BOA',                      'BAIXA',    'NENHUMA',      'ACIMA 35MIL'))
    CE.append((10, 'BAIXO',     'BOA',                      'ALTA',     'ADEQUADA',     'ACIMA 35MIL'))
    CE.append((11, 'ALTO',      'BOA',                      'ALTA',     'NENHUMA',      '0 A 15MIL'))
    CE.append((12, 'MODERADO',  'BOA',                      'ALTA',     'NENHUMA',      '15 A 35MIL'))
    CE.append((13, 'BAIXO',     'BOA',                      'ALTA',     'NENHUMA',      'ACIMA 35MIL'))
    CE.append((14, 'ALTO',      'RUIM',                     'ALTA',     'NENHUMA',      '15 A 35MIL'))


# Chamadas as funcoes

    inducao = ArvoreInducao()
    inducao.induzir(CE)
    #Caso não tenha a biblioteca grafica comentar a linha abaixo
    inducao.result()
    inducao.impressaoResultado()


