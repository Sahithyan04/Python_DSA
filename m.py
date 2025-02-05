def minEatingSpeed( piles, h) :
        k = 1
        while sum([i/k for i in piles]) == h:
            k+=1
        return k
piles = [1,2,3,5,7,9]
h = 2
print(minEatingSpeed(piles,h))