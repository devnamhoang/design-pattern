from abc import ABC, abstractmethod


class Device(ABC):  # INTERFACE

    @abstractmethod
    def isEnable(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def getVolume(self):
        pass

    @abstractmethod
    def setVolume(self, percent: int):
        pass

    @abstractmethod
    def getChannel(self):
        pass

    @abstractmethod
    def setChannel(self, channel: any):
        pass


class Remote(ABC):  # ABSTRACT CLASS

    device: Device

    def __init__(self, device) -> None:
        self.device = device

    @abstractmethod
    def togglePower(self):
        pass

    @abstractmethod
    def volumeDown(self):
        pass

    @abstractmethod
    def volumeUp(self):
        pass

    @abstractmethod
    def channelDown(self):
        pass

    @abstractmethod
    def channelUp(self, percent: int):
        pass


class Radio(Device):  # implement
    pass


class TV(Device):  # implement
    pass


class AdvancedRemote(Remote):  # extend Remote
    pass


class Application:

    def __init__(self) -> None:

        radio = Radio()
        remote_radio = AdvancedRemote(radio)

        tivi = TV()
        remote_tivi = AdvancedRemote(tivi)
