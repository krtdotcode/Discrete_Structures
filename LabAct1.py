# Cayaga, Kurt Joshua P.
# 2CS-A

def main():
    setA = {1, 2, 3}
    setB = {2, 3, 4}

    print("Exercise 1:")
    exercise1(setA, setB)

    print("\nExercise 2:")
    exercise2(setA, setB)

    print("\nExercise 3:")
    exercise3(setA, setB)

    print("\nExercise 4:")
    exercise4(setA, setB)

    print("\nExercise 5:")
    exercise5(setA, setB)

    print("\nExercise 6 (Recursive):")
    print("P(A): ", [list(subset) for subset in exercise6_Recursive(set(setA))])
    print("P(B): ", [list(subset) for subset in exercise6_Recursive(set(setB))])

    print("\nExercise 6 (Iterative):")
    print("P(A): ", [list(subset) for subset in exercise6_Iterative(set(setA))])
    print("P(B): ", [list(subset) for subset in exercise6_Iterative(set(setB))])

    P = True
    Q = False
    print("\nExercise 7:")
    exercise7(P, Q)

def exercise1(setA, setB):
    print(f"Set A: {setA}")
    print(f"Set B: {setB}")

def exercise2(setA, setB):
    print(f"Union of Set A and Set B: {setA.union(setB)}")

def exercise3(setA, setB):
    print(f"Intersection of Set A and Set B: {setA.intersection(setB)}")

def exercise4(setA, setB):
    print(f"Difference of Set A and Set B (A - B): {setA.difference(setB)}")

def exercise5(setA, setB):
    print(f"Is Set A a subset of Set B? {setA.issubset(setB)}")

def exercise6_Recursive(s):
    if not s:
        return [set()]
    
    elem = s.pop()
    subsets = exercise6_Recursive(s)

    newSubsets = [subset.union({elem}) for subset in subsets]

    return subsets + newSubsets

def exercise6_Iterative(s):
    s_list = list(s)
    size = 2 ** len(s_list)
    powerSet = []

    for i in range(size):
        subset = {s_list[j] for j in range(len(s_list)) if (i >> j) & 1}
        powerSet.append(subset)

    return powerSet

def exercise7(P, Q):
    print(f"P AND Q: {P and Q}")
    print(f"P OR Q: {P or Q}")
    print(f"NOT P: {not P}")

main()
