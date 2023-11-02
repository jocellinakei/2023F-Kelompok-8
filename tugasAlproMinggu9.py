print("======================================")
print(" Selamat Datang di Python Pizza ^_^ ")
print("Anda bisa mendapatkan pizza favoritmu disini!")
print("======================================")

hargaPizza = 0

# Pelanggan memilih topping pizza
print("Topping pizza yang tersedia: ")
print("Frankfurter BBQ")
print("Meat Monsta")
print("Super Supreme")
print("Super Supreme Chicken")
print("Meat Lovers")
MenuPizza = input("Silahkan pilih topping favorit anda: ")
MenuPizza = MenuPizza.lower()
if MenuPizza in ["frankfurter bbq", "meat monsta", "super supreme", "super supreme chicken", "meat lovers"]:
    hargaPizza = 43637
else:
    hargaPizza = 0
    print("Maaf, Topping pizza yang anda pilih tidak tersedia")

# Pelanggan memilih crust pizza
print("Pilihan Crust: ")
print("Pan")
print("StuffedCrust Cheese")
print("StuffedCrust Sausage")
print("Cheesy Bites")
print("Crown Crust")
CrustPizza = input("Silahkan pilih crust pizza favorit anda: ")
CrustPizza = CrustPizza.lower()

if CrustPizza == "pan":
    # Pelanggan memilih ukuran pizza
    print("Ukuran pizza:")
    print("personal")
    print("regular")
    print("large")
    sizePizza = input("Silahkan pilih ukuran pizza anda: ")
    #Apakah ingin menambah keju?
    cheese = input("Ingin menambahkan keju? (iya/tidak): ")
    if sizePizza == "personal":
        hargaPizza += 0
        if cheese == "iya":
            hargaPizza += 13636 
        elif cheese == "tidak":
            hargaPizza += 0
        else:
            print("Baik, Tidak menggunakan keju")
    elif sizePizza == "regular":
        hargaPizza += 57273 
        if cheese == "iya":
                hargaPizza += 16364 
        elif cheese == "tidak":
                hargaPizza += 0
        else:
            print("Baik, Tidak menggunakan keju")
    elif sizePizza == "large":
        hargaPizza += 89091 
        if cheese == "iya":
            hargaPizza += 19091 
        elif cheese == "tidak":
                hargaPizza += 0
        else:
            print("Baik, Tidak menggunakan keju")
    else:
        print("Maaf tidak tersedia ukuran pizza lain")
elif CrustPizza == "stuffedcrust cheese":
    # Pelanggan memilih ukuran pizza
    print("Ukuran pizza:")
    print("personal")
    print("regular")
    print("large")
    sizePizza = input("Silahkan pilih ukuran pizza anda: ")
    #Apakah ingin menambah keju?
    cheese = input("Ingin menambahkan keju? (iya/tidak): ")
    if sizePizza == "personal":
        hargaPizza += 11818
        if cheese == "iya":
            hargaPizza += 13636
        elif cheese == "tidak":
            hargaPizza += 0
        else:
            print("Baik, tidak menggunakan keju")
    elif sizePizza == "regular":
        hargaPizza += 77273
        if cheese == "iya":
            hargaPizza += 16364
        elif cheese == "tidak":
            hargaPizza+= 0
        else:
            print("Baik, tidak menggunakan keju")
    elif sizePizza == "large":
        hargaPizza += 116363
        if cheese == "iya":
            hargaPizza += 19091
        elif cheese == "tidak":
            hargaPizza += 0
        else:
            print("Baik, tidak menggunakan keju")
    else:
        print("Maaf tidak tersedia ukuran pizza lain")
