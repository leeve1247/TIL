// var : 변수, const : 상수스(불변스)  let :  
var a = 2;          // 숫자
var a = "aaa";      // 문자열
var a = 'aaa';      // 문자열
var a = true;       // boolean 타입
var a = [];         // 배열
var a = {};
var a = undefined;

//or 연산자 활용
var name = "crong";
var result = name || "codesquad";
console.log(result);

//삼항 연사자
const data = 11;
const result1 = (data > 10) ? "ok" : "fail"; //if data > 10 : result = "ok" else : result = "fail"
console.log(result);

//비교 연산자
0 == false;
"" == false;
null == false;
0 == "0"; //true
0 === "0"; //false , 습관적으로 이것을 쓰기를 권장.
null==undefined; //true 왜일까

console.log("함수")
function run(a) {
    console.log(typeof a)
}

// 타입은 선언할 때가 아닌, 실행할 때 결정된다. 함수 안에서 변수가 활용될 때 결정됨.
run("asdf")
run(false)

toString.call("ddd");
