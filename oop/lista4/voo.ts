class Voo {
  numeroVoo: string;
  data: Data;
  cadeiras: boolean[];

  constructor(numeroVoo: string, data: Data) {
    this.numeroVoo = numeroVoo;
    this.data = data;
    this.cadeiras = new Array(100).fill(false);
  }

  proximoLivre(): number {
    const index = this.cadeiras.findIndex((cadeira) => !cadeira);
    return index !== -1 ? index + 1 : -1;
  }

  verifica(numeroCadeira: number): boolean {
    if (numeroCadeira < 1 || numeroCadeira > 100) {
      throw new Error("Número de cadeira inválido. Deve ser entre 1 e 100.");
    }
    return this.cadeiras[numeroCadeira - 1];
  }

  ocupa(numeroCadeira: number): boolean {
    if (numeroCadeira < 1 || numeroCadeira > 100) {
      return false;
    }

    if (this.verifica(numeroCadeira)) {
      return false;
    }

    this.cadeiras[numeroCadeira - 1] = true;
    return true;
  }

  vagas(): number {
    return this.cadeiras.filter((cadeira) => !cadeira).length;
  }

  getVoo(): string {
    return this.numeroVoo;
  }

  getData(): Data {
    return this.data;
  }

  clone(): Voo {
    const novoVoo = new Voo(this.numeroVoo, this.data);
    novoVoo.cadeiras = [...this.cadeiras];
    return novoVoo;
  }
}
