def designerPdfViewer(h, word):
    height = list()
    ind = 0
    guide = {}
    for char in range(ord('a'),ord('z')+1):
        guide[chr(char)] = h[ind]
        ind += 1
    for let in word:
        height.append(guide[let])
    return(max(height)*len(word))

if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(str(result) + '\n')
