from rest_framework.exceptions import APIException


class NotValueExists(APIException):
    status_code = 204
    default_detail = "값이 존재하지않습니다. 값을 넣고, 다시 시도해주세요."
    default_code = "값이 존재하지않음"
