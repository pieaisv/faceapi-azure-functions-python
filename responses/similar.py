import azure.functions as func
from json import dumps


def response_json(similar: bool = True, message: str = "", facesNumber: dict = {}, drawUrl: str = "", status: int = 200):
    return func.HttpResponse(dumps({
        "similar": similar,
        "message": message,
        "facesNumber": facesNumber,
        "drawUrl": drawUrl
    }), status_code=status)
