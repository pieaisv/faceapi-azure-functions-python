from connection import face_client

# DETECT IF THERE ARE ONE OR MORE FACES AND RETURN AN ID


def detect_face(image_url: str) -> list:
    detected_face = face_client.face.detect_with_url(
        url=image_url, detection_model='detection_03')

    return detected_face


# DETECT IF THERE ARE ONE OR MORE SIMILAR FACES

def similar_images(image_id1: str, images_ids: list):
    similar_faces = face_client.face.find_similar(
        face_id=image_id1, face_ids=images_ids)

    return similar_faces
