from abc import ABC, abstractmethod

class SportEngine:
    pass

class Car:
    pass

class Manual:
    pass

class Builder(ABC): # ROOT INTERFACE
    
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def setSeats(self):
        pass
    
    @abstractmethod
    def setEngine(self):
        pass
    
    @abstractmethod
    def setTripComputer(self):
        pass

    @abstractmethod
    def setGPS(self):
        pass
    

class CarBuilder(Builder): # implement interface
    
    car: Car

    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()
    
    def setSeats(self):
        # do something
        pass

    def setEngine(self):
        # do something
        pass

    def setTripComputer(self):
        # do something
        pass

    def setGPS(self):
        # do something
        pass
    
    def getProduct(self) -> Car:
        product = self.car
        self.reset()
        return product

class CarManualBuilder(Builder): # implement interface
    
    manual: Manual

    def __init__(self):
        self.reset()

    def reset(self):
        self.manual = Manual()
    
    def setSeats(self):
        # do something
        pass

    def setEngine(self):
        # do something
        pass

    def setTripComputer(self):
        # do something
        pass

    def setGPS(self):
        # do something
        pass
    
    def getProduct(self) -> Car:
        manual = self.manual
        self.reset()
        return manual
    
class Director:
    
    def makeSportCar(builder: Builder):
        builder.reset()
        builder.setSeats(2)
        builder.setEngine(SportEngine())
        builder.setTripComputer(True)
        builder.setGPS(True)
        
    def makeSUV(builder: Builder):
        builder.reset()
        builder.setSeats(2)
        builder.setEngine(SportEngine())
        builder.setTripComputer(True)
        builder.setGPS(True)

class Application:
    
    def makeCar(self):
        director = Director()
        
        carBuilder = CarBuilder()
        director.makeSportCar(carBuilder)
        sportCar: Car = carBuilder.getProduct()
        
        manualCarBuilder = CarManualBuilder()
        director.makeSportCar(manualCarBuilder)
        manualSportCar: Manual = manualCarBuilder.getProduct()