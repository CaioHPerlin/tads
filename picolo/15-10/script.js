const container = document.querySelector('.elemento_div');
// container.textContent = '<p>exemplo</p>';

const div = document.createElement('div');
div.textContent = 'teste legal';
container.append(div);

const p = document.createElement('p');
p.textContent = 'Bom dia';
div.append(p);

console.log(div);
