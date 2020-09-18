import json, csv


class IStructureDriver:
    def red(self):
        pass

    def write(self, d):
        pass


class JsonDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def write(self, d):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(d, f)
            f.flush()


class CSVDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r', newline='') as f:
            r_lst = []
            reader = csv.reader(f, delimiter=';', quotechar='"')
            for row in reader:
                for el in row:
                    r_lst.append(el)
            return r_lst

    def write(self, d):
        with open(self.filename, 'w', newline='') as f:
            csv_writer = csv.writer(f, delimiter=';', quotechar='"')
            csv_writer.writerow(d)


if __name__ == '__main__':
    pass
