//setTimeout 함수는 함수를 받는 함수로, 비동기 callback 함수라고도 불림
//비동기 callback 함수는 모든 stack(코드라인)이 진행되고 나서 실행되은다

function run() {
    console.log("run start")
    setTimeout(function(){
        console.log("run........ing"); //이 메시지는 즉시 실행되지 않는다.
    },2000); //모든 프로그램이 저언부 실행되고 나서! 실행된다.

    console.log("run end");
}

console.log("execute start");
run();
console.log("execute end");