class Elevator:
    def __init__(self, current_floor):
        self.current_floor = current_floor
        
        
    def move_up(self):
        
        self.current_floor.up_btn(self)
        
    def move_down(self):
        
        self.current_floor.down_btn(self)
  
            
from abc import ABC, abstractmethod       
class Floor(ABC):
    @abstractmethod
    def up_btn(self):
        pass
    
    @abstractmethod
    def down_btn(self):
        pass
    
class first(Floor):
    def up_btn(self, context):
        print("Moving up")
        context.current_floor = second()
        print("Current floor:", context.current_floor.__class__.__name__)

    def down_btn(self, context):
        print("Already at the lowest floor")
        
class second(Floor):
    def up_btn(self, context):
        print("Moving up")
        context.current_floor = third()
        print("Current floor:", context.current_floor.__class__.__name__)

    def down_btn(self, context):
        print("Moving down")
        context.current_floor = first()
        print("Current floor:", context.current_floor.__class__.__name__)

class third(Floor):
    def up_btn(self, context):
        print("Already at the top floor")

    def down_btn(self, context):
        print("Moving down")
        context.current_floor = second()
        print("Current floor:", context.current_floor.__class__.__name__)


if __name__ == "__main__":
    elevator = Elevator(first())
    elevator.move_up()   
    elevator.move_up()   
    elevator.move_down() 
    elevator.move_down() 
    elevator.move_down() 