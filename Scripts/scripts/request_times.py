import scripts.utils as util


# Log Example: 2018-05-10 22:38:38.671 GET INCOMING 127.0.0.1 http://localhost:4000/users-ms/ 48738

list_file = []
with open("EventSequence.txt") as f:
    for line in f:
        words = line.split()
        list_file.append([util.get_date(words[0] + " " + words[1]), words[2],
                          words[3], words[4], words[5], words[6], "NO"])


result = []
for row in list_file:
    if row[2] == 'INCOMING':
        for row_again in list_file:
            if row_again[6] == 'NO' and util.is_the_response_request(row, row_again):
                result.append([util.get_microservice(row[4]), row_again[0] - row[0]])
                row_again[6] = 'YES'
                break















