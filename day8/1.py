# not sure if part 2 is clearest as possible.

with open("data.txt", 'r') as file:
    treedata = [int(x) for x in file.readline().split()]


def sum_metadata(data, index):
    sum_of_metadata = 0
    num_nodes = data[index]
    metadata_len = data[index+1]
    index += 2
    for i in range(num_nodes):
        index, metadata = sum_metadata(data, index)
        sum_of_metadata += metadata
    end_index = index+metadata_len
    return end_index, sum_of_metadata + sum(data[index:end_index])


def calculate_node_value(data, index):
    sum_of_metadata = 0
    num_nodes = data[index]
    metadata_len = data[index+1]
    index += 2
    sums = []
    for i in range(num_nodes):
        index, metadata = calculate_node_value(data, index)
        sums.append(metadata)
    end_index = index + metadata_len
    for child in data[index:end_index]:
        if child != 0 and not child > len(sums):
            sum_of_metadata += sums[child - 1]
    if not num_nodes:
        return end_index, sum(data[index:end_index])
    else:
        return end_index, sum_of_metadata


print("Part 1:", sum_metadata(treedata, 0)[1])
print("Part 2:", calculate_node_value(treedata, 0)[1])

