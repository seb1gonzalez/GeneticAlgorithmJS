import math
import random
class DNA:
    def __init__(self,size):
        super(DNA).__init__()
        self.genes = []
        self.target = []
        self.fitness = 0
        for i in range(size):
            self.genes.append(self.nextChar())

    def nextChar(self):
        storedCharacters = " -'KLMNOPQRSTUVWXYZmnopqrstuvwxyz,. !?&;ABCDEFGHIJabcdefghijkl "
        index = random.randint(0,len(storedCharacters)-1)
        return storedCharacters[index]

    def getFitness(self, target):
        self.target = target
        fit = 0
        for i in range(len(target)):
            if self.genes[i] == target[i]:
                fit += 1
        if len(target)> 0 :
            self.fitness = fit / len(target)
        else:
            self.fitness = 0

    def crossover(self,parent):
        newChild = DNA(len(parent.genes))
        mid = int(math.floor(random.random()*len(self.genes)))
        for i in range(len(self.genes)):
            if i < mid:
                newChild.genes[i] = self.genes[i]
            else:
                newChild.genes[i] = parent.genes[i]
        return newChild

    def mutation(self, rate):
        rand = random.random()
        for i in range(len(self.genes)):
            if rand < rate:
                self.genes[i] = self.nextChar()
