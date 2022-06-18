#METHOD 1: using DFS
# two arrays are made
# 1. visited array, 2. recursive array
#mark all the indices as F in both the arrays.
#mark the current node visited(T) in the visited array
#and mark current node as True in recursion array
#until all the adjecent nodes of a current node is processed 
#keep is marked as true in the recursive array,
#when all the the adjecent nodes is covered, mark it as False
#if we see an adjacent which is visited but it is there in the 
#recursive array then we return true . i.e, cycle exists

#METHOD 2: using Topological sort
#while doing the topological sort, there comes a point when the indegree of vertices
#are not zero, they cannot be pushed into the queue, therefore in this way, it detects a cycle
#so here, we make a count variable, and increase its count everytime we pop an element from queue
#if the count is less than no of vertices: cycle is present