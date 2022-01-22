import azure.functions as func
from functions.analyze_face import detect_face
from functions.rectangule import drawFaceRectangles


def main(req: func.HttpRequest) -> func.HttpResponse:

    # FIRST IMAGE

    first_detected_faces = detect_face(req.params.get("single"))

    # SECOND IMAGE

    image_multiple_faces = req.params.get("multiple")

    output = drawFaceRectangles(image_multiple_faces, first_detected_faces)

    headers = {
        "Content-Type": f"image/jpeg"
    }
    return func.HttpResponse(body=output, headers=headers)
