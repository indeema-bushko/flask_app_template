import os

curr_work_dir = os.path.dirname(os.path.realpath(__file__))

cert_dir = os.path.join(os.path.join(curr_work_dir, 'server_files/certs'))

device_config = os.path.join(curr_work_dir, 'server_files/device-config.json')

certs_tar_gz = os.path.join(curr_work_dir, 'server_files/certs.tar.gz')

rootCA = os.path.join(curr_work_dir, 'server_files/certs/rootCA.pem')

certificate = os.path.join(curr_work_dir, 'server_files/certs/certificate.pem.crt')

privateKey = os.path.join(curr_work_dir, 'server_files/certs/private.pem.key')

publicKey = os.path.join(curr_work_dir, 'server_files/certs/public.pem.key')

