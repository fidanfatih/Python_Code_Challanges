# düz ve tersi eşit olan stringlere polindrom denir.
def isPolindrom1 (string):
    flag=0
    for i in range(0, int(len(string) / 2)):
        if string[i] != string[-(i + 1)]:
            print(f"'{string}' is NOT a polindrom.")
            break
        else:
            flag +=1
    if flag == int(len(string) / 2):
        print(f"'{string}' is a polindrom.")


def isPolindrom2 (string):
    reverse=""
    for character in string:
        reverse=character+reverse
    if reverse==string:
        print(f"'{string}' is a polindrom.")
    else:
        print(f"'{string}' is NOT a polindrom.")


def isPolindrom3(string):
    reverse=string[::-1]
    if reverse==string:
        print(f"'{string}' is a polindrom.")
    else:
        print(f"'{string}' is NOT a polindrom.")


text=input("Enter a String: ")
isPolindrom1(text)
isPolindrom2(text)
isPolindrom3(text)