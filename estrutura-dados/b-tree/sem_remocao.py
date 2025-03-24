class NoB:
    """
    Classe que representa um nó da Árvore B.
    Cada nó pode conter um número máximo de chaves e filhos baseado na ordem da árvore.
    """
    def __init__(self, ordem):
        self.ordem = ordem 
        self.chaves = []  
        self.filhos = []  
        self.folha = True 

class ArvoreB:
    """
    Classe que representa a Árvore B e implementa as operações principais.
    """
    def __init__(self, ordem):
        self.raiz = NoB(ordem)  # Inicializa a árvore com um nó raiz vazio
        self.ordem = ordem
        
    
    def inserir(self, chave):
        """
        Insere uma chave na árvore B, garantindo que a estrutura permaneça balanceada.
        """
        raiz = self.raiz
        # Se a raiz está cheia, cria uma nova raiz e divide a antiga
        if len(raiz.chaves) == self.ordem - 1:  
            nova_raiz = NoB(self.ordem) 
            nova_raiz.filhos.append(self.raiz)  # A antiga raiz se torna filha
            nova_raiz.folha = False
            self.dividir_filho(nova_raiz, 0, raiz)  # Divide a raiz
            self.raiz = nova_raiz  # Atualiza a raiz
        self._inserir_nao_cheio(self.raiz, chave)  # Insere a chave na árvore
    
    def dividir_filho(self, pai, indice, filho):
        """
        Divide um nó cheio em dois, promovendo uma chave para o nó pai. (split)
        """
        nova_pagina = NoB(self.ordem)  # Cria um novo nó
        nova_pagina.folha = filho.folha 
        meio = (self.ordem - 1) // 2  # Determina o índice da chave que sobe para o pai

        # Move metade das chaves para a nova página
        nova_pagina.chaves = filho.chaves[meio + 1:]
        chave_subir = filho.chaves[meio]  
        filho.chaves = filho.chaves[:meio]  # Mantém apenas a parte esquerda no filho original
        
        if not filho.folha:
            nova_pagina.filhos = filho.filhos[meio + 1:] 
            filho.filhos = filho.filhos[:meio + 1]
        
        pai.filhos.insert(indice + 1, nova_pagina)  # Insere o novo nó no pai
        pai.chaves.insert(indice, chave_subir)  # Insere a chave promovida no pai
    
    def _inserir_nao_cheio(self, no, chave):
        """
        Insere uma chave em um nó que ainda não está cheio.
        """
        if no.folha:
            no.chaves.append(chave)  
            no.chaves.sort()  
        else:
            i = len(no.chaves) - 1  # Encontra a posição correta para a nova chave
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            i += 1
            # Se o nó filho estiver cheio, precisa ser dividido antes da inserção
            if len(no.filhos[i].chaves) == self.ordem - 1:
                self.dividir_filho(no, i, no.filhos[i]) 
                if chave > no.chaves[i]:  # Decide se a chave deve ser inserida no novo nó criado
                    i += 1
            self._inserir_nao_cheio(no.filhos[i], chave)  # Insere recursivamente no filho adequado
    
    def imprimir(self, no=None, nivel=0):
        """
        Imprime a árvore B de forma hierárquica para facilitar a visualização.
        """
        if no is None:
            no = self.raiz 
        print(f"{nivel}:", no.chaves)
        for filho in no.filhos: 
            self.imprimir(filho, nivel + 1)
    


# Execução
ordem = 4
arvore = ArvoreB(ordem)
chaves = [10, 15, 25, 30, 35, 40]
for chave in chaves:
    print(f"\nInserindo {chave}...")
    arvore.inserir(chave) 
    print(f"Estado da árvore:")
    arvore.imprimir()

