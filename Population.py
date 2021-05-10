import random
import math
from DNA import DNA
import numpy as np

class Population:
    def __init__(self):
        super(Population).__init__()
        self.population= []
        self.pool = []
        self.generations = 0
        self.done = False
        self.mutationRate = 0.01
        self.targets = []
        self.target = ''
        self.best_match = ''
        self.current = ""
        self.score = 1

    def getFitness(self):
        for dna in self.population:
            dna.getFitness(self.target)

    def generatePopulation(self,size):
        for c in range(size):
            dna = DNA(len(self.target))
            self.population.append(dna)

    def getTargets(self):
        with open("resources/harry_potter.txt",'r') as file:
            for line in file:
                line = line.rstrip()
                self.targets.append(line)

    def naturalSelection(self):
        self.pool = []
        maxFit = 0
        for dna in self.population:
            if dna.fitness > maxFit:
                maxFit = dna.fitness
                self.best_match = "".join(dna.genes)
        if self.targetReached():
            self.done = True
            return
        # pool  = [DNA,DNA,DNA]
        for dna in self.population:
            fitness = self.normalizeData(dna.fitness,maxFit)
            n = math.floor(fitness*100)
            for i in range(n):
                self.pool.append(dna)

    def generation(self):
        for i in range(len(self.population)):
            a = math.floor(random.random()*len(self.pool))
            b = math.floor(random.random() * len(self.pool))
            parentA: DNA = self.pool[a]
            parentB: DNA = self.pool[b]
            child: DNA = parentA.crossover(parentB)
            child.mutation(self.mutationRate)
            self.population[i] = child

    def normalizeData(self,data,max):
        if max > 0:
         return data/max
        return 1

    def targetReached(self):
        if self.best_match == ''.join(self.target):
            return True
        return False
