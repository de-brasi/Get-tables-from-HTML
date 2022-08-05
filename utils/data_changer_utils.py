def misis_snils_changer(source: str) -> str:
    result_string = source.replace('-', '')
    result_string = result_string.replace(' ', '')
    return result_string


def misis_field_view_changer(source_collection: list, field_idx: int, change_function):
    for i in range(len(source_collection)):
        source_collection[i][field_idx] = change_function(source_collection[i][field_idx])
