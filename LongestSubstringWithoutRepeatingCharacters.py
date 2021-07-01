# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def checkUniqueString(substring_map):
    count = 0
    for key in substring_map:
        if substring_map[key] > 1:
            return False,count
        if substring_map[key]:
            count = count + 1
    return True,count
    
class Solution:   
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        # handling the edge cases
        if len(s) > 1:
            j = 1
        elif len(s) == 1:
            return 1
        else:
            return 0
        
        ans = 1
        # created a dict(map) to check the frequency of character which will help to check unique substring
        substring_map = {}
        substring_map[s[0]] = 1
        # created a window of two at first. incrementing the window size to right and increasing frequency of character when got unique string 
        # else decreasing the window size from left and decreasing frequency of character.
        while i < j and j < len(s):
            if s[j] in substring_map:
                substring_map[s[j]] = substring_map[s[j]] + 1
            else:
                substring_map[s[j]] = 1
            is_substring_unique, count = checkUniqueString(substring_map)
            if is_substring_unique:
                if count > ans:
                    ans = count
            else:
                substring_map[s[i]] = substring_map[s[i]] - 1
                i = i + 1
            j = j + 1
                
        return ans