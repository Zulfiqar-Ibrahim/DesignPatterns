class EuropeanSocket:
    def voltage(self):
        return 230

# Target interface that the client expects
class USASocketInterface:
    def voltage(self):
        pass

# Adapter - Adapts the EuropeanSocket to the USASocketInterface
class EuropeanToUSASocketAdapter(USASocketInterface):
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        return 110 if self.socket.voltage() == 230 else 0  # Convert voltage to 110V

# Client code expecting a USASocketInterface
class ElectricKettle:
    def __init__(self, socket):
        self.socket = socket

    def boil(self):
        if self.socket.voltage() == 110:
            print("Boiling water")
        else:
            print("Unable to boil: Incorrect voltage")

# Usage
def main():
    # Using a EuropeanSocket
    euro_socket = EuropeanSocket()
    usa_adapter = EuropeanToUSASocketAdapter(euro_socket)
    kettle = ElectricKettle(usa_adapter)
    kettle.boil()  # Should print "Unable to boil: Incorrect voltage"

if __name__ == "__main__":
    main()