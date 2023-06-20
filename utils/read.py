from . import Database;

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            data = file.readlines();
            jumlah_data = len(data);
            
            if 'index' in kwargs:
                index = kwargs['index'] - 1;
            
                if index > jumlah_data or index < 0:
                    display([data[index]]);
                    
                else:
                    display([data[index]]);
                    return data[index];
            
            else:
                display(data);

    except Exception as err:
        header();
        print(f'\n|{"---DATA KOSONG---":^48}|')
        print('-' * 50);

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