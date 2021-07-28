import yaml
import random
from argparse import ArgumentParser
from functools import reduce


def main():
    parser = ArgumentParser()
    parser.add_argument('--version', default='default', help='Map pool version, such as \'cog2021\' (default: default)')
    args = parser.parse_args()

    with open('config.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    config = config[args.version]
    assert sum(config['ratio']) == 1.0

    with open(config['pool'], 'r') as f:
        pool = yaml.load(f, Loader=yaml.FullLoader)

    xor_seed = reduce(lambda x, y: x ^ y, config['seeds'])
    random.seed(xor_seed)

    maps2p = random.sample(pool[args.version]['maps2p'], k=int(config['num'] * config['ratio'][0]))
    maps3p = random.sample(pool[args.version]['maps3p'], k=int(config['num'] * config['ratio'][1]))
    maps4p = random.sample(pool[args.version]['maps4p'], k=int(config['num'] * config['ratio'][2]))

    chosen_map_set = set(maps2p + maps3p + maps4p)

    assert len(chosen_map_set) == config['num']
    print(sorted(chosen_map_set))


if __name__ == '__main__':
    main()
