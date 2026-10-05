import CSV

from archive.errors import MalformedRecordError

FIELD_NAMES = ["id", "title", "city", "year", "condition"]


def parse_line(line):
    line = line.strip()
    fields = line.split(",")

    if len(fields) != 5:
        raise MalformedRecordError()

    fields = [field.strip() for field in fields]

    return dict(zip(FIELD_NAMES, fields))
    raise NotImplementedError("parse_line")


def load_archive(path):
    valid_records = []
    rejected_lines = []

    try:
        with(path, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                original_line = line

                try:
                    record = parse_line(line)
                except MalformedRecordError:
                    rejected_lines.append(original_line)
                    continue
                errors = validate_record(record)

                if errors:
                    rejected_lines.append(original_line)
                else:
                    valid_records.append(record)
    except FileNotFoundError:
        return [], []

    return valid_records, rejected_lines

    raise NotImplementedError("load_archive")


def save_archive(path, records):
    """Write every record to `path` as CSV, one per line, no header.

    Field order is FIELD_NAMES. The file is overwritten, not appended to.

    Returns None.
    """
    raise NotImplementedError("save_archive")
