#!/usr/bin/env python3

'''
    Assume you are in a speceship and a unidimensional rain of meteorites 
    is ahead of the spaceship.

    Determine if one or more meteorites will hit the spaceship and 
    the (speed, size) of them.

    The rain of meteorites is represented by a list of pairs: speed and size. 
    --> All speeds are in the same unit system
    --> all masses are in the same unit system.

    A negative speed means approaching (or reducing distance to) spaceship; 
    positive speed means running away from spaceship.

    When two meteorites collide: 
    -  momentums (speed * mass) are compared to determine final direction 
    of colliding results, largest momentum wins
    -  new mass is the absolute value of the difference in masses
    -  new momentum is the difference of the momentums
    -  new speed is the quotient of new momentum divided by new mass
'''
def GetCollisionResult(m1, m2):
    result = (0,0)

def EvaluateAsteroidRain(rain):
    '''
    rain: a list of pairs of speed and mass of meteorites in relative position of the speceship
          rain[0] would be the closest meteorite and rain[n-1] would be the farthest
    '''
    incoming = []
    for i in range(len(rain)-1, -1, -1):
        if not incoming:
            if rain[i][0] >= 0:
                continue

            incoming.append(rain[i])
        else:
            # do something here
            continue


if __name__ == "__main__":
    print("... starting {0}".format(__file__))
