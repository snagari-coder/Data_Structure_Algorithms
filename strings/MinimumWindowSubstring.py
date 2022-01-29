class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        if t == "": return ""
        
        # t_hashmap is counting unique chars of t
        # s_hashmap is counting unique chars of s
        t_hashmap, s_hashmap = {}, {}
        
        #adding unique chars from t into hashmap
        for c in t:
            t_hashmap[c] = 1 + t_hashmap.get(c, 0)
        
        #have holds what s chars we captured in our window
        #need holds what unique chars of t
        # res holds the pointers l&r ( left and right )
        
        have, need = 0, len(t_hashmap)
        res, resLen = [-1, -1], float("infinity")
        l = 0 #left pointer of s window starts from 0
        
        # for each char of string s
        for r in range(len(s)):
            c = s[r]
            #add to s hashmap
            s_hashmap[c] = 1 + s_hashmap.get(c, 0)
            #if that char is in t hashmap, and the count is what we need,
            #increment have
            if c in t_hashmap and s_hashmap[c] == t_hashmap[c]:
                have += 1
            
            # when have and need are the same we have needed substring
            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our s, in order to get min substring
                s_hashmap[s[l]] -= 1
                if s[l] in t_hashmap and s_hashmap[s[l]] < t_hashmap[s[l]]:
                    have -= 1
                #move the left point forward
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        
        # Time = space = O(n)
