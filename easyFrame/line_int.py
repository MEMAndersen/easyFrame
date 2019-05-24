import numpy as np


def line_int(m, lower_limit=-1, upper_limit=1):
    """
    line_int(m, dist_1, upper_limit)

    Numerical line integration up to polynomial degree 9.

    Parameters
    ----------
    m : int
        Polynomial degree
    lower_limit : float
        Lower limit of line integral
    upper_limit : float
        upper limit of line integral

    Returns
    -------
    xp : numpy.array of floats
        Integration points
    wp : numpy.array of floats
        Weights
    coords : int
        Number of integration points and weights
    """
    if m <= 1:
        a = 0
        e = 2
        xp = np.array([a])
        wp = np.array([e])
        n = 1
    elif m <= 3:
        a = 0.5773502691896257
        e = 1
        xp = np.array([-a, a])
        wp = np.array([e, e])
        n = 2
    elif m <= 5:
        a = 0
        b = 0.7745966692414834
        e = 0.8888888888888889
        f = 0.5555555555555556
        xp = np.array([a, b, -b])
        wp = np.array([e, f, f])
        n = 3
    elif m <= 7:
        a = 0.3399810435848563
        b = 0.8611363115940526
        e = 0.6521451548625461
        f = 0.3478548451374538
        xp = np.array([-a, a, b, -b])
        wp = np.array([e, e, f, f])
        n = 4
    elif m <= 9:
        a = 0
        b = 0.5384693101056831
        c = 0.9061798459386640
        e = 0.5688888888888889
        f = 0.4786286704993665
        g = 0.2369268850561891
        xp = np.array([a, b, -b, -c, c])
        wp = np.array([e, f, f, g, g])
        n = 5
    else:
        raise Exception('function cannot handle polynomial degree above 9, m was: {}'.format(m))

    # Convert to correct range only if not default range
    if lower_limit != -1 or upper_limit != 1:
        wp = ((upper_limit - lower_limit) / 2) * wp
        xp = lower_limit / 2 * (1 - xp) + upper_limit / 2 * (1 + xp)
    return xp, wp, n


"""
# Test code for function

m = 5
lower_limit = -1
upper_limit = 2

xp, wp, n = line_int(m, lower_limit, upper_limit)
print(xp, wp, n)

f = lambda x: x**2

val = 0
for i in range(n):
    val += wp[i]*f(xp[i])
    print(val)

a = 0.5773502691896257
e = 1
xp = np.array([-a, a])
wp = np.array([e, e])
"""
