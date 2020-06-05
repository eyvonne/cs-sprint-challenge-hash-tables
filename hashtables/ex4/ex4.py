def has_negatives(a):
    cache = {}

    for x in a:
        if x > 0:
            if x in cache:
                cache[x].append(x)
            else:
                cache[x] = [x]
        else:
            if -x in cache:
                cache[-x].append(x)
            else:
                cache[-x] = [x]
    result = [key for key, x in cache.items() if len(x) == 2 and x[0]+x[1] == 0]
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
