import numpy as np

def shift_ra(ra, org):
    """
    Shift the right ascension to belong between -180 and 180. 

    Parameters
    ----------
    ra : float
        right ascension
    org : int
        origin of the coordinates

    Returns
    -------
    float
        shifted right ascension
    """
    x = np.remainder(ra + 360 - org, 360)  # shift RA values
    ind = x > 180
    x[ind] -= 360  # scale conversion to [-180, 180]
    x = -x  # reverse the scale: East to the left
    return x