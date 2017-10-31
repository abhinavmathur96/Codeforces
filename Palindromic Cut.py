from collections import *
n = input()
s = raw_input()
c = Counter(s)
odd = []
even = []
for k in c.keys():
    if c[k]&1:
        odd.append(k)
    else:
        even.append(k)
if len(odd)==0:
    ans = []
    ans_s = ''
    for k in c.keys():
        ans_s = k*(c[k]/2)+ans_s+k*(c[k]/2)
    ans.append(ans_s)
elif len(odd)>(n/3):
    ans = list(s)
else:
    l_each = 1
    a_each = l_each
    while l_each<=n:
        if n%l_each==0 and (n/l_each)%2==len(odd)%2 and len(odd)<=(n/l_each):
            a_each = l_each
        l_each += 2
    a_each = min(n,a_each)
    if a_each==1 or len(odd)>(n/a_each):
        ans = list(s)
    else:
        ans = ['']*(n/a_each)
        mod = n/a_each
        i = 0
        while i<len(odd):
            ans[i] += odd[i]
            c[odd[i]] -=1
            i+=1
        i = len(odd)
        
        even = c.keys()
        eind = 0
        while eind<len(even) and i<(n/a_each-1):
            if c[even[eind]]>0:
                ans[i] += even[eind]
                ans[i+1] += even[eind]
                c[even[eind]] -= 2
            if c[even[eind]]==0:
                eind += 1
            i+=2
        ind = 0
        for k in c.keys():
            while c[k]%2==0 and c[k]>0:
                need = a_each-len(ans[ind%mod])
                have = c[k]
                canbe = min(need,have)
                ans[ind%mod] = (canbe/2)*k+ans[ind%mod]+(canbe/2)*k
                c[k]-=canbe
                if len(ans[ind%mod])==a_each:
                    ind += 1        

print len(ans)
print " ".join(ans)
