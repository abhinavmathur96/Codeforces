import re
from collections import *
m_words = 0
c = Counter()
l = input()
word = raw_input()
word = word.replace('*','.')
pres = defaultdict(bool)
for i in word:
    if i!='.':
        pres[i] =True
pw = re.compile(word)
m = input()
for i in range(m):
    w = raw_input()
    if pw.match(w):
        #print i
        temp = Counter()
        flag = False
        for j in range(l):
            if word[j]=='.':
                temp[w[j]]=1
                if pres[w[j]]:
                    flag = True
                    break
        if not flag:
            m_words += 1
            c += temp
ans = 0
if m_words==0:
    ans = 0
else:
    for k in c.keys():
        if c[k]==m_words:
            ans += 1
print ans
