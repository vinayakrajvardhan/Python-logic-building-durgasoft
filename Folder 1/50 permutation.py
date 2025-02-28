def generate_permutations(lst):
    if len(lst) == 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        current = lst[i]
        rest = lst[:i] + lst[i+1:]
        for p in generate_permutations(rest):
            result.append([current] + p)
    return result

# Test the function
print(generate_permutations([1, 2, 3]))