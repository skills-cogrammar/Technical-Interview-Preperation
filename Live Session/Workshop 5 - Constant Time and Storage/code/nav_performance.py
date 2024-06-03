from timeit import timeit
import navigation
import random

def run(function_a, function_b, args_a: tuple):
    performance_a = []
    performance_b = []
    iterations = 500

    for i in range(1):
        performance_a.append(timeit(lambda: function_a(*args_a), number=iterations))
        performance_b.append(timeit(lambda: function_b(*args_a), number=iterations))

    average_a = sum(performance_a) / len(performance_a)
    average_b = sum(performance_b) / len(performance_b)

    return average_a, average_b

def generate_large_graph(num_nodes, max_edges_per_node):
    graph = {f'node_{i}': [] for i in range(num_nodes)}
    
    for i in range(num_nodes):
        num_edges = random.randint(1, max_edges_per_node)
        connections = random.sample(range(num_nodes), num_edges)
        connections = [f'node_{j}' for j in connections if j != i]
        graph[f'node_{i}'] = connections
        
    return graph

    
        
if __name__ == "__main__":
    num_nodes = 1000
    num_edges_per_node = 5
    large_graph = generate_large_graph(num_nodes, num_edges_per_node)
    navigation.map = large_graph

    normal, constant = run(navigation.find_path, navigation.find_path_opt, ('node_998', 'node_2'))

    print('O(n) DS', normal, '\nO(1) DS:', constant)
        

