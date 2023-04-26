"""
Aplikasi deteksi gempa , data source dari BMKG
"""
from gempaterkini import tampilkan_data, ekstrasi_data

if __name__ == '__main__':
    print("Aplikasi Utama")
    result = ekstrasi_data()
    tampilkan_data(result)
