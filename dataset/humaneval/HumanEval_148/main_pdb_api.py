from typing import *	##line:(1)
def bf(planet1, planet2):	##line:(2)
    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")	##line:(3)
    if planet1 not in planet_names or planet2 not in planet_names or planet1 == planet2:	##line:(4)
        return ()	##line:(5)
    planet1_index = planet_names.index(planet1)	##line:(6)
    planet2_index = planet_names.index(planet2)	##line:(7)
    if planet1_index < planet2_index:	##line:(8)
        return (planet_names[planet1_index + 1: planet2_index])	##line:(9)
    else:	##line:(10)
        return (planet_names[planet2_index + 1 : planet1_index])	##line:(11)

bf("Jupiter", "Neptune") 