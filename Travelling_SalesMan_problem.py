def shortest_path(graph,start):
    current_node=start
    path=[[0,'A']]
    unvisited=[]
    for node in graph.keys():
        unvisited.append(node)
    unvisited.remove(start)
    while unvisited:
        next_nodes=graph[current_node]
        min_val=999

        for node in next_nodes:
            if(node[1] in unvisited)and (node[0]<min_val):
                min_val=node[0]
                next_node=node
        path.append(next_node)
        print(next_node[1])
        unvisited.remove(next_node[1])
        current_node=next_node[1]
    for ele in graph[current_node]:
        if ele[1]==start:
            path.append([ele[0],start])
    print(path)
    print('shortest distence=',end=" ")
    dis=0
    for i in path:
        dis=dis+i[0]
    print(dis)

graph={'A':[[6,'C'],[8,'D'],[15,'E'],[12,'B']],
       'B':[[12,'A'],[20,'C'],[12,'D'],[10,'E']],
       'C':[[20,'B'],[6,'A'],[15,'D'],[30,'E']],
       'D':[[8,'A'],[12,'B'],[15,'C'],[8,'E']],
       'E':[[15,'A'],[10,'B'],[30,'C'],[8,'D']]}
shortest_path(graph,'A')
        
