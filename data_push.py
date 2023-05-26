import mysql.connector


def write_to_mysql_database(data, host, user, password, database, table_name):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()

    # Check if the table exists
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    table_exists = cursor.fetchone()

    if not table_exists:
        # Create the table
        headers = ['ID', 'Name', 'Identity', 'Alignment', 'EyeColor', 'HairColor', 'Gender', 'Status', 'Appearances',
                   'FirstAppearance', 'Year', 'Universe']
        create_table_query = f"CREATE TABLE {table_name} ({', '.join(f'`{header}` VARCHAR(255)' for header in headers)})"
        cursor.execute(create_table_query)

        headers_str = ', '.join(headers)
        values_placeholder = ', '.join(['%s'] * len(headers))
        insert_query = f"INSERT INTO {table_name} ({headers_str}) VALUES ({values_placeholder})"
        cursor.executemany(insert_query, data)

    connection.commit()
    connection.close()
