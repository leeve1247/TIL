var el = document.querySelector(".outside");
el.addEventListener("click", function(e){
    // console.log('clicked!!',e);
    var target1 = e.target;
    console.log(target1.className, target1.dataset)
    console.log(target1.innerText)
//do something..
}, false);