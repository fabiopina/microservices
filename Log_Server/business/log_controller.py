import business.response_handling as RESP


def hello_world():
    return RESP.response_200(message='Log_Server working!')


def create_log_entry(body):

    with open('EventSequence.txt', 'a') as file:
        file.write(body['timestamp']+" ["+body['status']+"] "+body['message']+"\n")

    return RESP.response_200(message='Log written with success!')
