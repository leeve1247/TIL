// 함수는 js에서 조온나리 중요한 물건이다.
function printName(firstname) {
    var myname = "jisu";
    return myname + " " + firstname;
}

console.log(printName()); //선언되지 않고 할당되지 않은 변수는 undefined가 자동 할당된다.


var sirname = "park";
sirname=printName(sirname);
console.log(sirname);

//////////////////////////////////////////////////////////////////////////////////////
function printName(firstname) {
    var result = inner();
    
    var inner = function() {
        return "inner value";
    }    
    console.log("name is " + result);
}

