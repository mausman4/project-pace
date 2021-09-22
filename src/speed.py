import math
import numpy as np
#g is the gravitational force constant
g = 9.80655

def forceOfGravity(totalSystemWeight, grade):
    fg = g * math.sin(math.atan(grade/100)) * totalSystemWeight
    return fg

def rollingResistance(totalSystemWeight, grade, crr):
    rr = g * math.cos(math.atan(grade/100)) * totalSystemWeight * crr
    return rr

def airResistance(speedKPH, grade, elevation):
    #first, convert speed from kph to m/s
    v = speedKPH / 3.6
    
    #later, perhaps modify to also account for the wind speed/direction
    windV = 0
    #if grade over 2.5%, assumed hoods riding postion @ 0.324 cda
    #if grade below 2.5%, assumed drops riding position @ 0.307 cda
    if grade > 2.5:
        cda = 0.324
    else:
        cda = 0.307
    ar = 0.5 * cda * airDensity(elevation) * (v**2)
    #ar = 0.5 * cda * airDensity(elevation) * ((v + windV)**2)
    return ar

def airDensity(elevation):
    ad = 1.225 * math.exp(-0.00011856 * elevation)
    return ad

def powerRequired(speedKPH, totalSystemWeight, grade, elevation, crr):
    tf = (forceOfGravity(totalSystemWeight, grade) 
    + rollingResistance(totalSystemWeight, grade, crr) 
    + airResistance(speedKPH, grade, elevation))
    v = speedKPH/3.6
    return tf * v

#current iteration of speedAtPower only accounts for air drag
#rolling resistance and force of gravity are unaccounted for
#THIS IS IMPORTANT
def speedKPHAtPower(power, totalSystemWeight, grade, elevation, crr):
    ad = airDensity(elevation)
    rr = rollingResistance(totalSystemWeight, grade, crr)
    fg = forceOfGravity(totalSystemWeight, grade)
    
    if grade > 2.5:
        cda = 0.324
    else:
        cda = 0.307
    
    #equation is:
    #(0.5*cda*ad)*v^3+(fg+rr)*v-pwr = 0
    
    coeff = [0.5*cda*ad, 0, fg+rr, -power]
    print(np.roots(coeff))
    
    kph = 3.6
   
    return kph

s = speedKPHAtPower(100, 80, 0, 0, 0)
print(s)