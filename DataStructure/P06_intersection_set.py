# Implement a function that finds the intersection of two sets.

def find_intersection(set1, set2):
    intersection = set()
    for element in set1:
        if element in set2:
            intersection.add(element)
    return intersection


# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = find_intersection(set1, set2)
print(intersection)
