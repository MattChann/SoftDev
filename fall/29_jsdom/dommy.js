/*
Mo Abedin, Matthew Chan
SoftDev1 pd2
K29 -- Sequential Progression III: Season of the Witch
2019-12-12
*/


// Lo, what is this? Coult it be a VALUE-ADDED-KEY2SUCCESS?!?!

var changeHeading = function(e) {
    //console.log(e);
    var h = document.getElementById("h");
    h.innerHTML = e.target.innerHTML;
};

var removeItem = function(e) {
    e.target.remove();
};

var lis = document.getElementsByTagName("li");
for (var i=0; i<lis.length; i++) {
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout',  () => {document.getElementById("h").innerHTML = "Hello World!";});
    lis[i].addEventListener('click',     removeItem);
};

var addItem = function(e) {
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";

    item.addEventListener('mouseover', changeHeading);
    item.addEventListener('mouseout',  () => {document.getElementById("h").innerHTML = "Hello World!";});
    item.addEventListener('click',     removeItem);

    list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
    if (n < 2) {
        return 1;
    }
    else {
        return fib(n-1) + fib(n-1);
    }
};

var addFib = function(e) {
    console.log(e);
    var list = document.getElementById("fiblist");
    var item = document.createElement("li");
    item.innerHTML = fib(list.children.length);
    list.appendChild(item);
};

var addFib2 = function(e) {
    console.log(e);
    // See QAF re: DYNAMIC PROGRAMMING ...
};

var fb = document.getElementById("fb");
fb.addEventListener('click', addFib);