elif CrustPizza == "stuffedcrust sausage":
    # Pelanggan memilih ukuran pizza
    print("Ukuran pizza:")
    print("personal")
    print("regular")
    print("large")
    sizePizza = input("Silahkan pilih ukuran pizza anda: ")
    #Apakah ingin menambah keju?
    cheese = input("Ingin menambahkan keju? (iya/tidak): ")
    if sizePizza == "personal":
        hargaPizza += 9091
        if cheese == "iya":
            hargaPizza += 13636
        elif cheese == "tidak":
            hargaPizza += 0
        else:
            print("Baik, tidak menggunakan keju")
    elif sizePizza == "regular":
        hargaPizza += 73636
        if cheese == "iya":
            hargaPizza += 16364
        elif cheese == "tidak":
            hargaPizza += 0
        else:
            print("Baik, tidak menggunakan keju")
    elif sizePizza == "large":
        hargaPizza += 111818
        if cheese == "iya":
            hargaPizza += 19091
        elif cheese == "tidak":
            hargaPizza += 0
        else:
            print("Baik, tidak menggunakan keju")
    else:
        print("Maaf tidak tersedia ukuran pizza lain")
elif CrustPizza == "cheesy bites":
    # Pelanggan memilih ukuran pizza
    print("Ukuran pizza:")
    print("personal")
    print("regular")
    print("large")
    sizePizza = input("Silahkan pilih ukuran pizza anda: ")
    #Apakah ingin menambah keju?
    cheese = input("Ingin menambahkan keju? (iya/tidak): ")
    if sizePizza == "personal":
        hargaPizza += 13636
        if cheese == "iya":
            hargaPizza += 13636
        elif cheese == "tidak":
            hargaPizza += 0
        else:
            print("Baik, tidak menggunakan keju")
    elif sizePizza == "regular":
        hargaPizza += 80000
        if cheese == "iya":
            hargaPizza += 16364
        elif cheese == "tidak":
            hargaPizza += 0
        else:
            print("Baik, tidak menggunakan keju")
    elif sizePizza == "large":
        hargaPizza += 120909
        if cheese == "iya":
 hargaPizza += 19091
        elif cheese == "tidak":
            hargaPizza += 0
        else:
            print("Baik, tidak menggunakan keju")
    else:
        print("Maaf tidak tersedia ukuran pizza lain")
elif CrustPizza == "crown crust":
    # Pelanggan memilih ukuran pizza
    print("Ukuran pizza:")
    print("personal")
    print("regular")
    print("large")
    sizePizza = input("Silahkan pilih ukuran pizza anda: ")
    #Apakah ingin menambah keju?
    cheese = input("Ingin menambahkan keju? (iya/tidak): ")
    if sizePizza == "personal":
        hargaPizza += 11818
        if cheese == "iya":
            hargaPizza += 13636
        elif cheese == "tidak":
            hargaPizza += 0
        else:
            print("Baik, tidak menggunakan keju")
    elif sizePizza == "regular":
        hargaPizza += 77273
        if cheese == "iya":
            hargaPizza += 16364
        elif cheese == "tidak":
            hargaPizza += 0
        else:
            print("Baik, tidak menggunakan keju")
    elif sizePizza == "large":
        hargaPizza += 116363
        if cheese == "iya":
            hargaPizza += 19091
        elif cheese == "tidak":
            hargaPizza += 0
        else:
            print("Baik, tidak menggunakan keju")
    else:
        print("Maaf tidak tersedia ukuran pizza lain")
else:
    hargaPizza += 0
    print("Maaf, Crust yang anda pilih tidak tersedia")


# Total harga ditambah biaya pajak restoran
taxs = 1.0
totalharga = hargaPizza
TotalTaxs = totalharga * (taxs / 100)
TotalhargaPizza = totalharga + TotalTaxs

#cara pembayaran
print ("Silahkan pilih pembayaran : ")
print("Tunai, Kartu Kredit, Kartu Debit")
pembayaran = input()
if pembayaran == "Tunai" or pembayaran == "Kartu Kredit" or pembayaran == "Kartu Debit":
    if pembayaran == "Tunai":
        TotalhargaPizza += 0
elif pembayaran == "Kartu Kredit":
    TotalhargaPizza += 2500

#menampilkan nota pembelian customer
print("========================")
print("""YOURS RECEPTION""")
print("Order Pizza with this detail :")
print("Your topping : ", MenuPizza
    , "Your Crust : ", CrustPizza
    , "Your Size : ", sizePizza
    , "Extra Cheese : ", cheese)
print("Payment : ", pembayaran)
print("Total : Rp.", totalharga)
print("Taxs : {: .2f}%" .format(TotalTaxs))
print("Your Bill : Rp.", TotalhargaPizza)
print("=========================")
