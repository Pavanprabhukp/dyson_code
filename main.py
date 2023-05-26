import data_pull
import data_push
from data_quality_checker import check_duplicates, check_null_empty_rows, check_csv_columns

# Configurations
csv_file_path = 'data.csv'  # Replace with the actual path to your CSV file
output_db_file = 'output/cleaned_data.db'  # Replace with the desired output database file path
host = 'localhost'  # Replace with the MySQL host
user = 'root'  # Replace with your MySQL username
password = 'Mysql@2023'  # Replace with your MySQL password
database = 'learning'  # Replace with your MySQL database name
table_name = 'cleaned_data'  # Replace with the desired table name

if __name__ == '__main__':
    filename = 'data.csv'
    # Reading the File(Injection)
    csv_data = data_pull.read_csv_file(filename)

    # Running Data Quality Checks (Transformation)
    valid, invalid_columns = check_csv_columns(csv_file_path)
    if valid:
        print("All Columns are valid")
    else:
        print('Invalid Columns:', invalid_columns)

    check_dup_data = check_duplicates(csv_data)
    updated_data = check_null_empty_rows(check_dup_data)

    # Writing the Data into Database (Loading)
    data_push.write_to_mysql_database(updated_data, host, user, password, database, table_name)
