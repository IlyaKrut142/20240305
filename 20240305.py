import csv

def read_csv(filename):
    with open(filename, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        return list(reader)
def find_telephone(data, fio):
    for record in data:
        if record['FIO'] == fio:
            return record['Telephone']
    return 'Телефон не найден'# Чтение данных из файла
data = read_csv('FIOandTelephone.csv')

def main():
    fio = input('Введите ФИО для поиска: ')
    telephone = find_telephone(data, fio)
    if telephone != 'Телефон не найден':
        print(f'Номер телефона: {telephone}')
    else:
        print(telephone)# Вызов основной функции
if __name__ == "__main__":
    main()

