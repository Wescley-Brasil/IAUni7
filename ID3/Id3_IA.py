from copy import deepcopy


class ArvoreInducao:




    arvore_inducao = []
    id_no= 1
    id_pai= 0





    def selecao_propriedade(self,PR):
        return PR.pop(0)


    def busca_particao(self,CE,propriedade):
        nova_particao =[]
        nova_particao.append(CE[0])
        for registro in CE:
            if registro.__contains__(propriedade):
                nova_particao.append(registro)
        return nova_particao

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




    def induzir_arvore(self,CE,PR):
        if len(self.coluna_propriedade_classe(CE)) == 1:
            classe =[]
            classe.append((self.id_no,self.id_pai,CE[1][1]))
            return classe
        elif not PR:
            classe = []
            valoresClasse = self.coluna_propriedade_classe(CE)
            classes = ""
            for indice in range(0,len(valoresClasse)):
                classes += valoresClasse.pop()
                if len(valoresClasse)== 0:
                   break
                else:
                    classes += " ou "
            classe.append((self.id_no,self.id_pai,classes))
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

    def result(self):
        print(self.arvore_inducao)


CE =[]

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
CE.append((15, 'MODERADO',  'RUIM',                     'ALTA',     'NENHUMA',      '15 A 35MIL'))
CE.append((16, 'BAIXO',     'RUIM',                     'ALTA',     'NENHUMA',      '15 A 35MIL'))
CE.append((17, 'BAIXO',     'RUIM',                     'ALTA',     'NENHUMA',      '15 A 35MIL'))

PR = []
for atributo in CE[0][2:]:
    PR.append(atributo)


inducao = ArvoreInducao()
inducao.induzir_arvore(CE,PR)
inducao.result()





