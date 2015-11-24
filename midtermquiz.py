# PROBLEM 5

import random, pylab
def oneTrial():
    '''
    Simulates one trial of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns True if all three balls are the same color,
    False otherwise.
    '''
    balls = ['r']*4 + ['g']*4
    chosen_balls = random.sample(balls,3)
    if chosen_balls[0] == chosen_balls[1] == chosen_balls[2]:
        return True
    return False

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    num_true = 0
    for trial in xrange(numTrials):
        if oneTrial() == True:
            num_true += 1
    return float(num_true)/(numTrials)


## problem 6

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel) 
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show() 
                    
# Implement this -- Coding Part 2 of 2
def getLongestRun(l):
    if len(l) == 0: return 0
    current_num = l[0]
    size = 1
    max_size = 1
    for elem in l[1:]:
        if elem == current_num:
            size += 1
            max_size = max(max_size, size)
        else:
            current_num = elem
            size = 1
    return max_size

# print getLongestRun([5, 4, 4, 4, 5, 5, 2, 5]) #3
# print getLongestRun([5,5,5,5,5,6,2]) #5
# print getLongestRun([5,4,1]) #1
# print getLongestRun([]) #0

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longest_run = []
    for i in range(numTrials):
        vals = [die.roll() for v in range(numRolls)]
        longest_run.append(getLongestRun(vals))
    mean, std = getMeanAndStd(longest_run)
    makeHistogram(longest_run, 10, 'longest run size', 'times', None)
    return mean
    

# print getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000) 
# print getAverage(Die([1]), 10, 1000) 
# print getAverage(Die([1,1]), 10, 1000) 
# print getAverage(Die([1,2,3,4,5,6]), 50, 1000) 
# print getAverage(Die([1,2,3,4,5,6,6,6,7]), 50, 1000) 
# print getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000) 