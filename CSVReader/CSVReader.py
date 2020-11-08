import csv


class CSVReader:
    def __init__(self, file_path):
        self.data = []
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                self.data.append(row)
        pass
