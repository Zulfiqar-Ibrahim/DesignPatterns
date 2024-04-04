import copy

class Prototype:
    def clone(self):
        pass

class ConcretePrototype(Prototype):
    def __init__(self, attribute):
        self.attribute = attribute

    def clone(self):
        return copy.deepcopy(self)

# Client code
if __name__ == "__main__":
    prototype = ConcretePrototype("Prototype")

    # Clone the prototype to create a new object
    cloned_object = prototype.clone()

    # Output the attributes of the cloned object
    print(cloned_object.attribute)