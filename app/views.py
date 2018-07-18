#!/usr/bin/python

from app import app
import os
from flask import Response
from flask import send_file, make_response
from flask import request
import hashlib

from app import utils
from app import config

curr_dir = os.path.dirname(os.path.realpath(__file__))


@app.route('/', methods=['GET'])
def home():
    return '<a href=\"/auth?uuid=1234567890\">auth</a><br>' \
           '<a href=\"/device-config\">download device config json</a><br>' \
           '<a href=\"/rca\">download rootCA file</a><br>' \
           '<a href=\"/cert\">download certificate pem</a><br>' \
           '<a href=\"/public_key\">download public key</a><br>' \
           '<a href=\"/private_key\">download private key</a><br>' \
           '<a href=\"/certs_tar\">download certs tar.gz</a><br>'


@app.route('/auth', methods=['GET'])
def auth():
    print(request.headers)
    dev_uuid = request.args.get('uuid')
    print('UUID: {}'.format(dev_uuid))
    if dev_uuid:
        return 'Success'
    else:
        return 'Error authentication', 404


@app.route('/device-config', methods=['GET'])
def device_config():
    error, context = utils.load_text_file(config.device_config)
    if error:
        return error
    return Response(context, mimetype='application/json',
                    headers={'Content-Disposition': 'attachment;filename=device-config.json'})


@app.route('/rca', methods=['GET'])
def get_rca():
    error, content = utils.load_text_file(os.path.join(curr_dir, 'server_files/certs/rootCA.pem'))
    if error:
        return error
    head, tail = os.path.split(config.rootCA)
    print('{}: {}'.format(head, tail))
    md5 = hashlib.md5(open(config.rootCA, 'rb').read()).hexdigest()
    response = Response(content, mimetype='application/text',
                        headers={'Content-Disposition': 'attachment;filename={}'.format(tail),
                                 'Content-MD5': md5})
    return response


@app.route('/certs_tar', methods=['GET'])
def certs_tar():
    path_to_tar = utils.tar_compress(config.cert_dir)
    if path_to_tar is None:
        content = 'File not found..'
        return Response(content=content, status=404, mimetype='text/plain')
    head, tail = os.path.split(path_to_tar)
    md5 = hashlib.md5(open(path_to_tar, 'rb').read()).hexdigest()
    print(path_to_tar)
    print(md5)
    print(tail)
    response = make_response(send_file(path_to_tar, attachment_filename=tail))
    response.headers['Content-MD5'] = md5
    response.headers['Content-Disposition'] = 'attachment;filename={}'.format(tail)
    return response


@app.route('/cert', methods=['GET'])
def get_certificate():
    error, content = utils.load_text_file(config.certificate)
    if error:
        return error
    head, tail = os.path.split(config.certificate)
    print('{}: {}'.format(head, tail))
    md5 = hashlib.md5(open(config.certificate, 'rb').read()).hexdigest()
    return Response(content, mimetype='application/text',
                    headers={'Content-Disposition': 'attachment;filename={}'.format(tail),
                             'Content-MD5': md5})


@app.route('/public_key', methods=['GET'])
def get_public_key():
    error, content = utils.load_text_file(config.publicKey)
    if error:
        return error
    head, tail = os.path.split(config.publicKey)
    print('{}: {}'.format(head, tail))
    md5 = hashlib.md5(open(config.publicKey, 'rb').read()).hexdigest()
    return Response(content, mimetype='application/text',
                    headers={'Content-Disposition': 'attachment;filename={}'.format(tail),
                             'Content-MD5': md5})


@app.route('/private_key', methods=['GET'])
def get_private_key():
    error, content = utils.load_text_file(config.privateKey)
    if error:
        return error
    head, tail = os.path.split(config.privateKey)
    print('{}: {}'.format(head, tail))
    md5 = hashlib.md5(open(config.privateKey, 'rb').read()).hexdigest()
    return Response(content, mimetype='application/text',
                    headers={'Content-Disposition': 'attachment;filename={}'.format(tail),
                             'Content-MD5': md5})

