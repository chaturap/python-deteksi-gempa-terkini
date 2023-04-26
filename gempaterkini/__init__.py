
def ekstrasi_data():
    """
tanggal : 26 April 2023,
waktu : 09:56:27 WIB
Magnitudo :     4.7
Kedalaman : 61 km
Lokasi :  4.77 LU - 95.56 BT
Pusat gempa : Pusat gempa berada di darat 15 km BaratLaut Calang
Dirasakan : Dirasakan (Skala MMI): II Aceh Besar, II Banda Aceh
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '26 April 2023'
    hasil['waktu'] = '09:56:27 WIB'
    hasil['magnitudo'] = 4.7
    hasil['kedalaman'] = '61 km'
    hasil['lokasi'] = '4.77 LU - 95.56 BT'
    hasil['pusat_gempa'] = 'Pusat gempa berada di darat 15 km BaratLaut Calang'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II Aceh Besar, II Banda Aceh'

    return hasil




def tampilkan_data(result):
    print('gempa terakhir berdasarkan BMKG')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi : {result['lokasi']}")
    print(f"Pusat_gempa : {result['pusat_gempa']}")
    print(f"Dirasakan : {result['dirasakan']}")

    #pass