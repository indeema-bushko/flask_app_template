from app import app
from flask import send_file


@app.route('/')
def index():
    return "Flask application template! Home Page"


@app.route('/download')
def download():
    filename = 'README.md'
    response = send_file('../{}'.format(filename), attachment_filename=filename, as_attachment=True)
    response.headers["x-filename"] = filename
    response.headers["Access-Control-Expose-Header"] = 'x-filename'
    return response
