class Node():
    def __init__( self ):
        self. code  = -1
        self. price = -1
        self. l     = 0
        self. r     = 0

    def __init__( self, code, price ):
        self. code  = code
        self. price = price
        self. l     = 0
        self. r     = 0

    def add( self, code, price ):
        if self. code > code:
            if self. l != 0:
                self. l. add( code, price )
            else:
                self. l = Node( code, price )
        else:
            if self. r != 0:
                self. r. add( code, price )
            else:
                self. r = Node( code, price )

    def search( self, code ):
        if self. code == code:
            return self.price
        if self. code > code:
            if self. l == 0:
                print( "code not here" )
                return 0
            return self. l. search( code )
        else:
            if self. r == 0:
                print( "code not here" )
                return 0
            return self. r. search( code )


root = Node( 30, 50 )
root.add( 20, 50 )
root.add( 780, 392 )
root.add( 80, 3822 )
root.add( 70, 39 )
root.add( 78, 32 )
root.add( 730, 2 )

if __name__ == '__main__':
    while( True ):
        k = input( "Enter product code and amount " )
        k = k.split( ',' )
        print( "for code "+ str( k[0] ) + ", " +str( k[1] ) + " elements cost "+ str( int( k[1] ) * root.search( int( k[0] ) ) ) +"." )