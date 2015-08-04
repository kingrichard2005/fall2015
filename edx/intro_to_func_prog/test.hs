--eDx 

--Ch1 & Ch2
-- First steps and Types and classes
double x = x + x
quadruple x = double (double x)

factorial n = product [1..n]
average ns = sum ns `div` length ns

n = a `div` length xs
    where
      a  = 10
      xs = [1,2,3,4,5]
      
--Ch3
-- Guards, defining functions and lambda expressions
myabs n | n >= 0    = n
        | otherwise = -n
        
mysignum n  | n < 0     = -1
            | n==0      = 0
            | otherwise = 1
            
(&&) :: Bool -> Bool -> Bool
True && True  = True
_   &&  _     =  False
--pt 2
add = \x -> (\y -> x + y)

my_const x = \_ -> x


--notes: lambda expression in HAskell
my_odds n = map (\x -> x*2 + 1) [0..n-1]

--Ch4 - list comprehensions
-- note: can't have 'naked' expressions in Haskell scripts, i.e. 
-- examples that are not functions
--ex 1:
--[x^2 | x <- [1..5]]

--ex 2:
--[(x,y) | x <- [1..5], y <- [4..5] ]

--ex 3:
--[(x,y) | x <- [1..3], y <- [x..5] ]

--ex 4:
-- notes: list comprehension applied to function definition
concat      :: [[a]] -> [a]
concat xss  = [x | xs <- xss, x <- xs ]
--concat [[1,2,3], [4,5], [6]]

--ex 5: using Guards, analogous to TSQL WHERE clause or LINQ statement's predicate parameter
--[x | x <- [1..10], even x]

--ex 6: factors 
factors :: Int -> [Int]
factors n = [x | x <- [1..n], n `mod` x == 0]

--ex 7: prime, uses factors 
prime :: Int -> Bool
prime n = factors n == [1,n]

--ex 7: primes (not the most efficient but helps build intuition), uses factors 
primes :: Int -> [Int]
primes n = [x | x <- [2..n], prime x]

-- Left off: starting vid Ch4 Part 2