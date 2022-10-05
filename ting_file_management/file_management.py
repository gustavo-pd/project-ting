import sys
import os


def txt_importer(path_file):
    if not os.path.exists(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    if ".txt" not in path_file:
        return sys.stderr.write("Formato inválido\n")

    with open(path_file) as file:
        split_file = file.read().splitlines()
        return split_file
