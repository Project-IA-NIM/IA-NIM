#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:40:54 2023

@author: r21210010
"""

from random import randint
import time

q = [[-0.10000000000000002, -0.05000000000000001, -0.05000000000000001], [0.15000000000000005, 0.0, 0.0], [0.0, 0.39999999999999997, 0.0], [0.0, 0.0, 0.25], [-0.05000000000000001, -0.05000000000000001, -0.05000000000000001], [0.19999999999999998, -0.05000000000000001, 0.0], [-0.05000000000000001, 0.25, 0.0], [0.0, 0.0, 0.35000000000000003], [0.0, 0.0, -0.05000000000000001], [0.0, 0.0, 0.0], [-0.05000000000000001, 0.7000000000000001, -0.05000000000000001]]

def choix_action(l):
    if l[0] == l[1] == l[2]:
        print("choisi aléatoirement")
        return randint(1,3)
    elif max(l) == l[0]:
        print("choisi 1")
        return 1
    elif max(l) == l[1]:
        print("choisi 2")
        return 2
    else:
        print("choisi 3")
        return 3
    
def partie(q):
    iaPerdu = False
    etat = 11
    coupsJouer = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    while(etat >= 1):
        action = choix_action(q[etat - 1])
        coupsJouer[etat -1][action - 1] += 1
        etat -= action
        print(etat)
        time.sleep(0.01)
        
        if(etat >= 1):   
            etat -= int(input("votre coups"))
        elif etat < 1:
            iaPerdu = True
    
    print(iaPerdu)
    if iaPerdu:
        for i in range(len(coupsJouer)):
            for j in range(len(coupsJouer[i])):
                if(coupsJouer[i][j] == 1):
                    coupsJouer[i][j] = -1
    
    return coupsJouer
    
def monte_carlo(q):
    moyenneCoups = q
    for n in range (1,21):
        coupsJouer = partie(moyenneCoups)
        for i in range(len(coupsJouer)):
            for j in range(len(coupsJouer[i])):
                moyenneCoups[i][j] = moyenneCoups[i][j] + 1/n * (coupsJouer[i][j] -   moyenneCoups[i][j])
    return(moyenneCoups)
    

print(monte_carlo(q))
    
