#!/usr/bin/python

from app import app
import os
from flask import Response
from app import utils

curr_dir = os.path.dirname(os.path.realpath(__file__))


@app.route('/', methods=['GET'])
def home():
    return '<a href=\"/device_config\">download device config json</a><br>' \
           '<a href=\"/certs\">download certificates</a><br>' \
           '<a href=\"/cpuid\">get cpu serial number</a><br>'


@app.route('/device-config', methods=['GET'])
def device_config():
    context = utils.load_text_file(os.path.join(curr_dir, 'server/file/device-config.json'))
    return Response(context, mimetype='application/json',
                    headers={'Content-Disposition': 'attachment;filename=device-config.json'})