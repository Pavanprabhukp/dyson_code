import csv


def check_csv_columns(csv_file):
    valid_columns = {
        'ID': lambda value: value.isdigit(),
        'Name': lambda value: len(value.strip()) > 0,
        'Identity': lambda value: len(value.strip()) > 0,
        'Alignment': lambda value: value in ['Good', 'Bad', 'Neutral'],
        'EyeColor': lambda value: len(value.strip()) > 0,
        'HairColor': lambda value: len(value.strip()) > 0,
        'Gender': lambda value: value in ['Male', 'Female'],
        'Status': lambda value: value in ['Living', 'Deceased'],
        'Appearances': lambda value: value.isdigit(),
        'FirstAppearance': lambda value: len(value.strip()) > 0,
        'Year': lambda value: value.isdigit(),
        'Universe': lambda value: len(value.strip()) > 0
    }

    invalid_columns = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for column, value in row.items():
                validator = valid_columns.get(column)
                if validator is not None and not validator(value):
                    invalid_columns.append(column)

    if invalid_columns:
        return False, set(invalid_columns)
    else:
        return True, None


def check_duplicates(data):
    unique_rows = []
    duplicate_rows = []

    for row in data:
        if row in unique_rows:
            duplicate_rows.append(row)
        else:
            unique_rows.append(row)

    if duplicate_rows:
        print("Duplicate rows found. Removing duplicates...")
        cleaned_data = [row for row in data if row not in duplicate_rows]
        return cleaned_data
    else:
        print("No duplicate rows found.")
        return data


def check_null_empty_rows(data):
    updated_data = []
    null_empty_rows = []

    for row_idx, row in enumerate(data):
        null_values = [col_idx + 1 for col_idx, value in enumerate(row) if value.strip() == ""]
        if len(null_values) == len(row) or all(value.strip() == "" for value in row):
            null_empty_rows.append(row_idx + 1)
        else:
            updated_data.append(row)

    if null_empty_rows:
        print("Null or empty rows found. Removing rows:", null_empty_rows)
    else:
        print("No null or empty rows found.")

    return updated_data
