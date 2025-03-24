class Autor {
  nome: string;
  nacionalidade: string;
  dataDeNascimento: Date;

  constructor(nome: string, nacionalidade: string, dataNascimento: Date) {
    this.nome = nome;
    this.nacionalidade = nacionalidade;
    this.dataDeNascimento = dataNascimento;
  }

  public imprimirDetalhes(): void {
    console.log(
      `Autor: ${this.nome}, Nacionalidade: ${
        this.nacionalidade
      }, Data de Nascimento: ${this.dataDeNascimento.toLocaleDateString()}`
    );
  }
}

class Livro {
  titulo: string;
  anoDePublicacao: number;
  autores: Autor[];

  constructor(titulo: string, anoDePublicacao: number, autores: Autor[] = []) {
    this.autores = autores;
    this.titulo = titulo;
    this.anoDePublicacao = anoDePublicacao;
  }

  public imprimirDetalhes(): void {
    console.log(
      `Livro: ${this.titulo}, Ano de Publicação: ${
        this.anoDePublicacao
      }, Autores: ${this.autores.map((a) => a.nome).join(", ")}`
    );
  }
}

class Usuario {
  nome: string;
  idade: number;
  livrosReservados: Livro[] = [];

  constructor(nome: string, idade: number) {
    this.nome = nome;
    this.idade = idade;
  }

  public reservarLivro(livro: Livro): void {
    this.livrosReservados.push(livro);
    console.log(`${this.nome} reservou o livro: ${livro.titulo}`);
  }

  public devolverLivro(livro: Livro): void {
    this.livrosReservados = this.livrosReservados.filter(
      (l) => l.titulo !== livro.titulo
    );
    console.log(`${this.nome} devolveu o livro: ${livro.titulo}`);
  }

  public imprimirLivrosReservados(): void {
    console.log(
      `${this.nome} tem os seguintes livros reservados: ${this.livrosReservados
        .map((l) => l.titulo)
        .join(", ")}`
    );
  }

  public imprimirDetalhes(): void {
    console.log(`Usuário: ${this.nome}, Idade: ${this.idade}`);
  }
}

// Criando autores
const autor1 = new Autor(
  "Machado de Assis",
  "Brasileiro",
  new Date("1839-06-21")
);
const autor2 = new Autor(
  "José de Alencar",
  "Brasileiro",
  new Date("1829-05-01")
);

// Criando livros
const livro1 = new Livro("Dom Casmurro", 1899, [autor1]);
const livro2 = new Livro("Literatura Brasileira", 1920, [autor1, autor2]);

// Criando usuários
const usuario = new Usuario("João Doe", 30);

// Imprimindo objetos criados
console.log("\n- Autores");
autor1.imprimirDetalhes();
autor2.imprimirDetalhes();

console.log("\n- Livros");
livro1.imprimirDetalhes();
livro2.imprimirDetalhes();

console.log("\n- Usuário");
usuario.imprimirDetalhes();

// Ações do usuário
console.log("\n- Ações do Usuário");
usuario.reservarLivro(livro1);
usuario.reservarLivro(livro2);

usuario.imprimirLivrosReservados();

usuario.devolverLivro(livro1);
usuario.imprimirLivrosReservados();
