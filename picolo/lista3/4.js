const adicionarTarefa = (lista, tarefa) => {
	lista.push(tarefa);
	console.log(`Tarefa adicionada: ${tarefa}`);
};

const listarTarefas = (lista) => {
	for (let i = 0; i < lista.length; i++) {
		console.log(`${i + 1}: ${lista[i]}`);
	}
};

const removerTarefa = (lista, indice) => {
	if (indice > 0 && indice <= lista.length) {
		const tarefaRemovida = tarefas.splice(indice - 1, 1);
		console.log(`Tarefa removida: ${tarefaRemovida}`);
	} else {
		console.log('Índice inválido.');
	}
};

let tarefas = [];

adicionarTarefa(tarefas, 'Estudar JavaScript');
adicionarTarefa(tarefas, 'Fazer Exercícios');
adicionarTarefa(tarefas, 'Ler um livro');

listarTarefas(tarefas);

removerTarefa(tarefas, 2);

listarTarefas(tarefas);
