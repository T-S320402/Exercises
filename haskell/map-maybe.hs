safeHead :: [a] -> Maybe a
safeTail :: [a] -> Maybe [a]
mapMaybe :: (a -> Maybe b) -> [a] -> [b]

safeHead [] = Nothing
safeHead (x:_) = Just x

safeTail [] = Nothing
safetail (_:xs) = Just xs

mapMaybe _ [] = []
mapMaybe f (x:xs) = 
    case f x of
        Nothing -> mapMaybe f xs
        Just r -> r :mapMaybe f xs

