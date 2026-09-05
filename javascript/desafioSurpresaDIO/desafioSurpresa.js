//Crie um código para armazenar o máximo de informações possível dos pokemon da imagem e ao final, 
//para cada um, exiba uma mensagem de saída escrita o nome do pokemon concatenado com "Cadastrado com sucesso".

const pokemons = [{
    name: "Poochyena",
    lvl: 2,
    gender: "M",
    hp: 13,
},
{
    name: "Zigzagoon",
    lvl: 2,
    gender: "F",
    hp: 13,
},

{
    name: "Dragonite",
    lvl: 5,
    gender: "M",
    hp: 25,
},

{
    name: "Dragonite",
    lvl: 5,
    gender: "F",
    hp: 24,
},

{
    name: "Dragonite",
    lvl: 5,
    gender: "F",
    hp: 24,
},

{
    name: "Poochyena",
    lvl: 3,
    gender: "F",
    hp: 15
},

{
    name: "Hurmple",
    lvl: 2,
    gender: "M",
    hp: 7
    
}]

for ( const pokemon of pokemons){
    console.log("O Pokemon " + pokemon.name + " foi cadastrado com sucesso!")
}