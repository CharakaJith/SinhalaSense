class http_status:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500

class app_envs:
    DEV = 'development'
    PROD = 'production'
    STAGE = 'staging'
    QA = 'qa'