def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    cache = []
    time = 0
    
    for city in cities:
        c = city.lower()
        
        if c in cache:
            time += 1
            cache.remove(c)
            cache.append(c)
        else:
            time += 5
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(c)
    return time