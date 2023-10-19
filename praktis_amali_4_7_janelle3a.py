'''Ini merupakan satu program ringkas untuk mendapatkan isipadu kuboid'''
pi=3.142
def kira_kuboid(tinggi,panjang,lebar):
    isipadu_kuboid=tinggi*panjang*lebar
    return isipadu_kuboid
    
def kuboid(): #Isipadu kuboid
    tinggi=float(input("Masukkan panjang:"))
    panjang=float(input("Masukkan panjang:"))
    lebar=float(input("Masukkan lebar:"))
    print("Isipadu kuboid=",kira_kuboid(tinggi,panjang,lebar))
    
def kira_silinder(pi,jejari,tinggi):
    isipadu_silinder=pi*(jejari**2)*(tinggi)
    return isipadu_silinder
    
def silinder(): #Isipadu silinder
    jejari=int(input("Masukkan jejari:"))
    tinggi=int(input("Masukkkan tinggi:"))
    print("Isipadu silinder",kira_silinder(pi,jejari,tinggi))
    
def kira_kon(pi,jejari,tinggi):
    isipadu_kon=(1/3)*pi*(jejari**2)*(tinggi)
    return isipadu_kon
    
def kon(): #Isipadu kon
    jejari=int(input("Masukkan jejari"))
    tinggi=int(input("Masukkan tinggi"))
    print("Isipadu kon=",kira_kon(pi,jejari,tinggi))
    
def kira_sfera(pi,jejari):
    isipadu_sfera=4/3*pi*(jejari**3)
    return isipadu_sfera
    
def sfera(): #Isipadu sfera
    jejari=int(input("Masukkan jejar:"))
    print("Isipadu sfera=",kira_sfera(pi,jejari))
#######################
#Subatur cara uatama
#######################
ulang=True

while(ulang):
    print(
'''
    ******************************
    *   MENU MENGIRA ISIPADU     *
    ******************************
    1.kuboid
    2.silinder
    3.kon
    4.sfera
    5.tamat program
''')
    print("")
    
    pilih=int(input("Sila masukkan pilihan anda:"))
    
    if (pilih==1):
        kuboid()   #memanggil fungsi kuboid
    elif(pilih==2):
        silinder()   #memanggil fungsi silinder
    elif(pilih==3):
        kon()         #memanggil fungsi kon
    elif(pilih==4):
        sfera()          #memanggil fungsi sfera
    elif(pilih==5):
        ulang=False
        print("Bye Bye")
        exit
    else:
        print("Pilihan tiada dalam senari")
        print("")