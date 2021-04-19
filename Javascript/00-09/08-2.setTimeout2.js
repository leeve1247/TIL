//setInterval 이거슨 주기적으로 실행슨이라고 합니다. 알겠습니까?
//$(document).ready(function () 
function run(){
    var testInterval = setInterval(function()
    {
       console.log("야! 나는 피카츄다");
    },500);
    setTimeout(function(){
        clearTimeout(testInterval);
    },8000)
}

run()
