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
    
    # data['id'] = random_id(6);
    # data['nama'] = nama + Database.TEMPLATE['nama'][len(nama):];
    # data['jurusan'] = jurusan + Database.TEMPLATE['jurusan'][len(jurusan):];
    # data['kelas'] = str(kelas) + Database.TEMPLATE['kelas'][len(str(kelas)):];
    # data['date'] = time.strftime('%Y-%m-%d %H:%M:%S%z', time.gmtime());

    # data_str = f'{data["id"]},{data["nama"]},{data["jurusan"]},{data["kelas"]},{data["date"]}\n';

    # return data_str;

    while(True):
        rubah = input('\napa yang dirubah : ');  

        match(rubah):
            case 'nama':
                nama = input('\nNama : ');  
                new_data['nama'] = nama + Database.TEMPLATE['nama'][len(nama):];
            case 'jurusan':
                jurusan = input('\nJurusan : ');  
                new_data['jurusan'] = jurusan + Database.TEMPLATE['jurusan'][len(jurusan):];
            case 'kelas':
                kelas = int(input('\nKelas : '));  
                new_data['kelas'] = str(kelas) + Database.TEMPLATE['kelas'][len(str(kelas)):];
            case _:
                print('gak ada......');
        
        lanjut = input('\nLanjut Update : ');
        if((lanjut == 'n') or (lanjut == 'N')): break;
    
    return new_data;
