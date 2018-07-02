class book:
    def __init__(self,ttl='Harry Potter',athr='JK Rowling',pbl='Bloomsbury',prc=300,rylt=100):
        self.title=ttl
        self.author=athr
        self.publisher=pbl
        self.price=prc
        self.royalityamt=rylt
    def get_title(self):
        return self.title
    def set_title(self,a):
        self.title=a
    def get_author(self):
        return self.author
    def set_author(self,b):
        self.author=b
    def get_publisher(self):
        return self.publisher
    def set_publisher(self,c):
        self.publisher=c
    def get_price(self):
        return self.price
    def set_publisher(self,d):
        self.price=d
    def royality(self):
        n=int(input("enter the no.of copies sold"))
        if n>=500:
            self.royalityamt=0.1*self.price*500
            n=n-500
            if n>=1000:
                self.royalityamt=self.royalityamt+0.125*self.price*1000
                n=n-1000
                self.royalityamt=self.royalityamt+0.15*self.price*n
        return self.royalityamt
               
class ebook(book):
    def __init__(self,ttl='Harry Potter',athr='JK Rowling',pbl='Bloomsbury',prc=300,rylt=100,_format='pdf'):
        self.ebookformat=_format
        super().__init__(ttl,athr,pbl,prc,rylt)
    def royality(self):
        rlt=super().royality()
        gst=0.12*rlt
        return rlt-gst
        
          
       
    
        
        
