// 함수가 실행되면 그 안에서 arguments라는 특별한 지역변수가 존재한다.
// 자바스크립트 함수는 선언한 파라미터보다 더 많은 인자를 보낼 수도 있다. 
// 이 때 넘어온 인자를 arguments로 만들어, 마치 배열의 형태로 하나씩 접근 할 수 있다.
// 엄밀히 하면 arguemnets는 배열 형태가 아니므로, 배열 메서드를 사용할 수 없다.

function a() {
    // if(arguments.length < 4) return; 
    console.log(arguments);
    for(var i=0; i < arguments.length;i++){
        console.log(arguments[i])
    }
}
// a(1,2,3); //마치 오브젝트 스럽군
// 함수의 인자값이 바뀐다거나, 변수 이름을 정할수가 없어서 arguments 사용할 때는 조심스러워야 한다.

a(1,2,"merongson");

function getName(name) {
    return "Kim" + name;
}

// var getName = (name) => "Kim" + name; // 상단과 동일슨

console.log(getName("hello"))