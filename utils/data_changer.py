from settings.settings import USING_SETTINGS


def discard_extra_data(table: list) -> list:
    assert table
    assert len(table[0]) == len(
        USING_SETTINGS.ordered_source_table_fields
    )

    reworked_table = list()

    for entrant_info in table:
        info_batch = list()
        for i in range(len(
                USING_SETTINGS.ordered_source_table_fields
        )):
            if USING_SETTINGS.ordered_source_table_fields[i] in \
                    USING_SETTINGS.ordered_dest_table_fields:
                field_value = entrant_info[i]
                try:
                    field_value = int(field_value)
                except ValueError:
                    pass
                info_batch.append(field_value)
        reworked_table.append(info_batch)

    return reworked_table
