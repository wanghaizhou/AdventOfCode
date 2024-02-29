
# filename = 'input_test.txt'
# multiple = 2
# multiple = 10
# multiple = 100

filename = 'input.txt'
# multiple = 2
multiple = 1000000

with open(filename, 'r') as file:
    content = file.readlines()

orgin_metrix = [list(text.strip()) for text in content]
print(orgin_metrix)



lineToExpand = []
rowToExpand = []

def initExpandData(orgin_metrix):
    list = []
    list_str = []
    for i in range(len(orgin_metrix)):
        row = orgin_metrix[i]
        row_text = ''.join(row)
        row_text = row_text.replace('#','1').replace('.','0')
        row_val = int(row_text,2)
        if row_val == 0:
            rowToExpand.append(i)
        list.append(row_val)
        list_str.append(row_text)
        print(row_text)


    first = ~list[0]
    for i in range(1, len(list)):
        first = (~list[i]) & first
    first = ~first

    print('二进制数字',bin(first))

    row_len = len(list_str[0])
    for i in range(row_len):
        v = first & (1 << i)
        if v==0:
            # expand line
            lineToExpand.append(row_len-i-1)
            pass
    pass

initExpandData(orgin_metrix)

print("changed")

metrix = orgin_metrix

def printMetrix(metrix):
    for line in metrix:
        str = ''.join([e[0] for e in line])
        str = str.replace('0','.').replace('1','#')
        print(str)
    pass

printMetrix(metrix)

galaxy = [(j,i) for i in range(len(metrix)) for j in range(len(metrix[0]))  if metrix[i][j] == '#']
print('galaxy', galaxy)


def calculateWithMultiple(x1, x2, lineToExpand):
    min_v = min([x1, x2])
    max_v = max([x1, x2])
    length = 0
    for i in range(min_v, max_v):
        if i in lineToExpand:
            length += multiple
        else:
            length += 1
    return length
    pass


def calculatePath(galaxy):
    length = 0
    for i in galaxy:
        for j in galaxy:
            if not (i[0] == j[0] and i[1] == j[1]) :
                width = calculateWithMultiple(i[0],j[0],lineToExpand)
                height = calculateWithMultiple(i[1],j[1],rowToExpand)
                length += abs(width)+abs(height)
    return length/2

length = calculatePath(galaxy)
print("length",length)

