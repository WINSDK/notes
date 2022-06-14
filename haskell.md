haskell
=====

sqrt :: Floating a => a -> a
sqrt for example expects a float, take's a value and returns a value.

$ expr     == (expr)
f <$> expr == fmap f (expr)
html
#0d1117
## Lists
immutable and singly linked.

**create list**
```haskell
1 : 2 : 3 : 4 : []
[1, 2, 3, 4]
```

**get item at index**
```haskell
list !! idx
```

**first**
```haskell
head list
```

**last**
```haskell
tail list
```

**everything but the last**
```haskell
init list
```

**x first elements of list**
```haskell
take x list
```

**first elements of list while they meet the conditional**
```haskell
takeWhile (<5) list
```

**everything except x first elements of list**
```haskell
drop x list
```

**everything except x first elements of list that meet the conditional**
```haskell
dropWhile (<5) list
```

**check if value is in list**
```haskell
elem x list
```

**max value in list**
```haskell
maximum list
```

**min value in list**
```haskell
minimum list
```

**list in intervals of (x - y) up to z**
```haskell
[x,y..z]
```

**infinite list**
```haskell
[x..]
```

**infinite list of x**
```haskell
repeat x
```

**n number of x's**
```haskell
replicate x n
```

**repeat list infinitely**
```haskell
cycle list
```

**apply operation to each element of an array**
```haskell
foldl (+) 1 2 3 [4 5 6] [7 8 9]
```

**apply operation with joining arrays**
```haskell
zipWith (+) [12..16] [4..8]
zipWith (\a b -> a * b) [1, 2, 3, 4] [5, 6, 7, 8]
```

**list comprehension**
```haskell
[expr | lamba, filter]

[mod x y | x <- [1..10], y <- [10..100], x * 3 < 30, mod y 3 == 0]
```

## Tuples

**create tuple**
```haskell
(a, b, c...)
```

**first part or second part**
```haskell
fst tuple
snd tuple
```
