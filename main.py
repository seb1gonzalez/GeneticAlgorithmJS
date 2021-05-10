from Population import Population
import time

# Word wise
def runWordWise(pop,pop_size,full_sentence):
    #run evolution
    for sentence in pop.targets:
        words = sentence.split(" ")
        for word in words:
            index = 0
            pop.population = []
            pop.pool = []
            pop.done = False
            pop.best_match = ''
            pop.target = []
            for char in word:
                pop.target.append(char)

            pop.generatePopulation(200)
            while True:
                pop.getFitness()
                pop.naturalSelection()
                if pop.done:
                    full_sentence += " " +pop.best_match
                    break
                print(pop.best_match)
                pop.generation()
        full_sentence += "\n"
        print(full_sentence)
        time.sleep(3)

# Sentence Wise
def runSentenceWise(pop,pop_size,full_sentence):
    # Run Evolution
    for word in pop.targets:
        pop.target = []
        pop.population = []
        pop.pool = []
        pop.done = False
        pop.best_match = ''
        pop.target = []
        
        count = 0
        for c in word: #create array of chars
            pop.target.append(c)
        pop.generatePopulation(pop_size)
        while True:
            pop.getFitness()
            pop.naturalSelection()
            if pop.done:
                print(pop.best_match)
                full_sentence += " " +pop.best_match
                break
            pop.generation()
            print(pop.best_match)
              
        full_sentence += "\n"
        print(full_sentence)
        time.sleep(3)


if __name__ == '__main__':
    user_in = int(input("Type 1 for word wise [FAST] | 2 for sentence wise [SLOW]\n"))
    # Generate population parameters
    pop = Population()
    pop.getTargets() #must be declared right after Population instantiation
    pop.mutationRate = .6 # recommended [.1 <= x <=.5 ]too high will introduce too many mutations, too low and it will take much longer to finish
    pop_size = 950 # [up to hardware limitations] too high will make it slow but have more variations, too low and it will run very fast but not enough variation
    full_sentence = ''
    
    if user_in == 1:
        runWordWise(pop,pop_size,full_sentence)
    elif user_in == 2:
        runSentenceWise(pop,pop_size,full_sentence)
    
