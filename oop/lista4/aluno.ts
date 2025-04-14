class Aluno {
  matricula: string;
  nome: string;
  notaProva1: number;
  notaProva2: number;
  notaTrabalho: number;

  constructor(
    matricula: string,
    nome: string,
    notaProva1: number,
    notaProva2: number,
    notaTrabalho: number
  ) {
    this.matricula = matricula;
    this.nome = nome;
    this.notaProva1 = notaProva1;
    this.notaProva2 = notaProva2;
    this.notaTrabalho = notaTrabalho;
  }

  get media(): number {
    const media =
      (this.notaProva1 * 2.5 + this.notaProva2 * 2.5 + this.notaTrabalho * 2) /
      7;
    return media;
  }

  get final(): number {
    const media = this.media;
    if (media >= 7) {
      return 0;
    } else {
      const notaNecessaria = (5 - media * 0.6) / 0.4;
      return notaNecessaria > 0 ? notaNecessaria : 0;
    }
  }
}

const aluno1 = new Aluno("123", "João", 8, 9, 7);
const aluno2 = new Aluno("456", "Maria", 5, 6, 7);
const aluno3 = new Aluno("789", "José", 4, 5, 6);

const alunos = [aluno1, aluno2, aluno3];
console.log(alunos);

for (const aluno of alunos) {
  console.log(
    `Aluno: ${aluno.nome}, Média: ${aluno.media.toFixed(
      2
    )}, Nota Final: ${aluno.final.toFixed(2)}`
  );
}
