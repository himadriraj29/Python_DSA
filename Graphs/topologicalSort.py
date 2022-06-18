#TOPOLOGICAL SORT
#find indegree of every vertices
#indegree is the no of edges coming on a node
#     A(0)    D(0)   edges are from A to B, A to C, D to C and D to E
#    /  \   /   \
#(1)B   C(2)    E(1)
#after finding the indegree we make a queue  //[      ]
#we push elements having indegree = 0  //[ A , D ]
#now pop 1 element from the queue (A), check for its adjecent nodes, 
# and reduce their indegree by 1. and add A to the ans[] // B = 0, C = 1// Q[D], ans[A]
#Again push all the element into the queue having indegree = 0, and reduce indegree of the adjecent element by 1
#repeat these steps until every element is processed.
#ans = [A,D,B,E,C]