#brute force algorithm
def bruteFind(search, query):
    print("start brute force")
    ans = []
    found = False 
    searchLen = len(search)
    queryLen = len(query)
    for i in range(0,searchLen): # repeats n times, n = searchLen
        if (search[i] == query[0]):
            found = True
            for j in range(1,queryLen): #repeats m-1 times, m = keyLen
                if ((i+j) >= searchLen or search[i+j] != query[j]): 
                    found = False
                    break
            if found:
                ans.append(i)
                i = i+queryLen #start searching from where the found query stops (to prevent overlapping)
    if (len(ans) > 0):
        return ans
    else:
        return -1