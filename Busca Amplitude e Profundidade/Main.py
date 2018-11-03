from Arvore import Arvore

if __name__ == '__main__':


    #Segue alguns modelos de exemplos com bastantes Nós

    inicioProfundidade = [

        [1, 2, 3],
        [0, 4, 8],
        [7, 6, 5],
    ]

    fimProfundidade = [

        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]
    ]

    inicioAmplitude = [

        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8],
    ]

    fimAmplitude = [

        [2, 7, 3],
        [1, 0, 5],
        [4, 6, 8]
    ]

    tree = Arvore()
    print(tree.buscaProfundidade(fimProfundidade, inicioProfundidade))
    print('\n\n\n---------------------------------------------------------')
    print(tree.buscaAmplitude(fimProfundidade, inicioProfundidade))