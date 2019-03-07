bound_limit = 10e-8

def logloss(p, y):
    p = max(min(p, 1. - bound_limit), bound_limit)
    return -log(p) if y == 1. else -log(1. - p)