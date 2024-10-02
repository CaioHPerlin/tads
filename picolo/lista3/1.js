const printarTabuada = (x, n) => {
	for (let i = 1; i <= n; i++) {
		console.log(`${x} x ${i} = ${x * i}`);
	}
};

const entrada = 5;
printarTabuada(entrada, 10);
