import time
# ssaha algorithm (hash table)
def ssahaFind(search, query): 

    #compute the lengths only once
    queryLen = len(query)
    searchLen = len(search)

    #This function converts the search string into a hash table.
    #The hash keys are all the possible base pairs.
    #The values stored are all the locations of every non-overlapping base pair in the search string.
    def make_hash(search):
        hash_dict = {} #the hash table will be stored here.
        hash_dict['AA']=[]
        hash_dict['AC']=[]
        hash_dict['AG']=[]
        hash_dict['AT']=[]
        hash_dict['AZ']=[]
        hash_dict['GA']=[]
        hash_dict['GG']=[]
        hash_dict['GC']=[]
        hash_dict['GT']=[]
        hash_dict['GZ']=[]
        hash_dict['TT']=[]
        hash_dict['TA']=[]
        hash_dict['TC']=[]
        hash_dict['TG']=[]
        hash_dict['TZ']=[]
        hash_dict['CC']=[]
        hash_dict['CG']=[]
        hash_dict['CT']=[]
        hash_dict['CA']=[]
        hash_dict['CZ']=[]
        hash_dict['ZZ']=[]
        hash_dict['ZA']=[]
        hash_dict['ZT']=[]
        hash_dict['ZG']=[]
        hash_dict['ZC']=[]
        for i in range(0, searchLen-1, 2): #separate the search string into non-overlapping base pairs and add into the hash table
            if (i == searchLen-1):
                temp_key = search[i] + 'Z' #if searchLen is odd, append a non-ATGC base to prevent any match
            else:
                temp_key = search[i] + search[i+1]
            hash_dict[temp_key].append(i) #We use closed address hashing
        return hash_dict
    
    #Search for the query base pairs using the hash table.
    def search_hash(hash_dict, query):
        #First, we extract all base pairs present in the query string (overlapping pairs are included)
        # and store them in the keys list.
        keys=[]
        for i in range(0,queryLen-1):
            k = query[i] + query[i+1]
            keys.append(k)
        
        #Next, we get the locations of each query key in the search string
        # and store them in the hits list along with their respective offsets.
        #The offset stores the location of the key with respect to the location of the query.
        #If the key found indicates the location of the query, the query would be found at
        # the key location minus the offset.
        hits=[]
        keys_size = len(keys)
        hits_size = 0
        for t in range(0,keys_size):
            h = hash_dict[keys[t]] #gets all the locations that key appears in search
            if (len(h) > 0):
                hits.append([h,t]) #the index of hits is equal to t, the offset
                hits_size += 1
        return hits,hits_size

    #Check if the locations in hits represent actual locations of the query.
    #Returns a list of query location if found.
    #If not found, returns -1.
    def getFinalLocations(hits, hits_size):
        consecutive = [] #locations where needsCons number of the same location is referenced by hits and its offsets
        consecutive2 = [] #locations where (needsCons-1) number of the same location is referenced by hits and its offsets
        needsCons = queryLen//2
        counts = [0] * searchLen #counts the number of times a location is referenced by hits and its offsets
        consecutiveLen = 0 #number of locations found in consecutive = number of locations deleted from consecutive2
        for item in hits:
            t = item[1] #the offset
            for h in item[0]:
                counts[h-t] += 1 #h-t is the location of the first base of the query, if h indeed indicates the presence of the query
                if (counts[h-t] == needsCons):
                    consecutive.append(h-t)
                    for c in range(0,len(consecutive2)): #h-t would have been included in consecutive2 already, so we need to remove it
                        if (consecutive2[c] == h-t):
                            consecutive2[c] = -1
                            consecutiveLen += 1
                elif (counts[h-t] == needsCons-1):
                    consecutive2.append(h-t)
        
        foundQuery = []
        if (queryLen%2 == 0): #if even query length
            if (consecutiveLen > 0): #if no overlap
                foundQuery.extend(consecutive) #these are all valid locations
            if (len(consecutive2)>(0+consecutiveLen)): #if overlap
                for loc in consecutive2: #check the first and last bases in the query
                    if ((loc != -1) and (loc >= 0 and search[loc] == query[0]) and (loc <= (searchLen-queryLen) and search[loc+queryLen-1] == query[queryLen-1])):
                        foundQuery.append(loc)
            if (len(foundQuery) > 0): #query is found in the search string
                return foundQuery
            else: #query does not exist in the search string
                return -1
        else: #if odd query length
            #There are 2 cases - (1)overlooked first base of query, (2)overlooked last base of query
            for loc in consecutive: #check that first and last bases match
                if (loc >= 0 and search[loc] == query[0]) and (loc <= (searchLen-queryLen) and search[loc+queryLen-1] == query[queryLen-1]):
                    foundQuery.append(loc)
            if (len(foundQuery) > 0): #query is found in the search string
                return foundQuery
            else: #query does not exist in the search string
                return -1
        

    print("start ssaha")
    start = time.perf_counter()
    hash_dict = make_hash(search)           #make the hash-table
    hits, hits_size = search_hash(hash_dict, query)    #find all query key locations in the search string
    x = getFinalLocations(hits,hits_size)
    stop = time.perf_counter()
    clock = stop-start
    print(clock)
    return x