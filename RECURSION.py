def combinations(iterable):
    print("recursion iterable:", iterable)
    if len(iterable) == 0: 
        return [[]]
        
    combos = []
    recursive_loop = combinations(iterable[1:])
    for combo in recursive_loop: 
        combos += [combo, combo + [iterable[0]]]
        print()
        print("iterable[0]:", iterable[0])
        print("recursive loop:", recursive_loop)
        print(f"combos += {combo}, {combo} + {[iterable[0]]}")
        print("combos:", combos)
    
    return combos

numbers = [1, 2, 3, 4]
print("Final combinations:", combinations(numbers))
