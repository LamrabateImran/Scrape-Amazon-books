import app
import pandas as pd

def entry(choice):
    if choice == 'AA':
        df = pd.DataFrame(app.Action_Adventure(),['Name','Rang','Price','Edition','Stars'])
        writer = pd.ExcelWriter('Fav Books.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Action Adventure')
        writer.save()
        
        print('''\n Do you choose again ? or you quit the app ?''')
        reset = input(' Write c for Choose OR q for Quit: ')
        if reset == 'c':
            make_choice()
        elif reset == 'q':
            print('See you again !')
            exit()
        
    elif choice == 'AFP':
        df = pd.DataFrame(app.Arts_Film_Photography(),['Name','Rang','Price','Edition','Stars'])
        writer = pd.ExcelWriter('Fav Books.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Arts Film Photography')
        writer.save()  
        
        print('''\n Do you choose again ? or you quit the app ?''')
        reset = input(' Write c for Choose OR q for Quit: ')
        if reset == 'c':
            make_choice()
        elif reset == 'q':
            print('See you again !')
            exit() 
            
    elif choice == 'BDA':
        df = pd.DataFrame(app.Biographies_Diaries_Accounts(),['Name','Rang','Price','Edition','Stars'])
        writer = pd.ExcelWriter('Fav Books.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Biographies Diaries Accounts')
        writer.save()
        
        print('''\n Do you choose again ? or you quit the app ?''')
        reset = input(' Write c for Choose OR q for Quit: ')
        if reset == 'c':
            make_choice()
        elif reset == 'q':
            print('See you again !')
            exit() 
    
    elif choice == 'BE':
        df = pd.DataFrame(app.Business_Economics(),['Name','Rang','Price','Edition','Stars'])
        writer = pd.ExcelWriter('Fav Books.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Business Economics')
        writer.save()
        
        print('''\n Do you choose again ? or you quit the app ?''')
        reset = input(' Write c for Choose OR q for Quit: ')
        if reset == 'c':
            make_choice()
        elif reset == 'q':
            print('See you again !')
            exit() 
        
    elif choice == 'CY':
        df = pd.DataFrame(app.Children_YoungAdult(),['Name','Rang','Price','Edition','Stars'])
        writer = pd.ExcelWriter('Fav Books.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Children YoungAdult()')
        writer.save()
        
        print('''\n Do you choose again ? or you quit the app ?''')
        reset = input(' Write c for Choose OR q for Quit: ')
        if reset == 'c':
            make_choice()
        elif reset == 'q':
            print('See you again !')
            exit() 

def make_choice():
    print("""
    Action Adventure = AA
    Arts Film Photography = AFP
    Biographies Diaries Accounts = BDA
    Business Economics = BE
    Children YoungAdult = CY
    """)
    choice = input('Choose your Favorite Books : ')
    if choice == 'AA' or choice == 'AFP' or choice == 'BDA' or choice == 'BE' or choice == 'CY':
        entry(choice)
        exit()
    else:
        print('''PLEASE choose again your Favorite Books : ''')
        make_choice()

make_choice()
