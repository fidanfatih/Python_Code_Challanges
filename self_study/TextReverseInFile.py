#Girilen metni dosyaya yazdırıp, tersini tekrar aynı dosyanın altına yazdırıp, tüm dosyayı terminale yazdıran program.

with open("sample.txt","w",encoding="utf-8") as fileObject:
    text="İSTİKLAL MARŞI\n" \
         "Korkma, sönmez bu şafaklarda yüzen al sancak;\n" \
         "Sönmeden yurdumun üstünde tüten en son ocak.\n" \
         "O benim milletimin yıldızıdır, parlayacak;\n" \
         "O benimdir, o benim milletimindir ancak.\n"
    fileObject.write(text)

with open("sample.txt","a+",encoding="utf-8") as fileObject:
    fileObject.seek(0)
    text=fileObject.read()
    reversedText=text[::-1]
    fileObject.write(reversedText)

    fileObject.seek(0)
    print(fileObject.read())

