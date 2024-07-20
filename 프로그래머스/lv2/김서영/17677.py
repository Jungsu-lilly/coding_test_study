def solution(str1, str2):
    import re
    from collections import Counter
    
    str1, str2 = str1.lower(), str2.lower()
    
    is_valid = lambda x: re.compile(r'[A-Za-z]{2}').match(x)

    lst1 = [str1[i:i+2] for i in range(len(str1) - 1) if is_valid(str1[i:i+2])]
    lst2 = [str2[i:i+2] for i in range(len(str2) - 1) if is_valid(str2[i:i+2])]

    c1, c2 = Counter(lst1), Counter(lst2)
    
    union = len(set(list(set(lst1))+list(set(lst2))))
    inter = len(set(lst1))+len(set(lst2))-len(set(lst1+lst2))
    
    print(inter, union)

    
    return 65536 if union==0 else inter/union*65536