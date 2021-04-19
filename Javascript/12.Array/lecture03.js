//origin과 changed는 같은 배열원소를 가지고 있지만, 두 개가 가리키는 메모리 주소는 다릅니다.즉 reference가 다르다고 할 수 있습니다. 
var origin = [1,2,3,4];
var changed = origin.concat();  //[1,2,3,4]
console.log(origin === changed);  //[1, 2, 3, 4] [1, 2, 3, 4] false

//forEach는 함수를 인자로 받고 있어요.
["apple","tomato"].forEach(function(value) {
    console.log(value)
 });


 var newArr = ["apple","tomato"].map(function(value, index) {
    return index + "번째 과일은 " + value + "입니다";
 });
 console.log(newArr)// 여러분들이 실행해보세요