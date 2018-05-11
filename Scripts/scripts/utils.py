import datetime


def get_date(string):
    """ Breaks the entire log string into a datetime object"""
    """ Input: 2018-05-10 22:38:38.671 -> datetime object"""
    words = string.split()

    # Need to cut the first two digits from the year
    string_date = words[0][2:] + " " + words[1]
    dt = datetime.datetime.strptime(string_date, "%y-%m-%d %H:%M:%S.%f")
    return dt


def get_microservice(string):
    """ Breaks a partial log string into its microservice"""
    """ Input: http://localhost:4000/auth-ms"""
    """ Output: auth-ms -> string"""
    # 1st word: http -- 2nd word: //localhost -- 3rd word:  4000/auth-ms/......
    words = string.split(":")
    # Always need second word here!
    return words[2].split("/")[1]


def is_the_response_request(first_list, second_list):
    """ List input example: [datetime.datetime(2018, 5, 10, 22, 38, 38, 671000), 'GET', 'INCOMING', '127.0.0.1',
    'http://localhost:4000/users-ms/', '48738', 'NO']"""
    if second_list[2] == 'LEAVING' and second_list[1] == first_list[1] and second_list[3] == first_list[3] and second_list[4] == first_list[4] and second_list[5] == first_list[5]:
        return True
    return False






