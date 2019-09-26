def pressure(force, radius):
    "Calculate the pressure over a circular area of given radius"
    "and force. Returns the pressure"

    from numpy import pi
    # Import system package which defines a small floating point number
    import sys
    eps = sys.float_info.epsilon # see help(sys.float_info)
    area = pi*radius**2
    if abs(area) > eps:
        pressure = force/area
        print('pressure = ', pressure)
    else:
        print('radius = ', radius, ' gives area = ', area, \
        ' which is too small to calculate the pressure')

pressure(force=10, radius=1e-164)
