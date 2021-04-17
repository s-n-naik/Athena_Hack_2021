
from flask import Flask, request, jsonify, render_template, abort, send_from_directory, session, redirect, url_for, make_response

app = Flask(__name__)


# decorating index function with the app.route with url as /login
@app.route('/')
def start_page():
    return render_template('results_page.html')

@app.route('/upload', methods=['POST'])
def upload_img():
    if request.method == "POST":
        f = request.files["image"]
        f.save(f.filename)
        # use this to get the file
        return render_template("recycling_habits.html")

if __name__ == "__main__":
    app.run(debug=True)
    # socketio.run(app, debug=False, host='0.0.0.0', port=8080)
