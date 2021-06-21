import yaml
import random
from argparse import ArgumentParser
from functools import reduce


def main():
    parser = ArgumentParser()
    parser.add_argument('--seeds', nargs="+", type=int, required=True)
    parser.add_argument('--num', type=int, default=5)
    parser.add_argument('--ratio', type=list, default=[0.2, 0.4, 0.4])
    parser.add_argument('--pool', default='pool.yaml')
    parser.add_argument('--version', default='default', help='Map pool version, such as \'cog2021\' (default: default)')
    args = parser.parse_args()

    assert sum(args.ratio) == 1.0

    with open(args.pool, 'r') as f:
        pool = yaml.load(f, Loader=yaml.FullLoader)

    xor_seed = reduce(lambda x, y: x ^ y, args.seeds)
    random.seed(xor_seed)

    maps2p = random.sample(pool[args.version]['maps2p'], k=int(args.num * args.ratio[0]))
    maps3p = random.sample(pool[args.version]['maps3p'], k=int(args.num * args.ratio[1]))
    maps4p = random.sample(pool[args.version]['maps4p'], k=int(args.num * args.ratio[2]))

    chosen_map_set = set(maps2p + maps3p + maps4p)

    assert len(chosen_map_set) == 5
    print(sorted(chosen_map_set))


if __name__ == '__main__':
    main()
