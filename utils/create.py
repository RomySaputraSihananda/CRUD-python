from . import Database;
from .Random import random_id;
import time;

def create():
    data = Database.TEMPLATE.copy();

    nama = input('nama \t: ');
    jurusan = input('jurusan : ');
    kelas = input('kelas \t: ');

    data['id'] = random_id(6);
    data['nama'] = nama + Database.TEMPLATE['nama'][len(nama):];
    data['jurusan'] = jurusan + Database.TEMPLATE['jurusan'][len(jurusan):];
    data['kelas'] = kelas + Database.TEMPLATE['kelas'][len(kelas):];
    data['date'] = time.strftime('%Y-%m-%d %H:%M:%S%z', time.gmtime());
    
    data_str = f'{data["id"]},{data["nama"]},{data["jurusan"]},{data["kelas"]},{data["date"]}\n';
    
    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str);
    except:
        print('kontoooooooool........');