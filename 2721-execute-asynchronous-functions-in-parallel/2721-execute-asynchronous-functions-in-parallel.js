/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = [];
        let completedCount = 0;

        // Iterate through each function in the array
        functions.forEach((func, index) => {
            // Execute the function to get the promise
            func()
                .then((value) => {
                    results[index] = value; // Store the resolved value at the correct index
                    completedCount++;

                    // If all promises are resolved, resolve the overall promise
                    if (completedCount === functions.length) {
                        resolve(results);
                    }
                })
                .catch((error) => {
                    // Reject the overall promise if any promise is rejected
                    reject(error);
                });
        });
    });
};
