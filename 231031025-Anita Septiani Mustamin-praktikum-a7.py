pass_bnr = "jeje23"
percobaan = 3
a = True
while a:
    masukan = input("masukkan password: ")
    if masukan == pass_bnr:
        print("selamat anda login!")
        a = False
    else: 
        if percobaan == 0: 
            print("Akun Anda Terblokir")
            a = False
        else:
            print("password yang anda masukkan salah! coba lagi")
            percobaan -= 1