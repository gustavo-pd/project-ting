def exists_word(word, instance):
    list_data = []
    occurrence = []
    for i in range(len(instance)):
        searched_i = instance.search(i)
        for i, line in enumerate(instance.search(i)["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrence.append({"linha": i + 1})

        if len(occurrence):
            list_data.append({
                "palavra": word,
                "arquivo": searched_i["nome_do_arquivo"],
                "ocorrencias": occurrence,
            })

    return list_data


def search_by_word(word, instance):
    list_data = []
    occurrence = []
    for i in range(len(instance)):
        searched_i = instance.search(i)
        for i, line in enumerate(instance.search(i)["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurrence.append({"linha": i + 1, "conteudo": line})

        if len(occurrence):
            list_data.append({
                "palavra": word,
                "arquivo": searched_i["nome_do_arquivo"],
                "ocorrencias": occurrence,
            })

    return list_data