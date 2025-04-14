class Equipamento {
  valores: number[];

  constructor(numeroEquipamentos: number) {
    this.valores = new Array(numeroEquipamentos).fill(0);
  }

  getNumeroEquipamentos(): number {
    return this.valores.length;
  }

  getValor(numeroEquipamento: number): number {
    if (numeroEquipamento < 0 || numeroEquipamento >= this.valores.length) {
      throw new Error("Número de equipamento inválido");
    }
    return this.valores[numeroEquipamento];
  }

  setValor(numeroEquipamento: number, valor: number): void {
    if (numeroEquipamento < 0 || numeroEquipamento >= this.valores.length) {
      throw new Error("Número de equipamento inválido");
    }
    this.valores[numeroEquipamento] = valor;
  }
}

class EquipamentoCorrigido extends Equipamento {
  mesesCompra: number[];
  mesCorrente: number;

  constructor(numeroEquipamentos: number, mesCorrente: number = 1) {
    super(numeroEquipamentos);
    this.mesesCompra = new Array(numeroEquipamentos).fill(0);
    this.mesCorrente = mesCorrente >= 1 && mesCorrente <= 12 ? mesCorrente : 1;
  }

  getMesCompra(numeroEquipamento: number): number {
    if (
      numeroEquipamento < 0 ||
      numeroEquipamento >= this.getNumeroEquipamentos()
    ) {
      throw new Error("Número de equipamento inválido");
    }
    return this.mesesCompra[numeroEquipamento];
  }

  setMesCompra(numeroEquipamento: number, mesCompra: number): void {
    if (
      numeroEquipamento < 0 ||
      numeroEquipamento >= this.getNumeroEquipamentos()
    ) {
      throw new Error("Número de equipamento inválido");
    }
    if (mesCompra < 1 || mesCompra > 12) {
      throw new Error("Mês de compra inválido (deve ser entre 1 e 12)");
    }
    this.mesesCompra[numeroEquipamento] = mesCompra;
  }

  corrige(percentualCorrecao: number): void {
    for (let i = 0; i < this.getNumeroEquipamentos(); i++) {
      if (this.mesesCompra[i] === this.mesCorrente) {
        const valorAtual = this.getValor(i);
        const novoValor = valorAtual * (1 + percentualCorrecao / 100);
        this.setValor(i, novoValor);
      }
    }
    this.mesCorrente = this.mesCorrente === 12 ? 1 : this.mesCorrente + 1;
  }

  substitui(outroEquipamento: EquipamentoCorrigido): boolean {
    if (
      this.getNumeroEquipamentos() !== outroEquipamento.getNumeroEquipamentos()
    ) {
      return false;
    }

    for (let i = 0; i < this.getNumeroEquipamentos(); i++) {
      this.setValor(i, outroEquipamento.getValor(i));
      this.mesesCompra[i] = outroEquipamento.getMesCompra(i);
    }

    return true;
  }

  getMesCorrente(): number {
    return this.mesCorrente;
  }
}
