#Interview question, Counting the maximum
def maximum(items,indexes):
    Rep = poor = list()
    for share in indexes:
        poor = items[share-1:]
        Rep.append(poor.count(items[share-1]))
    return(Rep)

if __name__ == '__main__':
    items = list(map(int, input().rstrip().split()))
    indexes = list(map(int, input().rstrip().split()))
    print(maximum(items,indexes))
