#zakładam, że slowa skladaja sie od "a-z"
def possible(w1,w2,word):
    nw1 = len(w1)
    nw2 = len(w2)
    n = len(word)

    count = [0 for _ in range(97,123)]
    #ord('a')=97     ord('z')=122
    for i in range(n):
        count[ord(word[i])-97] += 1
    
    for j in range(nw1):
        count[ord(w1[j])-97] -= 1
    
    for k in range(nw2):
        count[ord(w2[k])-97] -= 1

    for c in count:
        if c > 0: return False
    
    return True

print(possible("abc","def","abqdef"))

