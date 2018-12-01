def difference(b1, b2):
    cnt, common = 0, ""
    for i, char in enumerate(b1):
        if char == b2[i]:
            common = common + char
        else:
            cnt += 1
    return cnt, common


def identify():
    for i, box in enumerate(boxes):
        for otherBox in boxes[i:]:
            cnt, common = difference(box, otherBox)
            if cnt == 1:
                return common


boxes = None
with open("data.txt", 'r') as data:
    boxes = data.readlines()

print(identify())
