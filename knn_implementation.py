import csv,random,math,operator
from audioop import reverse
from networkx.classes.function import neighbors

def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for row in range(len(dataset)-1):
            for col in range(4):
                dataset[row][col] = float(dataset[row][col])
            if random.random() < split:
                trainingSet.append(dataset[row])
            else:
                testSet.append(dataset[row])
                
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for i in range(length):
        distance += pow((instance1[i] - instance2[i]), 2)
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for i in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[i], length)
        distances.append((trainingSet[i], dist))
    distances.sort(key=operator.itemgetter(1)) #sort based on distance
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def main():
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataset(r'E:\eclipse\workspace\dataset\iris.data.txt', split, trainingSet, testSet)
    print('Training Set: ' +  repr(len(trainingSet)))
    print('Test Set: ' + repr(len(testSet)))
    
    predictions = []
    k = 3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted = ' + repr(result) + ',actual = ' + repr(testSet[x][-1]))
    accuarcy =getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuarcy) + '%')
    
main()


    
    
    
    
    
        
        
        
    
    
    