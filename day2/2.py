with open("data.txt", 'r') as data:
    boxes = [box.strip() for box in data.readlines()]

for i, box in enumerate(boxes):
    for otherBox in boxes[i+1:]:
        cnt, common = 0, ""
        for c1, c2 in zip(box, otherBox):
            if c1 == c2:
                common = common + c1
            else:
                cnt += 1
        if cnt == 1:
            print(common)
            exit()
