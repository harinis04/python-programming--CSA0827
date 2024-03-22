def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t_mapping = {}
    t_to_s_mapping = {}
    
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        if char_s in s_to_t_mapping:
            if s_to_t_mapping[char_s] != char_t:
                return False
        else:
            s_to_t_mapping[char_s] = char_t
        
        if char_t in t_to_s_mapping:
            if t_to_s_mapping[char_t] != char_s:
                return False
        else:
            t_to_s_mapping[char_t] = char_s
    
    return True


s1 = "egg"
t1 = "add"
print(is_isomorphic(s1, t1))  # Output: True

s2 = "foo"
t2 = "bar"
print(is_isomorphic(s2, t2))  # Output: False
