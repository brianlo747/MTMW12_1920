def pressure(force, radius):
    "Calculate the pressure over a circular area of given radius"
    "and force. Returns the pressure"

    from numpy import pi
    # Pressure = force/area
    if radius != 0:
        area = pi*radius**2
        pressure = force/area
        print('pressure = ', pressure)
    else:
        print('error, cannot calculate pressure over \
                a zero radius circle')

pressure(force=10, radius=1e-164)
