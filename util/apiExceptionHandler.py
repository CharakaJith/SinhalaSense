def api_exception_handler(message, status):
    return ({
        'success': False,
        'httpStatus': status,
        'data': {
            'exception': message
        }        
    })