class myList ( list ) :  # sub class
    def __add__ ( self , other ) :
        """
        normalde list super classına ait [....]+[.....] işlemini yapan
        __add__ fonksiyonu liste öğlerini birleştirerek tek liste yapar.
        Ancak biz dunder yaparak __add__ metodunun kendimize göre nasıl çalışacağını belirledik.
        aynı zamanda override yapmış olduk

        """
        resultList = myList ( )
        if len ( self ) == len ( other ) :
            for i in range ( len ( self ) ) :
                resultList.append ( self [ i ] + other [ i ] )
            return resultList
        return "These lists cannot be summed with each other."

    def __sub__ ( self , other ) :
        """
        normalde list super classına ait [....]-[.....] işlemi yapan
        fonksiyon yoktur.
        Ancak biz dunder yaparak __sub__ metodu ile kendimize göre nasıl çalışacağını belirledik.
        """
        resultList = myList ( )
        if len ( self ) == len ( other ) :
            for i in range ( len ( self ) ) :
                resultList.append ( self [ i ] - other [ i ] )
            return resultList
        return "These lists cannot be subtracted from each other."


myList1 = myList ( [ 1 , 2 , 3 ] )
myList2 = myList ( [ 4 , 5 , 6 ] )
print ( myList1 + myList2 )
print ( myList1 - myList2 )
