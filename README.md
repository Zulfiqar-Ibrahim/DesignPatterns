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