# random_map_selector
Just random map selector from map pool for IEEE CoG StarCraft AI competition

> __Requirements__
> - pyyaml


__Usage__
~~~
$ map_selector.py --seeds [SEEDS ...] [--num NUM] [--ratio RATIO] [--pool POOL] [--version VERSION]
~~~
__Example__
~~~
$ map_selector.py --seeds 1 2 3 4 5 --version cog2021
['(2)Destination1.1', '(3)Alchemist1.0', '(3)TauCross1.1', '(4)Andromeda1.0', '(4)CircuitBreakers1.0']
~~~

