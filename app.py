from flask import Flask, render_template, request
from predict import predict_phishing

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form.get("url")
        result = predict_phishing(url)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)