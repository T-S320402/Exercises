smallest :: (Num a, Ord a) => [a] -> Maybe a
smallest0 :: (Num a, Ord a) => [a] -> a

smallest x = s Nothing x where
    s Nothing [] = Nothing
    s (Just a) [] = Just a
    s Nothing (x:xs) =
        if x > 0
            then s (Just x) xs
            else s Nothing xs
    s (Just a) (x:xs) =
        if x > 0 && x < a
            then s (Just x) xs
            else s (Just x) xs

smallest0 l =
    case smallest l of
         Nothing -> 0
         Just a -> a        
