if __name__ == '__main__':
    str = '''62 0A 0A 7F 20 05 0A 7D 47 20 14 0A 10 20 0E 0A
07 11 00 7F 20 0A 09 00 20 08 0A 0D 00 20 7E 03
7C 07 07 00 09 02 00 20 04 09 20 14 0A 10 0D 20
05 0A 10 0D 09 00 14 49 20 6F 03 04 0E 20 0A 09
00 20 12 7C 0E 20 01 7C 04 0D 07 14 20 00 7C 0E
14 20 0F 0A 20 7E 0D 7C 7E 06 49 20 72 7C 0E 09
42 0F 20 04 0F 5A 20 4C 4D 53 20 06 00 14 0E 20
04 0E 20 7C 20 0C 10 04 0F 00 20 0E 08 7C 07 07
20 06 00 14 0E 0B 7C 7E 00 47 20 0E 0A 20 04 0F
20 0E 03 0A 10 07 7F 09 42 0F 20 03 7C 11 00 20
0F 7C 06 00 09 20 14 0A 10 20 0F 0A 0A 20 07 0A
09 02 20 0F 0A 20 7F 00 7E 0D 14 0B 0F 20 0F 03
04 0E 20 08 00 0E 0E 7C 02 00 49 20 72 00 07 07
20 7F 0A 09 00 47 20 14 0A 10 0D 20 0E 0A 07 10
0F 04 0A 09 20 04 0E 20 07 01 02 0B 02 03 07 0E
7C 0D 7F 00 49 '''
    str = str.split()
    print(str)

    for j in range(0, 256):
        for i in str:
            print(chr((int(i,16)+j)%128), end='')
        print()
