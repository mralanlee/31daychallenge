class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str = ''
        for letter in s:
            if letter.isalnum() is False:
                continue

            str += letter.lower()

        return str == str[::-1]
