def lengthOfLongestSubstring(s):
    right = 1
    left = 0
    _max = 1

    if len(s) == 0:
        return 0

    dicionario = {}
    dicionario[s[0]] = 1

    while right < len(s):

        if dicionario.get(s[right]):
            dicionario[s[left]] -= 1
            left += 1
        else:
            dicionario[s[right]] = 1
            right+=1

        _max = max(_max, right-left)

    return _max

a = lengthOfLongestSubstring("abcabcbb")
b = lengthOfLongestSubstring("au")
c = lengthOfLongestSubstring("")
d = lengthOfLongestSubstring("   ")

print(a)
print(b)
print(c)
print(d)