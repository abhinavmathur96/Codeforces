from collections import *

def f(w):
    if len(w)==1: return w
    if len(w)==2:
        if w=='oo': return 'u'
        if w=='kh': return 'h'
    l = len(w)
    wn = ''
    for i in range(l-1,-1,-1):
        if w[i]=='u':
            wn = 'oo'+wn
        elif w[i]=='h':
            wn = 'kh'+wn
        else:
            wn = w[i]+wn
    l = len(wn)
    minim = ''
    i = l-2
    last = wn[l-1]
    while i>=0:
        if (wn[i]+last)=='oo':
            last = 'u'
        elif (wn[i]+last)=='kh':
            last = 'h'
        else:
            minim = last+minim
            last = wn[i]
        i-=1
    return last+minim
n = input()
words = []
for i in range(n):
    words.append(raw_input())
dist = set()
for word in words:
    #print word,f(word)
    dist.add(f(word))    
#print dist
print len(dist)
