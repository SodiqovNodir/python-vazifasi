

ism = ['Olim', 'Salim', 'Obit']
print(ism)

familya = ['Olimov', 'Salimov', 'Obidov1']
print(familya)

yosh = [14, 53, 23]
print(yosh)

while True:
    import os
    ism = input('Ismingizni kiriting: ')
    familya = input('Familyangizni kiriting: ')
    yosh = input('Yoshingizni kiriting: ')
    tel = input('telefon raqamingizni kiriting: ')
    elektron_p = input('Email ni kiriting: ')
    manzil = input('manzilingizni kiriting: ')

    if yosh.isdigit():
        yosh = int(yosh)
        print(yosh)

    while True:
        if tel.startswith("+998"):
            break
        else:
            print("Iltimos telefon raqmingizni togri kiriting.")

    fayl_nomi = 'users_info.txt'

    def o_idni_olish():
        if os.path.exists(fayl_nomi):
            with open(fayl_nomi, 'r') as file:
                l = file.readlines()
                if l:
                    qator = l[-1]
                    id_qator = int(qator.split(',')[0])
                    return id_qator
        return 0


    def faylga_qoshish(malumot):
        with open(fayl_nomi, 'a') as file:
            file.write(
                f"{malumot['id']},{malumot['ism']},{malumot['familya']},{malumot['yosh']},{malumot['telefon']},{malumot['elektron_pochta']},{malumot['manzil']}")


    o_id = o_idni_olish()
    y_id = o_id + 1

    mal = {
        'id' : y_id,
        'ism' : ism,
        'familya' : familya,
        'yosh' : yosh,
        'telefon' : tel,
        'elektron_pochta' : elektron_p,
        'manzil' : manzil
    }

    faylga_qoshish(mal)