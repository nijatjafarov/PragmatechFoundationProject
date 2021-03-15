var a = prompt("Ilk ededi daxil edin: ");

while (a != Number(a)){
  a = prompt("Daxil etdiyiniz eded deyil. Yeniden daxil edin: ")
}

var b = prompt("Ikinci ededi daxil edin: ");

while (b != Number(b)){
  b = prompt("Daxil etdiyiniz eded deyil. Yeniden daxil edin: ")
}
a = Number(a)
b = Number(b)
console.log(a + " + " + b + " = " + (a + b))
