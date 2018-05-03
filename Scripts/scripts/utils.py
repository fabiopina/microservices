import datetime


def get_date(string):
    """ Breaks the entire log string into a datetime object"""
    """ Input: 2018-04-30 00:55:07.782 [LEAVING] FROM-> 127.0.0.1 TO-> http://localhost:4000/users-ms/users METHOD-> POST"""
    words = string.split()

    string_date = words[0][2:] + " " + words[1]
    dt = datetime.datetime.strptime(string_date, "%y-%m-%d %H:%M:%S.%f")
    return dt


def get_microservice(string):
    """ Breaks a partial log string into its microservice"""
    """ Input: FROM-> 127.0.0.1 TO-> http://localhost:4000/auth-ms METHOD-> GET"""
    """ Output: auth-ms"""
    words = string.split(":")
    last_url = words[2].split("/")[1]
    microservice = last_url.split(" ")[0]
    return microservice






