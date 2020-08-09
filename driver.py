from direct_chain import direct_chain
from tree_overflow import tree_overflow
import random
import time
import matplotlib.pyplot as plt


# Insert element into hashtable
def insertElement(table, value):
    startTime = time.time() # Get start time for insert
    table.insert(value)
    endTime = time.time() # Get end time for insert
    return (endTime - startTime) * 1000 # Return time difference in ms


# Simulate function
def sim(n, table):
    averageTimes = []
    averageTime = 0
    insertionTime = 0
    x = 1024

    # Loop for n times
    # Generate a random number for each iteration
    # Calculate insertion time and average times
    for i in range(1, n+1):
        value = random.randint(16385, 65335)
        insertionTime += insertElement(table, value)

        if i == x:
            averageTime = insertionTime / i
            averageTimes.append(averageTime)
            averageTime = 0
            insertionTime = 0
            x += 1024

    return averageTimes

# Plot lines using MatPlotLib
def plotLines(sChain, tree):
    runs = []
    for i in range(1, 9):
        runs.append(1024 * i)
        
    
    plt.plot(runs, sChain, marker = 'o', label = "Separate Chain")
    plt.plot(runs, tree, marker = 'o', label = "Tree", linestyle='dashed')
    plt.title("Average time vs Number of Runs")
    plt.xlabel("Runs")
    plt.ylabel("Time")
    plt.legend()
    plt.show()

def main():
    ht1 = direct_chain(509)
    ht2 = tree_overflow(509)
    table = sim(8192, ht1)
    tree = sim(8192, ht2)

    plotLines(table, tree)

main()

