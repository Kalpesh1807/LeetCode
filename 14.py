# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        result = ""
        base = strs[0]
        for i in range (len(base)):
            for j in strs[1:]:
                if i == len(j) or j[i] != base[i]:
                    return result
            result += base[i]
        return result