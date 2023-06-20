from . import Database;
from . import Read;
from .Random import random_id;
import time;

def create_data():
    data = Database.TEMPLATE.copy();

    nama = input('nama \t: ');
    jurusan = input('jurusan : ');
    while(True):
        try:
            kelas = int(input('kelas \t: '));
            break;
        except:
            print('kelas harus angka.. bos');
    data['id'] = random_id(6);
    data['nama'] = nama + Database.TEMPLATE['nama'][len(nama):];
    data['jurusan'] = jurusan + Database.TEMPLATE['jurusan'][len(jurusan):];
    data['kelas'] = str(kelas) + Database.TEMPLATE['kelas'][len(str(kelas)):];
    data['date'] = time.strftime('%Y-%m-%d %H:%M:%S%z', time.gmtime());

    data_str = f'{data["id"]},{data["nama"]},{data["jurusan"]},{data["kelas"]},{data["date"]}\n';

    return data_str;

def create():
    print('-' * 50);
    print(f'|{"Create Data":^48}|')
    print('-' * 50);

    data = create_data();
   
    try:
        with open(Database.DB_NAME, 'a', encoding='utf-8') as file:
            file.write(data);
    except:
        print('kontoooooooool........');
   
    Read.read();