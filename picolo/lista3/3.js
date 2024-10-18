const exibirResultadoFuncionario = (relatorioSalarial) => {
	console.log(
		`
-- Funcionário ${relatorioSalarial.indice}
Salário antes do reajuste: ${relatorioSalarial.salarioAtual}
Percentual de aumento aplicado: ${relatorioSalarial.percentualAumento}%
Valor do aumento: ${relatorioSalarial.aumento}
Novo salário após aumento: ${relatorioSalarial.salarioNovo}`
	);
};

const exibirResultados = (relatoriosSalariais) => {
	relatoriosSalariais.forEach((relatorioSalarial) => {
		exibirResultadoFuncionario(relatorioSalarial);
	});
};

const calcularAumentoParaFuncionarios = (salariosAtuais) => {
	let relatoriosSalariais = [];

	salariosAtuais.forEach((salarioAtual, i) => {
		let percentualAumento = 5;
		switch (salarioAtual) {
			case salarioAtual <= 280:
				percentualAumento = 20;
				break;
			case salarioAtual < 700:
				percentualAumento = 15;
				break;
			case salarioAtual < 1500:
				percentualAumento = 10;
				break;
		}
		const aumento = salarioAtual * percentualAumento;
		const salarioNovo = salarioAtual + aumento;
		relatoriosSalariais = [
			...relatoriosSalariais,
			{
				indice: i,
				salarioAtual: salarioAtual,
				salarioNovo: salarioNovo,
				percentualAumento: percentualAumento,
				aumento: aumento,
			},
		];
	});

	return relatoriosSalariais;
};

const salariosExemplo = [100, 300, 600, 700, 800, 1000, 1500, 1600];
const relatoriosAumento = calcularAumentoParaFuncionarios(salariosExemplo);
exibirResultados(relatoriosAumento);
