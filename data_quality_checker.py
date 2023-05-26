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
