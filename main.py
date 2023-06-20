from os import system
from utils import menu, create, read, update, delete, footer;

if(__name__ == '__main__'):
    while True:
        system('clear');
        menu();
        
        option = int(input('Massukan Opsi : '));

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
        
        lanjut = input('\nLanjut Program : ');
        if((lanjut == 'n') or (lanjut == 'N')): break;
    footer();

