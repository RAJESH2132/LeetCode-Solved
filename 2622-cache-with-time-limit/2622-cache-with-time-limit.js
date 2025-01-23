var TimeLimitedCache = function() {
    // Initialize an internal map to store key-value pairs and expiration times
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const currentTime = Date.now();

    // Check if the key exists and is unexpired
    const existingEntry = this.cache.get(key);
    const isUnexpired = existingEntry && currentTime < existingEntry.expiry;

    // Overwrite the key with the new value and expiration time
    this.cache.set(key, {
        value,
        expiry: currentTime + duration,
    });

    return Boolean(isUnexpired);
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const currentTime = Date.now();

    // Retrieve the entry from the cache
    const entry = this.cache.get(key);

    // Check if the entry is valid and unexpired
    if (entry && currentTime < entry.expiry) {
        return entry.value;
    } else {
        // If expired, remove it from the cache and return -1
        this.cache.delete(key);
        return -1;
    }
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    const currentTime = Date.now();
    let count = 0;

    // Iterate over the cache and count unexpired keys
    for (const [key, entry] of this.cache) {
        if (currentTime < entry.expiry) {
            count++;
        } else {
            // Remove expired keys
            this.cache.delete(key);
        }
    }

    return count;
};

/**
 * Usage example:
 * const timeLimitedCache = new TimeLimitedCache();
 * console.log(timeLimitedCache.set(1, 42, 1000)); // false
 * console.log(timeLimitedCache.get(1)); // 42
 * console.log(timeLimitedCache.count()); // 1
 */
