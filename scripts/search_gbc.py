import pyprimes


def order(n):
    rtv = 1
    for p, k in pyprimes.factorise(n):
        rtv *= p ** (k * 2) + p ** (k * 2 - 1) + p ** (k * 2 - 2)
    return rtv


def degree(n):
    rtv = 1
    for p, k in pyprimes.factorise(n):
        rtv *= p ** k + p ** (k - 1)
    return rtv


def pair(n):
    return order(n), degree(n)


def bc_order(p, k):
    q = p**k
    return q**2 + q + 1


def bc_degree(p, k):
    q = p**k
    return q + 1


def bc_pair(p, k):
    return bc_order(p, k), bc_degree(p, k)


if __name__ == '__main__':
    rtv = []
    for p in pyprimes.primes_below(100):
        for k in range(2, 10):
            rtv.append((bc_pair(p, k), (p, k)))

    for n in range(2, 1000):
        rtv.append((pair(n), n))

    rtv.sort()
    for r in rtv:
        print(r)
