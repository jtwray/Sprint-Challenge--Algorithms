#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I


# a) 
##  linear Time O(n)

```
i=[1,2,3,4,5]
a=0
while (a<n*n*n):
    a=a+n*n
```
n=1 while  a< 1**3||1
 - a:0
 - a:1 
#### 1step

n=2 while  a< 2**3||8
 - a:0
 - a:4
 - a:8
#### 2steps

n=3 while  a< 3**3||27
 - a:0
 - a:9
 - a:18
 - a:27
#### 3steps

n=4 while  a< 4**3||64
 - a:0
 -  a:16
 -  a:32
 -  a:48
 -  a:64
#### 4steps

n=5 while  a< 5**3||125
 - a:0
 - a:25
 - a:50
 - a:75
 - a:100
 - a:125
#### 5steps

input n scales with steps

linear Time O(n)


 for loop size n == O(n)
 while loop comparisons happen in constant time O(1),
 while loop itself happens n times= O(n)
 within the while loop more comparisons at 0(1) 

No compounding or nested for loops
the worst case rules
worstcase commplexity is o(n)



# b) 
##  logarithmic Time O(n*log(n)) 

```
 sum = 0
    for i in range(n):  
      j = 1
      while j < n:
        j *= 2
        sum += 1
 sum = 0
```

for i in range(n):  
linear

j = 1
 - constant
 - comparisons run in constant time

while j < n:
 - constant
 - comparison

j *= 2
 - constant 0(1)

 - O(logn)
 - similar to a search
 - j doubles each time
 - essentially halving the distance to n

sum += 1
 - constant  
 - 0(1)
 - operation on one item happens in constant time


n=1 while  j < n  
j:1 
1 step

n=2 while  j< n
j:1 j:2
2 steps

n=3 while  j< n
j:1 j:2 j:4
3 steps

n=4 while  j< n
j:1 j:2 j:4
3 steps

n=5 while  j< n
j:1 j:2 j:4 j:8
4 steps


- input size scales faster than the steps
 
- for input size + 1

- steps increase less than 1

## the worst case is O(n*log(n))

1  2   3  4  5
10 14 18 22 26


# c)
# O(n) linear or 4n+6 

```
 def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    return 2 + bunnyEars(bunnies-1)
```
                                       
/* 
 if else statements take the worst option
 comparisons run at constant time O(1)
 ''return 2 + '' o(1) 
 ''bunnyEars()bc it subtracts 1 each time-- this recursive function will run n times
*/

bunnies = 0
- steps = 1

bunnies =1
- steps = 10
 
bunnies = 2
- steps = 14

bunnies =3
- steps = 18

bunnies = 4
- steps = 22

bunnies =5
- steps = 26

4n+6


drop 4 
    -4n is not significantly worse than n at large scale
 drop the +6
    - integers added or subtracted from the base n dont count toward worst case 
if else statement use the worst case O(1) vs O(n) 
its n
O(n) linear




## Exercise II


### I would use a strategy similar to a Binary Search Tree recursively
## runtime  O(n logn)


n floors/2 starting floor
    drop egg
    breaks?
        floors below?
            current floor /2
            travel down that many floors
            repeat drop egg
        no floors below
            youre done

    doesnt break?
        floors above?
            current floor/2
            travel up that many floors
            repeat drop egg
        no floors above 
            your done





