from abc import ABC, abstractmethod


class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_radio(self):
        pass


class LightThemeFactory(UIFactory):
    def create_button(self):
        return LightButton()

    def create_radio(self):
        return LightRadio()


class DarkThemeFactory(UIFactory):
    def create_button(self):
        return DarkButton()

    def create_radio(self):
        return DarkRadio()


class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class Radio(ABC):
    @abstractmethod
    def check(self):
        pass


class LightButton(Button):
    def click(self):
        print("Light button clicked!")


class DarkButton(Button):
    def click(self):
        print("Dark button clicked!")


class LightRadio(Radio):
    def check(self):
        print("Light radio check!")


class DarkRadio(Radio):
    def check(self):
        print("Dark radio check!")


def client(factory):
    button = factory.create_button()
    radio = factory.create_radio()
    button.click()
    radio.check()

light_factory = LightThemeFactory()
client(light_factory)

dark_factory = DarkThemeFactory()
client(dark_factory)

