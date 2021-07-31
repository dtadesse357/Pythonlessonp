import time

username = 'flame77'
password = 'sick77'

username_user = input("ENTER YOUR USERNAME: ")
password_user = input("ENTER YOUR PASSWORD: ")

if username == username_user and password == password_user:
    print("ACCESS GRANTED")
    print('PLEASE WAIT')
    time.sleep(5)
    print('LOADING FILE #758494...')
    time.sleep(1)
    print('Ok... Loading.....')
    time.sleep(7)
    print('....')
    time.sleep(5)
    print("Alright you have clearance to access file #758494. Puilling it right up Sir.")
elif username != username_user and password == password_user:
    print("WRONG USERNAME")
elif username == username_user and password != password_user:
    print("WRONG PASSWORD")
else:
    print("TRY AGAIN! ACCESS DENIED!")
