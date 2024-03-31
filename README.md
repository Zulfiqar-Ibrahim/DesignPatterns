# DesignPatterns
This repo contains all the implememtation of different design patterns .
# Abstract design pattern
Abstract Factory:Defines an interface for creating a family of related objects without specifying their concrete classes.
Concrete Factories:Implement the Abstract Factory interface to create specific families of related objects.
Abstract Products: Declare interfaces for the products created by the Abstract Factory.
Concrete Products: Implement the Abstract Product interfaces to provide specific implementations of the products.
Imagine that you are creating a furniture shop simulator. Your code consists of classes that represent:
1. A family of related products, say: Chair + Sofa + CoffeeTable.
2. Several variants of this family. For example, products Chair + Sofa + CoffeeTable are available in these variants: Modern, Victorian, ArtDeco.
<img src="images/problem-en.png">
You need a way to create individual furniture objects so that they match other objects of the same family. Customers get quite mad when they receive non-matching furniture.
# what is the solution?
 the Abstract Factory pattern suggests is to explicitly declare interfaces for each distinct product of the product family (e.g., chair, sofa or coffee table). Then you can make all variants of products follow those interfaces. For example, all chair variants can implement the Chair interface; all coffee table variants can implement the CoffeeTable interface, and so on.
 <img src = "images/solution2.png">
 
 The whole Abstract design pattern is defined in this structural image.
 <img src = "images/structure.png">

 # Code example
 This example illustrates how the Abstract Factory pattern can be used for creating cross-platform UI elements without coupling the client code to concrete UI classes, while keeping all created elements consistent with a selected operating system.

 <img src = "images/example.png">

 The same UI elements in a cross-platform application are expected to behave similarly, but look a little bit different under different operating systems. Moreover, it’s your job to make sure that the UI elements match the style of the current operating system. You wouldn’t want your program to render macOS controls when it’s executed in Windows.

 It works like this: when an application launches, it checks the type of the current operating system. The app uses this information to create a factory object from a class that matches the operating system. The rest of the code uses this factory to create UI elements. This prevents the wrong elements from being created.

 With this approach, the client code doesn’t depend on concrete classes of factories and UI elements as long as it works with these objects via their abstract interfaces. This also lets the client code support other factories or UI elements that you might add in the future.

# factory method

The Factory Method pattern is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. It defines an interface for creating objects, but delegates the instantiation logic to subclasses.

Here's how the Factory Method pattern works:

Creator: This is an abstract class or interface that declares the Factory Method. The Creator may also provide a default implementation for the Factory Method that returns a default product.

Concrete Creator: These are subclasses of the Creator that implement the Factory Method to produce specific types of products.

Product: This is an interface or abstract class that defines the interface for the objects created by the Factory Method.

Concrete Product: These are the actual objects that are created by the Concrete Creators. They implement the Product interface.

# builder pattern
The Builder design pattern is a creational design pattern that separates the construction of a complex object from its representation, allowing the same construction process to create different representations. It is particularly useful when you need to create objects with many optional parameters or configurations, or when the construction process needs to be abstracted away from the client code.

Here's how the Builder pattern works:

Director: This is an optional component that oversees the construction process and delegates the actual construction steps to the builder.

Builder: This is an interface or abstract class that defines the steps for constructing the complex object. It typically has methods for setting various attributes or configurations of the object.

Concrete Builder: These are classes that implement the builder interface and provide specific implementations for constructing different representations of the complex object.

Product: This is the complex object being constructed. It can be composed of multiple parts or configurations.
