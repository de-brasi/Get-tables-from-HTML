from typing import NamedTuple


class TableSearchCriteria(NamedTuple):
    html_table_tag:   str = "tbody"
    html_table_class: str = ""


class RowSearchCriteria(NamedTuple):
    html_row_tag:   str = "tr"
    html_row_class: str = ""


class RowContentSearchCriteria(NamedTuple):
    html_row_content_tag: str = "td"


class CheckboxesProperties(NamedTuple):
    presence: bool = False
    checkbox_html_class_no: str = ""
    checkbox_html_class_yes: str = ""
    checkbox_mark_yes: str = "Yes"
    checkbox_mark_no: str = "No"


class Settings(NamedTuple):
    """
    Requirement:
        ordered_dest_table_fields must be
        a subset of ordered_source_table_fields;
    Parameters:
        html_source_page_path: str
        libreoffice_table_path: str
        ordered_source_table_fields: list
        ordered_dest_table_fields: list
        result_name: str
        html_table_properties:       TableSearchCriteria
        html_row_properties:         RowSearchCriteria
        html_row_content_properties: RowContentSearchCriteria
    Explanation:
        ordered_source_table_fields -
            В каком порядке идут и что содержат поля
            в исходной таблице html
        ordered_dest_table_fields -
            В каком порядке пойдут поля
            в распарсенной таблице ods
        html_table_properties -
            критерии для нахождения таблицы в
            html DOM-tree
        html_row_properties -
            критерии для нахождения строк в
            DOM-tree html-таблице
        html_row_content_properties -
            критерии для нахождения ячеек в
            DOM-tree строки
    """
    html_source_page_path: str
    libreoffice_table_path: str
    ordered_source_table_fields: list
    ordered_dest_table_fields: list
    result_name: str
    html_table_properties:       TableSearchCriteria
    html_row_properties:         RowSearchCriteria
    html_row_content_properties: RowContentSearchCriteria
    html_table_checkbox_info: CheckboxesProperties
