# random_map_selector
Random map selector from map pool for IEEE CoG StarCraft AI competition

__Usage__
~~~
$ selector.py [--version VERSION]
~~~
__Example__

___default___
~~~
$ selector.py --version default
============== Seed Numbers ==============
 1. example_seed_1  :                12345
 2. example_seed_2  :                23456
 3. example_seed_3  :                34567
==========================================
xor_result(random seed) >>           60574

Selected Maps >> ['(2)MatchPoint1.3', '(3)Alchemist1.0', '(3)TauCross1.1', '(4)Andromeda1.0', '(4)FightingSpirit1.3']


Selected Maps >> ['(2)MatchPoint1.3', '(3)Alchemist1.0', '(3)TauCross1.1', '(4)Andromeda1.0', '(4)FightingSpirit1.3']
~~~

___CoG 2021___ 
~~~
$ selector.py --version cog2021
version:  cog2021
============== Seed Numbers ==============
 1. CUNYbot         :           4534125834
 2. Stardust        :                   87
 3. McRave          :                   15
 4. BananaBrain     :                   37
 5. Granite         :                  777
 6. Microwave       :                 7777
==========================================
xor_result(random seed) >>      4534130719

Selected Maps >> ['(2)RideofValkyries1.', '(3)GreatBarrierReef1.0', '(3)NeoAztec2.1', '(4)NeoSniperRidge2.0', '(4)Python1.3']
~~~

