import os
from argparse import ArgumentParser
from collections import namedtuple
import logging

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_directory'])
logging.basicConfig(filename='dir_contents.log', encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s - %(message)s')


def directory_info(path):
    if not os.path.isdir(path):
        raise ValueError(f'Path {path} is not directory')
    parent_dir = os.path.basename(os.path.abspath(path))
    for item in os.listdir(path):
        current_path = os.path.join(path, item)
        if os.path.isdir(current_path):
            file_info = FileInfo(name=item, extension=None, is_dir=True, parent_directory=parent_dir)
        else:
            name, extension = os.path.splitext(item)
            file_info = FileInfo(name=name, extension=extension.lstrip('.'), is_dir=False, parent_directory=parent_dir)
        logging.info(
            f'{file_info.name} | '
            f'{file_info.extension if file_info.extension else "N/A"} | '
            f'{"Directory" if file_info.is_dir else "File"} | '
            f'{file_info.parent_directory}')


if __name__ == '__main__':
    parser = ArgumentParser(description="Collect info about content of the directory and log.")
    parser.add_argument('directory', type=str, help='Path to analyse')
    args = parser.parse_args()
    path = args.directory

    try:
        directory_info(path)
        print(f'Information about content of directory {path} is successfully recorded to file {"dir_contents.log"}')
    except ValueError as e:
        print(e)
