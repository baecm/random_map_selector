import random
from argparse import ArgumentParser
from functools import reduce

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
def main():
    parser = ArgumentParser()
    parser.add_argument('--seeds', nargs="+", type=int)
    args = parser.parse_args()

    xor_seed = reduce(lambda x, y: x ^ y, args.seeds)
    random.seed(xor_seed)

    chosen_map_set = set()
    while len(chosen_map_set) < 1:
        chosen_map_set.add(mapPool['maps2'][random.randint(0, len(mapPool['maps2'])) % len(mapPool['maps2'])])
    while len(chosen_map_set) < 3:
        chosen_map_set.add(mapPool['maps3'][random.randint(0, len(mapPool['maps3'])) % len(mapPool['maps3'])])
    while len(chosen_map_set) < 5:
        chosen_map_set.add(mapPool['maps4'][random.randint(0, len(mapPool['maps4'])) % len(mapPool['maps4'])])

    print(sorted(chosen_map_set))

if __name__ == '__main__':
    main()