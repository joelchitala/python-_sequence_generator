from cmath import log
import os
from pickle import TRUE
import utils

GEOMETRIC = "geometric"
SEQUENTIAL = "sequential"
DIFFERENCE = "difference"
DIFFERENTIAL = "differential"

def if_contains_constants(array):
    difference_array = []
    if len(array) > 0:
        difference_array.append(array[0])
        index = 0
        for num in array:
            if index+1 != len(array):
                if utils.getLastValue(difference_array) != array[index+1]:
                    return False
            index+1
        return True
    else:
        return False

def traverser(array,order=SEQUENTIAL):
    traversed_array = []
    traversed_array.append(array)

    if order == SEQUENTIAL:
        recurse = 1
        i = 0
        while recurse > 0:
            temp_array = []
            index = 0
            for num in traversed_array[i]:
                if index+1 != len(traversed_array[i]):
                    temp_array.append(traversed_array[i][index+1] - num)
                index += 1
            traversed_array.append(temp_array)
            if if_contains_constants(traversed_array[i+1]) == False:
                recurse += 1
            recurse -= 1
            i += 1
        
    elif order == GEOMETRIC:
        temp_array = []
        index = 0
        for num in array:
            if index+1 != len(array):
                temp_array.append(array[index+1] / num)
                index += 1
            
        traversed_array.append(temp_array)

    elif order == DIFFERENCE:
        temp_array = []
        index = 0
        for num in array:
            if index+1 != len(array):
                temp_array.append(num-array[index+1])
                index += 1
        traversed_array.append(temp_array)
    elif order == DIFFERENTIAL:
        temp_array = []
        index = 0
        for num in array:
            if index+1 != len(array):
                temp_array.append(array[0]-array[index+1])
                index += 1
        traversed_array.append(temp_array)
    return traversed_array

# traverser([1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795])

def metrics (array,order=SEQUENTIAL):
    os.system('cls||clear')
    traversed_array = traverser(array,order)
    index = 0
    for arr in traversed_array:
        print()
        print(index)
        print(arr)
        index += 1
    
    if order == GEOMETRIC:
        result = traversed_array[1][0]

        index = 1
        for num in traversed_array[1]:
            if index != len(traversed_array[1]):
                result *= num/traversed_array[1][index] 
            index += 1
        print("\nResult")
        print(result)
        print("\nPrevious term:")
        print(traversed_array[0][0]/result)
        print()
        print(traverser(traversed_array[1],GEOMETRIC)[1])

        

        expo_estimator_array = []
        index = 1
        for num in traversed_array[1]:
            if index != len(traversed_array[1]):
                expo_estimator_array.append(log(traversed_array[1][index])/log(traversed_array[1][0]))
            index += 1
        print("\nexponent real estimator")
        real = []
        real.append(1)
        for x in expo_estimator_array:
            real.append(x.real)
        
        print(real)
        
        print("\nreal "+DIFFERENTIAL)
        re_diff = traverser(real,order=DIFFERENTIAL)[1]
        print(re_diff)

        re_diff_di = traverser(re_diff,order=DIFFERENCE)[1]
        print("\nreal "+DIFFERENTIAL+" "+DIFFERENCE)
        print(re_diff_di)

        print("\nreal "+DIFFERENTIAL+" "+DIFFERENCE+" "+GEOMETRIC)
        print(traverser(re_diff_di,order=GEOMETRIC)[1])
    #     print("\nisolated")
    #     isolated = traverser(utils.sorter(real,reverse=True),GEOMETRIC)[1]
    #     print(isolated)

    #     mean = 0

    #     index = 0
    #     for x in isolated:
    #         mean += x
    #         index += 1
    # print("\nMean:")
    # print(mean/len(isolated))
    # print("\nIsol")
    # print(traverser(utils.sorter(isolated,reverse=True),DIFFERENCE)[1])
    # print("\nIsol geometric")
    # reverse = utils.sorter(traverser(isolated,DIFFERENCE)[1])
    # print(utils.sorter(traverser(reverse,GEOMETRIC)[1]))


seq = [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795]
seq_1 = [1.0, 2.8284271247461903, 5.196152422706632, 8.0, 11.180339887498949, 14.696938456699069, 18.520259177452132, 22.627416997969522, 27.0, 31.622776601683793] 
seq_2 = [1.0, 5.656854249492381, 15.588457268119896, 32.0, 55.90169943749474, 88.18163074019441, 129.64181424216494, 181.01933598375618, 243.0, 316.22776601683796] 

metrics([2,11,35,85,175,332],GEOMETRIC)
# metrics(seq,SEQUENTIAL)
