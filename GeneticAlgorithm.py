import random
import numpy as np
import math
import string

LIGHTBLUE = (30, 144, 255)
WHITE = (255, 255, 255)

class Population:

    def __init__(self,pop_size,mutation_rate):
        self.agents=[]
        self.pop_size=pop_size
        self.mutation_rate=mutation_rate
        for i in range(pop_size):
            self.agents.append(Individual(target))

    def print(self):
        for agent in population.agents:
            print(agent.toString())

    def calculateFitness(self):
        for i in range(pop_size):
            self.agents[i].calculateFitness()

    def selection(self):
        self.agents = sorted(self.agents, key=lambda agent: agent.fitness, reverse=True)
        return self.agents[:int(0.2*self.pop_size)]

    def generate_new_population(self,selectedParents):
        offSpring = []

        for i in range(int((self.pop_size-len(selectedParents))/2)):
            parent1=random.choice(selectedParents)
            parent2=random.choice(selectedParents)
            midPoint=len(parent1.string)/2
            child1=Individual(parent1.target)
            child2=Individual(parent2.target)
            temp1=[]
            temp2=[]
            for i in range(len(parent1.string)):
                if i<midPoint:
                    temp1.append(parent1.string[i])
                    temp2.append(parent2.string[i])
                else:
                    temp1.append(parent2.string[i])
                    temp2.append(parent1.string[i])

            child1.string=''.join(temp1)
            child2.string=''.join(temp2)
            self.mutate(child1,self.mutation_rate)
            self.mutate(child2,self.mutation_rate)
            offSpring.append(child1)
            offSpring.append(child2)
        newGen=selectedParents+offSpring
        self.agents=newGen

    def mutate(self,child,mutation_rate):
        temp = []
        for i in range(len(child.string)):
            if (random.randint(0, 1) <= mutation_rate):
                temp.append(random.choice(string.ascii_letters))
            else:
                temp.append(child.string[i])

        child.string = ''.join(temp)


class Individual:

    def __init__(self,target):
        self.target=target
        self.string = ''.join(random.choice(string.ascii_letters) for x in range(len(self.target)))
        self.fitness = 0
    def toString(self):
        temp = "Word: " + self.string + ", Fitness: " + str(self.fitness)
        return temp
    def calculateFitness(self):
        i=0
        score=0
        for letter in self.string:
            if letter == self.target[i]:
                score+=1
            i+=1

        self.fitness=int(score/len(self.target)*100)


if __name__ == "__main__":

    pop_size = 200
    mutation_rate = 0.01
    target = "stratocaster"
    generations = 5000

    population=Population(pop_size,mutation_rate)
    finished=False


    for i in range(generations):

        population.calculateFitness()
        selectedParents=population.selection()
        population.generate_new_population(selectedParents)

        print(": Generation:",i,population.agents[0].toString())
        # population.print()
        if any(agent.fitness == 100 for agent in population.agents):
            finished = True
            break

    if finished:
        print(population.agents[0].toString())




