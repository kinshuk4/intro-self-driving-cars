from math import sqrt
from queue import PriorityQueue

def shortest_path(M,start,goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    explored = {start:None}
    
    g_cost = {start:0}
    h_cost = {start:heuristic(start, goal, M.intersections)}
    
    while not frontier.empty():
        current_cost, current = frontier.get()
        
        if current == goal:
            break
        
        for neighbour in M.roads[current]:
            neighbour_possible_g_cost = f_cost(current, neighbour, M.intersections, g_cost)
            
            if neighbour not in g_cost or (neighbour_possible_g_cost < g_cost[neighbour]):
                g_cost[neighbour] = neighbour_possible_g_cost
                f_cost_val = f_cost(neighbour, goal, M.intersections, g_cost)
                frontier.put((f_cost_val,neighbour))
                explored[neighbour] = current     
    return reconstruct_path(explored, start, goal)

def reconstruct_path(explored, start, goal):
    path = []
    current = goal
    path.append(current)
    while current is not start:
        current = explored[current]
        path.append(current)
    path.reverse()
    return path

def f_cost(node, goal, intersections, g_cost):
    f_cost = g_cost[node] + heuristic(node, goal,intersections)
    return f_cost
    
def heuristic(node, goal, intersections):
    return euclid_distance(intersections[node], intersections[goal])

def euclid_distance(node1_coord, node2_coord):
    x1,y1 = node1_coord[0], node1_coord[1]
    x2,y2 = node2_coord[0], node2_coord[1]
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )