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

# Prototype design pattern
The Prototype design pattern is a creational design pattern that allows you to create new objects by cloning existing ones, without relying on their specific classes. This pattern is useful when the construction of an object is complex or when the exact class of the object needs to be hidden from the client code.

Here's how the Prototype pattern works:

Prototype Interface: This is an interface or abstract class that declares a method for cloning itself.

Concrete Prototype: These are classes that implement the Prototype interface and provide concrete implementations for cloning themselves.

Client: The client code creates new objects by cloning existing prototypes, without needing to know their specific classes.

# Singleton
Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance. The Singleton pattern solves two problems at the same time, violating the Single Responsibility Principle.
Ensure that a class has just a single instance. Why would anyone want to control how many instances a class has? The most common reason for this is to control access to some shared resource—for example, a database or a file.

Here’s how it works: imagine that you created an object, but after a while decided to create a new one. Instead of receiving a fresh object, you’ll get the one you already created.

Note that this behavior is impossible to implement with a regular constructor since a constructor call must always return a new object by design.

All implementations of the Singleton have these two steps in common:

Make the default constructor private, to prevent other objects from using the new operator with the Singleton class.
Create a static creation method that acts as a constructor. Under the hood, this method calls the private constructor to create an object and saves it in a static field. All following calls to this method return the cached object.
If your code has access to the Singleton class, then it’s able to call the Singleton’s static method. So whenever that method is called, the same object is always returned.

# adapter 

The Adapter design pattern is a structural pattern that allows objects with incompatible interfaces to collaborate. It acts as a bridge between two incompatible interfaces, converting the interface of one class into another interface that a client expects. This pattern is particularly useful when integrating existing or legacy code that cannot be directly modified.

# Bridge
Bridge is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

Say you have a geometric Shape class with a pair of subclasses: Circle and Square. You want to extend this class hierarchy to incorporate colors, so you plan to create Red and Blue shape subclasses. However, since you already have two subclasses, you’ll need to create four class combinations such as BlueCircle and RedSquare.

<img src = "images/problem-en-bridge.png">

Adding new shape types and colors to the hierarchy will grow it exponentially. For example, to add a triangle shape you’d need to introduce two subclasses, one for each color. And after that, adding a new color would require creating three subclasses, one for each shape type. The further we go, the worse it becomes.

This problem occurs because we’re trying to extend the shape classes in two independent dimensions: by form and by color. That’s a very common issue with class inheritance.

The Bridge pattern attempts to solve this problem by switching from inheritance to the object composition. What this means is that you extract one of the dimensions into a separate class hierarchy, so that the original classes will reference an object of the new hierarchy, instead of having all of its state and behaviors within one class.

<img src = "images/solution-en-bridge-1.png">

Following this approach, we can extract the color-related code into its own class with two subclasses: Red and Blue. The Shape class then gets a reference field pointing to one of the color objects. Now the shape can delegate any color-related work to the linked color object. That reference will act as a bridge between the Shape and Color classes. From now on, adding new colors won’t require changing the shape hierarchy, and vice versa.

# Decrator 
The Decorator pattern is a structural design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class. It is used to extend or modify the functionality of objects at runtime without directly altering their code.

# facade

The Facade pattern is a structural design pattern that provides a simplified interface to a complex system of classes, interfaces, or subsystems. It hides the complexities of the underlying system and provides a single interface for the client to interact with.


Let's say you have a complex video conversion system consisting of multiple classes for video formats, codecs, and conversion algorithms. You want to provide a simple interface for clients to convert videos without exposing the complexities of the system.