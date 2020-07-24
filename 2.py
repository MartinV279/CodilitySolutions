import sys
saved = ''
x_cropped = ''

def full(y, k):
    minn = sys.maxsize
    for i in range(len(y)-k):
        l = compress(y[:i] + y[i+k:])
        if len(l) < minn:
            saved = l
            minn = len(l)
    return saved

def compress(x):
    if (x != '') or x:
        s = x[0]
        count = 1
        out = ''
        for c in x[1:]:
            if (s == c):
                count +=1
            else:
                out = out + str(count if count>1 else '') + s
                count = 1
                s = c
        out = out + str(count if count>1 else '') + s
        return out

###############################TESTS#######################################
compress('ABBBCCDDCCC')
print(full('ABBBCCDDCCC',3))

full('AAAAAAAAAAAAAAAAABXXAAAAAAAAAAAAAAAAAAAAA', 3)
compress('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
compress('A')
compress('')
compress('1')