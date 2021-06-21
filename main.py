import itertools
import random

mapPool = {
    'maps2': [
        "(2)BlueStorm1.2",
        "(2)Destination1.1",
        "(2)Hitchhiker1.1",
        "(2)MatchPoint1.3",
        "(2)NeoChupungRyeong2.1",
        "(2)NeoHeartbreakerRidge",
        "(2)RideofValkyries1.0"
    ],
    'maps3': [
        "(3)Alchemist1.0",
        "(3)GreatBarrierReef1.0",
        "(3)NeoAztec2.1",
        "(3)Pathfinder1.0",
        # "(3)Plasma1.0",
        "(3)TauCross1.1"
    ],
    'maps4': [
        "(4)Andromeda1.0",
        "(4)ArcadiaII2.02",
        "(4)CircuitBreakers1.0",
        "(4)FightingSpirit1.3",
        "(4)LunaTheFinal2.3",
        "(4)NeoSniperRidge2.0",
        "(4)Python1.3"
    ]
}

# SEED = 1337
SEED =  seed1 ^
        seed2 ^
        seed3 ^
        seed4 ^
        seed5 ^
        ...
        seedN

mapSet = set()
random.seed(SEED)

while len(mapSet) < 1:
    mapSet.add(mapPool['maps2'][random.randint(0, len(mapPool['maps2'])) % len(mapPool['maps2'])])
while len(mapSet) < 3:
    mapSet.add(mapPool['maps3'][random.randint(0, len(mapPool['maps3'])) % len(mapPool['maps3'])])
while len(mapSet) < 5:
    mapSet.add(mapPool['maps4'][random.randint(0, len(mapPool['maps4'])) % len(mapPool['maps4'])])

print(sorted(mapSet))