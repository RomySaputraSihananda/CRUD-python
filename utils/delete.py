from . import Read;
from . import Database;
import os;

def delete():
    Read.read();
    print(f'\n|{"Delete Data":^48}|')
    print('-' * 50);
   
    while(True):
        no = int(input('Pilih nomor : '));
        data = Read.read(index=no).split(',');
        
        if(not data):
            print('salah...');
            return;
        
        yakin = input('\nYakin dek : ');

        if((yakin == 'y') or (yakin == 'Y')):
            delete_data(no);
            Read.read();
            break;

def delete_data(no):
    try:
        with open(Database.DB_NAME, 'r') as file:
            counter = 0;
            while(True):
                data = file.readline();

                if(len(data) == 0):
                    break;
                elif(counter == no - 1):
                    pass;
                else:
                    with open('data_temp.txt', 'a', encoding='utf-8') as temp_file:
                        temp_file.write(data);
                counter += 1;
    except:
        print('errrrrrr..............');
    os.remove(Database.DB_NAME);
    os.rename('data_temp.txt', Database.DB_NAME);