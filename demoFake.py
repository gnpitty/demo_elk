import uuid
from faker import Faker
import csv



def  genPersonas(locale,numero,gender):
     fake = Faker(locale)
     lista = []
     for i in range(1,numero):
        forname=""
        if gender == "F":
           forname= fake.first_name_female()
        else:
           forname = fake.first_name_male()
        surname = fake.last_name()
        person_id = fake.msisdn()
        document_id = fake.passport_number()


        fecha_nac = fake.date_of_birth()
        birth_mm =fecha_nac.month
        birth_dd= fecha_nac.day
        birth_yyyy= fecha_nac.year
        dat_id = uuid.uuid4().hex
       # lista.append( {'dat_id':dat_id,'birth_yyyy':birth_yyyy,'birth_mm':birth_mm,'birth_dd':birth_dd,'gender':gender,'forname':forname,'surname':surname,'person_id':person_id,'document_id':document_id})
        lista.append(  [ dat_id,birth_yyyy,   birth_mm,  birth_dd,  gender,  forname, surname,  person_id,   document_id,  ])
     return lista

data = genPersonas("FR",5,"F") + genPersonas("ES",5,"F") + genPersonas("EN",5,"F")
data = data + genPersonas("ja_JP",5,"M")
for i in data:
     print(i)


csv_file_name = "datos/output.csv"

# Write the list to the CSV file
with open(csv_file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file_name}' created successfully.")
