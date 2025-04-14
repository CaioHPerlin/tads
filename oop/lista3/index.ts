class Retangulo {
    largura: number;
    altura: number;

    constructor(largura: number, altura: number) {
        this.largura = largura;
        this.altura = altura;
    }

    get area() {
        return this.largura * this.altura;
    }

    get perimetro() {
        return 2 * (this.altura + this.largura);
    }
}

class Quadrado extends Retangulo {

    constructor(lado: number){
        super(lado, lado)
    }

}

const retangulo = new Retangulo(10, 40);
const quadrado = new Quadrado(20);

console.log('\nRetângulo')
console.log(`- Perímetro: ${retangulo.perimetro}`)
console.log(`- Área: ${retangulo.area}`)


console.log('\nQuadrado')
console.log(`- Perímetro: ${quadrado.perimetro}`)
console.log(`- Área: ${quadrado.area}`)