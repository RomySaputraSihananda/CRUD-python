from . import Database;

def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            data = file.readlines();
            display(data);
    except Exception as err:
        print(err);

def header():
        print('-' * 50);
        print(f'|{"No":^4}|{"nama":^25}|{"jurusan":^9}|{"kelas":^7}|')
        print('-' * 50, end='');

def main(data):
    for i, data in enumerate(data):
        data_split = data.split(',');
        print();
        print(f'|{i + 1:^4}|{data_split[1]:.25}|{data_split[2]:^9}|{data_split[3]:^7}|')
        print('-' * 50, end='');
     

def display(data):
    header();
    main(data);