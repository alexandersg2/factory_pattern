# Factory Method Design Pattern

The Factory Method is a creational design pattern.
It separates object creation from where the object will be used.

It helps you to adhere to:
- The Single Responsibility Principle
- The Open/Closed Principle

Use it when:
- You don't know the types and dependencies of the objects your code should work with
- You want your code to be highly extensible
- You want to maintain and reuse a pool of resources (not demonstrated here)


## The example:
This example centres around two payment processors; Stripe and Adyen.

Imagine we have a system that must support many different payment processors. The processor used is based on a user's payment configuration.

We will use the factory method for several reasons:
- We can separate payment processor creation logic from where it will be used. This allows us to decouple our business logic from specific payment processors.
- We can very easily add new payment processors in the future, without modifying our existing logic.

## Class Diagram:

![Alt text](./class_diagrams.png?raw=true "Title")