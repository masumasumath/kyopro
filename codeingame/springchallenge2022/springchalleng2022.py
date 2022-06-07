import sys
import math
import random
from enum import Enum
from operator import itemgetter

#Calc the distance between (x1,y1) and (x2,y2)
def dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)

class NO(Enum):
    ID = 0
    X = 1
    Y = 2
    SHIED = 3
    CONTROL = 4
    HEALTH = 5
    VX = 6
    VY = 7
    NEAR = 8
    THREAT = 9
    BASE_D = 10
    TARGET = 11

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# base_x: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
heroes_per_player = int(input())  # Always 3
enemy_base_x, enemy_base_y = 17630-base_x, 9000 - base_y
#ターゲットにするMonsterのid
target_cor = []

#baseを狙っているmonsterの数
threat_cnt = 0

#Heros Infomations
HERO = []

#baseに最も近いモンスターの情報
MON = []

#モンスターを誰かが倒しに向かっているか
flg = False


WAIT = "WAIT"
MOVE = "MOVE"
WIND = "SPELL WIND"
CONTROL = "SPELL CONTROL"
# game loop
while True:
    for i in range(2):
        # health: Each player's base health
        # mana: Ignore in the first league; Spend ten mana to cast a spell
        health, mana = [int(j) for j in input().split()]
    entity_count = int(input())  # Amount of heros and monsters you can see
    for i in range(entity_count):
        # _id: Unique identifier
        # _type: 0=monster, 1=your hero, 2=opponent hero
        # x: Position of this entity
        # shield_life: Ignore for this league; Count down until shield spell fades
        # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
        # health: Remaining health of this monster
        # vx: Trajectory of this monster
        # near_base: 0=monster with no target yet, 1=monster targeting a base
        # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        #print([_id,_type,x,y], file=sys.stderr, flush=True)

        #Hero Infomaetions
        if _type == 1:
            HERO.append([_id,x,y])
        #Monster
        if _type == 0:
            baseD = dist(x,y,base_x,base_y)
            MON.append([_id, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for,baseD])

        #baseに近い順に並べ替える
        MON = sorted(MON, key=itemgetter(NO.BASE_D))

    #ターゲットにする敵を選定
    for i,mon in enumerate(MON):

        #targetにするmonsterの座標を格納
        target_cor.append([mon[NO.X],mon[NO.Y]])

        #baseを狙っているmonsterの数をカウント
        if mon[NO.NEAR] == 1 and mon[NO.THREAT] == 1:
            threat_cnt += 1

    #Heroの行動を決定
    for i,hero in HERO:
        #print(myX,myY, file=sys.stderr, flush=True)
        hero = HERO.pop(-1)
        hx = hero[NO.X]
        hy = hero[NO.Y]

        print(MOVE,target_cor[i][0],target_cor[i][1])

        if threat_cnt >= 4 and mana > 10: 
            print(WIND,enemy_base_x,enemy_base_y)
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)


        # In the first league: MOVE <x> <y> | WAIT; In later leagues: | SPELL <spellParams>;
