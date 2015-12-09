from __future__ import print_function
import itertools

verbose = False


# read in the locations and distances from the file
#f = open('inputs/input09_test.txt')
f = open('inputs/input09.txt')

path = {}
locations = []

for line in f:
    lline = line.split()
    city1 = lline[0]
    city2 = lline[2]
    distance = int(lline[4])

    path[city1 + city2] = distance
    path[city2 + city1] = distance

    locations.append(city1)
    locations.append(city2)
f.close()

locations = set(locations)  # find unique locations
if verbose:
    print(locations)
    print(path)


# find shortest route
shortest_route_length = 999999
for route in itertools.permutations(locations):
    route_length = 0
    for city1, city2 in zip(route[:-1], route[1:]):
        route_length += path[city1 + city2]
    if verbose:
        print(route, route_length)
    if route_length < shortest_route_length:
        shortest_route_length = route_length
print("Shortest route length:", shortest_route_length)

# find longest route
longest_route_length = 0
for route in itertools.permutations(locations):
    route_length = 0
    for city1, city2 in zip(route[:-1], route[1:]):
        route_length += path[city1 + city2]
    if verbose:
        print(route, route_length)
    if route_length > longest_route_length:
        longest_route_length = route_length
print("Longest route length:", longest_route_length)
