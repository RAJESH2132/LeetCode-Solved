/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    var variable = n
    return function() {
        return variable++
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */