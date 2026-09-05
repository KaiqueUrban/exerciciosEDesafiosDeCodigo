let nome = ("Trevor Belmont")
let xp = 8675

if (xp <= 1000){
    console.log("O Herói " + nome + " está no nivel " + "Ferro")
}else if (1001 <= xp && xp <= 2000){
    console.log("O Herói " + nome + " está no nível " + "Bronze")
}else if (2001 <= xp && xp <= 5000){
    console.log("O Herói " + nome + " está no nível " + "Prata")
}else if (5001 <= xp && xp <= 7000){
    console.log("O Herói " + nome + " está no nível " + "Ouro")
}else if (7001 <= xp && xp <= 8000){
    console.log("O Herói " + nome + " está no nível " + "Platina")
}else if (8001 <= xp && xp <= 9000){
    console.log("O Herói " + nome + " está no nível " + "Ascendente")
}else if (9001 <= xp && xp <= 10000){
    console.log("O Herói " + nome + " está no nível " + "Imortal")
}else{
    console.log("O Herói " + nome + " está no nível " + "Radiante")
}