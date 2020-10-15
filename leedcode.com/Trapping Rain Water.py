# https://leetcode.com/problems/trapping-rain-water/
def trap( height ):
    reverse= height[ ::-1 ]
    free=sum( height )
    for i in range( len( height ) - 1 ):
        if height[i ]>height[ i + 1 ]:
            height[ i + 1 ]=height[i ]
        if reverse[i]>reverse[i+1]:
            reverse[i+1]=reverse[i]
    full=sum( [ min(i,j) for i,j in zip( height , reverse[ ::-1 ] ) ] )
    return full-free


# pool=[0,1,0,2,1,0,1,3,2,1,2,1] # 6
pool=[0,1,3,0,2,1,3,1,0,3,1,0,1,1,2] #16
print(trap(pool))