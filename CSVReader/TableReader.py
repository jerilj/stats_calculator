import csv


class TableReader:
    def __init__(self, file_path):
        self.data = []
        self.header = None
        row_count = 0
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row_count == 0:
                    self.header = row
                else:
                    self.data.append(row)
                row_count = row_count+1
        pass