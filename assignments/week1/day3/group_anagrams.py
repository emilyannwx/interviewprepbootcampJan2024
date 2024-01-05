
def groupAnagramsSort(strs):
    map1 = {}
    for s in strs:
        t=''.join(sorted(s)) #created a sorted version of the string by using the sorted function on its characters then joins them back togther
        if t in map1: #checks if sorted version is already in map1 
            map1[t].append(s) #if it is then the current string is grouped with the other strings under this key
        else:
            map1[t]=[s]  # otherwise a new key-pair value is added to the dictionary 
    return map1.values()

    #map1.values() returns values
    #map1.keys() returns keys
    #print(map1) returns both


#BIG O
def groupAnagramsSort(strs):
    map1 = {}
    for s in strs: #Big O : n , where n is the size of the list strs
        t=''.join(sorted(s)) #Big O: mlogm, where m is the average length of s
        if t in map1: #Big O: super power maps O(1)
            map1[t].append(s) 
        else:
            map1[t]=[s]  
    return map1.values()

    #time complexity:  O(n*mlogm+m) == O(n*mlogm)
    #space complexity: O(n+m)

def groupAnagramTupleDict(strs):
    map1 = {}
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        if tuple(count) in map1:
            map1[tuple(count)].append(s)
        else:
            map1[tuple(count)]=[s]

    return map1.values()

