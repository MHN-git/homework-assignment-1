class Device:
    _observers = []
    def __init__(self , state:int):
        self._state = state
        
    def attach(self, obs):
        self._observers.append(obs)
        
    def detach(self, obs):
        self._observers.remove(obs)
        
    def notify(self):
        for obs in self._observers:
            obs.update(self._state)
        
    def change_state(self, state):
        self._state = state
        self.notify()
        
    
class observer1:
    _device_state = None
    @classmethod 
    def update(cls, state):
        print(f'{cls.__name__} has been notified')
        cls._device_state = state
        
        
class observer2:
    _device_state = None 
    @classmethod
    def update(cls, state):
        print(f"{cls.__name__} has been notified")
        cls._device_state = state
    
    
if __name__ == "__main__":
    device = Device(0)
    
    ob1 = observer1()
    ob2 = observer2()
    
    device.attach(ob1)
    device.attach(ob2)
    
    device.change_state(1)
    
    