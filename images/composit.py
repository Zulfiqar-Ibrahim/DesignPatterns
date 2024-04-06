class UIComponent:
    def draw(self):
        pass

# Leaf
class Button(UIComponent):
    def __init__(self, label):
        self.label = label

    def draw(self):
        print(f"Drawing button with label '{self.label}'")

# Leaf
class TextField(UIComponent):
    def draw(self):
        print("Drawing text field")

# Composite
class Panel(UIComponent):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def draw(self):
        print("Drawing panel:")
        for child in self.children:
            child.draw()

# Client code
def main():
    button1 = Button("OK")
    button2 = Button("Cancel")
    text_field = TextField()

    panel = Panel()
    panel.add(button1)
    panel.add(button2)
    panel.add(text_field)

    panel.draw()

if __name__ == "__main__":
    main()