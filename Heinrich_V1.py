
def VarianceCalc (relativeSum,   absolute, midpoints, relatives, classes):
    global variance
    variance =(1/(relativeSum-1))
    varianceCalc = 0
    averageCalc( relativeSum,relatives,midpoints,absolute)
    for i in range(len(absolute)):
        varianceCalc = varianceCalc + ((absolute[i] * (midpoints[i] - average)**2))
    variance = round(variance * varianceCalc,2)
    return variance
def stDeviationCalC():
    standartDeviation= round(variance**(1/2),2)
    return standartDeviation

def GiniCalc(numberClasses, mathusage, relativeSum, classes,absolute, midpoints):
    g = 0
    vpCalc =0
    sp =[0] * numberClasses
    up =[0] * numberClasses
    vp =[0] * numberClasses
    for i in range(len(absolute)):
        up[i]= round((absolute[i] / relativeSum) + up[i-1],2)
    for i in range(len(absolute)):
        sp[i]= round(((absolute[i]*midpoints[i])+sp[i-1]),2)
        vpCalc=sp[i]
    sp.extend(mathusage)
    for i in range(len(absolute)):
        classesmitte = (classes[i] + classes[i+1]) / 2
        vp[i]= round(((absolute[i]*classesmitte)+sp[i-1])/vpCalc,2)
    up.extend(mathusage)
    vp.extend(mathusage)
    for i in range(len(absolute)):
        g= g + (up[i]-up[i-1])*(vp[i]+vp[i-1])
    Ginik= round(1-g,2)              
    return(Ginik)
def empirische_verteilung(classes, absolute,results_empire,midpoints, x_axis):
    re_hau = []
    relativ_add = 0
    relativ_add_array = []
    jumps = []
    midpointCalc(midpoints,classes)
    for i in range(len(absolute)):
        re_hau.append(absolute[i] / sum(absolute)) #Relative Häufigkeiten Ausrechnen
        relativ_add = relativ_add + re_hau[i] #iterative addition zur Speicherung
        relativ_add_array.append(relativ_add) #addierte relative häufigkeiten
        jumps.append(i*4)
    for i in range(len(absolute)+1):
        results_empire.append(0)
        results_empire.append(0)
        results_empire.append(0)
        results_empire.append(0)
    for i in range(len(absolute)):
        j = jumps[i]
        results_empire[j+2] = midpoints[i]
        results_empire[j+5] = relativ_add_array[i]
        results_empire[j+4] = midpoints[i]
        results_empire[j+7] = relativ_add_array[i]
    results_empire[-2] = round(classes[-1]*1.1 ,2)
    print("x-axis",x_axis)
    return results_empire, x_axis
def histogramm(classes, absolute,hoe_brei):
    k_b = []
    re_hau = []
    kl_hoe = []
    for i in range(len(absolute)):
        k_b.append(classes[i+1] - classes[i]) #classesbreiten ausrechnen
        re_hau.append(absolute[i] / sum(absolute)) #Relative Häufigkeiten Ausrechnen
        kl_hoe.append(re_hau[i] / k_b[i]) #classeshöhen
        hoe_brei.append([k_b[i], kl_hoe[i]]) #Höhe und Breite im 2dimensionalen Array
    return kl_hoe, hoe_brei
def relativeCalc(relativeSum, relatives,absolute):
    for i in range (len(absolute)):
        relatives[i] = (round((absolute[i]/relativeSum), 2))
    return relatives
def midpointCalc(midpoints,classes):
    for i in range(len(classes)-1):
        midpoints[i] =(round(((classes[i]+classes[i+1])/2),2))
    return midpoints
def averageCalc( relativeSum,relatives,midpoints,absolute):
    global average
    average = 0
    relativeCalc(relativeSum, relatives,absolute)
    for i in range(len(relatives)):
        average = round(average + (relatives[i] * midpoints[i]),2)
    print("average:",average)
    return average
def medianCalc(quantilesX, relativeSum,quantiles,relatives,classes,absolute):
    quantileCalc(quantilesX, relativeSum,quantiles,relatives,classes,absolute)
    median = round(quantiles[3],2)
    return median
def quantileCalc(quantilesX,relativeSum,quantiles,relatives,classes,absolute):
    relativeCalc(relativeSum, relatives,absolute)
    mz= 0
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
        quantiles[mz] =(round((quantilX),2))
        mz += 1
    return quantiles
    #𝑥0,05; 𝑥0,1; 𝑥0,25; 𝑥0,75; 𝑥0,9; 𝑥0,95
    
def deviationCalc(z, quantilesX,relativeSum,quantiles,relatives,midpoints,classes,absolute): #med; av; NUMBER
    zSum = 0
    if(z == "med"):
        z = medianCalc(quantilesX, relativeSum,quantiles,relatives,classes,absolute)
    elif (z == "av"):
        z = averageCalc(relativeSum,relatives,midpoints,absolute)
    midpointCalc(midpoints,classes)
    for i in range(len(absolute)):
        zSum = zSum + (absolute[i]*abs(midpoints[i]-z))
    deviation = round((1/sum(absolute))*zSum ,2)
    return deviation
def Call(cl, ab, z):
    classes = cl
    absolute = ab
    numberClasses = (len(absolute))
    quantilesX = [0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95]
    numberQuantiles=len(quantilesX)
    mathusage=[0]
    relativeSum = sum(absolute)
    quantiles = [0] * numberQuantiles
    relatives = [0] * numberClasses
    midpoints = [0] * numberClasses
    hoe_brei = []
    results_empire = []
    x_axis = round(classes[-1],2)
    histogramm(classes, absolute,hoe_brei)
    empirische_verteilung(classes, absolute,results_empire,midpoints,x_axis)
   
    Mathdict = { 
        "midpoints" : midpointCalc(midpoints,classes),
        "median" : medianCalc(quantilesX,relativeSum,quantiles,relatives,classes,absolute),
        "quantiles" : quantileCalc(quantilesX, relativeSum,quantiles,relatives,classes,absolute),
        "deviation" : deviationCalc(z, quantilesX, relativeSum,quantiles,relatives,midpoints,classes,absolute),
        "variance" : VarianceCalc (relativeSum, absolute, midpoints, relatives, classes),
        "standart deviation" : stDeviationCalC(),
        "Ginik" : GiniCalc(numberClasses, mathusage,relativeSum,classes,absolute, midpoints) ,
        "Histogramm" : hoe_brei,
        "Empirically" : results_empire,
        "x-axis" : x_axis,
        "average" : averageCalc(relativeSum, relatives,midpoints,absolute),
        "relatives" : relatives 
        }
    print(Mathdict)
    return Mathdict




                        
