import pyexcel
from settings import settings
from utils import html_table_parser
from utils import data_changer
from utils import data_changer_utils

if __name__ == "__main__":
    parsed_table = html_table_parser.PARSED_TABLE
    table_discard_extra_fields = \
        data_changer.discard_extra_data(parsed_table)
    data_changer_utils.misis_field_view_changer(
            table_discard_extra_fields,
            settings.USING_SETTINGS.ordered_dest_table_fields.index("СНИЛС"),
            data_changer_utils.misis_snils_changer
        )

    res_file_name = settings.USING_SETTINGS.result_name
    res_file_path = settings.DESTINATION_DIR

    sheet = pyexcel.get_sheet(file_name=res_file_name)
    for row in table_discard_extra_fields:
        sheet.row += row
    sheet.save_as(res_file_path + res_file_name)
