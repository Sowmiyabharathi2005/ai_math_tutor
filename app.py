import os
from flask import Flask, render_template, request
from utils.ocr_utils import extract_equation_from_image
from utils.solver import solve_equation
from utils.mistake_check import detect_mistakes
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "outputs/results"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/solve", methods=["POST"])
def solve():

    if "image" not in request.files:
        return "No file uploaded"

    file = request.files["image"]

    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    # OCR extraction
    equation = extract_equation_from_image(path)

    # Solve equation
    steps, result = solve_equation(equation)

    # Mistake detection
    mistakes = detect_mistakes(equation)

    return render_template(
        "solution.html",
        equation=equation,
        steps=steps,
        result=result,
        mistakes=mistakes
    )


if __name__ == "__main__":
    app.run(debug=True)