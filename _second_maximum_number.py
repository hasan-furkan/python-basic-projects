# bir liste verilecek
# listede en buyuk ikinci sayi bulunacak
# bulunan sayi dondurulecek 
    
if __name__ == '__main__':
    n = [2, 3 ,6, 6, 5]
    arr = map(int, input().split())
    print(arr)
    print(arr[-2])
# bu sekilde de cozuluyor fakat iki tane en buyuk sayidan ayni olunca hata veriyor
    print(sorted(set(arr),reverse=True)[1])
# o yuzden en mantikli ve hizli cozum bu sekilde
