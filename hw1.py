#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import numpy as np
import math

def histogram_times(filename):
    import csv
    dataIndex = 10
    with open(filename) as f:
        csv_reader = csv.reader(f)
        airplane_data = list(csv_reader)
    airplane_fatalities = []
    for i in range(24):
        airplane_fatalities.append(0)
    for i in range(1, len(airplane_data)):
        try:
            hour = int(airplane_data[i][1][:2])
            airplane_fatalities[hour] += 1
        except ValueError:
            continue
    return airplane_fatalities

def weigh_pokemons(filename, weight):
    import json
    with open(filename) as f:
        pokedex = json.load(f)
    correctWeight = []
    for i in range(len(pokedex['pokemon'])):
        if (pokedex['pokemon'][i]['weight'] == str(weight) + " kg"):
            correctWeight.append(pokedex['pokemon'][i]['name'])
    return correctWeight

def single_type_candy_count(filename):
    import json
    with open(filename) as f:
        pokedex = json.load(f)
    numCandies = 0
    for pokemon in pokedex['pokemon']:
        if pokemon['candy'] != "None":
            numCandies += 1
        print(pokemon['name'] + ": " + pokemon['candy'])
    return numCandies

def reflections_and_projections(points):
    import numpy as np
    '''
    TODO: WRITE TEST CASES TO TEST
    '''
    # Reflects the points over the line y = 1
    xcoords = points[:,0]
    xcoords -= 1
    xcoords *= -1
    xcoords += 1
    print(points)

    # Rotates pi / 2 radians
    theta = np.pi / 2 
    matrix_to_multiply = np.array([[np.cos(theta), np.sin(theta) * -1], [np.sin(theta), np.cos(theta)]])
    points = np.matmul(matrix_to_multiply, points)
    print(points)

    # Project on the line y = 3x
    m = 3
    projection_matrix = np.array([[1, m], [m, m**2]])
    coefficient = 1/(m**2 + 1)
    print(points)
    
    points = np.matmul(projection_matrix, points) * coefficient
    return points

def normalize(image):
    import numpy as np
    max = np.amax(np.array([np.amax(x) for x in range(len(image))]))
    min = np.amin(np.array([np.amin(x) for x in range(len(image))]))
    coefficient = 255 / (max - min)
    image -= min
    image *= coefficient
    return image

def sigmoid_normalize(image, a):
    return 255*(1+e**((-a)**-1*image-128))**-1

#test_array = np.array([[1, 2], [3, 4]])
print(histogram_times('airplane_crashes.csv'))
#print(weigh_pokemons('pokedex.json', 10.0))
print(single_type_candy_count('pokedex.json'))
#reflections_and_projections(test_array)


#b = [x,y for x in range(10) for y in range(10) if y % 2 == 0]

#image_array = np.arange(32 ** 2).reshape(32, 32)
#print(normalize(image_array))
