/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let hash = {}
    let start = 0
    let greatest = 0

    for (let i = 0; i < s.length; i++) {
        let current = hash[s[i]]
        if (current!=null && start <= current) {
            start = current + 1
        } else {
            greatest = Math.max(greatest, i - start + 1)
        }

        hash[s[i]] = i
    }

    return greatest
};
