#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:20:54 2023

@author: r21210010
"""
import os.path
from random import random
import json


class iaMonteCarlo:
    def __init__(self, nbSticks, qJsonPath, piJsonPath):
        self.__nbSticks = nbSticks
        self.__qJsonPath = qJsonPath
        self.__piJsonPath = piJsonPath

        if(os.path.exists(qJsonPath)):
            with open(qJsonPath, "r") as qJson:
                qJson = json.load(qJson)
            if len(qJson) == 0:
                self.__q = [0, 0]
                self.__q.append([0, 0, 0] * nbSticks - 2)
            else:
                self.__q = qJson

        if(os.path.exists(piJsonPath)):
            with open(piJsonPath, "r") as piJson:
                piJson = json.load(piJson)
            if len(piJson) == 0:
                self.__pi = [0, 0]
                self.__pi.append([0, 0, 0] * nbSticks - 2)
            else:
                self.__q = qJson


        self.__movesPlay = [0, 0]
        self.__movesPlay.append([0, 0, 0] * nbSticks - 2)

        self.__nbGame = 0
        self.__epsilon = 0.8

    def action_choice(self,s):
        if s == 1:
            return 1

        movePlay = None
        while movePlay is None:
            randomNumber = random()

            if randomNumber <= self.__pi[s][0]:
                self.__movesPlay[s][0] = 1
                print("choisi 1")
                movePlay = 1
            elif randomNumber <= self.__pi[s][0] + self.__pi[s][1]:
                self.__movesPlay[s][0] = 1
                print("choisi 2")
                movePlay =  2
            elif len(self.__pi[s]) > 2 and randomNumber <= self.__pi[s][0] + self.__pi[s][1] + self.__pi[s][2]:
                self.__movesPlay[s][0] = 1
                print("choisi 3")
                movePlay = 3

        return movePlay



    def uptade(self,result):
        self.__nbGame += 1
        if not(result):
            for i in range(len(self.__movesPlay)):
                for j in range(len(self.__movesPlay[i])):
                    if self.__movesPlay[i][j] == 1:
                        self.__movesPlay[i][j] = -1

        for i in range(self.__nbSticks):
            for j in range(len(self.__q)):
                self.__q[i][j] = self.__q[i][j] + 1 / self.__nbGame * (self.__movesPlay[i][j] - self.__movesPlay[i][j])

        for i in range(self.__nbSticks):
            for j in range(len(self.__q)):
                if self.__movesPlay[i][j] != 0:
                    if self.__q[i][j] == max(self.__q[i]):
                        self.__pi[i][j] = self.__epsilon / 3 + (1 - self.__epsilon)
                    else:
                        self.__pi[i][j] = self.__epsilon / 3

        self.__movesPlay = [0, 0]
        self.__movesPlay.append([0, 0, 0] * self.__nbSticks - 2)

        if self.__epsilon - 0.00016 > 0:
            self.__epsilon -= 0.00016

        with open(self.__qJsonPath, "w+") as qJson:
            qJson.write(json.dumps(self.__q))

        with open(self.__piJsonPath, "w+") as piJson:
            piJson.write(json.dumps(self.__pi))


