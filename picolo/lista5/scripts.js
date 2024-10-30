// Atualizando o título
titleH1 = document.querySelector('#titulo');
titleH1.textContent = 'Título Atualizado';

// Adicionando classe destaque aos paragrafos
paragraphs = document.getElementsByClassName('paragrafo');
for (const el of paragraphs) {
	el.classList.add('destaque');
}

// Deixando o primeiro parágrafo do container em negrito
firstContainerParagraph = document.querySelector('.container > p');
firstContainerParagraph.style.fontWeight = 600;

// Criando nova div com conteúdo textual
newDiv = document.createElement('div');
newDiv.textContent = 'Sou a nova div.';

// Inserindo nova div no elemento de id='conteudo'
contentElement = document.querySelector('#conteudo');
contentElement.appendChild(newDiv);

// Inserindo novo parágrafo na div já adicionada
const newParagraph = document.createElement('p');
newParagraph.textContent = 'Novo parágrafo';
newDiv.appendChild(newParagraph);

// Adicionando texto adicional ao botão de id='botao'
const button = document.querySelector('#botao');
button.textContent += ' legal!';
