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
        self.ordem = ordem  # Define a ordem da árvore

    def inserir(self, chave):
        """
        Insere uma chave na árvore B, garantindo que a estrutura permaneça balanceada.
        """
        raiz = self.raiz
        # Se a raiz está cheia, cria uma nova raiz e divide a antiga
        if len(raiz.chaves) == self.ordem - 1:
            nova_raiz = NoB(self.ordem)  # Cria um novo nó raiz
            nova_raiz.filhos.append(self.raiz)  # A antiga raiz se torna filha
            nova_raiz.folha = False  # A nova raiz não é folha
            self.dividir_filho(nova_raiz, 0, raiz)  # Divide a raiz
            self.raiz = nova_raiz  # Atualiza a raiz
        self._inserir_nao_cheio(self.raiz, chave)  # Insere a chave na árvore

    def dividir_filho(self, pai, indice, filho):
        """
        Divide um nó cheio em dois, promovendo uma chave para o nó pai.
        """
        nova_pagina = NoB(self.ordem)  # Cria um novo nó
        nova_pagina.folha = filho.folha  # Copia se é folha ou não
        meio = (self.ordem - 1) // 2  # Determina o índice da chave que sobe para o pai

        # Move metade das chaves para a nova página
        nova_pagina.chaves = filho.chaves[meio + 1:]
        chave_subir = filho.chaves[meio]  # Chave que será promovida ao pai
        filho.chaves = filho.chaves[:meio]  # Mantém apenas a parte esquerda no filho original

        if not filho.folha:
            nova_pagina.filhos = filho.filhos[meio + 1:]  # Move os filhos correspondentes para a nova página
            filho.filhos = filho.filhos[:meio + 1]  # Mantém a parte esquerda dos filhos originais

        pai.filhos.insert(indice + 1, nova_pagina)  # Insere o novo nó no pai
        pai.chaves.insert(indice, chave_subir)  # Insere a chave promovida no pai

    def _inserir_nao_cheio(self, no, chave):
        """
        Insere uma chave em um nó que ainda não está cheio.
        """
        if no.folha:
            no.chaves.append(chave)  # Adiciona a chave na lista de chaves
            no.chaves.sort()  # Mantém as chaves ordenadas
        else:
            i = len(no.chaves) - 1  # Encontra a posição correta para a nova chave
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            i += 1
            # Se o nó filho estiver cheio, precisa ser dividido antes da inserção
            if len(no.filhos[i].chaves) == self.ordem - 1:
                self.dividir_filho(no, i, no.filhos[i])  # Divide o filho cheio
                if chave > no.chaves[i]:  # Decide se a chave deve ser inserida no novo nó criado
                    i += 1
            self._inserir_nao_cheio(no.filhos[i], chave)  # Insere recursivamente no filho adequado

    def remover(self, chave):
        """
        Remove uma chave da árvore B.
        """
        self._remover(self.raiz, chave)
        # Se a raiz ficar sem chaves após a remoção, atualiza a raiz
        if len(self.raiz.chaves) == 0 and not self.raiz.folha:
            self.raiz = self.raiz.filhos[0]

    def _remover(self, no, chave):
        """
        Função auxiliar para remover uma chave da subárvore enraizada no nó.
        """
        # Encontra a posição da chave (ou a primeira chave maior que ela)
        # Percorre as chaves até encontrar uma chave maior ou igual à chave que está sendo buscada.
        i = 0
        while i < len(no.chaves) and chave > no.chaves[i]:
            i += 1

        # Caso 1: A chave está no nó atual
        if i < len(no.chaves) and no.chaves[i] == chave:
            if no.folha:
                # Caso 1a: A chave está em um nó folha
                no.chaves.pop(i)  # Remove a chave
            else:
                # Caso 1b: A chave está em filho do nó atual
                self._remover_chave_interna(no, i)
        else:
            if no.folha:
                # A chave não está na árvore
                print(f"Chave {chave} não encontrada.")
                return

            # Caso 2: A chave está em um filho do nó atual
            filho = no.filhos[i]
            if len(filho.chaves) < self.ordem // 2:
                # Caso 2a: O filho tem menos chaves do que o mínimo necessário
                self._ajustar_filho(no, i)
                # Após o ajuste, o filho pode ter mudado, então recalculamos o índice
                if i > len(no.chaves):
                    i -= 1

            self._remover(no.filhos[i], chave)

    def _remover_chave_interna(self, no, indice):
        """
        Remove uma chave de um nó interno.
        """
        chave = no.chaves[indice]

        # Caso 1b1: O filho anterior tem pelo menos t chaves
        if len(no.filhos[indice].chaves) >= self.ordem // 2:
            predecessor = self._obter_predecessor(no, indice)
            no.chaves[indice] = predecessor
            self._remover(no.filhos[indice], predecessor)
        # Caso 1b2: O filho seguinte tem pelo menos t chaves
        elif len(no.filhos[indice + 1].chaves) >= self.ordem // 2:
            sucessor = self._obter_sucessor(no, indice)
            no.chaves[indice] = sucessor
            self._remover(no.filhos[indice + 1], sucessor)
        # Caso 1b3: Ambos os filhos têm t-1 chaves
        else:
            self._fundir_filhos(no, indice)
            self._remover(no.filhos[indice], chave)

    def _ajustar_filho(self, no, indice):
        """
        Ajusta um filho que tem menos chaves do que o mínimo necessário.
        """
        if indice > 0 and len(no.filhos[indice - 1].chaves) >= self.ordem // 2:
            # Caso 2a1: Pegar uma chave do irmão esquerdo
            self._pegar_do_irmao_esquerdo(no, indice)
        elif indice < len(no.filhos) - 1 and len(no.filhos[indice + 1].chaves) >= self.ordem // 2:
            # Caso 2a2: Pegar uma chave do irmão direito
            self._pegar_do_irmao_direito(no, indice)
        else:
            # Caso 2a3: Fundir com um irmão
            if indice > 0:
                self._fundir_filhos(no, indice - 1)
            else:
                self._fundir_filhos(no, indice)

    def _pegar_do_irmao_esquerdo(self, no, indice):
        """
        Move uma chave do irmão esquerdo para o nó atual.
        """
        filho = no.filhos[indice]
        irmao_esquerdo = no.filhos[indice - 1]

        # Move a chave do nó pai para o filho
        filho.chaves.insert(0, no.chaves[indice - 1])
        # Move a última chave do irmão esquerdo para o nó pai
        no.chaves[indice - 1] = irmao_esquerdo.chaves.pop()

        if not irmao_esquerdo.folha:
            # Move o último filho do irmão esquerdo para o filho
            filho.filhos.insert(0, irmao_esquerdo.filhos.pop())

    def _pegar_do_irmao_direito(self, no, indice):
        """
        Move uma chave do irmão direito para o nó atual.
        """
        filho = no.filhos[indice]
        irmao_direito = no.filhos[indice + 1]

        # Move a chave do nó pai para o filho
        filho.chaves.append(no.chaves[indice])
        # Move a primeira chave do irmão direito para o nó pai
        no.chaves[indice] = irmao_direito.chaves.pop(0)

        if not irmao_direito.folha:
            # Move o primeiro filho do irmão direito para o filho
            filho.filhos.append(irmao_direito.filhos.pop(0))

    def _fundir_filhos(self, no, indice):
        """
        Funde dois filhos do nó.
        """
        filho = no.filhos[indice]
        irmao = no.filhos[indice + 1]

        # Move a chave do nó pai para o filho
        filho.chaves.append(no.chaves.pop(indice))
        # Move as chaves do irmão para o filho
        filho.chaves.extend(irmao.chaves)
        # Move os filhos do irmão para o filho (se não forem folhas)
        if not irmao.folha:
            filho.filhos.extend(irmao.filhos)

        # Remove o irmão da lista de filhos
        no.filhos.pop(indice + 1)

    def _obter_predecessor(self, no, indice):
        """
        Obtém o predecessor de uma chave.
        """
        no = no.filhos[indice]
        while not no.folha:
            no = no.filhos[-1]
        return no.chaves[-1]

    def _obter_sucessor(self, no, indice):
        """
        Obtém o sucessor de uma chave.
        """
        no = no.filhos[indice + 1]
        while not no.folha:
            no = no.filhos[0]
        return no.chaves[0]

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

chaves_remover = [10, 25, 30]
for chave in chaves_remover:
    print(f"\nRemovendo {chave}...")
    arvore.remover(chave)
    print(f"Estado da árvore:")
    arvore.imprimir()