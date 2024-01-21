import csv
import os


class import_export:
    def __init__(self, path):
        self.path = path

    def export_passwords(self, data):
        with open(self.path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "Password", "URL", "Notes"])
            for i in data:
                writer.writerow([i[0], i[1], i[2], i[3]])

    def import_passwords(self):
        data = []
        with open(self.path, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
            return data

    def delete(self):
        os.remove(self.path)

# if __name__ == "__main__":
#     llave = b"-vn-5Gh28Z3gcyfArydyKE-5uzXN8giqbesjhtVsJsQ="
#     # import_export("Passwords.csv").export([["test", "test", "test", "test"]])
#     print(import_export(
#         "./ArchivosTemporales/Contraseñas de Microsoft Edge personal.csv ").import_passwords())
#     # import_export("Passwords.csv").delete()
