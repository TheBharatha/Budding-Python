import numpy as np
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
#Brute force solution, runs out of time for larger arrays
    reps = list()
    counts = list()
    for no in range(int(input())):
        reps.append(str(input()))
    for each in range(len(reps)):
        if reps[each] not in reps[:each]:
            counts.append(reps[each:].count(reps[each]))
    print(len(counts))
    print(*counts)
#Solution using numpy
    reps = np.array(reps)
    uni,uni_count = np.unique(reps,return_counts=True)
    print(len(uni_count))
    print(*uni_count)
