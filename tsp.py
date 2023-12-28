from itertools import permutations

def calculate_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def calculate_total_distance(path, coordinates):
    total_distance = 0
    for i in range(len(path) - 1):
        customer_a = path[i]
        customer_b = path[i + 1]
        x1, y1 = coordinates[customer_a * 2 + 4], coordinates[customer_a * 2 + 5]
        x2, y2 = coordinates[customer_b * 2 + 4], coordinates[customer_b * 2 + 5]
        total_distance += calculate_distance(x1, y1, x2, y2)
    return total_distance

def find_shortest_path(coordinates):
    total_customers = len(coordinates) // 2
    # customer_indices = list(range(total_customers))
    # print("customer_indices",customer_indices)
    
    shortest_distance = float('inf')
    shortest_path = None

    for path in permutations(coordinates):
        total_distance = calculate_total_distance(path, coordinates)
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = path

    return shortest_distance

def build_graph(start, end, coordinates):
    graph = {}
    i = 1

    for coodinate in coordinates:
        coodinate[start] = []
        if i == 2:
            pass


def create_tsp_graph(coordinates):
    tsp_graph = {}
    total_customers = (len(coordinates) - 4) // 2

    for i in range(total_customers):
        customer_a = i
        x1, y1 = coordinates[customer_a * 2 + 4], coordinates[customer_a * 2 + 5]
        tsp_graph[customer_a] = {}

        for j in range(total_customers):
            if i != j:
                customer_b = j
                x2, y2 = coordinates[customer_b * 2 + 4], coordinates[customer_b * 2 + 5]
                distance = calculate_distance(x1, y1, x2, y2)
                tsp_graph[customer_a][customer_b] = distance

    return tsp_graph



def process_input():
    test_cases = 1
    cus = "30 30 5 5 15 15"

    for test_case in range(1, test_cases + 1):
        total_customer = int(input().strip())
        coordinates = list(map(int, cus.strip().split()))
        # coordinates = list(map(int, input().strip().split()))

        office = (coordinates[0], coordinates[1])
        home = (coordinates[2], coordinates[3])

        customer_order = find_shortest_path(coordinates)
        print(f"#{test_case} {customer_order}")

        # gr = create_tsp_graph(coordinates)
        # print(gr)

# def process_input():
#     test_cases = 10

#     for test_case in range(0, test_cases):
#         total_customer = input().strip()
#         coordinates = input().strip()
#         # coordinates = list(map(int, input().strip().split()))

#         # print(f"#{test_case} {total_customer}")
#         # print(f"coordinates: {coordinates}")

if __name__ == "__main__":
    process_input()