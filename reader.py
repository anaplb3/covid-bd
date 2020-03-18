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
        case_in_country INTEGER,
        reporting_date TEXT,
        Column1 TEXT,
        summary TEXT,
        location TEXT,
        country TEXT,
        gender TEXT,
        age TEXT,
        symptom_onset TEXT,
        if_onset_approximated TEXT,
        hosp_visit_date TEXT,
        exposure_start TEXT,
        exposure_end TEXT,
        visiting_Wuhan BOOLEAN,
        from_wuhan BOOLEAN,
        death INTEGER,
        recovered TEXT,
        symptom TEXT, 
        source TEXT,
        link TEXT,
        _1 TEXT,
        _2 TEXT,
        _3 TEXT,
        _4 TEXT,
        _5 TEXT,
        _6 TEXT
    )
"""

cursor.execute(command)
connection.commit()

with open('csv\COVID19_line_list_data1.csv', 'r', encoding='utf-8') as f:
    print(next(f))
    cursor.copy_from(f, 'cases', sep=',')

connection.commit()

connection.close()