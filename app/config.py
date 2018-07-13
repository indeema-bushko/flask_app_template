import os

curr_work_dir = os.path.dirname(os.path.realpath(__file__))

device_config = os.path.join(curr_work_dir, 'server_files/device-config.json')

rootCA = os.path.join(curr_work_dir, 'server_files/certs/rootCA.pem')

certificate = os.path.join(curr_work_dir, 'server_files/certs/f926e85654-certificate.pem.crt')

privateKey = os.path.join(curr_work_dir, 'server_files/certs/f926e85654-private.pem.key')

publicKey = os.path.join(curr_work_dir, 'server_files/certs/f926e85654-public.pem.key')

