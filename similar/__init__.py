import azure.functions as func
from functions.analyze_face import detect_face, similar_images
from os import path
from json import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
    body = req.get_json()

    #FIRST IMAGE

    first_detected_faces = detect_face(body["single"])

    first_image_face_ID = first_detected_faces[0].face_id

    #SECOND IMAGE

    detected_faces2 = detect_face(body["multiple"])

    second_image_face_IDs = list(map(lambda x: x.face_id, detected_faces2))

    similar_faces = similar_images(image_id1=first_image_face_ID,
                                   images_ids=second_image_face_IDs)

    if similar_faces:
        return func.HttpResponse(dumps({
            "similar": True,
            "message": "Similar Faces"
        }))
    if not similar_faces:
        return func.HttpResponse(dumps({
            "similar": False,
            "message": "No similar faces found in" + path.basename(body["multiple"])

        }), status_code=500)
