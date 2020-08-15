#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
constant time
O(n)
no for loops

a)
i=[1,2,3,4,5]
a=0
for n in i:
    while (a<n*n*n):
            a=a+n*n
            f' a:{a} |  n:{n }'
' a:0 |  n:1'
' a:1 |  n:1'
' a:5 |  n:2'
' a:9 |  n:2'
' a:18 |  n:3'
' a:27 |  n:3'
' a:43 |  n:4'
' a:59 |  n:4'
' a:75 |  n:4'
' a:100 |  n:5'
' a:125 |  n:5'

with respect to an input of size n to mean im hearing we have a list of length n
we have a for loop running N times
    inside theres a while loop executing on each of the N times
    the while loop has comparisons which run at constant time
    after the while loop are also comparisons again constant time
the worst of all these is the original the while loop will run N times

O(n)


for loop size n == O(n)
    while loop comparisons happen in constant time O(1), while loop itself happens n times= O(n)
    within the while loop more comparisons at 0(1) 

No compounding or nested for loops
the worst case rules
worstcase commplexity is o(n)

















b)
```
b)  sum = 0
    for i in range(n):   // O(n)
      j = 1              // O(1)
      while j < n:       // 0(1)    
        j *= 2           // 0(1)    j doubles each time O(logn)
        sum += 1         // 0(1)
```
sum is irrelevant to the runtime

while loop runtime scales up logtime
but the for loop will still run n times
big o of n
O(n)


























c)```
 def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)   //''return 2 + ''=> o(1) ''bunnyEars() recursive part'' will return the worst case from entire function 
```
## Exercise II

if else use the worst case time complexity

both are constant

it runs for ever if bunnies is considered 'n'
or it runs never if bunnies is !== n bc 'n' isnt used here





