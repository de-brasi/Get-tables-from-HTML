import bs4.element
from bs4 import BeautifulSoup
from settings import settings

current_settings = settings.USING_SETTINGS

table_tag = current_settings.html_table_properties.html_table_tag
table_class = current_settings.html_table_properties.html_table_class

row_tag = current_settings.html_row_properties.html_row_tag
row_class = current_settings.html_row_properties.html_row_class

row_content_tag = \
    current_settings.html_row_content_properties.html_row_content_tag
table_content_checkbox_info = \
    current_settings.html_table_checkbox_info

source_html_file = open(current_settings.html_source_page_path, 'r')
parsed_html = BeautifulSoup(source_html_file, "html.parser")

if table_class:
    table_content = parsed_html.find(table_tag, class_=table_class)
else:
    table_content = parsed_html.find(table_tag)
if row_class:
    table_content = table_content.find_all(row_tag, class_=row_class)
else:
    table_content = table_content.find_all(row_tag)


def html_row_to_data_collection(data: bs4.element.Tag) -> list:
    parsed_data = list()

    if table_content_checkbox_info.presence:
        for col_value in data.select(row_content_tag):
            if col_value.select(table_content_checkbox_info.checkbox_html_class_yes):
                parsed_data.append(
                    table_content_checkbox_info.checkbox_mark_yes
                )
            elif col_value.select(table_content_checkbox_info.checkbox_html_class_no):
                parsed_data.append(
                    table_content_checkbox_info.checkbox_mark_no
                )
            else:
                parsed_data.append(col_value.text.strip())
    else:
        for col_value in data.select(row_content_tag):
            parsed_data.append(col_value.text.strip())

    return parsed_data


def make_collection_from_html_table(content: bs4.element.ResultSet) -> list:
    result_py_datastructure = list()

    for entrant_data in content:
        result_py_datastructure.append(
            html_row_to_data_collection(entrant_data)
        )

    return result_py_datastructure


PARSED_TABLE = make_collection_from_html_table(table_content)
