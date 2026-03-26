import cv2
import easyocr

reader = easyocr.Reader(['en'])

def preprocess_image(path):

    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    thresh = cv2.adaptiveThreshold(
        blur,255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,2
    )

    return thresh


def extract_equation_from_image(path):

    img = preprocess_image(path)

    results = reader.readtext(img)

    equation = ""

    for res in results:
        equation += res[1]

    equation = equation.replace(" ", "")

    return equation