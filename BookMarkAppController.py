from flask import Flask, jsonify, abort, request, send_from_directory, send_file
from service.search_data_service import *
import os
from shutil import copyfile

app = Flask(__name__)


@app.route("/")
def welcome():
    return 'Welcome to the Bookmark application!!'


@app.route("/api/bookmarks/", methods=["GET"])
def get_all_bookmarks():
    if request.method == 'GET':
        bookmarks1 = load_all_bookmarks()
        return jsonify(bookmarks1)


@app.route("/api/bookmarks/<int:id>")
def get_bookmarks_by_id(id):
    bookmarks1 = load_bookmarks_by_id(id)
    return jsonify(bookmarks1)


@app.route("/api/bookmarks/", methods=["POST"])
def create_bookmark():
    print(request.json)
    data = request.json
    message = add_bookmarks(data)
    return message


@app.route("/api/bookmarks/<int:id>", methods=["PUT"])
def update_bookmarks(id):
    data = request.json
    message = modify_bookmarks(data, id)
    return message


@app.route("/api/bookmarks/<int:id>", methods=["DELETE"])
def remove_bookmarks(id):
    message = delete_bookmarks(id)
    return message


@app.route("/api/bookmarks/export/", methods=["GET"])
def export_bookmarks():
    result= send_file('model/data.json',attachment_filename='bookmarks.json',as_attachment=True)
    return result

    #return send_from_directory('/model/data.json', 'bookmarks.json', as_attachment=True)
