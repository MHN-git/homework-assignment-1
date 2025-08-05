from abc import ABC , abstractmethod
from json import dump
import csv

class manipulate(ABC):
    @abstractmethod
    def write(self):
        pass 
    
    
class json_file(manipulate):
    def write(self , file_address , content):
        with open(file_address , 'a') as jf:
            dump(content , jf)
    
    
class csv_file(manipulate):
    def write(self, file_address , content):
        with open(file_address , 'a') as cf:
            writer = csv.writer(cf)
            writer.writerow(content)
    
   
class fileFactory(ABC):
    @abstractmethod
    def create_change():
        pass 
    

class json_fileFactory(fileFactory):
    def create_change():
        return json_file()


class csv_fileFactory(fileFactory):
    def create_change():
        return csv_file()
    

def file_writing(factory: fileFactory , file_address, content):
    file = factory.create_change()
    file.write(file_address , content)
    
    
if __name__ == "__main__":
    content1 = {'name' : 'ehsan' , 'age': 21}
    content2 = ['ehasan', 21]
    
    file_writing(json_fileFactory , "c:\\Users\\user1\\Desktop\\learn.json" , content1)
    file_writing(csv_fileFactory, "c:\\Users\\user1\\Desktop\\learn.csv" , content2)
    
    
