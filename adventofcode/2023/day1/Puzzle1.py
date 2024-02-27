def calculate(line):
    first = next((int(element) for element in line if element.isdigit()),None)
    last = next((int(element) for element in line[::-1] if element.isdigit()),None)
    if first is not None and last is not None:
        return first*10+last
    return 0


with open('input1.txt',"r",encoding="utf-8") as file:
    content = file.readlines()

Number = {
    "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9
}

letterNum = [key for (key,value) in Number.items()]


def deal(line):
    newline = line
    indexs = [(key,newline.index(key),value) for (key,value) in Number.items()  if key in newline]
    rindexs = [(key,newline.rindex(key),value) for (key,value) in Number.items()  if key in newline]
    try:
        firstNumLetter = min(filter(lambda x: x[1] != "-1", indexs), key=lambda x: x[1])
        # newline = newline.replace(firstNumLetter[0], str(firstNumLetter[2]), 1)

        modified_string = newline.split(firstNumLetter[0], 1)
        newline = str(str(firstNumLetter[2])+firstNumLetter[0]).join(modified_string)
    except ValueError:
        firstNumLetter = None
    try:
        lastNumLetter = max(filter(lambda x: x[1] != "-1", rindexs), key=lambda x: x[1])
        modified_string = newline.rsplit(lastNumLetter[0], 1)
        newline = str(lastNumLetter[0]+str(lastNumLetter[2])).join(modified_string)
    except ValueError:
        lastNumLetter = None

    # for key,value in Number.items():
    #     newline = newline.replace(key,str(value))
    return newline

t = deal("xtwone3four")
print(t)

content2 = [ deal(line) for line in content]

total2 = sum([calculate(line) for line in content2])
total = sum([calculate(line) for line in content])
print("总值：",total)
print("总值：",total2)
# 55712
