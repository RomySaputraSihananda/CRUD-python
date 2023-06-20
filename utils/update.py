from . import Read;
from . import Database;

def update():
    Read.read();
    print(f'\n|{"Update Data":^48}|')
    print('-' * 50);
    
    no = int(input('Pilih nomor : '));
    data = Read.read(index=no).split(',');
    if(not data):
       print('salah...');
       return;
    
    write_data(data, no);
    Read.read();


def write_data(new_data, no):
    data = get_data(new_data);
    data_str = f'{data["id"]},{data["nama"]},{data["jurusan"]},{data["kelas"]},{data["date"]}';

    try:
        with open(Database.DB_NAME, 'r+', encoding='utf-8') as file:
            file.seek((len(data_str) + 1) * (no - 1));
            file.write(data_str);
    except:
        print('Errorrrrr........');


def get_data(data):
    new_data = Database.TEMPLATE.copy();

    new_data['id'] = data[0];
    new_data['nama'] = data[1] + Database.TEMPLATE['nama'][len(data[1]):];
    new_data['jurusan'] = data[2] + Database.TEMPLATE['jurusan'][len(data[2]):];
    new_data['kelas'] = str(data[3]) + Database.TEMPLATE['kelas'][len(str(data[3])):];
    new_data['date'] = data[4];
    
    while(True):
        rubah = input('\nApa yang diUpdate : ');  

        match(rubah):
            case 'nama':
                print('-' * 50);
                nama = input('Nama : ');  
                new_data['nama'] = nama + Database.TEMPLATE['nama'][len(nama):];
            case 'jurusan':
                print('-' * 50);
                jurusan = input('Jurusan : ');  
                new_data['jurusan'] = jurusan + Database.TEMPLATE['jurusan'][len(jurusan):];
            case 'kelas':
                print('-' * 50); 
                kelas = int(input('Kelas : '));  
                new_data['kelas'] = str(kelas) + Database.TEMPLATE['kelas'][len(str(kelas)):];
            case _:
                print('gak ada......');
        
        print('-' * 50); 
        lanjut = input('Lanjut Update : ');
        print('-' * 50); 
        if((lanjut == 'n') or (lanjut == 'N')): break;
    
    return new_data;
