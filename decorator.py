from abc import ABC , abstractmethod

class page(ABC):
    @abstractmethod
    def show(self):
        pass 
    
    
class page1(page):
    def show(self):
        print('you are in page1')
        
class page2(page):
    def show(self):
        print('you are in page2')
        
        
class page1Decorator:
    _accounts = {'ali': '1234' , 'hosein': '5678'}
    def __init__(self , page):
        self.page = page
        
    def show(self):
        username = input('username: ')
        password = input('password: ')
        if self._accounts.get(username) == password:
            self.page.show()
        else:
            print('wrong username or password')
            
        
    
p = page1()
pDec = page1Decorator(p)
pDec.show()