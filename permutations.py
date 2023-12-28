from itertools import permutations

# Given numbers
numbers = [[20,40],[50,10]]

# Generate all possible permutations

# def generate_permutations(elements):
#     if len(elements) == 0:
#         return [[]]  # Base case: an empty list has one permutation, an empty list

#     all_permutations = []
#     for i in range(len(elements)):
#         current_element = elements[i]
#         remaining_elements = elements[:i] + elements[i + 1:]
#         remaining_permutations = generate_permutations(remaining_elements)

#         for perm in remaining_permutations:
#             all_permutations.append([current_element] + perm)
#     return all_permutations

# Display the permutations
# for perm in all_permutations:
#     print(perm)

def build_customer_coordinates(coordinates):
    customer_coordinates = []
    prev_coordinate = 0
    i = 0

    for coordinate in coordinates:
        if i == 1:
            customer_coordinates.append([prev_coordinate, coordinate])
            prev_coordinate = 0
            i = 0
            continue
        
        prev_coordinate = coordinate
        i += 1

    return customer_coordinates


def calculate_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]) 

def calculate_total_distance(office, home, coordinates):
    shortest_path = float("inf")
    print("office coordinate:",office)

    for path in coordinates[1:]:
        start_distance = calculate_distance(office, path[0])
        total_size_home = calculate_distance(path[-1], home)
        print("PATH: ", path)
        print("start_distance",start_distance)
        print("total_size_home",total_size_home)

        size = sum(calculate_distance(path[i], path[i+1]) for i in range(len(path)-1))
        total_distance = start_distance + size + total_size_home
        print("total_distance",total_distance)
        print("-")

        if total_distance < shortest_path:
            shortest_path = total_distance

    return shortest_path

def process_input():
    test_cases = 10

    for test_case in range(1, test_cases + 1):
        total_customer = int(input().strip())
        coordinates = list(map(int, input().strip().split()))

        office = coordinates[:2]
        home = coordinates[2:4]
        customer_coordinates = build_customer_coordinates(coordinates[4:])
        all_permutations = list(permutations(customer_coordinates))
        print()
        print(all_permutations)

        shortest_distance = calculate_total_distance(office, home, all_permutations)

        print("shortest_distance",shortest_distance)

if __name__ == "__main__":
    process_input()