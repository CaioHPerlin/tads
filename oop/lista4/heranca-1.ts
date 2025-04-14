class VooComFumantes extends Voo {
  maxVagas: number;
  cadeirasFumantes: number;

  constructor(
    numeroVoo: string,
    data: Data,
    maxVagas: number,
    cadeirasFumantes: number
  ) {
    super(numeroVoo, data);

    this.maxVagas = maxVagas > 0 ? maxVagas : 100;
    this.cadeirasFumantes = Math.min(
      Math.max(0, cadeirasFumantes),
      this.maxVagas
    );

    this.cadeiras = new Array(this.maxVagas).fill(false);
  }

  public tipo(numeroCadeira: number): string {
    if (numeroCadeira < 1 || numeroCadeira > this.maxVagas) {
      throw new Error(
        `Número de cadeira inválido. Deve ser entre 1 e ${this.maxVagas}.`
      );
    }

    return numeroCadeira > this.maxVagas - this.cadeirasFumantes ? "F" : "N";
  }

  public proximoLivre(): number {
    const index = this.cadeiras.findIndex(
      (cadeira, idx) => !cadeira && idx < this.maxVagas
    );
    return index !== -1 ? index + 1 : -1;
  }

  public verifica(numeroCadeira: number): boolean {
    if (numeroCadeira < 1 || numeroCadeira > this.maxVagas) {
      throw new Error(
        `Número de cadeira inválido. Deve ser entre 1 e ${this.maxVagas}.`
      );
    }
    return this.cadeiras[numeroCadeira - 1];
  }

  public ocupa(numeroCadeira: number): boolean {
    if (numeroCadeira < 1 || numeroCadeira > this.maxVagas) {
      return false;
    }

    if (this.verifica(numeroCadeira)) {
      return false;
    }

    this.cadeiras[numeroCadeira - 1] = true;
    return true;
  }

  public clone(): VooComFumantes {
    const novoVoo = new VooComFumantes(
      this.numeroVoo,
      this.data,
      this.maxVagas,
      this.cadeirasFumantes
    );
    novoVoo.cadeiras = [...this.cadeiras];
    return novoVoo;
  }
}
