from abc import ABC , abstractmethod

class SUV(ABC):
    @abstractmethod
    def Specifications(self):
        pass
    
class Coupe(ABC):
    @abstractmethod
    def Specifications(self):
        pass 
    

class BenzSUV(SUV):
    def Specifications(self):
        return "Benz SUV - Luxury, Comfort, 4x4"
    
class BMWSUV(SUV):
    def Specifications(self):
        return "BMW SUV - Powerful, All-terrain"    

class BenzCoupe(Coupe):
    def Specifications(self):
        return "Benz Coupe - Sporty, Elegant"
    
class BMWCoupe(Coupe):
    def Specifications(self):
        return "BMW Coupe - Dynamic, High Performance"
    
class carfactory(ABC):
    @abstractmethod
    def create_Coupe(self):
        pass 
    
    @abstractmethod
    def create_SUV(self):
        pass 
    
    
class BenzFactory(carfactory):
    def create_Coupe(self):
        return BenzCoupe()
    
    def create_SUV(self):
        return BenzSUV()
    
class BMWFactory(carfactory):
    def create_Coupe(self):
        return BMWCoupe()
    
    def create_SUV(self):
        return BMWSUV()
    

def client_code(factory):
    coupe = factory.create_Coupe()
    suv = factory.create_SUV()
    
    print(coupe.Specifications())
    print(suv.Specifications())
    

if __name__ == "__main__":
    client_code(BenzFactory())
    client_code(BMWFactory())
