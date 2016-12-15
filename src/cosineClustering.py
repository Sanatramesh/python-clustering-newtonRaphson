"""
For Python iMTech Mid Semester Exam - 26 Sep, 2012
For Question 2
cosineCLustering module - must contain a function with the name 'cluster'

"""

import math

def average(clst,h):
    for word in h:
        if word in clst:
            clst[word]+=h[word]
        else:
            clst[word]=h[word]
    return Normalize(clst)

def Normalize(h):
    total=0
    for word in h:
        total+=h[word]**2
    
    for word in h:
        h[word]/=(math.sqrt(total))
    
    return h

def cluster(fileList, threshold, stopWords, stems):
    """
    Top level function that gets called when this code is tested.
    
    'threshold'- is < 1; two documents are considered close enough if their cosine-distance is not less than this
    'stopWords' - list of words that ought to be ignored
    'stems' - list of word endings that need to be removed to reduce the words to their roots
    """
    clusters = []
    
    
    
    for filename in fileList:
        h={}
        d={}
        f=open(filename,"r")
        words=f.read().lower().split()
        f.close()
        for word in words:
            if word not in stopWords:
                if word[-2:] in stems:
                    word=word[0:-2]
                elif word[-3:] in stems:
                    word=word[0:-3]
                if word in h.keys(): 
                    h[word]+=1
                else:
                    h[word]=1        
        h=Normalize(h)        
        if clusters==[]:
            clusters.append((h,[filename]))
            continue
        for clust in clusters:
            total=0
            for word in clust[0]:
                if word in h:
                    total+=h[word]*clust[0][word]
            
            d[total]=clust                
        
        c=max(d.keys())
        
        if c>threshold:
            clusters[clusters.index(d[c])]=(average(clusters[clusters.index(d[c])][0],h),clusters[clusters.index(d[c])][1]+[filename])
        else:
            clusters.append((h,[filename]))
    clust=[]
    for cls in clusters:
        clust.append(cls[1])
    
    return clust

if __name__ == '__main__':
    print cluster(["data/doc01", "data/doc02"],
                  0.01,
                  ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'do', 'does', 'each', 'for', 'from',
                 'has', 'have', 'how', 'i', 'if', 'in', 'is', 'it', 'its', 'just', 'no', 'not', 'of', 'on', 'or',
                 'such', 'than', 'that', 'the', 'then', 'there', 'they', 'this', 'those', 'to',
                 'was', 'we', 'what', 'when', 'where', 'which', 'who', 'why', 'will', 'with', 'would', 'yes', 'you'],
                  ['ed', 'ly', 'ing'])
