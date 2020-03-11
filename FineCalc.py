def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return(10000)
    elif y1 == y2 and m1 > m2:
        return(500 * (m1-m2))
    elif y1 == y2 and m1 == m2 and d1 > d2:
        return(15 *abs(d1-d2))
    elif y1 <= y2 and m1 <= m2 and d1 <= d2:
        return(0)
    elif y1 == y2 and m1 < m2 and d1 > d2:
        return(0)
    elif y1 < y2:
        return(0)

if __name__ == '__main__':
    d1M1Y1 = input('Return date: ').split()
    d1 = int(d1M1Y1[0])
    m1 = int(d1M1Y1[1])
    y1 = int(d1M1Y1[2])
    d2M2Y2 = input('Due date: ').split()
    d2 = int(d2M2Y2[0])
    m2 = int(d2M2Y2[1])
    y2 = int(d2M2Y2[2])
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(str(result) + '\n')
