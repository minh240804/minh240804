
// var text={
//     "1a" : "a",
//     "2b" : "bb",
// };
// text["2b"]="BB";
// text["3c"]="ccc";
// console.log(text);
// console.log(text["2b"]);


// function hello(things) {
//     console.log(things);
// }

// function sum(a, b){
//     s=a+b;
//     console.log(s)
// }
// function goodbye(){
//     console.log("byebye")
// }


// function showPopup() {
//     console.log("“I Love JS”");
// }
// s
// function howPopupWithLove(x)
//     console.log("I love",x);
// }

// var l= document.getElementById("BTN_SEACHER");
// var R=document.getElementsByClassName("rect red");
// console.log(R)

// console.log(l);

// var rects=document.getElementsByClassName("rect");
// console.log(rects);
// for (var i=0; i<3;i++){
    
// }

// var divs = document.getElementsByTagName("div");
// console.log(divs);

// for (var i=0 ;i <5;i++){
//     console.log(divs[i]);
//}


// var ul= document.getElementById("2.");
// var ullist=ul.getElementsByTagName("li");
// console.log(ullist);


function find(){
 console.log("clicked")
}



var btn = document.getElementById("btn");
console.log(btn.textContent);
btn.textContent="stop";
btn.addEventListener('click', function (e) {
    var btn=e.target;
    var div=btn.parentNode
    console.log (btn)
});


var sea = document.getElementById("sea");
sea.value="";
sea.style.backgroundColor="black";   
sea.style.color="white";


var apa= document.getElementById("apa");
// var newLI= document.createElement("li");
// newLI.textContent="c";
// apa.appendChild(newLI)

// var lil=apa.getElementsByTagName("li")
// var delet=lil[0];
// delet.remove();
//apa.textContent="";
