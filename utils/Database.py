from . import Create;

DB_NAME = 'siswa.txt';
TEMPLATE = {
    'id': 'xxxxxx',
    'date': 'yyyy-mm-dd HH:MM:SS+',
    'nama': 255 * ' ',
    'jurusan': 4 * ' ',
    'kelas': 2 * ' '
} 

def init_console():
    try:
        with open(DB_NAME, 'r') as file:
            print('ok........');
    except:
        Create.create();
