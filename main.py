from os import system
from utils import menu, create, read, update, delete;

if(__name__ == '__main__'):
    while True:
        system('cls');
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
        
        lanjut = input('Lanjut : ');
        if((lanjut == 'n') or (lanjut == 'N')): break;

    print('tq');
