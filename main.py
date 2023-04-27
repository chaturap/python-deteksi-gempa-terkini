"""
Aplikasi deteksi gempa , data source dari BMKG
"""
#from gempaterkini import tampilkan_data, ekstrasi_data

import gempaterkini

if __name__ == '__main__':
    print("Aplikasi Utama")
    result = gempaterkini.ekstrasi_data()
    gempaterkini.tampilkan_data(result)
