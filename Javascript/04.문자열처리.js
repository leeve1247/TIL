// 문자 하나도 문자열입니다.


var result = "ab:cd".replace(":","%"); //"ab$cd"
var result1 = "ab:cd".split(":"); //"ab$cd"
var a = "abc";
var b = "b";
var c = "c";

console.log(result);
console.log(toString.call(result));
console.log(result1);
console.log(toString.call(result1));
console.log(typeof a);
console.log(typeof b);
console.log(typeof c);
