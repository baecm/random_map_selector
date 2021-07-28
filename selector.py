import yaml
import random
from argparse import ArgumentParser
from functools import reduce


def main():
    parser = ArgumentParser()
    parser.add_argument('--version', default='default', help='Map pool version, such as \'cog2021\' (default: default)')
    args = parser.parse_args()

    print('version: ', args.version)

    with open('config.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    config = config[args.version]
    assert sum(config['ratio']) == 1.0

    print('============== Seed Numbers ==============')
    for i, (k, v) in enumerate(config['seeds'].items()):
        print('{:>2}. {:<16}: {:>20}'.format(i+1, k, v))
    print('==========================================')

    xor_seed = reduce(lambda x, y: x ^ y, list(config['seeds'].values()))
    print('xor_result(random seed) >> {:>15}'.format(xor_seed))
    random.seed(xor_seed)

    pool = config['pool']
    maps2p = random.sample(pool['maps2p'], k=int(config['num'] * config['ratio'][0]))
    maps3p = random.sample(pool['maps3p'], k=int(config['num'] * config['ratio'][1]))
    maps4p = random.sample(pool['maps4p'], k=int(config['num'] * config['ratio'][2]))

    chosen_map_set = set(maps2p + maps3p + maps4p)

    assert len(chosen_map_set) == config['num']
    print('\nSelected Maps >> {}'.format(sorted(chosen_map_set)))


if __name__ == '__main__':
    main()
