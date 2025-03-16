from util.apiExceptionHandler import api_exception_handler
from constants.appConstants import http_status

def analyze_text():
    try:
        return ({
            'success': True,
            'httpStatus': http_status.OK,
            'data': {
                'message': 'OK'
            }
        })
    except Exception as error:
        api_exception_handler(error, http_status.INTERNAL_SERVER_ERROR)