import business.response_handling as RESP

def hello_world():
    return RESP.response_200(message='Log_Server working!')