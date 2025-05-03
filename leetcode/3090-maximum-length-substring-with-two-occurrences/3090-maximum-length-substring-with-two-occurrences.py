def maximumLengthSubstring(s: str) -> int:
        right = 1
        left = 0
        _max = 1

        dictionary = {}
        dictionary[s[0]] = 1

        while right < len(s):

            if dictionary.get(s[right]):
                if dictionary[s[right]] == 2:
                    dictionary[s[left]] -= 1
                    left += 1
                else:
                    dictionary[s[right]] += 1
                    right += 1
            else:
                dictionary[s[right]] = 1
                right += 1
        
            _max = max(_max, right-left) 

        return _max

print(maximumLengthSubstring("aadaad"))
print(maximumLengthSubstring([1,3,2,1,4,1,7,2,3,6,12]));