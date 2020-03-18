import psycopg2
import csv

#covid_file = open('csv\COVID19_line_list_data.csv', 'r')

connection = psycopg2.connect("host = 'localhost' port = '5432' dbname = 'covid-19' user = 'postgres' password = 'starwars'")
cursor = connection.cursor()

drop_table = "DROP TABLE IF EXISTS cases"

cursor.execute(drop_table)
connection.commit()

command = """
    CREATE TABLE cases(
        id integer PRIMARY KEY,
        case_in_country VARCHAR,
        reporting_date VARCHAR,
        Column1 VARCHAR,
        summary VARCHAR,
        location VARCHAR,
        country VARCHAR,
        gender VARCHAR,
        age VARCHAR,
        symptom_onset VARCHAR,
        if_onset_approximated VARCHAR,
        hosp_visit_date VARCHAR,
        exposure_start VARCHAR,
        exposure_end VARCHAR,
        visiting_Wuhan VARCHAR,
        from_wuhan VARCHAR,
        death VARCHAR,
        recovered VARCHAR,
        symptom VARCHAR, 
        source VARCHAR,
        link VARCHAR
    )
"""

cursor.execute(command)
connection.commit()

with open('csv\COVID19_line_list_data.tsv', 'r', encoding='utf-8') as f:
    print(next(f))
    cursor.copy_from(f, 'cases')

connection.commit()

connection.close()