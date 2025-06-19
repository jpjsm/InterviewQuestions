import weightedrandom

if __name__ == "__main__":
    weightedRandom = weightedrandom.WeightedRandom([
        ("Alpha",   0.1),
        ("Bravo",   0.2),
        ("Charlie", 0.4),
        ("Delta",   0.8),
        ("Echo",    1.6),
        ("Foxtrot", 3.2)
    ])

    labelFrequency_forSearch = {}
    labelFrequency_forAccess = {}
    for i in range(0,100000):
        label = weightedRandom.rnd_bysearch()

        if label not in labelFrequency_forSearch:
            labelFrequency_forSearch[label] = 0

        labelFrequency_forSearch[label] += 1

        label = weightedRandom.rnd_byaccess()

        if label not in labelFrequency_forAccess:
            labelFrequency_forAccess[label] = 0

        labelFrequency_forAccess[label] += 1

    print("Frequencies for random by search")
    for kvp in sorted(labelFrequency_forSearch.items(), key = lambda x: x[1]):
        print(kvp) 

    print("Frequencies for random by access")
    for kvp in sorted(labelFrequency_forAccess.items(), key = lambda x: x[1]):
        print(kvp) 
