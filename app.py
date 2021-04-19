import os
from flask import Flask, render_template, request, redirect, send_file
from s3_demo import list_files

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "1656"

@app.route('/')
def entry_point():
    return 'Hello World!'

@app.route("/storage")
def storage():
    contents = list_files("1656")
    return render_template('storage3.html', contents=contents)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8085)