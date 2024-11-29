// Removendo elementos
document.querySelector('p').remove();
document.querySelector('spam').remove();

const galeriaContainer = document.querySelector('#galeria');

// Criando titulo para galeria
galeriaContainer.insertAdjacentHTML(
	'beforebegin',
	'<h1 class="title">Galeria de Imagens</h1>'
);

for (let i = 0; i < 3; i++) {
	// Criando 3 divs para imagens
	const div = document.createElement('div');

	// Inserindo classe de card
	div.classList += 'card';

	// Inserindo parágrafos para cada uma das 3 imagens
	div.insertAdjacentHTML(
		'beforeend',
		`<p class="card-label">Imagem ${i + 1}</p>`
	);

	// Adicionando imagens às respectivas divs
	div.insertAdjacentHTML(
		'afterbegin',
		`<img class="card-image" src="./imagens/imagem-${i + 1}.jpg"></img>`
	);

	// Inserindo as divs na galeria
	galeriaContainer.insertAdjacentElement('beforeend', div);
}
