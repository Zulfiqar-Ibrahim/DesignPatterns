# Abstraction
class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

# Implementor
class Renderer:
    def render_circle(self, radius):
        pass

    def render_square(self, side):
        pass

# Concrete Implementor - RasterRenderer
class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius} using raster rendering")

    def render_square(self, side):
        print(f"Drawing a square with side {side} using raster rendering")

# Concrete Implementor - VectorRenderer
class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius} using vector rendering")

    def render_square(self, side):
        print(f"Drawing a square with side {side} using vector rendering")

# Refined Abstraction - Circle
class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

# Refined Abstraction - Square
class Square(Shape):
    def __init__(self, renderer, side):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        self.renderer.render_square(self.side)

# Client code
def main():
    raster_renderer = RasterRenderer()
    vector_renderer = VectorRenderer()

    circle = Circle(raster_renderer, 5)
    circle.draw()

    square = Square(vector_renderer, 10)
    square.draw()

if __name__ == "__main__":
    main()