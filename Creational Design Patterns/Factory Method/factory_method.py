from abc import ABC, abstractmethod

class Button: # an interface
    @abstractmethod
    def click(self) -> None:
        pass
    
    @abstractmethod
    def render(self) -> None:
        pass
    
class WindowButton(Button): # implement Button interface
    def click(self) -> None:
        # implement click method with window button
        pass
    
    def render(self) -> None:
        # Render a button in Windows style.
        pass

class HtmlButton(Button): # implement Button interface
    def click(self) -> None:
        # implement click method with html button
        pass
    
    def render(self) -> None:
        # Return an HTML representation of a button.
        pass

class Dialog(ABC): # abstract class
    
    @abstractmethod
    def createButton(self) -> Button:
        pass
    
    
    def render(self) -> None:
        button = Button()
        button.click()
        button.render()
    
    
class WindowDialog(Dialog): # extend Dialog abstract class
    
    def createButton(self) -> Button:
        return WindowButton()

class WebDialog(Dialog): # extend Dialog abstract class
    
    def createButton(self) -> Button:
        return HtmlButton()
