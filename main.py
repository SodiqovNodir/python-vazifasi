

ism = ['Olim', 'Salim', 'Obit']
print(ism)

familya = ['Olimov', 'Salimov', 'Obidov1']
print(familya)

yosh = [14, 53, 23]
print(yosh)

while True:
    ism = input('Ismingizni kiriting: ')
    familya = input('Familyangizni kiriting: ')
    yosh = input('Yoshingizni kiriting: ')
    tel = input('telefon raqamingizni kiriting: ')
    elektron_p = input('Email ni kiriting: ')
    manzil = input('manzilingizni kiriting: ')

    if yosh.isdigit():
        yosh = int(yosh)
        print(yosh)
    

