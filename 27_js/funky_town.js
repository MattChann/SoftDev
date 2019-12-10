var fibonacci = function(n) {
    if (n == 0) {
        return 0;
    }
    else {
        if (n == 1 || n == 2) {
            return 1;
        }
    }
    return fibonacci(n-2) + fibonacci(n-1);
}

var gcd = (a, b) => {
    let greatest = 1;
    let i;
    for(i=1; i<=Math.min(a,b); i++) {
        if ((a%i == 0) && (b%i == 0)) {
            greatest = i;
        }
    }
    return greatest;
}
