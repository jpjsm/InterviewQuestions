# Weighted random library
import random
import sys
import math

class WeightedRandom:
    _weightsList = []
    _cummulativeList = []
    _accumulatedWeights = 0
    _minvalue = sys.float_info.max
    _maxvalue = 0.0
    _normalizedWeights = []
    _big_map_of_weights = []

    def __init__(self, labelWeightList) :
        for i in labelWeightList:
            if i[1] <= 0:
                raise ValueError(f"Weights must be greater than zero! --> Weight for '{i[0]}' is {i[1]} <= 0")

            if i[1] < WeightedRandom._minvalue:
                WeightedRandom._minvalue = i[1]

            if i[1] > WeightedRandom._maxvalue:
                WeightedRandom._maxvalue = i[1]

            WeightedRandom._weightsList.append((i[0],i[1]))

            WeightedRandom._accumulatedWeights += i[1]
            WeightedRandom._cummulativeList.append((WeightedRandom._accumulatedWeights, i[0]))

        # Building big map of labels to make rnd_byaccess ~~ BigO(1)
        #
        # if WeightedRandom._minvalue between (0, 1), excluding both ends, we neeed to normalize the weights proportional to the minimum weight
        zValue = 1.0
        if WeightedRandom._minvalue < 1:
            weightScale = 10 ** math.ceil(-math.log(WeightedRandom._minvalue))
            ratio = weightScale * WeightedRandom._minvalue
            zValue = weightScale / ratio

        for i in WeightedRandom._weightsList:
            normalizedWeight = round(i[1]*zValue)
            WeightedRandom._normalizedWeights.append((i[0], normalizedWeight))
            for _ in range(normalizedWeight):
                WeightedRandom._big_map_of_weights.append(i[0])

    def rnd_bysearch(self):
        n = random.uniform(0, WeightedRandom._accumulatedWeights)

        for i in range(0, len(WeightedRandom._cummulativeList)):
            if n <= WeightedRandom._cummulativeList[i][0]:
                return WeightedRandom._cummulativeList[i][1]

    def rnd_byaccess(self):
        big_map_of_weights_size = len(WeightedRandom._big_map_of_weights)-1
        random_index = random.randint(0, big_map_of_weights_size)
        return WeightedRandom._big_map_of_weights[random_index]