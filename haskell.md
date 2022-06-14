sqrt :: Floating a => a -> a
sqrt for example expects a float, take's a value and returns a value.

$ expr     == (expr)
f <$> expr == fmap f (expr)

*create list*
```haskell
1 : 2 : 3 : 4 : []
[1, 2, 3, 4]
```

gotta remember lists are singly linked and immutable.

*get item at index*
list !! idx

*first*
head list

*last*
tail list

*everything but the last*
init list

*x first elements of list*
take x list

*list except x first elements of list*
drop x list

*check if value is in list
elem x list

*max value in list*
maximum list

*min value in list*
minimum list

*list in intervals of (x - y) up to z*
[x,y..z]

*infinite list*
[x..]

*infinite list of x*
repeat x

*n number of x's*
replicate x n
