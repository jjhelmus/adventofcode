from __future__ import print_function
from collections import namedtuple

BOSS_HIT_POINTS = 104
BOSS_DAMAGE = 8
BOSS_ARMOR = 1

Item = namedtuple('Item', ['name', 'cost', 'dmg', 'armor'])

WEAPONS = [
    Item('Dagger',        8,     4,       0),
    Item('Shortsword',   10,     5,       0),
    Item('Warhammer',    25,     6,       0),
    Item('Longsword',    40,     7,       0),
    Item('Greataxe',     74,     8,       0),
]
ARMOR = [
    Item('Nothing',       0,     0,       0),
    Item('Leather',      13,     0,       1),
    Item('Chainmail',    31,     0,       2),
    Item('Splintmail',   53,     0,       3),
    Item('Bandedmail',   75,     0,       4),
    Item('Platemail',   102,     0,       5),
]

RINGS = [
    Item('Nothing 1',     0,     0,       0),
    Item('Nothing 2',     0,     0,       0),
    Item('Damage +1',    25,     1,       0),
    Item('Damage +2',    50,     2,       0),
    Item('Damage +3',   100,     3,       0),
    Item('Defense +1',   20,     0,       1),
    Item('Defense +2',   40,     0,       2),
    Item('Defense +3',   80,     0,       3),
]


def does_player_win(player_hit, player_dmg, player_armor,
                    boss_hit, boss_dmg, boss_armor):

    boss_loss_per_turn = player_dmg - boss_armor
    if boss_loss_per_turn < 1:
        boss_loss_per_turn = 1
    player_loss_per_turn = boss_dmg - player_armor
    if player_loss_per_turn < 1:
        player_loss_per_turn = 1

    # the player goes first and gets n+1 turns
    n, remain = divmod(boss_hit, boss_loss_per_turn)
    if remain == 0:
        n -= 1
    if player_loss_per_turn * (n) >= player_hit:
        return False
    return True


min_cost = 999
max_cost = 0
for weapon in WEAPONS:
    for armor in ARMOR:
        for ring1 in RINGS:
            for ring2 in RINGS:

                # cannot own two of the same ring
                if ring1.name == ring2.name:
                    continue

                player_hit = 100
                player_dmg = weapon.dmg + ring1.dmg + ring2.dmg
                player_armor = armor.armor + ring1.armor + ring2.armor
                cost = weapon.cost + armor.cost + ring1.cost + ring2.cost

                if does_player_win(player_hit, player_dmg, player_armor,
                                   BOSS_HIT_POINTS, BOSS_DAMAGE, BOSS_ARMOR):
                    # part a, lowest cost items to win
                    min_cost = min(cost, min_cost)
                else:
                    # part b, highest cost items and still lose
                    max_cost = max(cost, max_cost)
print(min_cost)
print(max_cost)
