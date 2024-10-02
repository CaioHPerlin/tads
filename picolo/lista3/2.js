let i = 1;
const printarTabuada = (x, n) => {
	console.log(`${x} x ${i} = ${x * i}`);
	if (i === n) {
		i = 1;
		return;
	}

	i++;

	printarTabuada(x, n);
};

const entrada = 5;
printarTabuada(entrada, 10);
