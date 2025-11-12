#Topological_Sorting
testGraph = {
    'A' : {'B','C'},
    'B' : {'C','D'},
    'C' : {'D'},
    'D' : {},
    'E' : {'C','F'},
    'F' : {'D'}
}

in_degree = {}
zero_list = list() #진입차수 0인 점을 관리할 Deque - Stack을 이용해야 하지만 편의를 위해 Deque
topo_order = list() #위상 순서

def count_in_degree(graph): #진입 차수 카운트
    val_list = list(graph.values()) 
    for key in list(graph.keys()):
        in_degree[key] = 0 #진입 차수 딕셔너리 초기화
    for i in val_list:
        for node in i:
            in_degree[node] += 1
    #print(in_degree)

#DFS를 이용할까, Decrease and Conquer를 이용할까?
#우선 Decrease and conquer

def topological_sort(graph,res):
    count_in_degree(graph)
    zero_list = [key for key,val in in_degree.items() if val==0] #진입차수가 0인 정점만을 zero_list에 넣기
    while zero_list:
        poped = zero_list.pop(0)
        res.append(poped)
        for i in graph[poped]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                zero_list.insert(0,i)
    print(res)

topological_sort(testGraph,topo_order)
