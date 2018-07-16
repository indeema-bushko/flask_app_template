import json
import shutil
import glob
import os
import tarfile


def load_text_file(file_path):
    """
    Load JSON data from file.
    :param file_path: absolute file path
    :return: return json data.
    """
    try:
        with open(file_path) as data_file:
            return None, data_file.read()
    except IOError as e:
        print("utils.load_text_file: {}".format(e))
        return '{}'.format(e), None


def save_json_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, ensure_ascii=False)
    except IOError as e:
        print('Failed save json file -> {}'.format(e))


def recursively_copying_files(source_path, destination_path, override=False):
    """
    Recursive copies files from source  to destination directory.
    :param source_path: source directory
    :param destination_path: destination directory
    :param override if True all files will be overridden otherwise skip if file exist
    :return: count of copied files
    """
    files_count = 0
    if not os.path.exists(destination_path):
        os.makedirs(destination_path, exist_ok=True)
    items = glob.glob(source_path + '/*')
    for item in items:
        if os.path.isdir(item):
            path = os.path.join(destination_path, item.split('/')[-1])
            files_count += recursively_copying_files(source_path=item, destination_path=path, override=override)
        else:
            file = os.path.join(destination_path, item.split('/')[-1])
            if not os.path.exists(file) or override:
                shutil.copyfile(item, file)
                files_count += 1
    return files_count


def clear_folder(path, excepted_files=list()):
    files = glob.glob(path)
    for file in files:
        for ex_file in excepted_files:
            if ex_file not in file:
                os.remove(file)
                continue


def delete_files(path, list_of_files):
    """
    :param path:
    :param list_of_files:
    :return:
    """
    files = glob.glob(path + '/*')
    for f in list_of_files:
        for file in files:
            if f in file:
                os.remove(file)


def tar_extract(target_dir='.', absolute_path_to_file=None, compression='r:gz'):
    """
    Extract tar.gz archive in to current directory
    :param target_dir:
    :param absolute_path_to_file:
    :param compression:
    :return:
    """
    if absolute_path_to_file:
        try:
            tar_file = tarfile.open(absolute_path_to_file, compression)
            tar_file.extractall(target_dir)
        except tarfile.TarError as e:
            raise Exception(e)


def tar_compress(target_dir):
    """
    Compress target directory to tar.gz archive format
    :param target_dir:
    :return:
    """
    with tarfile.open('{}.tar.gz'.format(target_dir), 'w:gz') as tar:
        tar.add(target_dir, arcname=os.path.basename(target_dir))
    if os.path.exists('{}.tar.gz'.format(target_dir)):
        return '{}.tar.gz'.format(target_dir)
    else:
        return None


def get_files_list_from_tar(path, compression='r:gz'):
    if path:
        try:
            tar_file = tarfile.open(path, compression)
            return tar_file.getnames()
        except tarfile.TarError as e:
            raise Exception(e)
        return None


