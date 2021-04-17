
from flask import Flask, request, jsonify, render_template, abort, send_from_directory, session, redirect, url_for, make_response
import os
from pathlib import Path

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()+"/static"


# decorating index function with the app.route with url as /login
@app.route('/')
def start_page():
    return render_template('homepage.html')

@app.route('/home')
def get_home():
    return render_template('homepage.html')

@app.route('/checker')
def get_results():
    return render_template('results_page.html')

@app.route('/recycling_habits')
def get_habits():
    return render_template('recycling_habits.html')

@app.route('/rewards')
def get_rewards():
    return render_template('rewards.html')

@app.route('/upload', methods=['POST'])
def upload_img():
    if request.method == "POST":
        f = request.files["image"]
        f.save(app.config['UPLOAD_FOLDER'] + "/"+f.filename)
        if f.filename in os.listdir(os.getcwd()):
            success = "file uploaded successfully"
        else:
            success = "upload failed"

        working_dir = Path.cwd()

        img_path = str(f.filename)
        print("path", img_path)
        label = "Plastic"
        confidence = 0.8

        item_string = f"We have identified your item as **{label}** with confidence {confidence*100:.2f}%"
        can_recycle = f"{label} can be recycled if it is CLEAN"

        # use this to get the file
        return render_template("output_page.html",
                               img_path=img_path,
                               item_string=item_string,
                               can_recycle=can_recycle)

if __name__ == "__main__":
    app.run(debug=True)
    # socketio.run(app, debug=False, host='0.0.0.0', port=8080)
