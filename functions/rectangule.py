from io import BytesIO
from PIL import Image, ImageDraw
from requests import get


# Convert width height to a point in a rectangle
def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height

    return ((left, top), (right, bottom))


def drawFaceRectangles(image_multiple_faces: str, first_detected_faces: list) -> bytes:
    response = get(image_multiple_faces)

    img = Image.open(BytesIO(response.content))

    draw = ImageDraw.Draw(img)
    for face in first_detected_faces:
        draw.rectangle(getRectangle(face), outline='red')
    
    # SAVES THE "FILE" IN MEMORY AND THEN RETURNS IT
    with BytesIO() as output:
        img.save(output, format="JPEG")
        return output.getvalue()
