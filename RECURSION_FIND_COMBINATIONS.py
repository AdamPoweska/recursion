def list_of_comb(iterable, num_to_find):
    """
    Returns all possible combinations of num_to_find(int) in given iterable(list).
    """
    def combinations(iterable):
        if len(iterable) == 0: 
            return [[]]
            
        combos = []
        recursive_loop = combinations(iterable[1:])
        for combo in recursive_loop:
            combos += [combo, combo + [iterable[0]]]
        return combos
    
    return [lst for lst in combinations(iterable) if sum(lst) == num_to_find]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
comb_num_to_be_found = 9
print(f"Combinations from {numbers} that sum up to {comb_num_to_be_found} are {list_of_comb(numbers, comb_num_to_be_found)}")

#  Combinations from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] that sum up to 9 are [[4, 3, 2], [5, 3, 1], [5, 4], [6, 2, 1], [6, 3], [7, 2], [8, 1], [9]]