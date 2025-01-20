/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    var size = args.length
    return size
};

/**
 * argumentsLength(1, 2, 3); // 3
 */