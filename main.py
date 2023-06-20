from os import system
from utils import menu, create, read, update, delete, init_console;

if(__name__ == '__main__'):
    init_console();
    while True:
        system('clear');
        menu();
        
        option = int(input('Massukan opsi : '));

        match(option):
            case 1:
                read();
            case 2:
                create();
            case 3:
                update();
            case 4:
                delete();
            case _:
                print('salah blok......');
        
        lanjut = input('\nLanjut : ');
        if((lanjut == 'n') or (lanjut == 'N')): break;

    print('tq');
