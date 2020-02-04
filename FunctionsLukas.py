'''
Author: Lukas R.
Last edited: 04.02.20

TODO:
* Run often used functions at start
* Comment Code
* Check performance of functions and optimize
'''

classes = [0, 20, 50, 70, 100, 120]
absolute = [3, 12, 6, 5, 4]
average = 0
median = 0
deviation= 0
quantilesX = [0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95]
quantiles = []
relatives = []
midpoints = []


def relativeCalc():
    relativeSum = 0
    relativeSum = sum(absolute)
    for i in absolute:
        relatives.append(i/relativeSum)
    return relatives

def midpointCalc():
    for i in range(len(classes)-1):
      midpoints.append((classes[i]+classes[i+1])/2)
    return midpoints

def averageCalc():
    midpointCalc()
    relativeCalc()
    global average
    for i in range(len(relatives)):
        average = average + (relatives[i] * midpoints[i])
    return average

def medianCalc():
    quantileCalc()
    median = quantiles[3]
    return median

def quantileCalc():
    relativeCalc()

    for quantil in quantilesX:
        m = 0
        i = 0
        r1 = 0
        r2 = 0

        while m < quantil:
            m = m + relatives[i]
            if(m < quantil):
                i += 1
        
        for x in range(i+1):
            if(x == i):
                r1 = r2
            r2 = r2 + relatives[x]
        quantilX = classes[i] + ((quantil-r1)/(r2-r1))*(classes[i+1]-classes[i])
        print(classes[i], quantil, r1, r2)
        quantiles.append(quantilX)

    return quantiles
    #𝑥0,05; 𝑥0,1; 𝑥0,25; 𝑥0,75; 𝑥0,9; 𝑥0,95

def deviationCalc(z): #med; av; NUMBER
    zSum = 0
    if(z == "med"):
        z = medianCalc()
    elif (z == "av"):
        z = averageCalc()
    midpointCalc()
    for i in range(len(absolute)):
        zSum = zSum + (absolute[i]*abs(midpoints[i]-z))
    deviation = (1/sum(absolute))*zSum
    return deviation

print(deviationCalc(35))