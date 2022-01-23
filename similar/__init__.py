import azure.functions as func
from functions.analyze_face import detect_face, similar_images
from os import path
from urllib.parse import urlparse
from responses.similar import response_json


def main(req: func.HttpRequest) -> func.HttpResponse:
    body = req.get_json()

    url = urlparse(req.url)
    host = url.scheme + "://" + url.netloc

    image_single = body["single"]
    image_multiple = body["multiple"]

    # FIRST IMAGE

    first_detected_faces = detect_face(image_single)

    first_image_face_ID = first_detected_faces[0].face_id

    # SECOND IMAGE

    detected_faces2 = detect_face(image_multiple)

    second_image_face_IDs = list(map(lambda x: x.face_id, detected_faces2))

    similar_faces = similar_images(image_id1=first_image_face_ID,
                                   images_ids=second_image_face_IDs)
    facesNumber = {
        "single": len(first_detected_faces),
        "multiple": len(detected_faces2)
    }

    drawUrl = f"{host}/api/draw?single={image_single}&multiple={image_multiple}"

    if similar_faces:
        return response_json(message="Similar Faces",
                             facesNumber=facesNumber, drawUrl=drawUrl)
    else:
        message = "No similar faces found in" + path.basename(image_multiple)

        return response_json(similar=False, message=message,
                             status=404, facesNumber=facesNumber)
