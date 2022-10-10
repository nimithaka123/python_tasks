import itertools
string1=input("enter a string:")
permutation_list=list(itertools.permutations(string1))
for tup in permutation_list:
    print("".join(tup))