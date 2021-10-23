sqrtMaybe :: (Num a, Ord a) => a -> Maybe a

sqrtMaybe n =
    if n < 0 then Nothing else Just (s 1 n)
        where
            s x n = if x * x > n then x - 1 else s (x + 1) n

