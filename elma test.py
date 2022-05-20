a =[]
b = -1
for i in range(1,101):
    
   a.append(i)

for i in a:
    b+=1
    if i%3==0:
        a[b] = 'FiZZ'
    if i%5==0:
        a[b] = 'BiZZ'
    if i%15==0:
        a[b]='FiZZBiZZ'
print(a)
    
