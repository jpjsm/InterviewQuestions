#!/usr/bin/env python3
import random

ValueWeight_Tuple_Array =[
    ('Alabama', 4887871, 4887871),
    ('Alaska', 737438, 5625309),
    ('American Samoa', 55641, 5680950),
    ('Arizona', 7171646, 12852596),
    ('Arkansas', 3013825, 15866421),
    ('California', 39557045, 55423466),
    ('Colorado', 5695564, 61119030),
    ('Connecticut', 3572665, 64691695),
    ('Delaware', 967171, 65658866),
    ('District of Columbia', 702455, 66361321),
    ('Florida', 21299325, 87660646),
    ('Georgia', 10519475, 98180121),
    ('Guam', 165718, 98345839),
    ('Hawaii', 1420491, 99766330),
    ('Idaho', 1754208, 101520538),
    ('Illinois', 12741080, 114261618),
    ('Indiana', 6691878, 120953496),
    ('Iowa', 3156145, 124109641),
    ('Kansas', 2911505, 127021146),
    ('Kentucky', 4468402, 131489548),
    ('Louisiana', 4659978, 136149526),
    ('Maine', 1338404, 137487930),
    ('Maryland', 6042718, 143530648),
    ('Massachusetts', 6902149, 150432797),
    ('Michigan', 9995915, 160428712),
    ('Minnesota', 5611179, 166039891),
    ('Mississippi', 2986530, 169026421),
    ('Missouri', 6126452, 175152873),
    ('Montana', 1062305, 176215178),
    ('Nebraska', 1929268, 178144446),
    ('Nevada', 3034392, 181178838),
    ('New Hampshire', 1356458, 182535296),
    ('New Jersey', 8908520, 191443816),
    ('New Mexico', 2095428, 193539244),
    ('New York', 19542209, 213081453),
    ('North Carolina', 10383620, 223465073),
    ('North Dakota', 760077, 224225150),
    ('Northern Mariana Islands', 55194, 224280344),
    ('Ohio', 11689442, 235969786),
    ('Oklahoma', 3943079, 239912865),
    ('Oregon', 4190713, 244103578),
    ('Pennsylvania', 12807060, 256910638),
    ('Puerto Rico', 3195153, 260105791),
    ('Rhode Island', 1057315, 261163106),
    ('South Carolina', 5084127, 266247233),
    ('South Dakota', 882235, 267129468),
    ('Tennessee', 6770010, 273899478),
    ('Texas', 28701845, 302601323),
    ('U.S. Virgin Islands', 104914, 302706237),
    ('Utah', 3161105, 305867342),
    ('Vermont', 626299, 306493641),
    ('Virginia', 8517685, 315011326),
    ('Washington', 7535591, 322546917),
    ('West Virginia', 1805832, 324352749),
    ('Wisconsin', 5813568, 330166317),
    ('Wyoming', 577737, 330744054),
]

# Building big map of population
big_map_of_population = []
for p in ValueWeight_Tuple_Array:
    for _ in range(0, p[1]):
        big_map_of_population.append(p[0])


def WeightedRandom1():
    r = random.randint(0,ValueWeight_Tuple_Array[-1][2]-1)
    i = 0
    while ValueWeight_Tuple_Array[i][2] < r:
        i += 1

    return ValueWeight_Tuple_Array[i][0]


def WeightedRandom2():
    return big_map_of_population[random.randint(0,ValueWeight_Tuple_Array[-1][2]-1)]


if __name__ == "__main__":
    print("Total Population: {0:,}".format(ValueWeight_Tuple_Array[-1][2]-1))
    sample_counts = { 'WeightedRandom1': dict(), 'WeightedRandom2': dict() }
    WeightedRandom = { 'WeightedRandom1': WeightedRandom1, 'WeightedRandom2': WeightedRandom2 }
    for _ in range(0,330744):
        for RandomFunction in ["WeightedRandom1", "WeightedRandom2"]:
            label = WeightedRandom[RandomFunction]()
        
            if not label in sample_counts[RandomFunction]:
                sample_counts[RandomFunction][label] = 0

            sample_counts[RandomFunction][label] += 1

    states = set()
    for RandomFunction in ["WeightedRandom1", "WeightedRandom2"]:
        states |=set(sample_counts[RandomFunction].keys())

    for label in sorted(states):
        print("{0: <30} {1: 12,} {2: 12,}".format(
            label, 
            sample_counts["WeightedRandom1"][label] if label in sample_counts["WeightedRandom1"] else "-", 
            sample_counts["WeightedRandom2"][label] if label in sample_counts["WeightedRandom2"] else "-"))