

with open('input.txt', 'r') as file:
    content = file.readlines()

orgin_metrix = [list(text.strip()) for text in content]
print(orgin_metrix)


def expandLine(list_str,lineToExpand):
    length = len(list_str[0])
    result = []
    for row in list_str:
        list_row = list(row)
        result_row = []
        for i in range(len(list_row)):
            result_row.append(list_row[i])
            if i in lineToExpand:
                result_row.append(list_row[i])
        result.append(result_row)
    return result
    pass


def expand(orgin_metrix):
    list = []
    list_str = []
    for row in orgin_metrix:
        row_text = ''.join(row)
        row_text = row_text.replace('#','1').replace('.','0')
        row_val = int(row_text,2)
        if row_val == 0:
            list.append(row_val)
            list_str.append(row_text)
        list.append(row_val)
        list_str.append(row_text)
        print(row_text)


    first = ~list[0]
    for i in range(1, len(list)):
        first = (~list[i]) & first
    first = ~first

    print('二进制数字',bin(first))

    lineToExpand = []
    row_len = len(list_str[0])
    for i in range(row_len):
        v = first & (1 << i)
        if v==0:
            # expand line
            lineToExpand.append(row_len-i-1)
            pass

    result = expandLine(list_str,lineToExpand)
    return result
    pass

metrix = expand(orgin_metrix)

print("changed")


def printMetrix(metrix):
    for line in metrix:
        str = ''.join(line)
        str = str.replace('0','.').replace('1','#')
        print(str)
    pass

printMetrix(metrix)

galaxy = [(j,i) for i in range(len(metrix)) for j in range(len(metrix[0]))  if metrix[i][j] == '1']
print('galaxy', galaxy)

def calculatePath(galaxy):
    length = 0
    for i in galaxy:
        for j in galaxy:
            if not (i[0] == j[0] and i[1] == j[1]) :
                length += abs(i[0]-j[0])+abs(i[1]-j[1])
    return length/2

length = calculatePath(galaxy)
print("length",length)

