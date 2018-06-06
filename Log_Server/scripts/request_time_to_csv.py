import scripts.utils as util

# EXAMPLE
# 2018-05-26 15:02:52.789 INCOMING GET 172.18.0.7 52370 http://zuul:4000/playlists-ms/playlists/songs/1 null null
# 2018-05-26 15:02:52.945 LEAVING GET 172.18.0.7 52370 http://zuul:4000/playlists-ms/playlists/songs/1 /playlists-ms http://55e6783ec759:5002/playlists/songs/1


def run():
    list_file = []
    with open("EventSequence.txt") as f:
        for line in f:
            words = line.split()
            list_file.append([util.get_date(words[0] + " " + words[1]), words[2],
                              words[3], words[4], words[5], words[6], words[7], words[8], "NO"])
    f.close()


    with open('Data.csv', 'w') as f:
        id = 1
        f.write('id,microservice,begin_request_time,end_request_time,client_ip,client_port,function_called,microservice_instance\n')
        for row in list_file:
            if row[1] == 'INCOMING':
                for row_again in list_file:
                    if row_again[8] == 'NO' and util.is_the_response_request(row, row_again):
                        f.write(str(id) + "," + row_again[6][1:] + "," + row[0].strftime("%y-%m-%d %H:%M:%S.%f") + "," + row_again[0].strftime("%y-%m-%d %H:%M:%S.%f") + "," + row_again[3] + "," + row_again[4] + "," + util.get_function(row_again[2], row_again[5]) + "," + util.get_instance(row_again[7]) + "\n")
                        row_again[8] = 'YES'
                        id = id + 1
                        break
    f.close()
















