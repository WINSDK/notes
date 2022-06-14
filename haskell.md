<p>
sqrt :: Floating a => a -> a
sqrt for example expects a float, take's a value and returns a value.

$ expr     == (expr)
f <$> expr == fmap f (expr)
</p>

**create list**
```haskell
1 : 2 : 3 : 4 : []
[1, 2, 3, 4]
```

gotta remember lists are singly linked and immutable.

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

**list except x first elements of list**
```haskell
drop x list
```

**check if value is in list
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
