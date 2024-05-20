from abc import ABC, abstractmethod


class Button(ABC): # abstract class
    
    @abstractmethod
    def paint(self):
        pass

class WinButton(Button):
    
    def paint(self):
        pass

class MacButton(Button):
    
    def paint(self):
        pass
    

class Checkbox(ABC): # abstract class
    
    @abstractmethod
    def paint(self):
        pass

class WinCheckbox(Checkbox):
    
    def paint(self):
        pass

class MacCheckbox(Checkbox):
    
    def paint(self):
        pass


class GuiFactory(ABC): # an interface # ROOT HERE #
    
    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass
    

class WinFactory(GuiFactory):
    
    def createButton(self) -> Button:
        return WinButton()

    def createCheckbox(self) -> Checkbox:
        return WinCheckbox()


class MacFactory(GuiFactory):
    
    def createButton(self) -> Button:
        return MacButton()

    def createCheckbox(self) -> Checkbox:
        return MacCheckbox()