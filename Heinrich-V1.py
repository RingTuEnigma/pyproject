classes = [0, 20, 50, 70, 100, 120]
absolute = [3, 12, 6, 5, 4]
w=len(absolute)
umfang = 0
average = 0
median = 0
deviation= 0
sq = 0
s = 0
quantilesX = [0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95]
q=len(quantilesX)
quantiles = [0] *q
relatives = [0] * w
midpoints = [0] * w
zweck=[0]
hoe_brei = []
results_empire = []
x_achse = 0 
for i in range(len(absolute)):
    umfang += absolute[i]
mittelwert =55.83
def VarianzxAbweichung ():
        sq = (1/(umfang - 1))
        sq2 = 0
        for i in range(len(absolute)):
            classesmitte = (classes[i] + classes[i+1]) / 2
            sq2 = sq2 + ((absolute[i] * (classesmitte - mittelwert)**2))
        sq = round(sq * sq2,2)
        print("Varianz:",sq)
        s = round(sq**(1/2),2)
        print("Standardabweichung:",s)
        return sq, s

def Gini():
    g = 0
    vps =0
    sp =[0] * w
    up =[0] * w
    vp =[0] * w
    for i in range(len(absolute)):
        up[i]= round((absolute[i] / umfang) + up[i-1],2)
    for i in range(len(absolute)):
        classesmitte = (classes[i] + classes[i+1]) / 2
        sp[i]= round(((absolute[i]*classesmitte)+sp[i-1]),2)
        vps=sp[i]
    sp.extend(zweck)
    for i in range(len(absolute)):
        classesmitte = (classes[i] + classes[i+1]) / 2
        vp[i]= round(((absolute[i]*classesmitte)+sp[i-1])/vps,2)
    up.extend(zweck)
    vp.extend(zweck)
    for i in range(len(absolute)):
       g= g + (up[i]-up[i-1])*(vp[i]+vp[i-1])
    Gini= round(1-g,2)              
    print("Gini-Koeefizient:",Gini)
    return(Gini)
def empirische_verteilung(classes, absolute):
    re_hau = []
    class_mids = []
    
    relativ_add = 0
    relativ_add_array = []
    jumps = []

    x_achse = round(classes[-1],2)

    for i in range(len(absolute)):
        class_mids.append((classes[i]+classes[i+1])/2) #classesmitten
        re_hau.append(absolute[i] / sum(absolute)) #Relative Häufigkeiten Ausrechnen
        relativ_add = relativ_add + re_hau[i] #iterative addition zur Speicherung
        relativ_add_array.append(relativ_add) #addierte relative häufigkeiten
        jumps.append(i*4)
    

    for i in range(len(absolute)+1):
        results_empire.append(0)
        results_empire.append(0)
        results_empire.append(0)
        results_empire.append(0)
    
    #print(results_empire)
    for i in range(len(absolute)):
        j = jumps[i]
        results_empire[j+2] = class_mids[i]
        results_empire[j+5] = relativ_add_array[i]
        results_empire[j+4] = class_mids[i]
        results_empire[j+7] = relativ_add_array[i]
    

    results_empire[-2] = round(classes[-1]*1.1 ,2)

    print("empirische :",results_empire)
    print("x-achse",x_achse)
    return results_empire, x_achse



#print(empirische_verteilung(classes, absolute))
def histogramm(classes, absolute):
    
    k_b = []
    re_hau = []
    kl_hoe = []
    
    #flache = 0

    for i in range(len(absolute)):
        k_b.append(classes[i+1] - classes[i]) #classesbreiten ausrechnen
    
        re_hau.append(absolute[i] / sum(absolute)) #Relative Häufigkeiten Ausrechnen
    
        kl_hoe.append(re_hau[i] / k_b[i]) #classeshöhen
    
        hoe_brei.append([k_b[i], kl_hoe[i]]) #Höhe und Breite im 2dimensionalen Array
    
        #flache = flache + ((hoe_brei[i][0]) * (hoe_brei[i][1])) #Überprüpfung Ergebnis ca. 1
    print("kl-höhe",kl_hoe)
    print("histogramm",hoe_brei)
    return kl_hoe, hoe_brei

def relativeCalc():
    relativeSum = 0
    relativeSum = sum(absolute)
    for i in range (len(absolute)):
        relatives[i] = (round((absolute[i]/relativeSum), 2))
    print("relatives:",relatives)
    return relatives
    

def midpointCalc():
    for i in range(len(classes)-1):
      midpoints[i] =(round(((classes[i]+classes[i+1])/2),2))
    print("midpoints:",midpoints)
    return midpoints

def averageCalc():
    midpointCalc()
    relativeCalc()
    global average
    for i in range(len(relatives)):
        average = round(average + (relatives[i] * midpoints[i]),2)
    print("average:",average)
    return average

def medianCalc():
    quantileCalc()
    median = round(quantiles[3],2)
    print("median:",median)
    return median

def quantileCalc():
    relativeCalc()
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
       # print(quantilX)
       # print (x , i)
       # print(classes[i], quantil, r1, r2)
        quantiles[mz] =(round((quantilX),2))
        mz += 1
    print("quantiles:",quantiles)
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
    deviation = round((1/sum(absolute))*zSum ,2)
    print("deviation:",deviation)
    return deviation


def Call():
    VarianzxAbweichung()
    Gini()
    histogramm(classes, absolute)
    empirische_verteilung(classes, absolute)
    relativeCalc()
    midpointCalc()
    averageCalc()
    medianCalc()
    quantileCalc()
    deviationCalc("med")
    
    Mathdict = {
        "midpoints" : midpoints,
        "median" : median,
        "quantiles" : quantiles,
        "deviation" : deviation,
        "variance" : sq,
        "standart deviation" : s,
        "Gini" : Gini ,
        "Histogramm" : hoe_brei,
        "Empirically" : results_empire,
        "x-axis" : x_achse,
        "average" : average,
        "relatives" : relatives 
        }
    print(Mathdict)
    
Call()

                        