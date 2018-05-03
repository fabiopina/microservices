import scripts.utils as util


list_file = []
with open("EventSequence.txt") as f:
    for line in f:
        words = line.split()
        list_file.append([util.get_date(line), words[2],
                          words[3] + " " + words[4] + " " + words[5] + " " + words[6] + " " + words[7] + " " +
                          words[8], "NO"])

result = []
for row in list_file:
    if row[1] == '[INCOMING]':
        for row_second in list_file:
            if row_second[1] == '[LEAVING]' and row[2] == row_second[2] and row_second[3] == "NO":
                result.append([util.get_microservice(row[2]), row_second[0] - row[0]])
                row_second[3] = "YES"
                break











