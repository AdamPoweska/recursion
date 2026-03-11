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
print("Final combinations:", list_of_comb(numbers, 9))
