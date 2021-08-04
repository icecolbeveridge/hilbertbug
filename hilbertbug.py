import collections

def hilbert_iteration(s):
    s = s.lower()
    # copy-pasted from Wikipedia: https://en.wikipedia.org/wiki/Hilbert_curve#Representation_as_Lindenmayer_system
    s = s.replace("a", "+BF−AFA−FB+").replace("b", "−AF+BFB+FA−") 
    return s

DIRNS = {
    0: (1,0),
    90: (0,1),
    180: (-1,0),
    270: (0,-1)
}
  
def edges(h):
    edges_ = collections.defaultdict(str)
    dirn = 0
    X,Y = 0,0
    while h:
        c, *h = h
        if c == "+":
            dirn += 90
        elif c == "-":
            print (dirn)
            dirn -= 90
            print (dirn)
        elif c == "F":
            dirn = dirn % 360
            dX, dY = DIRNS[dirn]
            nX = X + dX
            nY = Y + dY
            edges_[ frozenset([(X,Y),(nX,nY)])] = ">"
            X,Y = nX, nY      
    return edges_
    
h = "A"
h = hilbert_iteration(h)
h = hilbert_iteration(h)
E = edges(h)
print(E) # the indices should be between (0,0) and (3,3) -- but aren't!
