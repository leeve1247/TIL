var a = [];
//배열 안에는 모든 타입이 다 들어갈 수 있다. 함수도 배열 안에 배열도, 배열 안에 객체도 들어갈 수 있음.
var a = [1,2,3,"hello", null, true, []];
a[1000] = 3;
console.log(a.length);  //얼마일까요? 한번 해보세요.
console.log(a[0]); //그럼, 이 결과는 무엇일까요?

var a = [4];
a.push(5);
console.log(a.length);
