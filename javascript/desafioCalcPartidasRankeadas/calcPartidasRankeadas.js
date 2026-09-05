const readline = require("readline");

// Configuração da interface de entrada e saída
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Função que calcula o saldo de vitórias e derrotas
function balanceVD(wins, losses) {
  return wins - losses;
}

// Função que determina o nível do herói com base nas vitórias
function heroStatus(winsParam, lossesParam) {
  const balance = balanceVD(winsParam, lossesParam);

  if (winsParam < 0) {
    console.log("Você ainda não atingiu nenhum ranking");
    return;
  }

  // Array que define as faixas de ranking
  const ranking = [
    { min: 0, max: 10, lvl: "Ferro" },
    { min: 11, max: 20, lvl: "Bronze" },
    { min: 21, max: 50, lvl: "Prata" },
    { min: 51, max: 80, lvl: "Ouro" },
    { min: 81, max: 90, lvl: "Diamante" },
    { min: 91, max: 100, lvl: "Lendário" },
    { min: 101, max: undefined, lvl: "Imortal" },
  ];

  let lvl = "";

  // Loop que verifica em qual faixa de ranking as vitórias se encaixam
  for (const rank of ranking) {
    if (
      winsParam >= rank.min &&(rank.max === undefined || winsParam <= rank.max)
    ) {
      lvl = rank.lvl;
      break;
    }
  }

  // Exibe resultado final
  console.log("O Herói tem um saldo de",balance,"vitórias, e está no nível",lvl);
}

// Função de validação de entrada
function validationTests(input) {
  // Verifica se a string está vazia
  function empty(input) {
    return input.trim() === "";
  }
  // Verifica se a quantidade de caracteres não ultrapassa o limite de 4 dígitos
  function charAmount(input) {
    return input.length > 4;
  }
  // Verifica se todos os caracteres são números inteiros positivos
  function charValidation(input) {
    const regex = /^[0-9]+$/;
    return regex.test(input);
  }
  // Retorna true se todas as validações forem passadas
  if (empty(input) || charAmount(input) || !charValidation(input)) {
    return false;
  }
  return true;
}

// Função principal que solicita as entradas do usuário
function promptInput() {
  rl.question("Insira o número de vitórias ", (winsInput) => {
    // Validação das vitórias
    if (!validationTests(winsInput)) {
      console.log("Entrada inválida para vitórias.");
      return promptInput();
    }
    const wins = parseInt(winsInput);

    // Função aninhada para solicitar as derrotas
    function promptLosses() {
      rl.question("Insira o número de derrotas ", (lossesInput) => {
        // Validação das derrotas
        if (!validationTests(lossesInput)) {
          console.log("Entrada inválida para derrotas.");
          return promptLosses();
        }
        const losses = parseInt(lossesInput);
        
        // Chama a função que calcula o ranking e exibe o resultado
        heroStatus(wins, losses);
        rl.close();
      });
    }
    promptLosses();// Inicia a solicitação de derrotas
  });
}
promptInput();// Inicia a solicitação de vitórias