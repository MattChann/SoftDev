/*
Matthew Chan, Hilary Zen
SoftDev1 pd2
K28 -- Sequential Progression II: Electric Boogaloo
2019-12-11
*/

document.getElementById("fibonacci").addEventListener('click', () => {
    var fib = fibonacci(7);
    console.log(fib);
    document.getElementById("fibonacciOut").innerHTML = fib;
});

var fibonacci = function(n) {
    if (n === 0) {
        return 0;
    } else if (n === 1) {
        return 1;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

document.getElementById("gcd").addEventListener('click', () => {
    var denominator = gcd(20,4);
    console.log(denominator);
    document.getElementById("gcdOut").innerHTML = denominator;
});

var gcd = function(a, b) {
    var currGreatest = 1;
    for (var i = 2; i <= Math.min(a, b); i++) {
        if (a % i == 0 && b % i == 0) {
            currGreatest = i;
        }
    }
    return currGreatest;
}

document.getElementById("randomStudent").addEventListener('click', () => {
    var student = randomStudent();
    console.log(student);
    document.getElementById("randomStudentOut").innerHTML = student;
});

var randomStudent = function() {
    var students = ["Dub Cao", "Coyote", "Matthew", "Blobfish"];
    var index = Math.floor(Math.random() * students.length);
    return students[index];
}

/*
document.getElementById()
document.getElementByTagName()
document.getElementByClassName()

.addEventListener()

document.createElement()
document.setAttribute()
document.getAttribute()

.remove()
.innerHTML()
.appendChild()

*/