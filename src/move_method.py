import math

tol = 1e-16
car_length=6

def phi(phi_t,theta_t):
    phi=phi_t-math.degrees(math.asin(2 * math.sin(math.radians(theta_t)) / car_length))
    return phi

def x_position(x_t,theta_t,phi_t):
    x=x_t+math.cos(math.radians(theta_t+phi_t))+(math.sin(math.radians(theta_t)))*(math.sin(math.radians(phi_t)))
    if 0<x<tol:
        x=0
    return x

def y_position(y_t,theta_t,phi_t):
    y=y_t+math.sin(math.radians(theta_t+phi_t))-math.sin(math.radians(theta_t))*math.cos(math.radians(phi_t))
    return y
