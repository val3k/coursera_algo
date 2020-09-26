def merge(a1, a2, comp_function):
    i = 0
    j = 0
    k = 0
    a = [None for i in range(len(a1) + len(a2))]
    for m in range(len(a)):
        if i > len(a1) - 1:
            a[k] = a2[j]
            k += 1
            j += 1
        elif j > len(a2) - 1:
            a[k] = a1[i]
            k += 1
            i += 1
        elif comp_function(a1[i], a2[j]):
            a[k] = a1[i]
            i += 1
            k += 1
        else:
            a[k] = a2[j]
            j += 1
            k += 1
    return a


def mergesort(a, comp_function=lambda x, y: x <= y):
    if len(a) > 2:
        mid = int(len(a) / 2)
        a1 = a[:mid]
        a2 = a[mid:]
        a1 = mergesort(a1, comp_function)
        a2 = mergesort(a2, comp_function)
        b = merge(a1, a2, comp_function)
        return b
    elif len(a) == 1:
        return a
    elif comp_function(a[0], a[1]):
        return a
    else:
        t = a[0]
        a[0] = a[1]
        a[1] = t
        return a
