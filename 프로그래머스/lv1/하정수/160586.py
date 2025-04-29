def solution(keymap, targets):
    answer = []
    dic = dict()
    
    for str in keymap:
        for i in range(len(str)):
            if str[i] not in dic:
                dic[str[i]] = i+1
            else:
                dic[str[i]] = min(dic[str[i]], i+1)
            
    for str in targets:
        tmp, flag = 0, False
        
        for i in str:
            if i not in dic: 
                flag = True
                break
            tmp += dic[i]
            
        if flag == True:
            answer.append(-1)
        else:
            answer.append(tmp)
            
    return answer
