--Description: Just a sandbox of Haskell snippets while practicing examples from lecture vids at https://github.com/fptudelft/FP101x-Content
-- Exercise imports
--For Ch4 Pt 2 ex4: 'lowers' implementation
import Data.Char

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


--notes: lambda expression in Haskell
my_odds n = map (\x -> x*2 + 1) [0..n-1]

--Ch4 - Part 1 - list comprehensions
-- note: can't have 'naked' expressions in Haskell scripts, i.e. 
-- examples that are not functions
--ex 1:
-- console ex:> [x^2 | x <- [1..5]]

--ex 2:
-- console ex:> [(x,y) | x <- [1..5], y <- [4..5] ]

--ex 3:
-- console ex:> [(x,y) | x <- [1..3], y <- [x..5] ]

--ex 4:
-- notes: list comprehension applied to function definition
concat      :: [[a]] -> [a]
concat xss  = [x | xs <- xss, x <- xs ]
--console ex:> concat [[1,2,3], [4,5], [6]]

--ex 5: using Guards, analogous to TSQL WHERE clause or LINQ statement's predicate parameter
--console ex:> [x | x <- [1..10], even x]

--ex 6: factors 
factors :: Int -> [Int]
factors n = [x | x <- [1..n], n `mod` x == 0]

--ex 7: prime, uses factors 
prime :: Int -> Bool
prime n = factors n == [1,n]

--ex 7: primes (not the most efficient but helps build intuition), uses factors 
primes :: Int -> [Int]
primes n = [x | x <- [2..n], prime x]

--Ch4 - Part 2 - list comprehensions
--built-in type signature for zip :: [a] -> [b] -> [(a,b)]
--console ex:> zip ['a', 'b', 'c'] [1..5]

--ex2: 'pairs' implementation
pairs :: [a] -> [(a,a)]
pairs xs = zip xs (tail xs)

--ex3: 'sorted' implementation
sorted :: Ord a => [a] -> Bool
sorted xs = 
      and [x <= y | (x, y) <- pairs xs]
--console ex:> sorted [1, 2, 3, 4]
--console ex:> sorted [1, 4, 3, 2]

--ex4: 'positions' implementation
positions :: Eq a => a -> [a] -> [Int]
positions x xs =
   [i | (x', i) <- zip xs [0..n], x == x']
   where n = length xs - 1
--console ex:> positions 0 [1,0,0,1,0,1,1,0]

--ex4: 'lowers' implementation
lowers :: String -> Int
lowers xs =
   length [x | x <- xs, isLower x]
--console ex:> lowers "Haskell"
   
-- Left-off: Chapter 5 Part 1