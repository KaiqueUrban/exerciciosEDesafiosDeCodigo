// Definindo os tipos válidos de heróis
const tiposValidos = ["Guerreiro", "Mago", "Monge", "Ninja"];

// Classe Heroi com validação de atributos e método de ataque
class Heroi {
  constructor(nome, idade, tipo) {
    this.result = this.validation(nome, idade, tipo);
    this.nome = this.result.nome;
    this.idade = this.result.idade;
    this.tipo = this.result.tipo;
  }

  // Método de validação dos atributos
  validation(nome, idade, tipo) {
    function nameValidation(nome) { // Validação do nome
      if (
        typeof nome !== "string" ||
        nome.trim() === "" ||
        !nome.match(/^[a-zA-Z]+$/)
      ) {
        throw new Error(
          "Nome inválido: deve conter apenas letras e não pode estar vazio."
        );
      }

      return nome.trim();
    }

    function ageValidation(idade) { // Validação da idade
      if (typeof idade !== "number" || idade <= 0 || !Number.isInteger(idade)) {
        throw new Error("Idade inválida: deve ser um número inteiro positivo.");
      }

      return idade;
    }

    function typeValidation(tipo) { // Validação do tipo
      if (typeof tipo !== "string" || tipo.trim() === "") {
        throw new Error("Tipo inválido: deve ser uma string não vazia.");
      }

      const cleanedType = tipo.trim();

      const normalizedtype = // Normaliza o tipo para comparação
        cleanedType.charAt(0).toUpperCase() +
        cleanedType.slice(1).toLowerCase();
      if (!tiposValidos.includes(normalizedtype)) {
        throw new Error("Tipo inválido: deve ser um dos tipos válidos.");
      }

      return normalizedtype; // Retorna o tipo validado
    }

    const validatedName = nameValidation(nome); // Chama a validação do nome
    const validatedAge = ageValidation(idade); // Chama a validação da idade
    const validatedType = typeValidation(tipo); // Chama a validação do tipo
 
    return { nome: validatedName, idade: validatedAge, tipo: validatedType };
  } // Fim do método de validação

  // Método de ataque baseado no tipo do herói
  atacar() { // Define os ataques para cada tipo de herói
    const ataque = {
      Guerreiro: "espada",
      Mago: "magia",
      Monge: "artes marciais",
      Ninja: "shuriken",
    };

    const handler = ataque[this.tipo]; // Obtém o ataque correspondente ao tipo do herói
    return `O ${this.tipo} atacou usando ${handler}!`; // Retorna a mensagem de ataque
  }
}
