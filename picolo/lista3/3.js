const exibirResultadoFuncionario = (salarioAtual, salarioNovo) => {};

const calcularAumentoParaFuncionarios = (salariosAtuais) => {
	salariosAtuais.forEach((sal) => {
		let percentualAumento = 5;
		switch (sal) {
			case sal <= 280:
				percentualAumento = 20;
				break;
			case sal < 700:
				percentualAumento = 15;
				break;
			case sal < 1500:
				percentualAumento = 10;
				break;
		}
        const aumento = salarioAtual * (percentualAumento/)
        exibirResultadoFuncionario(sal, )
	});
};
