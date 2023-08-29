#!usr/bin/python3
def divide(ml):
    pieces = []
    tmp = []
    for index in range(len(ml)):
        tmp.append(ml[index])
        try:
            if ml[index] >= ml[index+1]:
                pieces.append(tmp)
                tmp = []
        except IndexError:
            pieces.append(tmp)
    return pieces
def more_elements(ml):
    maxlen = 0
    more = 0
    for index in range(len(ml)):
        if len(ml[index]) > maxlen:
            maxlen = len(ml[index])
            more = ml[index]
    return more

def main():
    numbers = [12,1,3,4,25,13,17,32]
    llists = divide(numbers)
    score = more_elements(llists)
    print(score)

main()

