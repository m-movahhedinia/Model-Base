# -*- coding: utf-8 -*-
"""

"""

from flask import Blueprint, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from pathlib import Path


pages = Blueprint("temp_all_pages", __name__)
UPLOAD_FOLDER = Path("./uploads")


@pages.route("/")
@pages.route("/index")
def index():
    """
    Just returns a message if the server is up.

    :return: A simple string
    """

    return "We are online! The main page goes here later on."


@pages.route("/upload_data", methods=['POST'])
def upload_data():
    """
    Receives and stores a file from ths user. This file is either the training, testing, or validation set.

    :return:
    """
    if "file" not in request.files:
        flash("No file found in payload.")
        return redirect(request.url)

    file = request.files["file"]
    if len(file.filename) < 5:
        flash("Invalid file name.")
        return redirect(request.url)

    if file and extension_permitted(file.filename, "data"):
        filename = secure_filename(file.filename)
        file.save(Path(UPLOAD_FOLDER).joinpath(filename))
        return redirect(url_for("uploaded_file", filename=filename))
    return ""
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <input type=file name=file>
    #   <input type=submit value=Upload>
    # </form>
    # '''


@pages.route("/add_training_module", methods=['POST'])
def add_training_module():
    """
    Gets a file and trains the model by it

    :return:
    """
    if "file" not in request.files:
        flash("No file found in payload.")
        return redirect(request.url)

    file = request.files["file"]
    if len(file.filename) < 5:
        flash("Invalid file name.")
        return redirect(request.url)

    if file and extension_permitted(file.filename, "module"):
        filename = secure_filename(file.filename)
        file.save(Path(UPLOAD_FOLDER).joinpath(filename))
        return redirect(url_for("uploaded_file", filename=filename))
    return ""
    # return '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <input type=file name=file>
    #   <input type=submit value=Upload>
    # </form>
    # '''


@pages.route("/train", methods=['POST', 'get'])
def train():
    if request.method == 'POST':
        model = request.form["model"]
        training_set = request.form["training_set"]
        test_set = request.form["test_set"]
        validation_set = request.form["validation_set"]
        epochs = request.form["epochs"]
        print(request.form)
        flash('Training started')

    return '''<form method="POST">
                Model: <input type="text" name="model"><br>
                Training set: <input type="text" name="training_set"><br>
                Test set: <input type="text" name="test_set"><br>
                Validation set: <input type="text" name="validation_set"><br>
                Number of epochs: <input type="text" name="epochs"><br>
                <input type="submit" value="Submit"><br>
              </form>'''


@pages.route("/uploads/<filename>")
def upload_file(file):
    return send_from_directory(UPLOAD_FOLDER, file)


def extension_permitted(file: str, purpose: str):
    """
    Checks the extension of the file and determines if it is an allowed one or not.

    :param str file: The file sent to the server.
    :param str purpose: The purpose of the check determines the list of extensions to look into.
    :return: bool if the suffix of the file is a permitted one it returns True, and False if otherwise.
    """

    return Path(file).suffix.lower() in ([".csv"] if purpose == "data" else
                                         [".py"] if purpose == "module" else
                                         [".json"] if purpose == "config" else
                                         [".bin"] if purpose == "model" else
                                         [".html", ".js"] if purpose == "page" else
                                         [Path(file).suffix.lower()] if purpose == "test" else
                                         [])
