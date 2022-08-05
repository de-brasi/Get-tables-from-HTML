import settings.setting_structures as tune_up

# settings.py imported from main.py
# which stored in root and SOURCE_DIR
# will contain path: ~/source/
SOURCE_DIR = "source/"
DESTINATION_DIR = "result/"


# parsing MIPT tables from https://pk.mipt.ru/bachelor/competition-list/
MIPT_table_criteria = tune_up.TableSearchCriteria(
    html_table_tag="tbody",
    html_table_class="entrant-list-body"
    )
MIPT_row_criteria = tune_up.RowSearchCriteria(
    html_row_tag="tr",
    html_row_class="entrant entrant-success"
)
MIPT_content_criteria = tune_up.RowContentSearchCriteria(
    html_row_content_tag="td"
)
MIPT_checkbox_properties = tune_up.CheckboxesProperties(
    presence=True,
    checkbox_html_class_no=".checkbox_round_green_empty",
    checkbox_html_class_yes=".checkbox_round_green",
    checkbox_mark_yes="Yes",
    checkbox_mark_no="No"
)
MIPT_settings = tune_up.Settings(
    html_source_page_path=SOURCE_DIR + "Конкурсные списки.html",
    libreoffice_table_path=SOURCE_DIR + "result_table_mipt.ods",
    ordered_source_table_fields=[
        "№", "Приоритет", "СНИЛС", "ИД", "М", "И", "Ф", "Р",
        "Сумма без ИД", "Сумма с ИД", "Согласие на зачисление",
        "Пр. право", "Документ"
    ],
    ordered_dest_table_fields=[
        "№", "Приоритет", "СНИЛС", "Сумма с ИД",
        "Согласие на зачисление", "Документ"
    ],
    result_name="result_mipt.ods",
    html_table_properties=MIPT_table_criteria,
    html_row_properties=MIPT_row_criteria,
    html_row_content_properties=MIPT_content_criteria,
    html_table_checkbox_info=MIPT_checkbox_properties
)


# parsing MISIS tables from
# https://misis.ru/applicants/admission/progress/baccalaureate-and-specialties/list-of-applicants/
MISIS_table_criteria = tune_up.TableSearchCriteria(
    html_table_tag="tbody",
    )
MISIS_row_criteria = tune_up.RowSearchCriteria(
    html_row_tag="tr",
)
MISIS_content_criteria = tune_up.RowContentSearchCriteria(
    html_row_content_tag="td"
)
MISIS_checkbox_properties = tune_up.CheckboxesProperties(
    presence=False,
)
MISIS_settings = tune_up.Settings(
    html_source_page_path=SOURCE_DIR + "Конкурсные списки МИСИС.html",
    libreoffice_table_path=SOURCE_DIR + "result_table_misis.ods",
    ordered_source_table_fields=[
        "№", "Рег", "СНИЛС", "№ Спец.квота", "Общ сумма",
        "М", "И/Ф/Х", "Р",
        "Баллы ИД", "Согласие на зачисление", "Оригнал",
        "Условие приема", "Потребность в общежитии",
        "Решение ПК"
    ],
    ordered_dest_table_fields=[
        "№", "СНИЛС"
    ],
    result_name="result_misis.ods",
    html_table_properties=MISIS_table_criteria,
    html_row_properties=MISIS_row_criteria,
    html_row_content_properties=MISIS_content_criteria,
    html_table_checkbox_info=MIPT_checkbox_properties
)

USING_SETTINGS = MISIS_settings
