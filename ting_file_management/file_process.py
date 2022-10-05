import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in instance._data:
        if i["nome_do_arquivo"] == path_file:
            return
    txt = txt_importer(path_file)
    inst = {
      "nome_do_arquivo": path_file,
      "qtd_linhas": len(txt),
      "linhas_do_arquivo": txt
    }
    instance.enqueue(inst)
    print(inst)


def remove(instance):
    if len(instance) == 0:
        print('Não há elementos')
    else:
        remove_file = instance.dequeue()['nome_do_arquivo']
        print(f'Arquivo {remove_file} removido com sucesso')


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        sys.stdout.write(str(data))
    except IndexError:
        sys.stderr.write("Posição inválida")
