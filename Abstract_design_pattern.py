from abc import ABC, abstractmethod
# Abstract Product A
class Button(ABC):
    @abstractmethod
    def display(self):
        pass

# Concrete Product A1
class WindowsButton(Button):
    def display(self):
        print("Windows style button")



# Concrete Product A2
class MacOSButton(Button):
    def display(self):
        print("MacOs style button")


class Checkbox(ABC):
    @abstractmethod
    def display(self):
        pass




# Concrete Product B1
class WindowsCheckbox(Checkbox):
    def display(self):
        print("Windows style checkbox")


class MacOSCheckbox(Checkbox):
    def display(self):
        print("MacOS style checkbox")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.display()
    checkbox.display()


windows_factory = WindowsFactory()
client_code(windows_factory)
macOS_factory = MacOSFactory()
client_code(macOS_factory)