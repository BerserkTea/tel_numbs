import csv


def csv_to_data(file_name='PhoneBook.csv'):
    with open(file_name, newline='', encoding='UTF8') as f:
        csv_f = csv.reader(f, delimiter=';')
        data = []
        for row in csv_f:
            data.append(row)
    return data


def export_to_xml(data=csv_to_data()):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<contacts>\n'
    for row in data:
        xml += '    <contact>\n'
        xml += '        <id>{}</id>\n' \
            .format(row[0])
        xml += '        <Last_name>{}</Last_name>\n' \
            .format(row[1])
        xml += '        <Name>{}</Name>\n' \
            .format(row[2])
        xml += '        <Phone_number>{}</Phone_number>\n' \
            .format(row[3])
        xml += '        <Info>{}</Info>\n' \
            .format(row[4])
        xml += '    </contact>\n'
    xml += '</contacts>'
    with open('phonebook.xml', 'w', encoding='UTF8') as page:
        page.write(xml)
    return data

