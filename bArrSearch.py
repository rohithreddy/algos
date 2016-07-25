## Binary Array Search that breaks the linear behaviour of ordinary linear search
def contains(collection, target):
    """search that uses in keyword provided by Python(default search used most of the time)"""
    return target in collection


def bs_contains(ordered, target):
    """Binary Array Search to determine if target is present in Collection and return the probable Index number
    for Target in Collection if its not present"""
    low = 0
    high = len(ordered) -1
    while low <= high:
        mid = (low + high) / 2
        if target == ordered[mid]:
            return mid
        elif target < ordered[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -(low + 1)


def insertInPlace(ordered, target):
    """Insert the target into sorted collection at appropriate place"""
    idx = bs_contains(ordered, target)
    if idx < 0:
        ordered.insert(-(idx+1), target)
        return
    ordered.insert(idx, target)
