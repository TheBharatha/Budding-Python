def repeatedString(s, n):
    lenS = len(s)
    wholeReps = n//lenS
    remainingReps = n%lenS
    aCount = s.count('a') * wholeReps
    aCount += s[:remainingReps].count('a')
    return(aCount)

if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(str(result) + '\n')