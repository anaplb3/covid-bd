from bd.config import create_connection
import psycopg2

class CaseService:

    def get_case(self, uuid):
        cursor = create_cursor()

        query = "SELECT id, country, gender, age, death FROM cases WHERE id = {}".format(uuid)
        cursor.execute(query)
        case = list(cursor.fetchone())
        print(case)
        death = case[4]
        case[4] = self.convert_string_to_boolean(CaseService, death)

        return case
    
    def convert_string_to_boolean(self, death):
        if death == "0" or death == "1":
            return False
        else:
            return True

def create_cursor():
    connection = psycopg2.connect("host = 'localhost' port = '5432' dbname = 'covid-19'" 
    + "user = 'postgres' password = 'starwars'")
    return connection.cursor()