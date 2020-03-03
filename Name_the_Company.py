from collections import Counter
#Driving code
if __name__ == "__main__":
    s = str(input())
    s_count = (Counter(s))
    uni = sorted(set(s_count))
    logos = {}
    #To create a dictionary of characters and value pair
    for unique in uni:
        if s_count[unique] >= 1:
            logos[unique] = s_count[unique]
    stop = 1
    #To loop through sorted dictionary with key as refeence
    for logo in sorted(logos, key=logos.get, reverse=True):
        if stop <= 3:
            print(logo, logos[logo])
            stop += 1
