'''FranceWithDXHeuristic.py
by Yen-Chu Yu
UWNetID: ayu1998
Student number: 1760258

Assignment 2, in CSE 415, Winter 2020.
January 21, 2020.
Univ. of Washington.

This file augments FranceWithCosts.py with heuristic information,
so that it can be used by an A* implementation.
The particular heuristic is 10 * longitude_difference, or
"the DX heuristic".

'''

from FranceWithCosts import *

LONGITUDE = {'Avignon':48, 'Bordeaux':-6, 'Brest': -45, 'Caen':-4,
             'Calais': 18, 'Dijon':51, 'Grenoble':57, 'Limoges':12,
             'Lyon':48, 'Marseille':53, 'Montpellier':36, 'Nancy':62,
             'Nantes': -16, 'Nice':73, 'Paris':23, 'Rennes': -17,
             'Strasbourg': 77, 'Toulouse':14}

def h(s):
  '''We return an estimate of the horizontal distance
  between s and the goal city.'''

  longitude1 = LONGITUDE[str(s)]  # Use of str means this will work
    # with either states or strings.
  longitude2 = LONGITUDE[str(DESTINATION_CITY)]
  dx = longitude1 - longitude2
  return 10.0 * abs(dx)

# A simple test:
#print(h('Nantes'))
##for s in LONGITUDE.keys():
##  print(s+": "+str(h(s)))
