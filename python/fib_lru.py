import functools
@functools.lru_cache(None)
def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def md(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n%3==0 and n%2==0:
        return min(md(n//2)+1,md(n//3)+1)
    elif n%3==0:
        return md(n//3)+1
    elif n%2==0:
        return min(md(n//2)+1,md(n-1)+1)
    else:
        return md(n-1)+1
    
print(md(84806671))
l=[0,1]
n=8480
for i in range(2,n+1):
        
    if i%3==0:
        k=l[i-2*(i//3)]+1
        
    else:
        k=l[-1]+1
        if      i%2==0:
            k=min(k,l[i//2]+1)
    
    print(i,k)
    l.append(k)
print (l[-1])
#for i in range(9408):
 #   print(i,md(i))
  #  if i%3==0:
   #     print(i,md(i-i//3*2),"-")
