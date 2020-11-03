###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cowsList = []
    totalCowsWeight = 0
    cowsCopy = sorted(cows, key=cows.get, reverse=True)    
    while True:
        if cowsCopy == []:
            break
        tempCowsList = []
        totalWeight = 0
        i= 0
        while totalCowsWeight < limit and i < len(cowsCopy):
            maxWeightCow = cowsCopy[i]
            totalWeight += cows[maxWeightCow]
            if totalWeight <= limit:
                tempCowsList.append(maxWeightCow)
                del cowsCopy[i]
            else:
                i += 1
                totalWeight -= cows[maxWeightCow]
        cowsList.append(tempCowsList)
    return cowsList
    


# Problem 2
def brute_force_cow_transport(cows,limit):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    # cowsWeight = list(sorted(cows.values(), reverse=True))
    # print(cowsWeight)

    cowsCopy = sorted(cows, key=cows.get, reverse=True)  
    best_partition = []
    for partition in get_partitions(cowsCopy):
        if best_partition == []:
            for item in partition:
                flag = 0
                cowsWeight = sum([cows[x] for x in item])
                if cowsWeight > limit:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 1:    
                best_partition = partition
        if  len(partition) < len(best_partition):
            for item in partition:
                flag = 0
                cowsWeight = sum([cows[x] for x in item])
                if cowsWeight > limit:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 1:
                best_partition = partition
            
    return best_partition

        
# Problem 3
def compare_cow_transport_algorithms():
    start = time.time()
    # print(greedy_cow_transport(cows, limit))
    print(brute_force_cow_transport(cows, limit))
    end = time.time()
    print(end - start)
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

compare_cow_transport_algorithms()
# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))


