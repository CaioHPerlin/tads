class Data {
  dia: number;
  mes: number;
  ano: number;

  constructor(dia: number, mes: number, ano: number) {
    if (this.dataValida(dia, mes, ano)) {
      this.dia = dia;
      this.mes = mes;
      this.ano = ano;
    } else {
      this.dia = 1;
      this.mes = 1;
      this.ano = 1;
    }
  }

  dataValida(dia: number, mes: number, ano: number): boolean {
    if (ano < 1 || mes < 1 || mes > 12 || dia < 1) return false;

    const diasNoMes = new Date(ano, mes, 0).getDate();
    return dia <= diasNoMes;
  }

  compara(outraData: Data): number {
    if (
      this.ano === outraData.ano &&
      this.mes === outraData.mes &&
      this.dia === outraData.dia
    ) {
      return 0;
    }

    if (
      this.ano > outraData.ano ||
      (this.ano === outraData.ano && this.mes > outraData.mes) ||
      (this.ano === outraData.ano &&
        this.mes === outraData.mes &&
        this.dia > outraData.dia)
    ) {
      return 1;
    }

    return -1;
  }

  getDia(): number {
    return this.dia;
  }

  getMes(): number {
    return this.mes;
  }

  getMesExtenso(): string {
    const meses = [
      "Janeiro",
      "Fevereiro",
      "Março",
      "Abril",
      "Maio",
      "Junho",
      "Julho",
      "Agosto",
      "Setembro",
      "Outubro",
      "Novembro",
      "Dezembro",
    ];
    return meses[this.mes - 1];
  }

  getAno(): number {
    return this.ano;
  }

  isBissexto(): boolean {
    return (this.ano % 4 === 0 && this.ano % 100 !== 0) || this.ano % 400 === 0;
  }

  clone(): Data {
    return new Data(this.dia, this.mes, this.ano);
  }
}

const data1 = new Data(15, 10, 2023);
const data2 = new Data(31, 2, 2023);
const data3 = new Data(29, 2, 2020);
const data4 = new Data(29, 2, 2021);
const data5 = new Data(15, 10, 2023);

console.log("--- Testes Básicos ---");
console.log(`Data1: ${data1.getDia()}/${data1.getMes()}/${data1.getAno()}`);
console.log(
  `Data2 (inválida): ${data2.getDia()}/${data2.getMes()}/${data2.getAno()}`
);
console.log(`Data1 mês por extenso: ${data1.getMesExtenso()}`);
console.log(`2020 é bissexto? ${data3.isBissexto()}`);
console.log(`2021 é bissexto? ${data4.isBissexto()}`);

console.log("\n--- Testes de Comparação ---");
console.log("Comparando data1 e data5:", data1.compara(data5));
console.log("Comparando data1 e data3:", data1.compara(data3));
console.log("Comparando data3 e data1:", data3.compara(data1));

console.log("\n--- Teste de Clone ---");
const cloneData1 = data1.clone();
console.log(
  `Clone de data1: ${cloneData1.getDia()}/${cloneData1.getMes()}/${cloneData1.getAno()}`
);
console.log("Clone é igual ao original?", data1.compara(cloneData1) === 0);

console.log("\n--- Testes com Datas Inválidas ---");
const data6 = new Data(31, 4, 2023);
const data7 = new Data(0, 15, 2023);
console.log(
  `Data6 (31/4/2023): ${data6.getDia()}/${data6.getMes()}/${data6.getAno()}`
);
console.log(
  `Data7 (0/15/2023): ${data7.getDia()}/${data7.getMes()}/${data7.getAno()}`
);

console.log("\n--- Testes de Ano Bissexto ---");
console.log("2000 é bissexto?", new Data(1, 1, 2000).isBissexto());
console.log("1900 é bissexto?", new Data(1, 1, 1900).isBissexto());
console.log("2024 é bissexto?", new Data(1, 1, 2024).isBissexto());
