import sys
import fileinput

def table(graph_size, n):
    t = []

    for i in range(graph_size + 1):
        t.append(n) 
    return t

def shortest_path(l, graph_size):
    d = table(graph_size, float('inf'))
    d[1] = 0
    
    for i in range(1, graph_size):
        path_edg = l[i]        
        for j in path_edg:
            if j == None:
                break 
            elif d[i] + 1 < d[int(j)]:
                d[int(j)] = (d[i] + 1)
    return d[graph_size]

def longest_path(l, graph_size):
    d = table(graph_size, -1)
    d[1] = 0

    for i in range(1, graph_size):
        path_edg = l[i] 
        for j in path_edg:
            if j == None:
                break
            elif d[i] + 1 > d[int(j)]:
                d[int(j)] = d[i] + 1
    return d[graph_size]

def num_paths(l, graph_size):
    paths = 0
    tot_path = table(graph_size, 0)
    tot_path[1] = 1

    for i in range(1, graph_size):
        path_edg = l[i] 
        for j in path_edg:
            if j == None:
                break
            else:
                tot_path[int(j)] = tot_path[i] + tot_path[int(j)]
    return tot_path[graph_size]

def main():
    file = fileinput.input()
#   graph_number = int(f.readline().rstrip('\n'))
    for l in file:
        if fileinput.isfirstline():
            graph_number = int(l)
        for i in range(graph_number):
            l=[]
            node = (next(file).strip())
            edge = (next(file).strip())            
            for j in range(int(node)):
                l.append([])
            for k in range(1,(2*int(edge)), 2):
                pos = next(file).strip().split()
                pos1 = pos[0]
                pos2 = pos[1]
                l[int(pos[0])].append(pos[1])
            
            print("graph number:", (i+1))
            print("Shortest path:", shortest_path(l, int(node)))
            print("Longest path:", longest_path(l, int(node)))
            print("Number of paths:", num_paths(l, int(node)))
            print("")

if __name__ == "__main__":
    main()
