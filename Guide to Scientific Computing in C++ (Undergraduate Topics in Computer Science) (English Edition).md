# **Undergraduate Topics in Computer Science** 

**Series Editor** Ian Mackie 

#### **Advisory Board** 

Samson Abramsky, University of Oxford, Oxford, UK Chris Hankin, Imperial College London, London, UK Mike Hinchey, University of Limerick, Limerick, Ireland Dexter C. Kozen, Cornell University, Ithaca, USA Andrew Pitts, University of Cambridge, Cambridge, UK Hanne Riis Nielson, Technical University of Denmark, Kongens Lyngby, Denmark 

Steven S. Skiena, Stony Brook University, Stony Brook, USA Iain Stewart, University of Durham, Durham, UK Undergraduate Topics in Computer Science (UTiCS) delivers highquality instructional content for undergraduates studying in all areas of computing and information science. From core foundational and theoretical material to �inal-year topics and applications, UTiCS books take a fresh, concise, and modern approach and are ideal for self-study or for a one- or two-semester course. The texts are all authored by established experts in their �ields, reviewed by an international advisory board, and contain numerous examples and problems. Many include fully worked solutions. 

More information about this series at http:// www. springer. com/ <u>series/ 7592</u> 

Joe Pitt-Francis and Jonathan Whiteley 

**Guide to Scienti�ic Computing in C++** 2nd ed. 2017 



Joe Pitt-Francis University of Oxford, Oxford, UK 

Jonathan Whiteley University of Oxford, Oxford, UK 

ISSN 1863-7310 e-ISSN 2197-1781 Undergraduate Topics in Computer Science ISBN 978-3-319-73131-5 e-ISBN 978-3-319-73132-2 <u>https://doi.org/10.1007/978-3-319-73132-2</u> 

Library of Congress Control Number: 2017962059 

© Springer International Publishing AG, part of Springer Nature 2017 

This work is subject to copyright. All rights are reserved by the Publisher, whether the whole or part of the material is concerned, speci�ically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on micro�ilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed. 

The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a speci�ic statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use. 

The publisher, the authors and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, express or implied, with respect to the material contained herein or for any errors or omissions that may have been 

made. The publisher remains neutral with regard to jurisdictional claims in published maps and institutional af�iliations. 

Printed on acid-free paper 

This Springer imprint is published by the registered company Springer International Publishing AG part of Springer Nature The registered company address is: Gewerbestrasse 11, 6330 Cham, Switzerland 

## **Preface to the Second Edition** 

The principle changes in this updated edition are additional material on software testing and on some of the new features introduced in the C++11 standard. When introducing this additional material, we have followed the same philosophy as when writing the �irst edition of this book. That is, we focus on a concise discussion of the key features that are most useful to the novice and intermediate programmer in the �ield of scienti�ic computing. We have found this an effective approach when teaching this course to graduate students—once the basics have been mastered, students then have the con�idence to �ind out about less wellused features themselves when they are needed. 

This second edition would not be as complete—or as enjoyable to update—without discussions with colleagues and other readers of the �irst edition, including those previously unknown to us who were kind enough to provide constructive feedback. We would like to express our gratitude to all who contributed in this way or offered their encouragement, and to the staff at Springer for inviting us to update the �irst edition. 

Finally, we would both again like to thank our families for their love and support. 

**Joe Pitt-Francis Jonathan Whiteley Oxford, UK October 2017** 

## **Preface to the First Edition** 

Many books have been written on the C++ programming language, varying across a spectrum from the very practical to the very theoretical. This book certainly lies at the practical end of this spectrum and has a particular focus for the practical treatment of this language: scienti�ic computing. 

Traditionally, Fortran and MATLAB<sup>®</sup> <u>1</u> have been the languages of choice for scienti�ic computing applications. The recent development of complex mathematical models—in �ields as diverse as biology, �inance and materials science, to name but a few—has driven a need for software packages that allow computational simulations based on these models. The complexity of the underlying models, together with the need to exchange code between co-workers, has motivated programmers to develop object-oriented code (often written in C++) for these simulation packages. The computational demands of these simulations may require software to be written for parallel computing facilities, typically using the Message Passing Interface (MPI). The need to train programmers in the skills to program applications such as these led to the development of a graduate-level course _C++ for Scienti�ic Computing_ , taught by the authors of this book, at the University of Oxford. 

This book provides a guide to C++ programming in scienti�ic computing. In contrast to many other books on C++, features of the language are demonstrated mainly using examples drawn from scienti�ic computing. Object orientation is �irst mentioned in Chap. 1 where we brie�ly describe what this phrase—and other related terms such as inheritance—means, before postponing any further discussion of object orientation or related topics until Chap. 6. In the intervening chapters until object orientation reappears, we present what is best described as “procedural programming in C++”, covering variables, �low of control, input and output, pointers (including dynamic allocation of memory), functions and reference variables. Armed with this grounding in C++, we then introduce classes in Chaps. 6 and 7. In these two chapters, where the main features of object orientation are showcased, we initially, for the sake of clarity, abandon our principle of using examples drawn from scienti�ic computing. Once the topics have 

been presented however, we resume our strategy of demonstrating concepts through scienti�ic computing examples. More advanced C++ features such as templates and exceptions are introduced in Chaps. 8 and 9. Having introduced the features of C++ required for scienti�ic computing, the remainder of the book focuses on the application of these features. In Chap. 10, we begin to develop a collection of classes for linear algebra calculations: these classes are then developed further in the exercises at the end of this chapter. Chapter 11 presents an introduction to parallel computing using MPI. Finally, in Chap. 12, we discuss how an object-oriented library for solving second-order differential equations may be constructed. The importance of a clear programming style to minimise the introduction of errors into code is stressed throughout the book. 

This book is aimed at programmers of all levels of expertise who wish to write scienti�ic computing programs in C++. Experience with a computer to the level where �iles can be stored and edited is expected. A basic knowledge of mathematics, such as operations between vectors and matrices, and the Newton–Raphson method for �inding the roots of nonlinear equations would be an advantage. 

The material presented here has been enhanced signi�icantly by discussions about C++ with colleagues, too numerous to list here, in the Department of Computer Science at the University of Oxford. A special mention must, however, be made of the Chaste <u>2</u> programming team: particular gratitude should be expressed to Jonathan Cooper for readily sharing with us his impressively wide and deep knowledge of the C++ language. Other members of the team who have signi�icantly helped clarify our thoughts on the C++ language are Miguel Bernabeu, James Osborne, Pras Pathmanathan and James Southern. We should also thank students from both the M.Sc. in Mathematical Modelling and Scienti�ic Computing and the Doctoral Training Centres at the University of Oxford for unwittingly aiding our understanding of the language through asking pertinent questions. 

Finally, it is always important to remember—especially when debugging a particularly tiresome code—that there is far more to life than C++ programming for scienti�ic computing. We would both like to thank our families for their love and support, especially during the writing of this book. 

**Joe Pitt-Francis Jonathan Whiteley Oxford October 2011** 

## **Contents** 

**<u>1 Getting Started</u>** 

**<u>1. 1 A Brief Introduction to C++</u>** 

**<u>1. 1. 1 C++ is “Object-Oriented”</u>** 

**<u>1. 1. 2 Why You Should Write Scienti�ic Programs in C++ 1. 1. 3 Why You Should Not Write Scienti�ic Programs in C++ 1. 1. 4 Scope of This Book</u>** 

**<u>1. 2 A First C++ Program</u>** 

**<u>1. 3 Compiling a C++ Program</u>** 

**<u>1. 3. 1 Integrated Development Environments</u>** 

**<u>1. 3. 2 Compiling at the Command Line</u>** 

**<u>1. 3. 3 Compiler Flags</u>** 

**<u>1. 4 Variables</u>** 

**<u>1. 4. 1 Basic Numerical Variables</u>** 

**<u>1. 4. 2 Other Numerical Variables</u>** 

**<u>1. 4. 3 Mathematical Operations on Numerical Variables</u>** 

**<u>1. 4. 4 Division of Integers</u>** 

**<u>1. 4. 5 Arrays</u>** 

**<u>1. 4. 6 ASCII Characters</u>** 

**<u>1. 4. 7 Boolean Variables</u>** 

**<u>1. 4. 8 Strings</u>** 

**<u>1. 5 Simple Input and Output</u>** 

**<u>1. 5. 1 Basic Console Output</u>** 

**<u>1. 5. 2 Keyboard Input</u>** 

**<u>1.6 The</u>** **<u>`assert` Statement</u>** 

**<u>1. 7 Tips: Debugging Code</u>** 

#### **<u>1. 8 Exercises</u>** 

#### **<u>2 Flow of Control</u>** 

**<u>2.1 The</u>** **<u>`if` Statement</u>** 

**<u>2.1.1 A Single</u>** **<u>`if` Statement</u>** 

**<u>2.1.2 Example: Code for a Single</u>** **<u>`if` Statement</u>** 

**<u>2.1.3</u>** **<u>`if`</u> –** **<u>`else` Statements</u>** 

**<u>2.1.4 Multiple</u>** **<u>`if` Statements</u>** 

**<u>2.1.5 Nested</u>** **<u>`if` Statements</u>** 

**<u>2. 1. 6 Boolean Variables</u>** 

**<u>2. 2 Logical and Relational Operators</u>** 

**<u>2.3 The</u>** **<u>`while` Statement</u>** 

**<u>2.4 Loops Using the</u>** **<u>`for` Statement</u>** 

**<u>2. 4. 1 Example: Calculating the Scalar Product of Two Vectors</u>** 

**<u>2.5 The</u>** **<u>`switch` Statement</u>** 

**<u>2. 6 Tips: Loops and Branches</u>** 

**<u>2. 6. 1 Tip 1: A Common Novice Coding Error</u>** 

**<u>2. 6. 2 Tip 2: Counting from Zero</u>** 

**<u>2. 6. 3 Tip 3: Equality Versus Assignment</u>** 

**<u>2.6.4 Tip 4: Never Ending</u>** **<u>`while` Loops</u>** 

**<u>2. 6. 5 Tip 5: Comparing Two Floating Point Numbers</u>** 

**<u>2. 7 Exercises</u>** 

**<u>3 File Input and Output</u>** 

**<u>3. 1 Redirecting Console Output to File</u>** 

**<u>3. 2 Writing to File</u>** 

**<u>3. 2. 1 Setting the Precision of the Output</u>** 

**<u>3. 3 Reading from File</u>** 

**<u>3. 4 Checking Input and Output are Successful 3. 5 Reading from the Command Line 3. 6 Tips: Controlling Output Format</u>** 

**<u>3. 7 Exercises</u>** 

**<u>4 Pointers 4. 1 Pointers and the Computer’s Memory</u>** 

**<u>4. 1. 1 Addresses 4. 1. 2 Pointer Variables 4. 1. 3 Example Use of Pointers 4. 1. 4 Warnings on the Use of Pointers</u>** 

**<u>4. 2 Dynamic Allocation of Memory for Arrays</u>** 

**<u>4. 2. 1 Vectors</u>** 

**<u>4. 2. 2 Matrices</u>** 

**<u>4. 2. 3 Irregularly Sized Matrices</u>** 

**<u>4. 3 Tips: Pointers</u>** 

**<u>4. 3. 1 Tip 1: Pointer Aliasing 4. 3. 2 Tip 2: Safe Dynamic Allocation 4.3.3 Tip 3: Every</u>** **<u>`new` Has a</u>** **<u>`delete`</u>** 

**<u>4. 4 Modern C++ Memory Management 4.4.1 The</u>** **<u>`unique_ptr` Smart Pointer 4.4.2 The</u>** **<u>`shared_ptr` Smart Pointer</u>** 

**<u>4. 5 Exercises</u>** 

**<u>5 Blocks, Functions and Reference Variables</u>** 

**<u>5. 1 Blocks</u>** 

**<u>5. 2 Functions</u>** 

**<u>5. 2. 1 Simple Functions</u>** 

**<u>5. 2. 2 Returning Pointer Variables from a Function</u>** 

**<u>5. 2. 3 Use of Pointers as Function Arguments</u>** 

**<u>5. 2. 4 Sending Arrays to Functions 5. 2. 5 Example: A Function to Calculate the Scalar Product of Two Vectors</u>** 

**<u>5. 3 Reference Variables</u>** 

**<u>5. 4 Default Values for Function Arguments</u>** 

**<u>5. 5 Function Overloading</u>** 

**<u>5. 6 Declaring Functions Without Prototypes</u>** 

**<u>5. 7 Function Pointers</u>** 

**<u>5. 8 Recursive Functions</u>** 

**<u>5. 9 Modules</u>** 

**<u>5. 10 Tips: Code Documentation</u>** 

**<u>5. 11 Exercises</u>** 

**<u>6 An Introduction to Classes</u>** 

**<u>6.1 The</u>** **_<u>Raison d’Être</u>_** **<u>for Classes</u>** 

**<u>6. 1. 1 Problems That May Arise When Using Modules 6. 1. 2 Abstraction, Encapsulation and Modularity Properties of Classes</u>** 

**<u>6. 2 A First Example Simple Class: A Class of Books</u>** 

**<u>6. 2. 1 Basic Features of Classes</u>** 

**<u>6. 2. 2 Header Files</u>** 

**<u>6. 2. 3 Setting and Accessing Variables</u>** 

**<u>6. 2. 4 Compiling Multiple Files</u>** 

**<u>6. 2. 5 Access Privileges</u>** 

**<u>6. 2. 6 Including Function Implementations in Header Files</u>** 

#### **<u>6. 2. 7 Constructors and Destructors</u>** 

**<u>6. 2. 8 Pointers to Classes</u>** 

**<u>6.3 The</u>** **<u>`friend` Keyword</u>** 

**<u>6. 4 A Second Example Class: A Class of Complex Numbers</u>** 

**<u>6. 4. 1 Operator Overloading</u>** 

**<u>6. 4. 2 The Class of Complex Numbers</u>** 

**<u>6. 5 Some Additional Remarks on Operator Overloading</u>** 

**<u>6. 6 Tips: Coding to a Standard</u>** 

**<u>6. 7 Exercises</u>** 

**<u>7 Inheritance and Derived Classes</u>** 

**<u>7. 1 Inheritance, Extensibility and Polymorphism 7. 2 Example: A Class of E-books Derived from a Class of Books</u>** 

**<u>7. 3 Access Privileges for Derived Classes</u>** 

**<u>7. 4 Classes Derived from Derived Classes</u>** 

**<u>7. 5 Run-Time Polymorphism</u>** 

**<u>7. 6 The Abstract Class Pattern</u>** 

**<u>7. 7 Tips: Using a Debugger</u>** 

**<u>7. 8 Exercises</u>** 

**<u>8 Templates</u>** 

**<u>8. 1 Templates to Control Dimensions and Verify Sizes</u>** 

**<u>8. 2 Templates for Polymorphism</u>** 

**<u>8. 3 A Brief Survey of the Standard Template Library</u>** 

**<u>8. 3. 1 Vectors</u>** 

**<u>8. 3. 2 Sets</u>** 

**<u>8. 4 A Survey of Some New Functionality in Modern C++ 8.4.1 The</u>** **<u>`auto` Type</u>** 

#### **<u>8. 4. 2 Some Useful Container Types with Uni�ied Functionality</u>** 

**<u>8.4.3 Range-based</u>** **<u>`for` Loops</u>** 

**<u>8. 4. 4 Mapping Lambda Functions</u>** 

**<u>8. 5 Tips: Template Compilation</u>** 

**<u>8. 6 Exercises 9 Errors, Exceptions and Testing</u>** 

**<u>9. 1 Preconditions</u>** 

**<u>9. 1. 1 Example: Two Implementations of a Graphics Function</u>** 

**<u>9. 2 Three Levels of Errors</u>** 

**<u>9. 3 Introducing the Exception 9. 4 Using Exceptions 9. 5 Testing Software</u>** 

**<u>9. 5. 1 Unit Testing</u>** 

**<u>9. 5. 2 Extending Software</u>** 

**<u>9. 5. 3 Black Box Testing</u>** 

**<u>9. 5. 4 White Box Testing</u>** 

**<u>9. 5. 5 Test Driven Development</u>** 

**<u>9. 6 Tips: Writing Appropriate Tests</u>** 

**<u>9. 7 Exercises</u>** 

**<u>10 Developing Classes for Linear Algebra Calculations 10. 1 Requirements of the Linear Algebra Classes</u>** 

**<u>10. 2 Constructors and Destructors</u>** 

**<u>10. 2. 1 The Default Constructor 10. 2. 2 The Copy Constructor 10. 2. 3 A Specialised Constructor</u>** 

#### **<u>10. 2. 4 Destructor</u>** 

**<u>10. 3 Accessing Private Class Members</u>** 

**<u>10. 3. 1 Accessing the Size of a Vector</u>** 

**<u>10. 3. 2 Overloading the Square Bracket Operator 10. 3. 3 Read-Only Access to Vector Entries 10. 3. 4 Overloading the Round Bracket Operator</u>** 

**<u>10. 4 Operator Overloading for Vector Operations 10. 4. 1 The Assignment Operator 10. 4. 2 Unary Operators 10. 4. 3 Binary Operators</u>** 

**<u>10. 5 Functions</u>** 

**<u>10. 5. 1 Members Versus Friends</u>** 

**<u>10. 6 Tips: Memory Debugging Tools</u>** 

**<u>10. 7 Exercises</u>** 

**<u>11 An Introduction to Parallel Programming Using MPI 11. 1 Distributed Memory Architectures 11. 2 Installing MPI</u>** 

**<u>11. 3 A First Program Using MPI</u>** 

**<u>11. 3. 1 Essential MPI Functions</u>** 

**<u>11. 3. 2 Compiling and Running MPI Code</u>** 

**<u>11. 4 Basic MPI Communication</u>** 

**<u>11. 4. 1 Point-to-Point Communication</u>** 

**<u>11. 4. 2 Collective Communication</u>** 

**<u>11. 5 Example MPI Applications</u>** 

**<u>11. 5. 1 Summation of Series</u>** 

**<u>11. 5. 2 Parallel Linear Algebra</u>** 

**<u>11. 6 Tips: Debugging a Parallel Program</u>** 

**<u>11. 6. 1 Tip 1: Make an Abstract Program</u>** 

**<u>11. 6. 2 Tip 2: Datatype Mismatch</u>** 

**<u>11. 6. 3 Tip 3: Intermittent Deadlock</u>** 

**<u>11. 6. 4 Tip 4: Almost Collective Communication</u>** 

**<u>11. 7 Exercises</u>** 

**<u>12 Designing Object-Oriented Numerical Libraries 12. 1 Developing the Library for Ordinary Differential Equations</u>** 

**<u>12. 1. 1 Model Problems</u>** 

**<u>12. 1. 2 Finite Difference Approximation to Derivatives 12. 1. 3 Application of Finite Difference Methods to Boundary Value Problems</u>** 

**<u>12. 1. 4 Concluding Remarks on Boundary Value Problems in One Dimension</u>** 

**<u>12. 2 Designing a Library for Solving Boundary Value Problems 12.2.1 The Class</u>** **<u>`SecondOrderOde`</u>** 

**<u>12.2.2 The Class</u>** **<u>`BoundaryConditions`</u>** 

**<u>12.2.3 The Class</u>** **<u>`FiniteDifferenceGrid`</u>** 

**<u>12.2.4 The Class</u>** **<u>`BvpOde`</u>** 

**<u>12.2.5 Using the Class</u>** **<u>`BvpOde`</u>** 

**<u>12. 3 Extending the Library to Two Dimensions</u>** 

**<u>12. 3. 1 Model Problem for Two Dimensions</u>** 

**<u>12. 3. 2 Finite Difference Methods for Boundary Value Problems in Two Dimensions</u>** 

**<u>12. 3. 3 Setting Up the Linear System for the Model Problem 12. 3. 4 Developing the Classes Required</u>** 

**<u>12. 4 Tips: Using Well-Written Libraries</u>** 

#### **<u>12. 5 Exercises</u>** 

**Appendix A: Linear Algebra Appendix B: Other Programming Constructs You Might Meet Appendix C: Solutions to Exercises Further Reading** 

**Index** 

## **Footnotes** 

<u>1</u> 

MATLAB is a registered trademark of The MathWorks, Inc. <u>2</u> 

The Cancer, Heart And Soft Tissue Environment (Chaste) is an object-oriented package, written in C++, for simulations in the �ield of biology. More details on this package may be found at <u>`https://www.cs.ox.ac.uk/chaste/` .</u> 

© Springer International Publishing AG, part of Springer Nature 2017 Joe Pitt-Francis and Jonathan Whiteley , _Guide to Scienti�ic Computing in C++_ ,  Undergraduate Topics in Computer Science <u>https://doi.org/10.1007/978-3-319-73132-2_1</u> 

# **1. Getting Started** 

Joe Pitt-Franci ~~s~~ <u>1</u> and Jonathan Whitele ~~y~~ <u>1</u> 

(1) University of Oxford, Oxford, UK 



**Joe Pitt-Francis Email:** <u>joe.pitt-francis@cs.ox.ac.uk</u> 

In this introductory chapter, you will learn a little bit about the features of C++ in terms of some of the common “buzzwords” you may have heard about the language, and in terms of its strengths and weaknesses. You will also learn how to edit, compile and run your �irst C++ program. This chapter also includes information on variables and simple ways of getting data into and out of your programs. 

The chapter concludes with tips on how you might, as a novice C++ programmer, go about debugging your programs. We have included tips with every chapter in this book. They are presented at an increasing level of sophistication—this should match your gaining knowledge as you read through the book and attempt some of the exercises. 

## **1.1 A Brief Introduction to C++** 

A very large number of programming languages for writing computer software exist. If one of these programming languages was the most suitable for all purposes, then it would be expected that everyone would use this language, and all other languages would eventually become obsolete. This, however, is certainly not the case. It seems appropriate to begin this book by describing the key features of C++, allowing us to explain why C++ is a suitable programming language for 

scienti�ic computing applications and why it isn’t the only suitable choice of language. 

### **1.1.1 C++ is “Object-Oriented”** 

You may have heard that C++ is an “object-oriented” language and have wondered what that means. What marks a language which is objectoriented out from one that is not? Fundamentally, it is because the basic unit of the language is an _object_ or _class_ —an entity which brings together related functionality and data. We will probe the ideas behind objects and classes more deeply in Chap. <u>6.</u> 

Many books on C++ start by de�ining _object-orientation_ more explicitly. If this book were aimed at a computer science or software engineering audience, then we would �ind it necessary to de�ine some speci�ic concepts related to object-orientation. We would need to convince you of the importance of the following concepts. 

- _Modularity_ . All the data of a particular object, and the operations that we perform on this object, are held in one or two �iles, and can be worked on independently. 

- _Abstraction_ . The essential features and functionality of a class are put in one place and the details of how they work are unimportant to the user of the class. For example, if you are using a linear system library to solve matrix equations you should not need to know the precise details of how matrices are laid out in memory or the exact order that a numerical solver performs its operations. You should only need to know how to use the functionality of the library. 

- _Encapsulation_ . The implementation of an object is kept hidden from the user of the class. This is not only about clarity ( _abstracting_ away the detail). It is also about preventing the user from accidentally amending internal workings of, for example, a linear solver, stopping it from working effectively. 

- _Extensibility_ . Functionality can be reused with selected parts extended. For example, much of the core of a linear solver is in matrix-vector products and scalar products—this type of functionality need only be implemented once, then other parts of the program can build on it. 

- _Polymorphism_ . The same code can be used for a variety of objects. For example, we would like to use similar looking C++ code to raise a 

matrix of complex numbers to a given power as we would to raise a real number to a given power—even though the basic arithmetic operations “behind the scenes” are different. 

_Inheritance_ . This, perhaps the most important feature of objectorientation, allows for code reuse, extensibility and polymorphism. For example, a new linear solver for singular matrix systems will share many of the features of a basic linear solver. Inheritance allows the new solver to derive functionality from the basic solver, and then build on this functionality. 

We are not going to discuss these terms in any more detail at this time. It is not that these things are unimportant. Quite the contrary—all these concepts add up to make C++ a very powerful language. However, we can cover the basics of programming without object-orientation. We will describe classes and objects in Chap. 6 and revisit some of these concepts. Then we can show exactly why _inheritance_ , for instance, is so powerful when we come to explain it in Chap. 7. 

**1.1.2 Why You Should Write Scienti�ic Programs in C++** Since you have selected a book with the words “C++” and “Scienti�ic Computing” in the title, then the chances are that you have decided to start writing your scienti�ic programs in C++. Perhaps not. Perhaps you are considering your options, or perhaps the choice of language has been foisted on you. 

It is not our place to �ight battles about which language is the very best, especially because the choice of language for a program will often depend on the problem that is being solved. In the �ield of numerical scienti�ic programming, there are many languages being used, with most scientists opting for M�����® ~~,~~ <u>1</u> C/C++ or Fortran. 

The �irst and most compelling reason for using C++ (as well as C and Fortran) is because they are _fast_ . That is, with careful programming and optimisations, they can be compiled to a machine code program which is able to use the full power of the available hardware. Many scripting languages (such as M����� and Python) are _interpreted_ languages, meaning that the code which you write is translated to machine code at run time. Other modern languages (such as Java and C#) compile halfway—to a hardware-independent byte-code which is then 

interpreted at run time. Run time interpretation means that some of the computer’s power is spent on the conversion process and also that it is harder to apply optimisations. Nowadays M�����, Python and Java implementations use clever tricks such as caching compilation steps and just-in-time compilation to make programs run faster. Nevertheless, these tricks require computational effort and so these languages may not fully utilise the power of all hardware. 

A second reason for using C++ is that there is a _wealth of numerical libraries_ for scienti�ic computing in C++ and related languages. Lots of numerical algorithms were established in the 1950s and were then incorporated into software libraries (such as EISPACK and LINPACK) in the 1970s ~~.~~ <u>2</u> If you write your own code using well-established, welltested software then you are building on decades of experience and improvement. 

A third reason for choosing to write in C++ is that there is a _widerange of open source and commercial tools_ to support you. We used the free GNU compiler tool-set to test the programs in this book and you can use any C++ compiler to compile them for your computer. In contrast, if we were distributing M����� programs, you would need to have M����� and a licence installed on your computer because it is a proprietary product. There are similar open source products (such as GNU Octave) but there is no guarantee that a M����� program will produce the same answer when run in Octave. Because it is closed source, the meaning of a program can change between versions of M�����. For example, when just-in-time compilation was introduced in M����� 7 the operational semantics of the language subtly changed. This meant that a small minority of M����� programs which were known to work well with one version of M����� could produce incorrect results, errors or warnings on another version. 

A fourth reason for C++ is that it has a _�lexible memory management model_ . In a Java program, some of the system memory is used in the interpretation and you rely on a garbage collector to tidy up memory which you are no longer using, and so you may not be able to predict how much memory a program is going to need. In C++ you can make this prediction, but this is a double-edged sword because you are also responsible for making sure that memory is managed properly. 

A �inal reason to program in C++ is that it is an _object-oriented language_ . We haven’t yet told you what this means exactly, but it is widely held that writing in an object-oriented style leads to programs which are easier to understand, to extend, to maintain and to refactor. 

### **1.1.3 Why You Should Not Write Scienti�ic Programs in C++** 

It is worth stressing that C++ is not the best language for every occasion. Some people say that _other languages may be faster_ . Many scienti�ic programmers believe that Fortran will always give the best performance in terms of raw speed and would reject C++ on the basis that features such as pointer chasing and virtual method look-up (don’t worry if you haven’t heard of these terms, or don’t know what they mean—you may never need to!) result in the code being executed at suboptimal speed. This may have some truth, but the fact that objectorientation leads to greater readability (as mentioned above) makes it a reasonable compromise language. It can be a very fast language and it is also a good language for readability. 

Sometimes _other languages are better for a specialised task_ . Scripting languages such as Perl and Python are ideal for text processing and string manipulation. If you need to sum columns of numbers from �iles then you could write a C++ program, but a short, disposable script would be far quicker to implement. 

Some languages are _better for writing prototype programs or for plotting data_ . M����� excels in the �ield of rapid prototyping—short programs to quickly explore some algorithm or phenomenon. To test a particular linear algebra algorithm on a range of matrices with various sizes and structures would take a few lines of M�����, but in C++ you might have to write several �iles and compile against someone else’s libraries. M����� also has the advantage of a fully-integrated graphical development environment, making many programming tasks easy without having to rely on extra tools. Furthermore, M����� has an inbuilt plotting environment, so if you want to visualise the results of your algorithms quickly M����� might be your best choice. 

So C++ may not be the best choice of language in _every_ situation. However, there are many situations in which C++ has the ideal �it for a particular problem. The discussion above may be enough to convince you that it is worth getting started with C++. 

### **1.1.4 Scope of This Book** 

Most C++ programs for scienti�ic computing can be written very effectively by using only a fraction of the total capabilities of the language. This book focuses on the aspects of C++ that you are most likely to utilise, or to encounter in other programmer’s code, for scienti�ic computing applications. When writing your own programs, you may occasionally need to understand one of the more advanced features of the language. In the Further Reading section at the end of this book, we direct the reader to a collection of resources that provide a more comprehensive description of the whole C++ language [5–8]. 

## **1.2 A First C++ Program** 

It is very common to introduce a programming language by using a program that prints the text “Hello World” to the screen. A simple example of a C++ program that does this is shown below. The code in Listing <u>1.1</u> illustrates several basic features of C++ programs. In line 1 of this code, we include the header �ile `iostream` . The name `iostream` pertains to **i** nput and **o** utput **stream** ing and is required in any C++ program that inputs data from the keyboard or outputs data to the console, that is, the screen. The second feature to note is that there is a section of code that: 

- begins with the line of code “ `int main(int argc, char* argv[])` ” (line 3 of this code); 

- is followed by more code enclosed between curly brackets, { and }; and 

- the code within the curly brackets ends with the statement “ `return 0;` ”. 

The section of the code between curly brackets contains the instructions that we want the computer to execute. The part of line 3 inside brackets allows us to execute the code using user-speci�ied arguments: we will postpone a discussion of this functionality until Chap. <u>3. Note that comments have been inserted into the code in lines 5,</u> 6, 7 and 9 to aid the reading of the code by humans: anything between the comment opener “ `/*` ” and the comment closer “ `*/` ”, or any line that 

starts with “ `//` ” is a comment, and is ignored when the code is converted into an executable, computer readable �ile. We have used the extension `.cpp` for the code below to indicate that the �ile `HelloWorld.cpp` is a C++ program. Choice of this extension is entirely a matter of personal choice: other authors use the extensions `.C` , `.c++` , `.cxx` or `.cc` . 

We now focus on the purpose of lines 10 and 12: these lines of code each contain an instruction to the computer, and are known as _statements_ . Note that all statements end with a semi-colon. It is suf�icient for the time being for the reader to know that line 10 is the line of code that directs the computer to print the contents within the quotation marks to the screen. The “ `n` ” denotes a new line, and so the 

phrase “Hello World”, followed by a new line, will be printed to the screen. The word `cout` is a contraction of **c** onsole **out** put, that is, printing to the screen. 



The word “ `int` ” at the start of line 3 indicates that the last line of the code within curly brackets will return an integer value. This is carried out using the statement in line 12 “ `return 0` ;”. Returning the value zero indicates to the computer that the program has reached the end without encountering any problems. 

Before moving on to explain how to get your computer to print `Hello World` to your screen we pause to discuss some stylistic issues of which you should be aware. You will see in the listing above that all 

lines of code within the curly brackets have been indented. This is not compulsory. However, it is standard practice when coding to indent these lines: this will become clearer in later chapters when we embed code within more than one set of curly brackets. The number of spaces indented is entirely for the programmer to decide: all spaces—termed “white space”—are ignored when executing the code above. A �inal point is that lines in C++ may be as long as the programmer wishes, and may run over the end of the line in the text editor used to write your C++ programs. For clarity, it is generally advisable to split a potentially long line over several lines. We will demonstrate this later when writing more complex statements. 

The code in Listing <u>1.1</u> is a correct C++ program for printing the text “Hello World” to the screen. However, before this program may be executed it must �irst be translated into a format that the computer can read: this process is known as _compilation_ . We now explain what compilation is, and how to do it. 

## **1.3 Compiling a C++ Program** 

Many readers will have experience of scienti�ic computing in M�����. A key difference between C++ and M����� is that a C++ program must be _compiled_ before it can be executed. There are many different ways that compilation can be performed which we now discuss. 

### **1.3.1 Integrated Development Environments** 

As you take your �irst steps in learning a new programming language, you may not want to invest a lot of time in installing new software and con�iguring applications to help you develop programs. For this reason, we recommend that you begin writing programs with your favourite text editor and a command line compiler (see the following Sect. <u>1.3.2).</u> However, as your programs and projects grow in size you will need to manage multiple �iles each containing various parts of the program. This becomes dif�icult when the number of �iles becomes large, and you may spend a lot of time switching between �iles in order to look up what you called some function or argument. At this point in your code development, we would recommend that you switch to using an Integrated Development Environment (IDE). 

Examples of IDEs that are available for C++ programmers at the time of writing include KDevelop for Linux, Microsoft Visual Studio for Windows, XCode for Mac OS X, and the cross-platform IDEs CLion and Eclipse. Eclipse is open source, runs on most operating systems and is well-maintained by a community of developers. Because it was originally built for developing Java programs, it is necessary to install a “C/C++ development tools plug-in” should it be used for developing C++ programs. 

The functionality of various IDEs varies according to their level of sophistication, but most present the seasoned programmer with several advantages over an old-school compile at the command line approach. Common features of IDEs are listed below. Don’t worry if you do not fully understand all the terms used: these will become clear as you work through this book. 

1. 

A program editor with syntax highlighting such as keyword colouring, automatic code indentation and identi�ication of illegal programming constructs. 

2. 

Context aware editing, so that you immediately know what functionality is present in one of your classes as you type its name. 3. 

Build automation, where your entire project code is managed so that changes to small parts of a large program only result in small compilation steps. Build automation is traditionally done with a handcrafted �ile known as a `Makefile` , which we introduce in Sect. 6. 2. 4. 1. Many IDEs analyse your code for dependencies and then use a `Makefile` behind the scenes. 

4. 

On-the-�ly compilation gives the system the ability to constantly save and compile your program as you write it. 5. 

“Step through” graphical debugging lets you walk through a program as it runs, pause it at critical points, and examine the internal state of its variables. (More information on debuggers is given in Sect. <u>7. 7.)</u> 6. 

Automatic code generation is particularly useful in IDEs for graphical tool development. When the user selects that they want to include a button on a graphical tool in their program some “boiler plate” code is generated including the functions that are activated when the button is pressed—these are then �illed in by the programmer. 

### **1.3.2 Compiling at the Command Line** 

When using the Linux operating system ~~,~~ <u>3</u> C++ codes may be compiled and executed at the command line within a terminal window. Many compilers—both open source and commercially developed—are available. In this book, we assume that the reader has access to the GNU `gcc` compiler. To ensure that this compiler is installed, open a terminal window and type “ `which g++` ” followed by return. Hopefully the computer will respond by reporting the location of this compiler, for example, 



If the compiler is not installed, it may be downloaded from <u>https:// gcc. gnu. org/ , where instructions for installation may also be found.</u> 

To compile the code given in Listing <u>1.1, open a terminal window</u> and create a directory where code may be saved. Move into this directory, and save the code as “ `HelloWorld.cpp` ”. In the same directory type 



In the command above, `g++` tells the computer that we want to use the GNU `gcc` compiler for C++. The section of the command “ `-o HelloWorld` ” tells the computer that we want to name the executable �ile “ `HelloWorld` ”. The “ `-o` ” is known as the _�lag_ that the computer expects will be followed by the executable name, in this case `HelloWorld` . The command ends by stating the C++ �ile that we wish to compile. This command produces an executable �ile called 

`HelloWorld` . This executable may be run by typing “ `./HelloWorld` ” inside the terminal. Running this executable will result in the text “Hello World” being printed to the screen inside the terminal. 

If we were to compile the code using the command above, but without the �lag and the executable name, then an executable �ile would still be produced. A default name would be allocated to the executable �ile. For many compilers, this default executable name is `a.out` . 

### **1.3.3 Compiler Flags** 

If we were to attempt to compile a code that was not written using correct C++ syntax, then the compiler would report an error, and would not produce an executable �ile. As such, the compiler can be thought of as a helpful tool that has the capability to perform some validation of the correctness of the code. 

Suppose we have written code where a calculation was stored as a variable, but this variable is never subsequently used. Although this may be written with correct C++ syntax it is likely that this is an error— we would expect that the result of every calculation will subsequently be used somewhere in the code, or there would be no point in performing this calculation. Compilers have the capacity to warn us of unexpected occurrences such as this by the use of _compiler �lags_ . The compilation command below will warn us of instances such as these. 



The compiler �lag `-Wall` above is a contraction of **w** arning **all** . The compilation command above will warn us of anything unexpected that is not actually an error, but will still create an executable �ile. We give an example instance of a situation in which the compiler will warn of a probable programming error as one of our programming tips in Sect. <u>2. 6. 3. Suppose we want to be stricter than this, and want the compiler to</u> treat anything unexpected as an error and, therefore, not to create an executable �ile when this occurs. This may be achieved using the compilation command below. 



There are a large number of compiler �lags available for most compilers. At this stage, there is no need to know about any more than the basic �lags. We have shown how to use compiler �lags to perform some validation of the code written. We will now discuss three more �lags that are particularly valuable when writing scienti�ic computing applications. The �irst �lag we discuss may be used to optimise the performance of the executable �ile. The default is no optimisation. By using the “ `-O` ” (upper case `o` ) �lag as shown below, the executable �ile should execute more quickly although compilation may take longer. 



If we are debugging a program, it is important that the executable and the debugger have information about which line in the source code produced speci�ic machine instructions. Normally this information is not retained after compilation. In order to produce a non-optimised version of the code with debugging information preserved, we use the “ `-g` ” �lag. 



The last �lag that we introduce here is one that allows us to link to a library of mathematical routines. We instruct the compiler to link to this library using the command below. 



We may use as many �lags as we wish when compiling—simply list them one after the other when compiling the code. 

## **1.4 Variables** 

In the example code in Listing 1.1 we simply printed some text to the screen. In most programs, especially scienti�ic computing applications, we wish to store entities and perform operations on them. These entities are known as _variables_ . In C++ programs, in common with most 

compiled languages, the variables must be declared to be an appropriate type before they are used. 

### **1.4.1 Basic Numerical Variables** 

The two most common types of variable that are used in scienti�ic computing applications are _integers_ and _double precision_ �loating point variables. Loosely speaking, if a numerical variable does not—and never will—require a decimal point it may be stored as an integer variable: if not it should be stored as a �loating point variable. If a code uses two integers denoted by `row` and `column` , and one double precision �loating point variable denoted by `temperature` , we may declare these before they are used, and set their values, using the following code fragment. 



The statements in lines 1 and 2 of the code above allocate memory for two integer variables `row` and `column` , and one double precision �loating point variable `temperature` . It is important to understand that, whilst memory is allocated for these variables, we do not know until we assign values to these variables in lines 3–5 what values are stored by these variables. A common mistake is to assume that these variables are initialised to zero when the memory is allocated: this is true some of the time, but you should not rely on this. 

Note the use of the decimal point for the double precision �loating point variable `temperature` in line 5 of the listing above. This is not strictly necessary, but emphasises that this variable is a �loating point variable. Use of this decimal point has the advantage that, provided we compile the code with suitable �lags, compilation will trigger a warning if we had mistakenly declared this variable to be an integer. 

We strongly encourage the use of variable names that have some relation to the variable that they represent, for example `row` as a variable that contains the index to the row of a matrix (see Sect. 6. 6 for 

a longer discussion of naming conventions for variables). There are certain rules that variable names in C++ must adhere to, but these rules are not particularly restrictive. The �irst rule is that all variables in C++ programs should begin with a letter. All other characters in variable names must be letters, numbers or underscores. Variable names are case–sensitive, and so “ `ROW` ” is a different variable to “ `row` ”. We would not, however, recommend writing a program with one variable called “ `ROW` ” and another variable called “ `row` ” as the potential for confusing these variables is obvious. One �inal restriction is that some names, such as `int, for, return` may not be used as variable names because they are used by the language. These words are known as _reserved words_ or _keywords_ . 

A variable may be _initialised_ when de�ining the variable type. For example, the code fragment in Listing 1.2 may be written as the following code fragment. 



The value of more than one variable may be assigned in each statement, as shown below. 



However, line 2 in the code fragment above may cause confusion—it actually means 



and so both `row` and `column` take the value 3 after this fragment of code has been executed. However, it may be mistakenly read to be 



in which `row` would �irst take the value 2 (which was the initial value of column), and then `row` , because it is the _result_ of the assignment `row` = `column` , would take the value 3. The value of column is unaffected. There is clearly potential for introducing errors when assigning more than one value in each statement, and so we do not recommend this approach. 

It is often the case that a programmer intends a variable to be constant throughout the code, for example the numerical value used for the density of a �luid. The programmer can ensure that a variable is guaranteed to be unchanged throughout the code by assigning a value to the variable when it is declared, together with use of the keyword `const` as shown in the fragment of code below. 



We may want to set the tolerance of some iterative solver to a very small number, for example . Clearly, we may set this tolerance 

using the code fragment below. 



The listing above is clearly not ideal—a casual glance at the code does not allow us to distinguish easily between, say, and . It 

would be much clearer if we could write the numerical value in _scienti�ic notation_ . This is demonstrated in the code below. 



The letter “ `e` ” in the line of code above may be read as “times 10 to the power of”: that is, 589.63 may be written `5.8963e2` as 589.63 5.8963 10 . 

### **1.4.2 Other Numerical Variables** 

In the previous section, we restricted ourselves to declaring all integer variables using the keyword `int` and all �loating point variables using the keyword `double` . There are—however—variants on these variable types which we now discuss. 

Integers can be declared as _integers_ , _short integers_ or _long integers_ as shown below. 



The actual range of integers that may be stored by each of these variables depends on the system that you are using. For example, on an obsolete 32-bit operating system the `long int` is completely synonymous with the `int` data type—but on modern 64-bit architectures the `long int` is assigned twice as much space as the `int` (so it can store numbers in the range as opposed to 



). 

Variables of type `short int` require the allocation of less memory, with a corresponding reduction in the range of values that may be stored in this memory. It may be tempting to try to use short integers where possible to free up as much memory as possible. We do not recommend this: in software written for scienti�ic computing applications the bulk of memory allocated is usually used to store �loating point variables. Reducing the memory allocated to integer variables is unlikely to free a signi�icant volume of memory. 

A further classi�ication of each of the integer types is as _signed_ or _unsigned_ integers. Signed integers may be used to store both positive and negative integers, whilst unsigned integers may be used to store only nonnegative integers. These variables may be used as shown below. 



The default for any integer is a signed integer, hence there is no purpose in explicitly declaring an integer as a signed integer. A variable of type `unsigned int` is allocated an identically sized memory location as a variable of type `int` . As would be expected, a variable of type `unsigned int` can then store a range of nonnegative integers roughly twice as big as a variable of type `int` . A programmer is, however, unlikely to notice the difference between these two variable types on modern systems. 

Floating point variables may be declared using the keywords `float` , `double` or `long double` as shown below. 



As with integers, the range of numbers that may be stored using each of these variable types depends on the system used. On modern systems it is very rare that the range of numbers that may be stored by a variable of type `double` differs from the range that may be stored by a variable of type `long double` . In the remainder of this book, we do not distinguish between these data types. Variables of type `float` typically store a smaller range of numbers than those of type `double` . Although variables of type `double` require more memory we strongly urge writers of scienti�ic computing applications to use double precision �loating point variables: this will minimise the effect of rounding errors, thus removing one potential source of error from any program written. 

### **1.4.3 Mathematical Operations on Numerical Variables** 

Sample C++ code for performing a variety of mathematical operations on variables is given below. Note the inclusion of the header �ile `cmath` . This �ile is needed for some mathematical operations and also includes values of some useful constants, such as `M_PI` , that contains the value of correct to about 20 decimal places. 



Many other mathematical functions are available. The functions `cos` , `sin` , `tan` , `acos` , `asin` , `atan` , `cosh` , `sinh` , `tanh` , `log` , `log10` , `ceil` , `floor` can be used in exactly the same way as `sqrt` and `exp` in the code above: that is, they accept one argument, and return one value. 

**_Table 1.1_** Shorthand for some mathematical operations 

|**Long**|**ha**|**nd**<br>**Shorthand**|
|---|---|---|
|`a =`<br>`b;`|`a`|`+`<br>`a += b;`|
|`a =`<br>`b;`|`a`|`-`<br>`a -= b;`|
|`a =`<br>`b;`|`a`|`*`<br>`a *= b;`|
|`a =`<br>`b;`|`a`|`/`<br>`a /= b;`|
|`a =`<br>`b;`|`a`|`%`<br>`a %= b;`if`a`and`b`are integers (_a_<br>mod_b_)|
|`a =`<br>`1;`|`a`|`+`<br>`a++;`if`a`is an integer|
|`a =`<br>`1;`|`a`|`-`<br>`a- -;`if`a`is an integer|



Some mathematical functions deserve more explanation. This is done through their implementation in code below. 



There are many instances in scienti�ic computing code where we wish to increment a variable `a` by the value `b` , that is, we want to replace the value that the variable `a` stores by the value `a+b` . There are shorthand operations for this and other similar operations in C++, shown in Table 1.1 ~~<u>.</u>~~ <u>4</u> Note that the `a%b` operation, pronounced “a mod b”, is a modulus operation and may be thought of as the remainder after dividing `a` by `b` using integer division as described in Sect. <u>1.4.4.</u> 

### **1.4.4 Division of Integers** 

One common error frequently made by inexperienced C++ programmers is in dividing an integer by another integer. Consider the fragment of code below. 



This code fragment will output the value 2, when the value of dividing 5 by 2—that is, 2.5—was actually intended. There are two potential problems with the code fragment as it is written above. The �irst operation that will be performed when executing line 2 of the listing 

above is to divide the integer `i` by the integer `j` . The value resulting from this operation will then be stored in the memory allocated to `k` . In C++, division of an integer by another integer will return _only the integer part of this division_ : hence dividing `i` by `j` will store the integer part of 2.5, which is 2 (as everything after the decimal point will be ignored). The second part of this statement—the assignment operator —will then assign the value 2 to the integer variable `k` . 

It may be thought that modifying the code fragment above so that `k` is de�ined to be a double precision �loating point variable may solve the problem, as shown in the code fragment below. 



This still does not give the correct value of 2.5. This is because the division is performed in line 3 before the result is stored as the double precision �loating point variable `k` . As division of an integer by another integer in C++ returns the integer part of the division, the division of `i` by `j` returns the value 2 as explained above. This value is then stored as the double precision �loating point number 2.0 in the memory allocated to `k` . 

To divide two integers as if they were �loating point variables, we may convert the integers to double precision �loating point variables as shown in the code fragment below. 



The code `((double)(i))` is known as “ _explicit type conversion_ ” and allows us to treat the integer variable `i` as a double precision �loating point variable, and so this code fragment does output the correct value of 2.5. 

### **1.4.5 Arrays** 

Many scienti�ic computing applications are underpinned by algorithms that are based on vectors and matrices. These may be stored in C++ as an entity known as an _array_ . If the size of the array is known in advance then it can be declared as follows. 



In the code fragment above, `array1` represents a vector of integers of length 2, whilst `array2` represents a matrix of double precision . �loating point variables of size 

In contrast to M����� and Fortran, in C++ the indices of an array of length `n` start with entry `0` and end with entry `n-1` . This is known as “ _zero-based indexing_ ”. Elements of an array are accessed by placing the indices in separate square brackets, and so we may completely populate the arrays `array1` and `array2` declared above using the following code. 



We may also perform operations on entries of the array as shown below. 



Arrays can be initialised when they are declared, for example, 



where the array `array3` represents the vector 



and `array4` represents the matrix 



Note that the curly bracket notation may only be used to populate arrays at the same time as when they are declared—for example the code 



is acceptable, but the code 



will not be accepted by the compiler. 

### **1.4.6 ASCII Characters** 

ASCII characters are numbers, uppercase letters, lowercase letters and some other commonly used symbols: most of the characters on your keyboard are ASCII characters. Variables that are ASCII characters are declared using the keyword `char` . Example code using an ASCII character is shown below. 



### **1.4.7 Boolean Variables** 

Boolean variables take either the value `true` or the value `false` . These variables are commonly used when specifying whether a portion of code should be executed in conjunction with `if` and `while` statements (which will be introduced in Chap. <u>2). Examples of Boolean</u> variables are given below. 



### **1.4.8 Strings** 

The data type `char` represents one ASCII character. A string may be thought of as an ordered collection of characters. For example, “C++” is a string consisting of the ordered list of characters “C”, “+”, and “+”. 

To use strings in C++ requires the header �ile `string` . The library which may be accessed using this header �ile contains signi�icant functionality for the use and manipulation of strings. The bulk of coding for scienti�ic computing applications requires operations on numerical variables, and so we do not discuss this data type in much detail. In the example code below, we demonstrate how to declare a string, how to determine the length of a string, how to access individual characters of the string, and how to print a string to the console. 

A string in C++ is a little like an array of characters together with a layer of extra functionality. There is no need to understand _why_ the length and elements of the string may be accessed in this way: an understanding of _how_ is suf�icient. 



In line 9 and line 10 of the code recall that arrays in C++ have indices that begin from zero: `city.at(2)` and `city[2]` both refer to the entry of the array of characters with index 2, that is, “f”, the third letter of the string “Oxford”. Lines 11 and 12 both have the effect of printing the contents of `city` (“Oxford”) to the screen. Line 12 prints the contents of `city` to the screen, but does so by �irst converting from a C++ string to a C string, which is an array of type `char` . The string utility function `c_str` is not needed here, but is useful in cases where we need to pass a C++ string to a function which expects an array of type `char` . 

## **1.5 Simple Input and Output** 

It would be pointless to write a code without having the means to communicate the output of the code to the user, or to some other application. As such, _output_ is a programming technique that must be mastered by all programmers. Similarly, the user of software would expect to be provided with the ability to specify data that the software would use to generate output: _input_ is therefore just as important a programming skill. We now describe basic C++ commands to allow output to the screen and input from the keyboard. In Chap. 3, we provide a fuller explanation, describing input from, and output to, a �ile, and a more �lexible speci�ication of the format of this output. 

### **1.5.1 Basic Console Output** 

We have already brie�ly discussed console—or screen—output in Sect. 1.2, and have seen that the statement 



prints the text “Hello World” to the screen, followed by a new line. We may use `std::cout` to write more than one entity to the console at a time. This is best explained by example: consider the statements below. 



The second statement above tells the computer to �irst print the string “ `x =` ”, followed by the value assigned to the variable `x` , then the string “ `and y =` ”, then the value assigned to the variable `y` , and �inally to �inish with a new line. The output is therefore 



Note that any spaces required in the output must be included within quotation marks in the statement that begins `std::cout` . 

We have already seen one formatting command for output in C++: the new line formatting command \ `n` . Some other useful formatting commands are shown in Table 1.2. 

**_Table 1.2_** Some formatting commands for console output 

|**Comman**<br>**d**|**Symb**<br>**ol**|
|---|---|
|new line|\`n`|
|tab|\`t`|
|’|\|
|”|\`"`|
|?|\`?`|
|bell<br>sound|\`a`|



Output from C++ is _buffered_ . Sometimes, for example, if the computer is busy doing a large volume of computation, the program may not print the output to the screen immediately. If immediate output is desirable then use the statement “ `std::cout.flush();` ” after any `std::cout` command to ensure the output is printed before any other statements are executed, as shown in the listing below. As with certain aspects of string manipulation discussed in Sect. 1.4.8, at this stage it is suf�icient to understand how to send output to the console immediately without worrying why it is done in this way. 



### **1.5.2 Keyboard Input** 

Keyboard input for numerical variables and characters is achieved using the input stream `std::cin` , where `cin` is a contraction of **c** onsole **in** . As with console output, the `iostream` header �ile must be included. The following code prompts someone to enter their Personal Identi�ication Number—commonly known as their PIN—and then assigns the number entered to the integer variable `pin` . 



`std::cin` may be used to ask for more than one input at a time, as shown below. 



Keyboard input for variables of type `string` is slightly different. An example of how to input a string is given below. As with the commands for basic manipulation of strings given in Sect. 1.4.8, we do not attempt 

to explain why strings are input in this way: this will become clear when more advanced features of C++ are explained later in this book. 



## **1.6 The** **`assert` Statement** 

Scienti�ic computing applications usually require a massive number of complicated mathematical computations. If any one of these computations is incorrect, then the �inal results of the computation will usually be incorrect. Finding the source of the error is an excruciatingly tedious process, and so we strongly recommend the use of the features of the C++ language that allow identi�ication of unexpected occurrences such as an attempt to compute the square root of a negative number. 

In Chap. <u>9</u> we point to the notion that there are various levels or degrees of error. In particular, we introduce _exceptions_ , which are a feature of the C++ language that allow very effective handling of an unexpected occurrence when a code is being run. A less sophisticated approach is to use `assert` statements, as demonstrated in the code below. Note the inclusion of the extra header �ile `cassert` that is required to use `assert` statements. 



The code above invites the user to enter a nonnegative number, and returns the square root of this number. Before the square root is calculated, we check that the number really is nonnegative through the `assert` statement. We will see in Chap. 2 that the “ `>=` ” that appears in line 10 of the code is the “greater than or equal to” operator: this line of code therefore checks that the variable `a` is nonnegative. To see the effect of the `assert` statement, we �irst save the code as `program.cpp` and then compile the code without any optimisation �lags to produce executable `a.out` . If, when this executable is run, the number −5 is entered, the code terminates at the `assert` statement with the following error message. 



A further C++ function that is useful in conjunction with assertions is the function `std::isfinite` . This allows con�irmation that a variable `x` contains a �inite value, and not an in�inite value (obtained, for example, by dividing a non-zero number by zero) or some other value that is not de�ined as a number (such as the square-root or logarithm of a negative number) ~~.~~ <u>5</u> The use of this function along with an assert statement is illustrated in the code fragment below. 



Although we emphasise that this is a very rudimentary technique for identifying errors, and that we will introduce more sophisticated techniques later, `assert` statements can provide signi�icant information: in the error message above we see that the exact line of code where the problem occurred has been identi�ied. Another advantage of `assert` statements is that they can be automatically removed when the code is compiled with the “ `-DNDEBUG` ” �lag. This allows you to test code with the assertions activated but to distribute a faster program that has the assertions deactivated by compiling using the command 



## **1.7 Tips: Debugging Code** 

There are many tools designed to aid with the debugging of code. The most basic of these is the compiler, and the �lags associated with the compiler, as described in Sects. <u>1.3.2</u> and 1.3.3. More sophisticated tools exist, but they are aimed at larger scale projects, such as those that we will develop in later chapters of this book. 

Rather than learning to use a sophisticated debugging tool whilst in the early stages of learning C++, we suggest below some simpler techniques for debugging the code that you will be writing when tackling the exercises in the early chapters of this book. 

_Compile your code frequently._ 

Saving your code and compiling it using the warning compiler �lag described in Sect. <u>1.3.3</u> every time a few statements are added is a useful diagnostic to see if any potential problems are being introduced. If there are any problems, comment out the new statements and recompile. Then add the statements in one at a time until the problem line is identi�ied. When you �irst write code in C++ you may be amazed how often you forget the basic syntax such as a semi-colon at the end of a statement. 

_Save your project frequently._ 

If you have code that works and you need to add new functionality, then do not throw away the old version. If things go wrong then you will be able to see exactly what you changed and if all else fails you will have a working version to roll back to. If it is critical that you are able to roll back to a working version of the code, or if you are in a collaborative project, we recommend that you use a version control <u>6</u> system ~~.~~ 

_Always test the code with a simple example._ For example, if you are writing code to add the elements of two arrays verify the output by comparison with a calculation that you have carried out yourself. 

_Understand errors that arise when executing the code._ 

If your program complains of a “segmentation error” when executing, it is likely that you have attempted to access a member of an array that is out-of-range: that is, you may have attempted to access the 6th entry of an array that was only declared to have 4 elements. 

_Use output._ 

If you need to know where your program is crashing, and why, then print out some values of variables at key points in the execution. Do not forget to `flush` the output so that it appears before the program crashes! 

_Use assertions._ 

If you expect a certain property at the start of a section of code, for example, that the scale factor is nonzero or that the argument of a square-root is nonnegative, you can check for it using assertions (introduced in Sect. 1.6). 

_C++ arrays are indexed beginning from zero._ 

If the array `temperature` is declared as having 4 elements, the statement “ `temperature[4] += 1.0;` ” will cause problems. _Use a debugger._ 

If all else fails then debug your program using a debugger. Tips on using a debugger are to be found in Sect. <u>7. 7.</u> 

## **1.8 Exercises** 

**1.1** To ensure that your compiler is correctly set up, copy and save the �ile `HelloWorld.cpp` displayed in Listing <u>1.1, compile it, and execute it.</u> 

**1.2** Write code that asks a user to enter two integers from the keyboard and then writes the product of these integers to the screen. 

**1.3** Write code that declares two vectors as arrays of double precision �loating point numbers of length 3 and assigns values to each of the entries. Extend this code so that it calculates the scalar (dot) product of these vectors and prints it to screen. Finally, extend the code so that it prints the Euclidean norm of both vectors to screen. 

[ _See Sect._ <u>A. 1. 2</u> _for a de�inition of the scalar product, and Sect._ <u>A. 1. 5</u> _for a de�inition of the Euclidean norm of a vector._ ] 

**1.4** Write code that declares four 2 2 matrices 

of double precision �loating point numbers, `A` , `B` , `C` , `D` , and assigns values to the entries of `A` and `B` . Let `C` = `A` + `B` , and `D=A*B` . Extend your code so that it calculates the entries of `C` and `D` , and then prints the entries of these matrices to screen. 

**1.5** Write code that invites the user to input separately strings that store their given name and their family name. Print the user’s full name to screen. 

**1.6** I want to record the number of cars that drive past my house each day for �ive consecutive days, and calculate the average of these numbers. Create an integer array to store these �ive numbers, and then write code to calculate the average of these numbers. Execute your code using the sample data 34, 58, 57, 32, 43. Verify that you get the correct answer of 44.8. 

[ _Hint: read the material in Sect._ <u>1.4.4</u> _on converting integers to double precision �loating point numbers_ .] 

**1.7** Investigate the use of the compiler error warning �lags discussed in Sect. <u>1.3.3. For</u> example: (i) declare an integer as a constant variable and then attempt to change this value later in the code; and (ii) attempt to set an integer variable to the value 3.2. 

## **Footnotes** 

<u>1</u> 

M����� is a registered trademark of The MathWorks, Inc. <u>2</u> 

The original version of M����� was written in Fortran and was intended as a simple interface into parts of the EISPACK and LINPACK Fortran libraries. 

##### <u>3</u> 

If you are working on a Mac operating system, we recommend that you install the Xcode developer tool-set. This comes complete with a GNU C++ compiler which you can use on the command line or within the developer environment. If you are working on a Windows operating system, we recommend that you install MinGW (a minimal environment for using GNU tools within Windows). Alternatively, you may want something more sophisticated built on MinGW such as Cygwin (a Unix-like environment) or Code::Blocks (an open source windows development environment containing MinGW and the GNU C++ compiler). 

##### <u>4</u> 

The “++” shorthand programming construct, which is also available in the C language, explains the original naming of the language “C++”. It is a pun which means “like C but one better”. 

<u>5</u> 

For those values which fail the `std::isfinite` test it is possible to differentiate between in�inite numbers (using `std::isinf` ) and those which are “not a number” (using `std::isnan` ). 

##### <u>6</u> 

There are many open source version control systems such as CVS, Subversion, Mercurial or Git to help you with this. There are also organisations who will host your code repository for you. 

© Springer International Publishing AG, part of Springer Nature 2017 Joe Pitt-Francis and Jonathan Whiteley , _Guide to Scienti�ic Computing in C++_ ,  Undergraduate Topics in Computer Science <u>https://doi.org/10.1007/978-3-319-73132-2_2</u> 

# **2. Flow of Control** 

Joe Pitt-Franci ~~s~~ <u>1</u> and Jonathan Whitele ~~y~~ <u>1</u> 

- (1) University of Oxford, Oxford, UK 



**Joe Pitt-Francis Email:** <u>joe.pitt-francis@cs.ox.ac.uk</u> 

In almost any computer program written for a scienti�ic computing application, we need to allow the computer to execute a collection of statements if—and only if—some criterion is met. For example, if we were writing a program to control the motion of a spacecraft travelling to Mars, the program would include lines of code that would control the safe landing of the spacecraft. As the craft completes its touchdown, it �ires retrorocket motors to control descent until the sensors detect that the landing gear is in contact with the planet’s surface. It is imperative that the lines of code which say “cut the motor if and only if there is a strong signal from the landing gear” are executed at exactly the right time. If these instructions are not executed when the spacecraft has landed, the retrorockets may �ire for too long and cause damage to the craft. On the other hand, if the instruction to cut the motors is executed when the spacecraft is still descending, we would expect the spacecraft to crash ~~.~~ <u>1</u> It is clear that the relevant lines of code should be executed if, and only if, certain conditions are met. 

As with most programming languages, conditional branching may be achieved in C++ programs by using an `if` statement. Similarly, we may use a `while` statement to execute a collection of statements until a speci�ied condition is met, and a `for` loop to execute a collection of statements a speci�ied number of times. In this chapter, we explain how to utilise these features of the C++ language. 

## **2.1 The** **`if` Statement** 

The most basic use of an `if` statement is to execute one or more statements if, and only if, a given condition is met. As we shall see in this section, we may build upon this simple construct to write more complicated statements when required. 

### **2.1.1 A Single** **`if` Statement** 

Let us suppose that we wish to execute two statements, `Statement1` and `Statement2` , if—and only if—the condition `p` > `q` is met. The following code demonstrates the basic syntax for this in C++. 



If the condition `p` > `q` is met, then the code enclosed by the curly brackets is executed. The condition (in round brackets) is technically know as the _guard_ . Note the indentation within the curly brackets in the above listing. While this is not necessary for the compiler to understand the meaning, it makes it clearer to the reader which statements are executed if the condition `p` > `q` is met. 

If only one statement— `Statement1` —is to be executed when the condition `p` > `q` is satis�ied, then curly brackets are not strictly necessary. For example, the following two code fragments will execute `Statement1` if the condition `p` > `q` is met. 





<!-- Start of picture text -->
or<br><!-- End of picture text -->



Although either of these two variants of the code will do what we want it to, we do not recommend them, as the curly brackets make it very clear precisely which statements are executed as a consequence of a given `if` statement. As such, we would strongly suggest the use of curly brackets, as shown in the code below. More suggestions on tips for ensuring code is clearly readable—known as _coding conventions_ —may be found in Sect. 6. 6. 



### **2.1.2 Example: Code for a Single** **`if` Statement** 

Below is a concrete example of code that uses an `if` statement. This code changes the value of `x` to zero if, and only if, `x` is negative. If `x` is not negative, line 5 of the code will not be executed, and the value of `x` will be unchanged. 



### **2.1.3** **`if` –** **`else` Statements** 

It is often the case that we want to set a variable to one value if a speci�ied condition is met, and to a different value otherwise. This may be implemented in C++ code by the use of an `if` statement in conjunction with an `else` statement. The fragment of code below sets the double precision �loating point variable `y` to the value 2 if the integer variable `i` is positive, and to the value 10 otherwise. 



Note the comment in line 10 of the listing above. As no condition is needed for the `else` condition, it is always good programming practice to use a comment to explicitly state under what conditions the `else` condition should be met. 

### **2.1.4 Multiple** **`if` Statements** 

We may extend the `if` and `else` statements described above to allow more complicated conditions on the execution of statements. Extending the previous example, suppose the double precision �loating point variable `y` takes the value 2 if the integer variable `i` is greater than 100, `y` takes the value 10 if `i` is negative, and `y` takes the value 5 otherwise. C++ code for this condition is given below. 



### **2.1.5 Nested** **`if` Statements** 

It is common in scienti�ic computing to have an algorithm where statements must be executed if, and only if, two separate conditions are met. One way of implementing this is to use _nested_ `if` statements, as shown below. In this code the double precision �loating point variable `y` is assigned the value 10 if, and only if, the conditions `x` > `z` and `p` > `q` are both met. 



### **2.1.6 Boolean Variables** 

Boolean variables may be used as the condition with an `if` statement. This is demonstrated in the fragment of code below. 



## **2.2 Logical and Relational Operators** 

In Sect. 2.1 we demonstrated the use of `if` statements by using the relational operator “greater than”. To fully utilise `if` statements and, as we shall see later, `while` statements and `for` loops, we need to extend our range of logical and relational operators. These are summarised in 

Tables 2.1 and 2.2. The combination of logical and relational operators allow any reasonable condition to be implemented in C++ code. 

**_Table 2.1_** Logical operators in C++ 

|**Logical**<br>**condition**|**Operat**<br>**or**|
|---|---|
|AND|`&&`|
|OR||
|NOT|`!`|



**_Table 2.2_** Relational operators in C++ 

|**Relation**|**Operator**|
|---|---|
|Equal to|`==`(note that it is not<br>“`=`”)|
|Not equal to|`!`=|
|Greater than|`>`|
|Less than|`<`|
|Greater than or equal<br>to|`>`=|
|Less than or equal to|`<`=|



A �irst example of the combination of logical and relational operators is to replace the nested `if` statements in Listing <u>2.1</u> by a single `if` statement. The condition in the new `if` statement is true if, and only if, both the condition `x` > `z` and the condition `p` > `q` are true. If this compound condition is met, the value 10 is assigned to the variable `y` . This is demonstrated in the code below. 



The example code fragment below uses a combination of logical and relational operators to set a double precision �loating point variable `y` 

to the value 10 if either `p` > `q` or the integer variable `i` is not equal to 1. If neither of these conditions has been met, then the variable `y` is assigned the value −10. 



The logical operator “NOT” is often used in conjunction with Boolean variables. This is demonstrated in the example code below, where the integer variable `i` is incremented by the value 2 if, and only if, the Boolean variable `flag` takes the value `false` . 



## **2.3 The** **`while` Statement** 

A `while` statement is used if a collection of statements are to be executed until some prescribed condition is not met. The C++ syntax for `while` statements is similar to that for `if` statements. 

A �irst example of a `while` statement is given below. A variable `x` is initially assigned the value 10. On each execution of the code inside the `while` statement the value of the variable `x` is halved. This is repeated while the value of the variable `x` is greater than 1. 



Although `while` statements are frequently used in C++ programming, they should be used with care. Consider the fragment of code below. Suppose we want to develop Listing <u>2.2</u> above so that we count the number of times that we halve the variable `x` . This may be achieved by the use of an integer variable `count` which is incremented every time the statements inside the curly brackets are executed, as shown below. 



The output of this code is shown below. 



The important thing to note in the example output above is that the condition `x` 1.0 is tested _only at the beginning_ of the statements enclosed within the curly brackets. In particular, this condition �irst became untrue when the variable `x` was assigned the value 0.625 at line 5 in the code. However, the condition `x` 1.0 was not tested at this point, and so the variable `count` was incremented as line 8 will be executed before leaving the `while` loop. 

Were we to want a loop to be executed _at least once_ , regardless of any other conditions, then we can use the `do-while` syntax which tests at the end of the loop, as shown below. 



The output of this code (shown below) demonstrates that the body of the loop is executed once, even though the initial value of `x` does not satisfy the condition in the guard. 



We may nest `while` statements in exactly the same way as `if` statements, described in Sect. 2.1.5. 

## **2.4 Loops Using the** **`for` Statement** 

The simplest application of a `for` loop is to execute a collection of statements a speci�ied number of times. The fragment of code below demonstrates how to execute a given statement 10 times. 



Line 1 of the code above deserves more explanation. The �irst statement in this line of code declares an integer variable `i` , and initialises this variable to the value 0. The code inside the curly brackets is executed if, and only if, the variable `i` is less than 10. The �inal content of this line of code increments `i` by the value 1 each time all the statements enclosed by the curly brackets have been executed. The output of this code is therefore 



We may also nest `for` loops in a similar way to that for `if` statements described in Sect. <u>2.1.5. Furthermore,</u> `for` loops may be de�ined to be executed a variable number of times, as demonstrated in the example code below. 



Before explaining what the code above does, it is important to understand what line 3 of code (the second `for` statement) does. In a similar vein to the discussion of the initial example of a `for` loop, we see that the �irst statement initialises the integer variable `j` to 5. The statements within the furthest indented curly brackets are executed when the variable `j` is greater than the variable `i` . Each time these statements have been executed, `j` is decremented by the value 1. 

We are now in a position to understand the whole of the code above. The loop over the variable `i` is known as the _outer loop_ , and the loop over the variable `j` is known as the _inner loop_ . The �irst time the statements in the outer loop are executed, `i` takes the value 0. When `i` takes this value, the third line of code tells us that `j` takes the values 5, 4, 3, 2, 1. The second time the statements in the outer loop are executed, `i` will take the value 1, and so `j` will take the values 5, 4, 3, 2. We may now deduce that the output of the code above will be 



### **2.4.1 Example: Calculating the Scalar Product of Two Vectors** 

The scalar product between two vectors of the same length may be computed using a `for` loop. Suppose the vectors are both of length `n` , and are stored in double precision �loating point arrays `vector1` and `vector2` of the correct size. Remembering that the indexing of C++ arrays begins from zero, the scalar product (discussed in more detail in Sect. A. 1. 2) between these vectors—de�ined to be a double precision �loating point variable `scalar_product` —is given mathematically by the following sum: 



The mathematical expression above for calculating the scalar product is implemented in C++ below for the case `n=2` . Note that the variable `scalar_product` must be initialised to 0 before any calculation is carried out. 



## **2.5 The** **`switch` Statement** 

A good understanding of the �low of control resulting from `if` , `while` and `for` statements is crucial for implementation of scienti�ic computing applications. One further statement that is used less frequently is the `switch` statement. This statement is best explained by example. Consider the code below, where the variable `i` has been declared as an integer. Note that the language speci�ication says that the 

_control variable_ , which is `i` in our case, must be an integer and not a �loating point type. 



If `i` takes the value 1 when the code above is executed, the statements below line 4 will be executed until the line of code `break` is reached (line 8). At the point when `break` is reached, the �low of execution will leave the code inside the curly brackets. Similarly, if the code is executed when `i` takes the value 20, then the statements below line 6 will be executed until the line of code `break` is reached. For all other values of `i` the line of code after `default` (line 9) will be executed. 

Switch statements were introduced to programming languages because they are very easy for compilers to implement ef�iciently. However, they are notorious as places where programmers introduce bugs by forgetting to end `case` statements with the `break` keyword or by forgetting to give a `default` case. Switch statements should be written with care. 

## **2.6 Tips: Loops and Branches** 

In this tips section, we highlight several traps that programmers who are new to C++ may fall into. 

### **2.6.1 Tip 1: A Common Novice Coding Error** 

Below is code that has been written with the intention of doubling a variable `x` �ive times. 





It would be expected that this code would output the value 

. However, the actual output of this code is 



Why is this? Hint: look very closely at line 2 of the code above. The reason for the surprising output is the semi-colon at the end of line 2. This is a common error for programmers who are new to the language. After seeing that most lines end with a semi-colon you might begin to get into the habit of ending _every_ line with one. When you see the guard at the beginning of a `for` , `while` or `if` statement without a semi-colon at the end then it might be tempting to stick one in! You might ask “If the loop is not executing as intended, why is the �inal answer `x = 4` and not `x = 2` ?”. The answer is that the empty space in line 2 between the “ `)` ” and the “ `;` ” is being interpreted as the body of the loop—it is the empty _nothing_ which is executed 5 times. The intended body of the loop (lines 3–5) is treated as a _block_ with special scope (see Sect. <u>5. 1</u> for more information). This block has no connection with the `for` loop and is executed once. 

### **2.6.2 Tip 2: Counting from Zero** 

Programmers who are experienced with M����� or Fortran may be used to a loop beginning from 1 and ending when the loop variable reaches a given value. If we wish a loop to execute exactly four times, we would write it in M����� or Fortran as 





In both cases the variable `j` (in the M����� code) or `J` (in the Fortran code) takes values from 1 to 4 inclusive. When programming in C++ it is common to write the equivalent loop from 0 up to, but not including, 4. That is, `j` = 0, 1, 2, 3. The reason for this is that while M����� and Fortran use _one-based indexing_ where array indexing starts at 1, C++ uses _zero-based indexing_ . It is a good idea to write loops in the form of the second loop given below. 



### **2.6.3 Tip 3: Equality Versus Assignment** 

When we introduced relational operators in Table 2.2, we noted that there is a difference between a single `=` and a double `==` . The operator `=` is an assignment operator which takes the value on the right-hand side and assigns it to the variable on the left-hand side. The equality operator `==` returns true if, and only if, the values on the left and right are equal. 

A common programming error is to mistake one for the other. 



The code above shows two common unintended bugs in C++ code. Line 2 of this code will test whether or not the variable `x` is equal to 4, but assign no value to `x` . This line therefore has no overall effect. Your compiler may give you a warning. However, as different compilers will give different warnings, you should not rely on this. Unless suitable compiler �lags are used the compiler will give no error since it is valid syntax. The second error is shown in lines 8–11 of the code. In this case, line 8 of the code uses assignment (a single equals sign) when equality testing (a double equals sign) was intended. This code will have the effect of changing the value of `x` to the value 4 when this was not intended. The condition which is actually tested is obtained from the value of the assignment. A non-zero value (in this case the value 4) is interpreted as success, and so this condition is met. The code inside the curly brackets therefore will be executed, and so the variable `x` will take the value 6. Again, this is valid syntax so the compiler may give no warning or error. 

Some compilers may report these types of problems as either warnings or errors. You may be able to ensure that the compiler informs you of these quite subtle problems by switching on warnings, as we described in Sect. <u>1. 3. 3.</u> 

If we include the above in a program called `Tip.cpp` , and compile with the �lag to switch on all warnings, then the GNU C++ compiler gives the following warnings: 



We see that, although the offending lines are not doing what was intended, an executable that can be run is still produced. If we compile with the compilation �lag `-Werror` discussed in Sect. <u>1. 3. 3, then the</u> warnings now become errors, and so no executable program is produced. In this case, we get the following output at compilation time: 



### **2.6.4 Tip 4: Never Ending** **`while` Loops** 

As discussed brie�ly in Sect. <u>2.3, it is essential to ensure that the code</u> can always leave a `while` loop. The code below was written to �ind the maximum of an array of four positive numbers called `positive_numbers` . Why will this code never leave the `while` loop? 



The problem with the code above is that the integer `count` is not incremented inside the `while` statement. The variable `count` will therefore always take the value 0, the condition `count < 4` will always be satis�ied, and the code will never exit the `while` loop. 

### **2.6.5 Tip 5: Comparing Two Floating Point Numbers** 

If `i` and `j` have been declared as integers, and we want to set another integer variable `k` to zero if these variables take the same value, then this may easily be written in C++ using the following code. 



Suppose, instead, we wanted to set `k` to zero if two double precision �loating point variables `p` and `q` take the same value. It may be thought that a very simple modi�ication of the code above will suf�ice, where `p` and `q` are declared as double precision �loating point variables and the guard in line 2 of the listing is modi�ied to test for equality of `p` and `q` . This, however, is not the case. Operations between �loating point numbers all induce rounding errors. As a consequence, if the true value of a calculation is 5, the number stored may be 5.000000000000186. Testing two double precision �loating point variables for equality is unlikely to give the expected answer, as due to rounding errors it is unlikely that two such variables will ever be equal. Instead, we should check that the two numbers differ by less than some very small number ~~,~~ <u>2</u> as shown below. 



## **2.7 Exercises** 

## **2.1** 

Below is an example fragment of code that uses several features introduced in this chapter. The variables `x` , `y` and `z` are all double 

precision �loating point variables. 



1. Explain, in words, what the fragment of code does. 2. 

What value would the fragment of code assign to the variable `z` when the variables `x` and `y` take the following values: 

(a) `x = 10.0` , and `y = -1.0` ; (b) `x = 10.0` , and `y = 20.0` ; and (c) `x = 0.0` , and `y = 20.0` . 3. 

Modify the code above so that the condition `x` > `y` is replaced by `x y` . 

## **2.2** 

Below is some example code. The exercises below all require modi�ication of this code. In all cases use a suitable check to ensure your code is correct. 



#### 1. 

Set the variable `x` to the value 5 if either `p` is greater than or equal to `q` , or the variable `j` is not equal to 10. 

2. 

Set the variable `x` to the value 5 if both `y` is greater than or equal to `q` , and the variable `j` is equal to 20. If this compound condition is not met, set `x` to take the same value as `p` . 

3. 

Set the variable `x` according to the following rule. 



**2.3** In this exercise you are asked to write and test a program which sums a list of numbers which are provided by a user via `std::cin` (see Sect. <u>1. 5. 2).</u> 

1. 

Write a program that calculates the sum of a collection of positive integers that are entered by the user from the keyboard. Your program should prompt the user to enter each integer followed by the return key, and to enter “−1” at the end of the list of integers to be added. Note that there is no need to store the list of integers: you can keep track of the sum as the user is entering the values. 

2. Modify your code so that the code terminates if the sum of integers entered up to that point exceeds 100. 3. 

Modify your code so that, if the user has entered an incorrect integer, they may enter “−2” to reset the sum to zero and begin entering integers again. 

## **2.4** 

This exercise uses the following vectors and matrices: 



Furthermore, the vector _w_ satis�ies . These vectors and matrices are stored in arrays using the following program. This program includes code to calculate the vector _w_ . 



We now de�ine vectors _x_ , _y_ , and _z_ , and matrices _C_ and _D_ , such that 



Develop the program above to calculate the vectors _x_ , _y_ , and _z_ and the matrices _C_ and _D_ , using loops where possible. Hint: make sure you de�ine arrays of an appropriate size for these variables. Check your answer by printing out the results, and comparing with direct calculation. 

## **2.5** The inverse of a 2 2 square matrix is given 

in Sect. <u>A. 1. 3.</u> 

1. 

Write code to calculate the inverse of the matrix given by 



2. 

Check that the inverse calculated is correct by printing out the entries of the inverse, and comparing with direct calculation. 3. 

Modify your code to include an `assert` statement that checks that the determinant of the matrix is nonzero. 

## **2.6** 

The Newton–Raphson method (see, for example, Kreyszig [2]) is often used to solve nonlinear equations of the form . This is an 

iterative algorithm: given an initial guess _x_ , successive iterates satisfy 



This algorithm may be terminated when for some user. prescribed 

In this exercise, we will apply the Newton–Raphson algorithm to the function _f_ ( _x_ ) = e + _x_ 5, with initial guess _x_ = 0. 

1. 

Write down (on paper) the Newton–Raphson iteration for this choice of _f_ ( _x_ ). 2. 

By using a `for` loop, and an array for the iterates _x_ , write a program 

that implements the Newton–Raphson iteration for _i_ = 1,2,3,..., 100. Print out the value of _x_ on each iteration, and con�irm that the 

iteration does converge as _i_ increases. At this stage, do not worry about terminating the iteration when is suf�iciently small. 

3. 

Think of a check that can be performed on the iterates _x_ , as _i_ becomes 

larger, that allows you to have con�idence that your solution is correct. Implement this check in your program. 4. 

It is not necessary to store the value of _x_ on each iteration to 

implement the Newton–Raphson algorithm. All that is needed is the previous iterate, , and the current iterate, _x_ . Modify your code so that the array representing is replaced by two scalar variables, `x_prev` and `x_next` . 5. 

Modify your code so that, by use of a `while` statement, the iteration terminates when | `x_next` - `x_prev` | . Investigate the use of 

different values of . 

## **Footnotes** 

##### <u>1</u> 

Nobody knows what happened to the Mars Polar Lander in the last few seconds of its descent in 1999, but experts believe there was a bug in the landing gear sensor code. This bug involved accumulating weak signals from the landing gear and may have caused the retrorockets to cut out too early. 

##### <u>2</u> 

If `p` and `q` are the results of two calculations which ought to be equal, to within machine precision, then they many differ by about | `p` | `DBL_EPSILON` , since `DBL_EPSILON` 2e–16 is de�ined in 

`#include <cfloat>` to be smallest double precision �loating point number such that 

1.0+ `DBL_EPSILON` is not equal to 1.0 when rounding errors are taken account of. 

© Springer International Publishing AG, part of Springer Nature 2017 Joe Pitt-Francis and Jonathan Whiteley , _Guide to Scienti�ic Computing in C++_ ,  Undergraduate Topics in Computer Science <u>https://doi.org/10.1007/978-3-319-73132-2_3</u> 

# **3. File Input and Output** 

Joe Pitt-Franci ~~s~~ <u>1</u> and Jonathan Whitele ~~y~~ <u>1</u> 

- (1) University of Oxford, Oxford, UK 



**Joe Pitt-Francis Email:** <u>joe.pitt-francis@cs.ox.ac.uk</u> 

Being able to transfer data between applications is an essential requirement of most scienti�ic computing software. For example, data de�ining the boundary of an object may be generated from an image processing application. This data may subsequently be used by many applications written by a variety of users. To allow exchange of data between applications in this manner requires us to store data in a clearly speci�ied format. Reading and writing �iles to a given speci�ication therefore plays a key role in scienti�ic computing applications, and is the subject of this chapter. 

## **3.1 Redirecting Console Output to File** 

We introduced basic C++ commands for writing text and the contents stored by a variable to the console in Sect. <u>1. 5. On a Linux system this</u> output may very easily be redirected to a single �ile rather than the screen. Should the executable �ile be called `SampleCode` , this output may be printed to the �ile `SampleOutput.txt` by executing at the command line, as described in Sect. <u>1. 3. 2, with the executable name</u> being followed by a speci�ication of the �ile to be written to, as shown below: 



When output has been redirected to �ile in this way, you may prefer to print to screen errors encountered by the program. This can be done using `std::cerr` as shown below. The word `cerr` is a contraction of **c** onsole **err** or. 



The syntax for `std::cerr` is identical to that for `std::cout` . When the console output is not redirected to �ile there is no difference between the effect of these two commands. However, when output is redirected to a speci�ied �ile, only the `std::cout` statements are redirected: the output from a `std::cerr` statement will still be printed to the screen. Should output from the code above be redirected to �ile, then the value given by dividing `x` by `y` will be written to the speci�ied �ile unless the variable `y` takes the value zero. Under these circumstances, the message “ `Error - division by zero` ” will be printed to the screen instead. 

## **3.2 Writing to File** 

In the previous section, we explained how all the output of an application may be printed to a single �ile. This may be adequate for some applications, but is de�initely not adequate for all applications. For example, were we to write a code to calculate the �inite element solution of a given differential equation we may want to store the nodes of the mesh in one �ile, the connectivity array de�ining the elements in 

another �ile, the �inite element solution in another �ile, and—perhaps— the nodes comprising the individual faces of the elements in another �ile. We therefore need to be able to write output to more than one �ile. Although C++ offers an extremely large number of commands for printing to �ile, almost all �ile formats can be achieved by using a very small subset of these commands. 

Writing to, or reading from, �ile requires the additional header �ile `fstream` . In the code below, we show how to write to �ile. We �irst declare an _output stream variable_ `write_output` by specifying it as being of type `std::ofstream` , and also specify the �ilename “ `Output.dat` ” as shown in line 9. Line 10 then checks that the �ile has been successfully opened: we return to this point below. Writing to �ile is similar to console output, but replacing `std::cout` with `write_output` in line 13: this writes the entries of the arrays `x` and `y` to the �ile associated with the output stream variable, in this case `Output.dat` . Finally, in line 15, when all required data has been written to �ile, we “close the �ile handle” . In Sect. <u>1. 5. 1, we explained</u> that console output is buffered, and so the output may not immediately be written to the console. Output to �ile is also buffered: closing the �ile handle _�lushes_ the buffer: that is, all data that has been buffered is written to �ile before the computer executes any further statements. It is important that this is done: if another part of the program reads a �ile which is still being written to, then we cannot be certain what data—if any—has yet been written to disk. Closing the �ile handle has the further effect that no more data can be written to this �ile: this prevents the �ile being corrupted by mistakenly attempting to write further data. We note at this point that explicitly closing the �ile handle on line 15, and in many of our later examples, is actually redundant for the simple reason that the call to `close()` will be run automatically as the �ile handle is tidied when the `main` function �inishes. However it is good practice for the novice programmer to make this call explicitly and thereby to know when to expect output from their program to be written to �ile. 



It is also possible to �lush a buffer without closing the �ile handle. This is done in a similar way as for console output in Sect. <u>1. 5. 1, and is</u> demonstrated below for the output stream variable `write_output` . 



We explained above that it is important to check that a �ile has been opened (line 10 of the Listing <u>3.1) before attempting to write any data</u> to it. If the �ile cannot be opened—perhaps we did not have permission to write to that �ile, or a directory we have speci�ied does not exist— then writing to the `ofstream` may cause no error even though writing to the �ile is not possible. For example, if in line 9 we renamed the location of the output �ile to a folder we are restricted from writing to as follows: 



then we might expect the program to fail as we are unlikely to have permission to write to the folder `/etc/` . However, without the test for the �ile being open the code will exit normally, producing no output �ile. This would clearly be very frustrating for the user of the code. 

The executable created from Listing <u>3.1</u> will create a new �ile, `Output.dat` , if this �ile does not already exist. If this �ile does exist, the executable generated from the listing above will delete the original �ile and write a new �ile with the same name: the original contents of the �ile will be lost ~~.~~ <u>1</u> Whether or not the �ile `Output.dat` existed before the code above was executed, after execution there will be a �ile called `Output.dat` that is listed below. 



The code in Listing <u>3.1</u> may do what was required, but it may not. Suppose that, rather than deleting the �ile if it exists, we want our code to append data to the end of this �ile. This would be achieved by modifying line 9 of Listing <u>3.1</u> to 



If the �ile `Output.dat` did not exist and we were to execute the code in Listing <u>3.1, with line 9 modi�ied as shown above, we would then</u> create the �ile `Output.dat` shown in Listing 3.2. If we were then to execute the code a second time we would then end up with the �ile `Output.dat` being modi�ied as shown in Listing 3.3 below. 



### **3.2.1 Setting the Precision of the Output** 

The key formatting command for scienti�ic computing applications is speci�ication of the precision of the output. This is demonstrated in the listing below. The number in brackets after the `precision` commands 

speci�ies the number of signi�icant �igures that the output is correct to. Note that when the precision is set to 10 signi�icant �igures in line 15 of the listing below only eight signi�icant �igures will be printed: this is because the variable `x` is only given to eight signi�icant �igures, and so the remaining accuracy requested is redundant. 



## **3.3 Reading from File** 

When reading from �ile we �irst need to declare an _input stream variable_ in a similar way to the output stream variable described in Sect. 3.2, and then specify the �ile that we wish to read. As with output to �ile, the header �ile `fstream` should be included. Reading the �ile is then performed in a similar way to that described for keyboard input in Sect. 1. 5. 2, with `std::cin` replaced by the input stream variable. Suppose we want to input the �ile `Output.dat` shown in Listing 3.3. We know that this �ile has six rows and two columns, and so we may read this �ile using the code shown in Listing 3.4. The assertion in line 9 ensures that `Output.dat` is on disk in the correct location and with the correct access privileges: if not, the assertion is tripped and the code is terminated. 



In the code above, we knew that the �ile we were reading had six rows and two columns, and so we knew when writing this code that the statements inside the `for` loop had to be executed six times. In many scienti�ic computing applications we will want to read a �ile, but do not know the length of the �ile in advance. For example, we may know that a �ile contains a list of the coordinates of an unknown number of points in two dimensions: the �ile therefore has two columns, but an unknown number of rows. We cannot use a `for` loop as we do not know how many times the statements in this loop need to be executed. Instead, we use the Boolean variable associated with the input stream variable `read_file.eof()` . This variable takes the value `true` when the **e** nd **o** f the **f** ile is reached, and allows us—through the use of a `while` statement—to carry on reading the �ile while this variable takes the value `false` . Assuming that we know that the number of points is fewer than 100, we may achieve this using the following code. Note that a potential problem with this code as given will be addressed in Exercise <u>3.2.</u> 



One additional feature of reading from �ile that is of use when writing scienti�ic computing applications is the ability to _rewind_ a �ile so that we can read a �ile starting from the beginning again. This may be achieved by inserting the statements below into the code at the point where the �ile should be rewound. 



## **3.4 Checking Input and Output are Successful** 

In Sect. 3.2 we advised C++ programmers to con�irm that a �ile has been opened before writing any data to that �ile. We justi�ied this using the example of attempting to open a �ile in a directory that doesn’t exist. Under these circumstances the intended data would not be written to �ile, but the code would proceed without informing us of this. 

Even if we do con�irm that a �ile we are intending to write to is open there are other problems that may occur. We may successfully write some data to �ile, and then reach our disk quota set by the system administrator. Subsequent attempts to write to �ile would then fail, although the code would continue to execute. Alternatively we may be expecting to read 50 double precision numbers from a �ile that only 

contains 40 such numbers. After successfully reading 40 numbers we would like to be informed that we had reached the end of the �ile, and no more numbers were available to read in. We can check that reading from or writing to �ile has taken place as expected using the C++ function `ios::good` . Use of this function is illustrated below for the case of writing to �ile; its use when reading from �ile follows a similar pattern. 



## **3.5 Reading from the Command Line** 

In scienti�ic computing applications, it is common for a user to want to set some of the parameters used themselves when executing the code. For example, if code has been written to calculate the temperature distribution in a bar using the �inite difference method the user may wish to set the thermal conductivity of the bar, or the number of nodes used in the �inite difference grid, at the same time that the code is executed. Fortunately, C++ allows the user to do this when running from the command line. 

In Sect. 1. 2 we promised to explain the third line of the C++ program given in Listing 1. 1, namely the line of code shown below. 



Although we are not quite ready to explain the _whole_ meaning of this line until we have introduced pointers in Chap. <u>4, we may explain how</u> this line allows us to specify input arguments to a program from the command line. Suppose—as described above—we want to write code that allows us to specify an integer number of nodes, `number_of_nodes` , to be used in a �inite difference grid, and a double precision �loating point variable, `conductivity` , that represents the 

thermal conductivity of a bar. This is demonstrated by the following code. We will explain the additional header �ile `cstdlib` used in line 2, and the functions `atoi` and `atof` used in lines 15 and 16 at the end of this section: for the time being we will focus on how to input data from the command line. 



We would instruct the user to specify these parameters by typing the executable name, followed by the number of nodes to be used in the �inite difference grid, followed by the value for the conductivity: that is, if we want to use 100 nodes and a conductivity of 5.0 we would compile the code above to produce the executable `CommandLineCode` and then enter the following at the command line: 



This would produce output 



We see from the code and output above that the integer variable `argc` contains the number of arguments speci�ied at the command line. In this case this is three: these are the executable name `./CommandLineCode` , the integer `100` , and the �loating point number `5.0` . These are stored as the ordered list 

`argv[0],argv[1],argv[2]` , as is demonstrated when we use the `for` loop to print these out. Each of these are stored as arrays of characters, and so we must �irst convert these arrays of characters to the appropriate variable types. This is performed by lines 14, 15 and 16 of the code listed. In line 15, we use the function `atoi(argv[1])` to convert the array of characters stored by `argv[1]` to an integer. Similarly, `atof(argv[2])` converts `argv[2]` to a �loating point variable. The functions `atoi` and `atof` require the header �ile `cstdlib` which has been included in line 2. 

## **3.6 Tips: Controlling Output Format** 

If the �iles that are written are to be read only by a computer, then it does not really matter whether these look attractive or not. For example, if a data �ile is only to be used for importing into a visualisation package then it does not matter if the format of this �ile is opaque to humans provided the visualisation package can read the �ile accurately. If, however, humans may want to look at these �iles then formatting commands, such as controlling the width of each column may be desirable. 

Below we show how to implement three commonly desired formatting techniques which we now list before demonstrating. 

1. 

_Output in scienti�ic format._ Scienti�ic format is where a number is written as a product of one number with only one signi�icant �igure to the left of the decimal point and an integer power of 10, that is, 465.78 in scienti�ic format is 4.6578 10 , which may be written in C++ 

notation as `4.6578e2` . This is achieved by the use of the �lag `std::ios::scientific` which requires the header �ile `fstream` . 2. 

_Always showing a or_ − _sign._ The default setting for an output stream is not to print a plus sign before a positive number. To line up numbers in neat columns, we may wish to always precede a number with a plus or minus sign: this is achieved by the use of the �lag `std::ios::showpos` which requires the header �ile `fstream` . 3. 

_Precision of scienti�ic output._ When scienti�ic format is used the `precision` statement works slightly differently to that described in Sect. 3.2.1: in this case the precision speci�ied is the number of digits _after_ the decimal point, and so the number of signi�icant �igures is one greater than this number (as there is another signi�icant �igure before the decimal point). Furthermore, in contrast to the precision set in Sect. 3.2.1, when scienti�ic format is used zeros are added after the decimal point to ensure that all output is of exactly the same width. 

These formatting techniques are demonstrated in the code below. 



## **3.7 Exercises** 

## **3.1** 

This question assumes that you are starting from the code in the listing below. 



1. 

Extend the code above to print the arrays `x` and `y` to a �ile called `x_and_y.dat` so that the data �ile has the four elements of `x` on the top line, and the four elements of `y` on the next line. 2. 

Extend the code so that the output stream is �lushed immediately after each line of the �ile is written. 3. 

Extend the code so that the precision is set to 10 signi�icant �igures, the output is in scienti�ic notation, and plus signs are shown for positive numbers. 

4. 

Amend the program so that it does not automatically create a fresh �ile `x_and_y.dat` every time it is run. Have the program �irst attempt to open the �ile `x_and_y.dat` as an `ifstream` for reading. If the �ile can be successfully opened then, after closing the `ifstream` , warn the user. Have the program prompt the user as to whether it should erase the existing �ile or append to the existing �ile. 

## **3.2** 

This question uses the data �ile `x_and_y.dat` that was written in the previous exercise. The code below assumes that we know that the data �ile has 4 columns and that we want to count the number of rows. 



Run the code above. This code does not give the correct answer. Why is this? Does the code give the correct answer if the �inal newline 

character is removed from the �ile `x_and_y.dat` ? Modify the code so that it gives the correct answer. [ _Hint: You might investigate the use of_ _`read_file.fail()` which may be used to probe whether the last read on the �ile stream was unsuccessful._ ] 

## **3.3** 

Write code to implement the implicit (or backward) Euler method to solve the initial value ordinary differential equation 



on the interval using a constant step size _h_ . Allow the user to 

specify the number of grid points, _N_ they want to use at the command line, and use an `assert` statement to ensure that the number of grid points is greater than 1. Use the number of grid points to calculate the step size _h_ . Your code should print a �ile called `xy.dat` that has two columns: the calculated values of _x_ ; and the calculated values of _y_ . Plot the data from the �ile `xy.dat` and hence compare it with the true solution . 

[ _The implicit Euler method_ ( _see, for example, Süli and Mayers_ [3]) _for this problem results in the difference relation_ 



_where h is step size_ and _y_ is the solution at 

, where _N_ is the number of grid points, and we have used zero-based indexing for the vectors `x` and `y` .] 

## **Footnotes** 

> If you want to check for the existence of a �ile before opening an output stream to it then a simple thing to do is to �irst attempt to read from it. See Exercise <u>3.1</u> 

<u>1</u> 

© Springer International Publishing AG, part of Springer Nature 2017 Joe Pitt-Francis and Jonathan Whiteley , _Guide to Scienti�ic Computing in C++_ ,  Undergraduate Topics in Computer Science <u>https://doi.org/10.1007/978-3-319-73132-2_4</u> 

# **4. Pointers** 

Joe Pitt-Franci ~~s~~ <u>1</u> and Jonathan Whitele ~~y~~ <u>1</u> 

- (1) University of Oxford, Oxford, UK 



**Joe Pitt-Francis Email:** <u>joe.pitt-francis@cs.ox.ac.uk</u> 

One of the key features of the C++ language is the concept of a _pointer_ . We will see later in this chapter that pointers are extremely useful for allocating memory for arrays whose sizes are not known when the code is compiled. We will see in Chap. 5 that they also have use when writing functions that allow us to repeat the same operation on different variables. We conclude this chapter by discussing some features of pointers that have been introduced in recent C++ standards. 

## **4.1 Pointers and the Computer’s Memory** 

Pointers are best introduced by explaining how they relate to the storage of variables in the computer’s memory. 

### **4.1.1 Addresses** 

Let us suppose that an integer variable `total_sum` is declared and assigned the value 10: 



The address—that is, location—of this variable in the computer’s memory is given by `&total_sum` and can be printed to the console in 

the usual way (as shown below) although this address will not be meaningful to humans. 



When the integer variable `total_sum` is declared, memory is allocated to this variable, and the location of this memory will not vary throughout execution of the code. As such, the expression `&total_sum` , which represents the address of this location, will take a constant value throughout execution of the code. 

### **4.1.2 Pointer Variables** 

In addition to data types such as integers and �loating point numbers that we have encountered earlier in this book, we may also declare _pointer variables_ which are variables that store addresses—that is, the location in the computer’s memory—of other variables. In the code below, `p_x` is a pointer to a double precision �loating point variable, and `p_i` is a pointer to an integer variable. The pointer `p_x` may then be used to store the address of a double precision �loating point number, whilst `p_i` may be used to store the address of an integer. The asterisk that pre�ixes these variables when they are declared indicates that these variables are pointers. In this book, we follow a coding standard where all pointer variables, apart from those introduced later in this chapter that represent arrays, have names that begin with `p_` to denote that they are a pointer variable: a discussion of conventions such of these that are used for variable names, which forms a part of what is known as _coding standards_ , is given in Sect. <u>6. 6.</u> 



Note that the spacing can vary, so that `int* p_i` and `int *p_i` are equivalent. However, `int* p_i` states more clearly that the type of `p_i` is a pointer to an integer, rather than an integer. 

All pointer variables require an asterisk when they are declared. Hence, in the code below, `p_x` , `p_y` , `p_i` are pointers, while `j` is an integer variable. 



When declaring more than one pointer on a line the asterisk must be repeated as shown in line 1 of the listing above, which means that `int* p_i` in line 2 would be less appropriate as only one variable ( `p_i` ) is a pointer variable. For this reason, we recommend only one pointer declaration per line. 

Now we have explained how to declare a pointer variable, and what these variables represent, we explain how to use them. 

### **4.1.3 Example Use of Pointers** 

If a variable `p_x` has been declared as a pointer to a double precision �loating point number, then it is clearly important to distinguish between: (i) the location of the memory to which this pointer points at (denoted by `p_x` ); and (ii) the contents of this memory (denoted by `*p_x` ). The asterisk operator in `*p_x` is called a _pointer de-reference_ and can be thought of as the opposite to the `&` operator introduced in Sect. 4.1.1. 

The code below shows how pointers to double precision �loating point variables may be combined with double precision �loating point variables. 



### **4.1.4 Warnings on the Use of Pointers** 

A variable pointer should not be used until �irst having been assigned a valid address. For example, the following fragment of code may cause problems that are dif�icult to locate. 



In the code above, we haven’t speci�ied the location of the double precision �loating point variable that `p_x` points at. It may therefore be pointing at _any_ location in the computer’s memory. Changing the contents of an unspeci�ied location in a computer’s memory—as is done in line 5 of the code above—clearly has the potential to cause problems that may be hard to locate. This problem may be avoided by the use of the `new` keyword as shown below to allocate a valid memory address to `p_x` , and the `delete` keyword which releases this memory to be used by other parts of the program when this memory is no longer required. 



A further reason to use pointers with care is shown in the code below. The �irst time `y` is printed (in line 5) it takes the value 3: the second time `y` is printed (in line 7) it takes the value 1 even though `y` is not explicitly altered in the code between these two lines. This is because the line between the `std::cout` statements, line 6, has altered the value of `y` , possibly unintentionally, by using the pointer variable `p_x` (which contains the address of `y` ) to change the value of `y` . 



A situation where the contents of the same variable may be accessed using different names, such as in the code above, is known as _aliasing_ . In C++, this is most likely to happen when pointers are involved, either when two pointers alias the same address in memory, or when a pointer references the contents of another variable. When one or more pointers allow the same variable to be accessed using different names, the aliasing is known as _pointer aliasing_ . 

## **4.2 Dynamic Allocation of Memory for Arrays** 

One of the main uses of pointers is the dynamic allocation of memory for storing arrays. In Sect. 1. 4. 5, we explained how arrays could be declared when the size of the array was known in advance. However, we do not always know the sizes of the arrays in a program when we compile the code. In Sect. 3. 5, for example, we demonstrated how to allow the user of a code to specify the number of nodes in a �inite difference grid when executing the code. If the coordinates of the nodes in this mesh were to be stored in an array we would not know, when compiling the code, what size to make this array. Under these circumstances, using the method of declaring arrays given in Sect. 1. 4. 5, we have to compile the code with some estimate of the size of this array. If we overestimate the size of this array, we are being wasteful of computational memory with the potential effect of preventing the execution of the code on a system with insuf�icient memory. If we underestimate the size of this array, the program will almost certainly crash. In either case, we will then have to recompile the code with a new estimate of the array size. The use of pointers to dynamically allocate memory for arrays avoids these problems, as we do not need to know the array size at compile time. 

A further use of pointers for dynamically allocating memory is for the ef�icient storage of irregularly sized arrays, for example a lower triangular matrix. If a lower triangular matrix is stored in an array as described in Sect. <u>1. 4. 5, we will have to allocate the same number of</u> columns to each row of the matrix. As we know that roughly half these entries are zero, we are being wasteful of computational memory. Dynamic allocation of memory allows us to allocate memory more prudently. 

Memory can be allocated using the `new` operator, and deallocated using the `delete` operator. 

### **4.2.1 Vectors** 

To use pointers to create a one-dimensional array of double precision �loating point numbers of length `10` called `x` , we use the following section of code. 



The elements of the array may then be accessed in exactly the same way as if the array had been created by using the type of declaration introduced in Sect. <u>1. 4. 5. In the dynamic allocation of memory for the</u> array using the pointer `x` above, `x` stores the address of the �irst element of the array. This can be seen by printing out both the pointer `x` and the address of the �irst element of the array, as shown below. 



The memory allocated to `x` may be, and should be, deallocated by using the statement below when this array is no longer required. 



Always be sure to free any memory allocated when it is no longer required—a code can very quickly use all available memory otherwise. 

In later chapters of this book, when we develop a class of vectors, we will see that one advantage of writing a class of vectors is that memory allocated to a vector is automatically freed when appropriate. 

An example code that uses dynamically allocated memory for arrays is shown below. This code creates two arrays, `x` and `y` , both of size 10. Elements of `x` are then assigned manually. Elements of `y` are then set to be twice the value of the corresponding element of `x` . Finally, all memory allocated is deleted. 



### **4.2.2 Matrices** 

Memory for matrices may also be allocated dynamically. For example, to create a two-dimensional array of double precision �loating point numbers with `5` rows and `3` columns called `A` we use the following section of code. 



The array may then be used in exactly the same way as if it had been created by using the declaration 



When allocating memory for the matrix dynamically in the code above, the variable `A` —which has been declared using line 2 of Listing <u>4.1—</u> has the following properties after the fragment of code has been executed: 

each `A[i]` is a pointer, and contains the address of `A[i][0]` ; and `A` contains the address of the pointer `A[0]` . 

As such, the variable `A` is an array of pointers, which explains the two asterisks in line 2 of Listing <u>4.1. Line 3 of this listing speci�ies that</u> `A` is a pointer to an array of pointers to double precision �loating point numbers, and that this array is of size `rows` . The `for` loop in this listing then speci�ies that each pointer in the array itself points to an array of double precision �loating point numbers of length `cols` . This has the effect that `A[i]` —which is a pointer—stores the address of the entry `A[i][0]` , that is, the �irst entry of row `i` . 

As was the case for vectors, it is important to deallocate memory dynamically allocated for a matrix when it is no longer needed. The memory allocated for the matrix `A` in Listing <u>4.1</u> may be freed using the following code. 



We cannot emphasise enough how important it is to always delete any memory dynamically allocated, particularly memory allocated inside loops—if not you will soon run out of memory. 

### **4.2.3 Irregularly Sized Matrices** 

Suppose we want to construct a lower triangular matrix `A` of integers with 1,000 rows and 1,000 columns. This may clearly be done using the declaration below. 



However, the declaration above wastes a considerable amount of memory storing the super-diagonal entries of the matrix which we know in advance all take the value 0. We may avoid wasting this memory by allocating the memory for this matrix dynamically, and only allocating memory for the diagonal and sub-diagonal elements. This is demonstrated in the fragment of code below, where in row `i` of the matrix we declare `i+1` nonzero elements: that is, 1 element in row 0, 2 elements in row 1, and so on. Memory can, and should be, deleted in the same way as demonstrated in the previous section when this array is no longer required. 



Although the fragment of code above does correctly allocate the memory required for a lower triangular matrix it should be used with 

care: errors would result if, for example, the entry `A[9][19]` were to be used in a code. When we develop classes later in this book, we will see how the use of classes may avoid problems such as this. 

## **4.3 Tips: Pointers** 

The concept of pointers is one that inexperienced C++ programmers often struggle with. We strongly urge the reader to attempt the exercises at the end of this chapter to improve their understanding of this topic. In this section, we give tips on the use of pointers. In all other chapters the tips section is the �inal section before the exercises. This chapter is the exception because some of the caution in the following tips may be mitigated in modern C++. We introduce these advanced topics in Sect. <u>4.4</u> which you might ignore on �irst reading. 

### **4.3.1 Tip 1: Pointer Aliasing** 

In Sect. 4.1.4, we gave an example where a pointer variable `p_x` was pointing to the memory location of the `double` variable `y` . A change was made to that variable by de-referencing the pointer `p_x` . This situation might lead to some confusion, although in a short code fragment it is easy to see that the two variables are leading to the same place: `*p_x` is an _alias_ for `y` . 

In large-scale programs, it may not be so easy to see where pointers are aliases for other variables. This is because the information that two names are pointing to same place may not be available in the same screen-full of code, or even in the same �ile. A good example of this would be a vector or matrix addition operation in which the vectors or matrices are stored as arrays and passed into a _function_ via pointers. We will deal with functions in the next chapter, but for now you need to be aware that the code for the function may be in a different �ile and that the variables may take different names inside the function de�inition. The operation to compute the matrix sum **A B C** would probably be implemented in such a function by a nested loop over the elements of the arrays, so that the actual implementation becomes an element-wise `A[i][j] = B[i][j] + C[i][j]` . There may be unknown pointer-aliasing in this function, because the user might wish 

to increment one matrix by another, i.e. to compute **X X Y** . It turns out that this pointer aliasing will be safe, because the inner loop will effectively be calculating `X[i][j] += Y[i][j]` as intended. Each of the ( _i_ , _j_ ) components of the result is independent of the others. However, what if the user were using a matrix–matrix product operation? In the computation **A BC** , the component `A[i][j]` depends on parts of **B** and **C** other than `B[i][j]` and `C[i][j]` . This means that, if the user wishes to compute **X XY** using a function written for calculating **A BC** , there is a chance that some components of **X** will be written to before they are read—leading to an incorrect calculation. One way to resolve this aliasing issue is to produce the matrix–matrix product result in temporary storage before copying it into the output argument **A** . However, this solution is inef�icient in cases where there is no pointer aliasing, especially when the sizes of the matrices are large. Another solution to the issue is to provide two versions of the matrix-matrix product operation: one which is ef�icient but only safe to use when there is no pointer aliasing and one which is safe to use in all circumstances. 

One can see that the problem of pointer aliasing is deeper than might appear from the trivial example in Sect. <u>4.1.4. In general, there is</u> no correct solution to these issues. Compiler writers spend a great deal of time �inding places where pointer aliasing has (or has not) de�initely happened so that code optimisation is only applied in situations where it is safe to do so. 

### **4.3.2 Tip 2: Safe Dynamic Allocation** 

There may be circumstances under which it is not possible to allocate memory either because the number of items in an array has been set with a negative argument or because there is not enough physical memory available to the program. Setting the number of elements in an array to a negative number is easier than you might think. If the size of a problem is con�igured via an input �ile, then a size may easily be mistyped. More subtly, if a number is assigned to an integer that is larger than the maximum value that can be stored by that integer, then the integer value stored may actually be a negative number: this is known as an _over�low error_ . 

Implementations of C++ may vary over how they treat such errors. The default behaviour is to throw an _exception_ when a memory error is encountered. We will deal with catching exceptions in Chap. <u>9</u> and note that an exception could terminate your program. Should your implementation of C++ not throw this sort of exception, then a safe way to program is to test that your variable has been assigned a value as the code fragment below illustrates. 



### **4.3.3 Tip 3: Every** **`new` Has a** **`delete`** 

We pointed out earlier in this chapter that all dynamically allocated memory must be freed, or else you may run out of memory. This problem is particularly noticeable when memory is dynamically allocated inside the body of a `for` loop, such as the one shown below. 



Each time the body of the loop in the code above is executed, new memory is allocated for the array `A` . The memory from the previous execution has not yet been freed, although it will not be available as the array `A` will be stored in the memory that has been allocated most recently: there is no automatic garbage collection for memory which is no longer accessible. You will see, when we discuss functions in Chap. <u>5,</u> that the same problem may arise when memory is allocated inside functions, but not freed before the function ends. 

If you do not delete memory which you have allocated dynamically, then that memory will not be accessible until your program �inishes 

(when all memory is handed back to the system). If you request more memory than you need, then it may be that the physical memory of the computer will be exhausted—your computer will run much more slowly and further memory allocation may fail. 

There are several ways around this issue. The �irst and foremost is to ensure that every `new` in your program is matched with a `delete` somewhere else. A second way to make sure that inaccessible or unnecessary memory is freed up is to run your program through a memory debugger (see Sect. <u>10. 6</u> for more details). Another solution, adopted by seasoned C++ programmers is to use _shared pointers_ . These are an advanced language feature which allow memory to be automatically de-allocated once there is no longer any other part of the program which can access it. 

## **4.4 Modern C++ Memory Management** 

In Sect. 1. 1. 2, when discussing why you should write scienti�ic programs in C++, we claimed that its �lexible memory management gave it an advantage over languages which use garbage collection, such as Java. However we also gave a caveat: this �lexible memory management means that you, the programmer, are responsible for making sure that memory is managed properly. Many novice C++ programmers are confused by dynamic memory allocation and become deterred when they learn that it is up to them to know when dynamically created data should be freed up with `delete` . The good news for C++ programmers is that over recent years the C++ standard has introduced smart pointer constructs which facilitate memory management—providing an ef�icient compromise between giving responsibility to the programmer and automatic run time garbage collection. These constructs were �irst introduced in the C++11 speci�ication and have been re�ined in subsequent speci�ications ~~.~~ <u>1</u> In this chapter we restrict attention to modern C++ _memory management_ but we will return to other modern C++ functionality in Chap. <u>8.</u> 

### **4.4.1 The** **`unique_ptr` Smart Pointer** 

In our �irst tip of this chapter, in Sect. <u>4.3.1, we warned about the</u> dangers of pointer aliasing. In particular we noted that there may be 

times when a programmer assumes that two pointers are pointing to different pieces of data, but that this assumption may not be true. When two pointers are pointing to the same piece of data it may lead to bugs such as an element of a matrix being overwritten before its value has been read. 

C++11 provides a smart pointer type which can guard against pointer aliasing errors. This smart pointer `unique_ptr` allows the run-time system to monitor certain pointers on an individual basis. The example of its use, given in Listing <u>4.2, is a little contrived because the</u> true power of the construct cannot be seen until it is used with functions. The program will, however, serve to illustrate a few of the main features. Your C++ compiler may not accept this program since most current compilers are set to read older C++98 standard programs by default. In order to compile the program you will need to add a �lag to indicate that the code adheres to the C++11 standard. In the case of the GNU compiler this means 



#### or similar. 

In line 6 of Listing 4.2 a new `int` is dynamically created via the `new` keyword and its address assigned to a `unique_ptr` called `p_x` . Note that the type description of the `unique_ptr` contains the type of the entity to which it points, which in this case is `int` , in angle brackets. This angle bracket notation is a _template_ description and we will see more of this in Chap. <u>8. The purpose of</u> `new int` in round brackets on line 6 is to dynamically create an `int` and pass its location into `p_x` . The variable `p_x` now acts as a facade through which the actual address of the dynamically-created integer storage may be accessed. There is more happening behind the scenes, but the reader may interpret line 7 as a de-reference used to store a value in the memory location at this address. 

We demonstrate that the compiler won’t allow us to easily assign the value of `p_x` by two lines which have been commented out: line 11 attempts to assign it to a raw pointer and line 16 attempts to assign it to another `unique_ptr` . The correct way to get the value out of `p_x` (line 

12) is to use the `get()` function to get the actual address of the managed data. Meanwhile the correct way to assign from one `unique_ptr` to another is for the ownership of the resource to be transferred between them with the function `std::move()` . This is demonstrated in line 17. Lines 18 and 19 show that the `unique_ptr` variables can be evaluated as Boolean values: true if the variable is managing a resource and false if not. 

Note that in Listing 4.2 there is no explicit call to `delete` to match with the `new` on line 6. It is actually the case that, because the `unique_ptr` is managing the resource, it is able to automatically free up memory. On line 20, `p_z` is told to relinquish ownership and this implicitly calls `delete` on the memory originally created on line 6. 



### **4.4.2 The** **`shared_ptr` Smart Pointer** 

The mismatch between the last code example (Listing 4.2) and our previously sound advice in Sect. 4.3.3, “Every `new` has a `delete` ”, prompts us to introduce the variable type `shared_ptr` . This smart 

pointer construct was not available in the of�icial C++ standard until C++14 but some C++11 compilers such as the GNU compiler support it anyway. 

The concept behind a smart shared pointer is simple. Alongside the address of the underlying resource the pointer also keeps track of a count of the number of times this resource has been used. Initially the count will be 1, but it will increment when the pointer is passed between various parts of the program. Whenever a use of the pointer �inishes the usage count will be decremented. When the count drops to 0, and there are no known uses of the pointer, the original resource will be freed up. This all happens automatically, without the user having to worry about it. It is effectively a local garbage collector which manages a small piece of memory. 

The code presented in Listing <u>4.3, illustrating the use of a smart</u> shared pointer, is again a little contrived, but it represents how this automatic memory management might work in practice. In line 6 a new integer value is dynamically created and its location is stored in a `shared_ptr` variable `p_x` . As with the previous C++11 example this new smart pointer is templated with the type of its argument in angle brackets. In line 10 another `shared_ptr` variable is created and it is assigned to the same value as `p_x` (this is an assignment which would not be possible with the `unique_ptr` type). In line 12 `p_y` is reset so that it relinquishes any claim on memory. While lines 10 and 12 are just a simple assignment and a reset, respectively, their use here actually represents general wider uses of a shared pointer. Copies of pointers may be made when they are passed into functions, as we will see in Chap. <u>5, or passed into</u> _containers_ —of the kind introduced in Chap. <u>8.</u> When functions or containers �inish, their copy of the pointer is not needed and is, in effect, reset. 



Lastly in line 14 the original pointer is reset. This has, again, the same effect as `p_x` going out of use: its claim on the data is relinquished. In this case the use count will drop to 0 and the smart pointer will automatically free up the original memory which was created on line 6. Throughout Listing 4.3 the use count of the main shared pointer `p_x` is written to the console. The output of this program is given below and re�lects the number of uses of the shared resource. This count is originally 1 when `p_x` is created, then 2 when `p_y` shares the resource, and 1 when `p_y` relinquishes its use on line 12. Finally, when `p_x` relinquishes its use, the count drops to 0. 



## **4.5 Exercises** 

**4.1** Write code that declares an integer `i` to take the value 5. Declare a pointer to an integer `p_j` , 

and store the address of `i` in this pointer. Multiply the value of the variable `i` by 5 by using a line of code that _only uses the pointer variable_ . Declare another pointer to an integer `p_k` and use the `new` keyword to allocate a location in memory that this pointer stores. Then store the contents of the variable `i` in this location. Now change the value pointed to by `p_j` to 0. Check that your program is correct by outputting the value of `i` and values pointed to by `p_j` and `p_k` . 

**4.2** Assign values to two integer variables. Swap the values stored by these variables using only pointers to integers. 

**4.3** Write code that allocates memory dynamically to two vectors of double precision �loating point numbers of length 3, assigns values to each of the entries, and then de-allocates the memory before the code terminates. Extend this code so that it calculates the scalar (dot) product of these vectors and prints it to screen before the memory is de-allocated. Put the allocation of memory, calculation and de-allocation of memory inside a `for` loop that runs 1,000,000,000 times: 

if the memory is not de-allocated properly your code will use all available resources and your computer may struggle. 

**4.4** Write code that dynamically allocates memory for three 2 2 matrices of double 

precision �loating point numbers, `A, B, C` , and assigns values to the entries of `A` and `B` . Let `C A B` . Extend your code so that it calculates the entries of `C` , and then prints the entries of `C` to screen. Finally, de-allocate memory. Again, check you have de-allocated memory correctly by using a `for` loop as in the previous exercise. 

**4.5** In Sect. <u>4.4</u> we introduced the `unique_ptr` and `shared_ptr` constructs. A useful further smart pointer is the `weak_ptr` , which is a smart pointer that does not contribute to the use count. It can be used in situations where variables need to be accessed, but only when they exist. It has functions `expired` and `lock` which can be used to check if its resource has been deleted and, if it has not been deleted, to get to the resource. 

Copy Listing <u>4.3</u> and compile it with a compatible C++11 compiler. Now add an extra smart pointer: a `weak_ptr` which is initialised to the 

value `p_x` . Experiment with printing the value original of `p_x` (i.e. the value 5) via this weak smart pointer. Try this before, and after, the `p_x` is reset on line 14. 

## **Footnotes** 

<u>1</u> 

At the time of writing the second edition of this book the relevant speci�ications are C++11, C++14 and C++17. 

© Springer International Publishing AG, part of Springer Nature 2017 Joe Pitt-Francis and Jonathan Whiteley , _Guide to Scienti�ic Computing in C++_ ,  Undergraduate Topics in Computer Science <u>https://doi.org/10.1007/978-3-319-73132-2_5</u> 

# **5. Blocks, Functions and Reference Variables** 

Joe Pitt-Franci ~~s~~ <u>1</u> and Jonathan Whitele ~~y~~ <u>1</u> 

(1) University of Oxford, Oxford, UK 



**Joe Pitt-Francis Email:** <u>joe.pitt-francis@cs.ox.ac.uk</u> 

The code developed in this book up to this point has been restricted to code that may be placed inside curly brackets after the initial line of code “ `int main(int argc, char* argv[])` ;”. Readers with previous programming experience will be aware of the limitations this places when writing code. For example, if we were to apply the same operations in different places in the code we would have to repeat the lines of code that performed these operations everywhere in the code where they were required. It would be much more convenient if we could write a function that we could call whenever we wanted to perform these operations. This chapter introduces the C++ machinery for writing functions. 

## **5.1 Blocks** 

A block is any piece of code between curly brackets. A variable, when declared inside a block, may be used throughout that block, but only within that block. This is demonstrated in the code below. In line 9, we attempt to use the variable `j` when it is only declared—and therefore available—in the block enclosed within the curly brackets in lines 4 and 8. In the language of programmers, “the scope of `j` is the block 

between lines 4 and 8”. If we attempted to use the code fragment below, the compiler would report this attempted use of `j` as an error: `j` is said to be _out of scope_ at line 9. 



The same variable name may be used for a variable declared both inside a block—termed the _local variable_ —and outside the scope of any function (including the `main` function)—termed the _global variable_ . Both of these variables may be accessed inside the block as shown in the code below, using the example of both a global and a local variable called `i` . Furthermore, we may de�ine a variable `j` in both the outer block and the inner block: inside the inner block the value of `j` stored by the variable declared in the outer block is not accessible. The multiple declaration of both `i` and `j` in the code below is bad programming practice, as it can clearly lead to confusion. In fact, since the scope of variables is so important, we suggest that variables are declared only within the block where they are needed, close to their �irst use. This multiple declaration of variables is known as _variable shadowing_ and you can avoid it happening by turning on “shadow warnings” in your compiler. With the GNU `g++` compiler this is achieved by adding the `-Wshadow` �lag to the compilation command. 



## **5.2 Functions** 

Now that we have de�ined what we mean by a block of code we may demonstrate how to write functions. 

### **5.2.1 Simple Functions** 

A simple program that writes and uses a function to determine the minimum value of two double precision �loating point variables `x` and `y` , and stores it in the double precision variable `minimum_value` is shown below. Note the _function prototype_ that is line 3 in the listing below. The function prototype tells the compiler what input variables are required, and what variable, if any, is returned. In the example below, the function prototype explains that later in the code there will be a function called `CalculateMinimum` that requires two double precision �loating point variables as input, and returns one double precision �loating point variable. The function prototype can be thought of as being similar to declaring a variable. The variable names `a` and `b` in the prototype are ignored by the compiler and don’t have to be included, but their inclusion can clarify the program. Note that the function prototype ends with a semi-colon. 

Lines 15–29 of the code contain the statements that perform the tasks required by the function. This code begins with a line of code that is identical to the function prototype (including the variable names) without the semi-colon. After this there is a block of code that ends with a `return` statement that returns the value required to the point in the code where this function was called from. Note that there is no need to declare the variables `a` and `b` inside the function—the declaration in line 15 has done this already. Variables such as `minimum` that are used inside the function but are not part of the function prototype must be declared within the function block. Line 8 demonstrates how to call a function: the variables in brackets ( `x` and `y` in this case) are sent to the function, and are known as the _arguments_ of the function. The variable returned from the function is stored as `minimum_value` . 



Note that only one variable may be returned from a function. Although suf�icient for some purposes, we may sometimes want to return more variables. We will see how this may be done later in this chapter. Of course, there are some circumstances where we do not want a function to return any variable: such functions may be prototyped as a `void` function. The code below contains an example of a function that prints out a message informing a candidate whether or not they have passed an exam. This function requires two integer variables as input: the �irst of these contains the mark that a candidate has scored; the second contains the pass mark for the exam. 



A function can only change the value of a variable sent to a function _inside_ that function: changes made within the function will have no effect on this variable after the function has been executed and the code continues to execute statements in the block where the function has been called from. This is because a copy is made of any variable that is sent to a function, and it is this copy of the variable, and not the original variable, that is modi�ied inside the function. For example, the following function has no effect on the variable `x` outside the function, even though the value of `x` _is_ changed inside the function. 



### **5.2.2 Returning Pointer Variables from a Function** 

In Sect. 5.2.1, we demonstrated how to write functions that returned either a variable that wasn’t a pointer, or had no return type. Functions can be used to return pointer variables as well, as shown in the code below. In this case, we have written a function that allocates memory for a matrix dynamically, and returns the pointer to the memory allocated. The array can then be used as if the memory were allocated in the `main` function, as demonstrated in lines 8 and 9. Because every `new` requires a matching `delete` we have avoided leaking memory by also providing a function called `FreeMatrixMemory` to free up the memory created in `AllocateMatrixMemory` . Both `AllocateMatrixMemory` and its partner function `FreeMatrixMemory` operate in the manner described in Sect. <u>4. 2. 2.</u> 



### **5.2.3 Use of Pointers as Function Arguments** 

We concluded Sect. <u>5.2.1</u> by explaining that any changes to a variable made inside a function would have no effect outside that function. This has the advantage that if a variable is altered unintentionally then the impact of this is localised to the function where this unintentional alteration was made. However, there are occasions where we _do_ wish changes to a variable inside a function to have an effect outside a function. For example, if we are given a complex number in polar form, _z r_ e , we may wish to write a function that returns the real part, denoted by the variable `x` , and imaginary part, denoted by the variable `y` , of this number. We have noted earlier that a function can only return 

one variable, and so we may not return both the variable `x` and the variable `y` . It would therefore be useful to include the variables `x` and `y` in the function call. However, this would not work either, as the values assigned to these variables would not have any effect outside the function. Fortunately pointers provide us with one way around this problem. Instead of sending the variables `x` and `y` to the function, we send the _addresses_ of these variables to the function. When the function is called, copies are made of the addresses of these variables, and it is these copies that are sent to the function. Changes to these addresses will not have any effect outside the function as we are working with a copy of these addresses. However, we can change the contents of the variable without changing the address through de-referencing the pointer, and this will have an effect outside of the function. This is demonstrated in the code below. 

Note that lines 4–6 of the code are really meant to be one long line, giving the function prototype of `CalculateRealAndImaginary` . Since the line is long, we have split it across several lines and indented the continuation lines for clarity (see Sect. <u>6. 6</u> for a discussion of stylistic conventions when writing code). The prototype lists the arguments for the function. The �irst two arguments are double precision �loating point variables representing the magnitude (denoted by `r` ) and argument (denoted by `theta` ) of the speci�ied complex number. The third and fourth arguments are pointers to—that is, the addresses of—the real part and imaginary part of the complex number. In line 12, we declare integers `x` and `y` that represent the real and imaginary parts of the complex number. To use the function `CalculateRealAndImaginary` , we send the addresses of these variables to the function. Behind the scenes a copy of these addresses is made, and it is these copies that are used in the function in lines 20–26. However, these copies refer to the same memory as the original variables `x` and `y` , and so it is this memory that the results of the calculations in lines 24 and 25 are stored in. 



### **5.2.4 Sending Arrays to Functions** 

When sending arrays to functions—whether or not the memory has been allocated dynamically—it should be noted that it is the address of the �irst element of the array that is being sent to the function. In common with sending the pointer to a variable to a function, changes to this address will not have an effect in the code from which this function is called: however, the contents of this address—that is, the contents of the array—may be changed. As such, any changes made to an array inside a function _will_ have an effect when that variable is used subsequently outside the function. 

We begin by showing how to send arrays whose size is known at compile time to a function. This is shown in the listing below. Note that we do not have to specify the size of the �irst index of an array in the 

function prototype. This size is computed by the compiler. It may be included if desired, but this will be ignored when the code is compiled. 



Arrays whose size has been dynamically allocated can also be sent to a function. Example code for this is shown below. 



### **5.2.5 Example: A Function to Calculate the Scalar Product of Two Vectors** 

Suppose we want to calculate the scalar product of two vectors of double precision �loating point numbers of length _n_ . Calculating the scalar product could be embedded within a function that inputs the two 

arrays, and the length _n_ of both vectors, and returns a double precision �loating point variable that represents the scalar product of the two vectors: see Sect. A. 1. 2 for a discussion of how to calculate the scalar product of two vectors. We would �irst need to allocate memory for the two vectors. We could then call the function that calculates the scalar product, before �inally deleting the memory allocated to the two vectors. Code for this is shown below. 



## **5.3 Reference Variables** 

In Sect. 5.2.3, we demonstrated the use of pointers to allow changes made to a variable within a function to have an effect outside the function, and showed how this could be used to allow a function to, in effect, return more than one variable. An alternative to using pointers is to use _reference variables_ : these are variables that are used inside a function that are a different name for the same variable as that sent to a function. When using reference variables any changes inside the function will have an effect outside the function. These are much easier to use than pointers: all that has to be done is the inclusion of the symbol `&` before the variable name in the declaration of the function and the prototype—this indicates that the variable is a reference variable. It is actually the case that references behave like pointers behind the scenes, but without the programmer having to convert to an address with `&` on the function call (as in Listing 5.1) and without having to de-reference inside the function—they provide a layer of syntactic sugar to ease the programmer’s burden. We now modify the example code in Listing 5.1 that wrote a function that calculated the real and imaginary parts of a complex number given in polar form to use references instead of pointers. 



## **5.4 Default Values for Function Arguments** 

If we are writing a function to implement an iterative technique, such as the Newton–Raphson technique for �inding a root of a nonlinear equation, we will usually be content if the solution is accurate to within a tolerance of, say, 10 . Only on very rare occasions would we want to change this tolerance. We might also want to restrict the number of function evaluations: the Newton–Raphson iteration will probably be implemented using a `while` loop, and numerical rounding errors may prevent the error being suf�iciently small for the iteration to terminate. Under these conditions, we would never exit the `while` loop, and the program that called this function would never terminate. It would therefore be prudent to write a function for implementing the Newton– 

Raphson technique that sets a default tolerance for the solution, and a default maximum number of iterations. We would then be able to call this function without specifying these default values. However, if we did want to call this function with different values then we would like to be able to do this. This is easily achieved by setting default values in the function prototype. This is demonstrated below in a program that uses the Newton–Raphson technique for calculating the cube root of a given . number _K_ through solving the nonlinear equation 

Using a given initial guess _x_ , the Newton–Raphson method results in the iteration 



By setting default values for the tolerance and maximum number of function iterations we may call the function using one of: (i) the default values of these parameters; (ii) specifying the tolerance (the �irst optional parameter in the function prototype) and using the default maximum number of function iterations; and (iii) specifying both of these parameters. All three of these cases are shown below. 



## **5.5 Function Overloading** 

Suppose we want to write one function to multiply a vector by a scalar, and another function to multiply a matrix by a scalar. It would seem natural to call both these functions `Multiply` . This is allowed in C++: we write different function prototypes and functions for both of these operations: the compiler then chooses the correct function based on the input arguments. This is demonstrated in the code below, and is known as _function overloading_ . 





Note that we can overload functions based only on the number and type of the _arguments_ and not on the return type. This means that we could not have vector multiply function `bool Multiply(double scalar, double* u, double* v, int n)` alongside the version which has a `void` return type. This is because the compiler can infer the correct version of an overloaded function from the types of its arguments from the context in which it is used. This is not the case with the return type, where you may want to call a function which returns something, but then to cast its output to another return type, or ignore its output completely. 

## **5.6 Declaring Functions Without Prototypes** 

It is good practice to give the function signature prototypes before you write the implementation. This is so that the function `main` , or any other function will recognise the name and argument types of the new function. However, it is possible to skip the writing of the function prototype by writing the function implementation before its �irst use, as is shown in the code below. 



If prototypes are not given, then the function implementations must be ordered in such a way that each implementation is seen by the compiler before its �irst use. Note that if two functions are mutually recursive, that is, both functions call the other function, then it will not 

be possible to order the functions in this way—and so prototypes must be declared in this case. 

## **5.7 Function Pointers** 

Suppose we want to write a function to implement the solution of the nonlinear equation _f_ ( _x_ ) 0 using the Newton–Raphson technique, where _f_ is a user-speci�ied function. We may want to call this function for solving nonlinear equations more than once during the execution of a given program, and for different user-speci�ied nonlinear functions. To achieve this, we need to specify the appropriate nonlinear function each time the function is called. This may be done, as demonstrated in the code below, using _function pointers_ . 

In the code below, we specify two functions `myFunction` and `myOtherFunction` . In line 8, we declare a _function pointer_ `*p_function` . This declaration speci�ies that the function that this pointer refers to must: (i) accept one (and only one) input argument which is a double precision �loating point variable; and (ii) return one double precision �loating point variable. In line 10, we specify that `p_function` points at the function `myFunction` : calling the function `p_function` in line 11 then has an identical effect to calling `myFunction` . In lines 13 and 14, we demonstrate how to use `p_function` to subsequently call the function `myOtherFunction` . 



The Newton–Raphson method for solving nonlinear equations is de�ined in Exercise <u>2. 6</u> in the Exercises at the end of Chap. <u>2. This is</u> implemented below for two different user-speci�ied functions through the use of function pointers. In lines 5–16, we write a function to implement this algorithm. This function requires speci�ication of: (i) a function pointer to the nonlinear function; (ii) a function pointer to the derivative of the nonlinear function; and (iii) an initial guess to the solution. Note that the function as it stands does not check for divergence, so is unsafe to use in some cases. 

In lines 46 and 47, we call the Newton–Raphson solver to solve the equation with initial guess _x_ 1: the nonlinear function 

`Sqrt10` , and the derivative of the nonlinear function `Sqrt10Prime` 

are given in lines 19–22 and 26–29 of the code. Similarly, in lines 48 and 49 we call the Newton–Raphson solver to solve the equation with initial guess _x_ 1: the nonlinear function `Cube10` , 

and the derivative of the nonlinear function `Cube10Prime` are given in lines 32–35 and 39–42 of the code. 



## **5.8 Recursive Functions** 

In some applications, we may wish to call a function from within the same function: this is known as _recursion_ , and is possible in C++. A simple application of this is the calculation of the factorial of a positive integer `n` , denoted by `fact(n)` , and written mathematically as _n_ !, which is de�ined by 



Code to implement this recursive de�inition of the factorial function is given below: we simply call the function `CalculateFactorial` from within the same function as many times as required. 



## **5.9 Modules** 

Suppose we want to write a code to allow us to solve linear systems of the form **Ax b** , where **A** is a square, invertible matrix of size _n_ , **b** is a speci�ied vector of size _n_ , and **x** is a vector to be calculated of size _n_ . It would be useful if we could write all the functions required to solve this linear system and then allow these functions to be called through an appropriate function—that is, we want to write a function called `SolveLinearSys` with the prototype shown below. 



The function `SolveLinearSys` , and all other functions associated with this linear solver, are known as a _module_ . In more concrete terms, a module is a collection of functions that performs a given task. Every module has an _interface_ . In the example above, this was de�ined by the prototype of the function `SolveLinearSys` , and may be thought of as a list of variables that contains: (i) those that must be input to the module; and (ii) those that are output by the module. 

Modules are very useful when sharing code. For example, if a colleague has written code for solving linear systems as described above then it would be a very simple task for another colleague to utilise this code. All that is required is an understanding of the interface and what the purpose of the code is: there is no need to understand the mathematical algorithm that determines _how_ the linear system has been solved, and the module may be thought of as a “black box”. 

## **5.10 Tips: Code Documentation** 

As you begin to write more programs, there is often a temptation to “just get on with the coding” without paying speci�ic attention to quality. After all “you generally know where you are going and understand the program which you are writing”. It is important to bear in mind, though, that your code will not always be as well understood as it is now. You might come back to a given �ile in three years’ time, because you need to correct it or to add some new functionality to it. Alternatively, you may at some stage hand your programs over to someone else who has the job of working out what you were doing. 

Our tip in this chapter is that computer programs should be humanreadable, as well as machine-readable. Even the smallest portion of code may prove to be opaque unless we include enough commentary to aid the human reader. Take for example the function given below, which calculates the _p_ -norm of a vector. Without comments in the code, it would not be obvious what was happening, even though there are only a few lines of code. A hint is given in the name of the function, `CalculateNorm` , but what is it meant to do? What is the signi�icance of the arguments `s` and `p` ? 



In the code segment below, we give a description of the function immediately before its de�inition. This description gives, in line 3, a means of mapping the mathematics of the function to its implementation. The rest of the description gives an alternate place to �ind more information about the _p_ -norm (lines 4–6) and an explanation of some of the arguments as necessary. In the body of the function, the loop has been commented to describe what its _functional purpose_ is: it is about computing a sum over the elements of the vector. Finally, the return value is commented with a few words of explanation. 



Note that documenting code is sometimes more of an art than a science. There is a balance to be struck concerning the right level of documentation. Too many comments can make the program less readable rather than more readable. Our tip here is that you should describe what part of the problem the code is solving and, perhaps, _how_ it is solving that problem. Do not be tempted to describe the code in overmuch detail. For example, the comment on the loop in line 12 of code above could have read 



While this comment is accurate (describing the range of the loop variable `vecSize` ), it does nothing to aid a programmer in their understanding of the code. 

The formatting of the code documentation can also help readability. A simple tip is that using empty lines to break code and comments into sections can make the code look more readable. If you want to 

emphasise something you can simulate underlining with hyphens or underscores, for example, 



Alternatively, you can emphasise something by putting it in a box: 



## **5.11 Exercises** 

In all exercises, we suggest that you use dynamic allocation of memory for vectors and matrices as described in Sect. 4. 2. Be sure that you are correctly de-allocating memory when using dynamic allocation of memory, as explained in the exercises at the end of Chap. <u>4.</u> 

**5.1** Write code that sends the _address_ of an integer to a function that prints out the _value_ of the integer. 

**5.2** Write code that sends the address of an integer to a function that changes the value of the integer. 

**5.3** Write a function that swaps the values of two double precision �loating point numbers, so 

that these changes are visible in the code that has called this function. 

1. 

Write this function using pointers. 2. 

Write this function using references. 

## **5.4** 

Write a function that can be used to calculate the mean and standard deviation of an array of double precision �loating point numbers. Note that the standard deviation of a collection of numbers 



is given by 



where is the mean of the numbers. 

**5.5** Write a function `Multiply` that may be used to multiply two matrices given the matrices and the size of both matrices. Use assertions to verify that the matrices are of suitable sizes to be multiplied. 

## **5.6** 

Overload the function `Multiply` written in the previous exercise so that it may be used to multiply: 

1. a vector and a matrix of given sizes; 2. a matrix and a vector of given sizes; 3. a scalar and a matrix of a given size; and 4. a matrix of a given size and a scalar. 

## **5.7** 

The _p_ -norm of a vector **v** of length _n_ is given by 



where _p_ is a positive integer. Extend the code in Sect. 5.10 to calculate the _p_ -norm of a given vector, where _p_ takes the default value 2. 

## **5.8** 

The determinant of a square matrix may be de�ined recursively: see Sect. A. 1. 3. Write a recursive function that may be used to calculate the determinant of a square matrix of a given size. Check the accuracy of your code by comparison with the known formulae for square matrices of size 2 and 3: 



**5.9** Write a module for solving the 3 3 linear 

system **Au b** where **A** is nonsingular. 

**5.10** Write a module for solving the _n n_ linear system **Au b** using Gaussian elimination with pivoting, where **A** is nonsingular. See Sect. A. 2. 1. 3 for details of this algorithm. 

© Springer International Publishing AG, part of Springer Nature 2017 Joe Pitt-Francis and Jonathan Whiteley , _Guide to Scienti�ic Computing in C++_ ,  Undergraduate Topics in Computer Science <u>https://doi.org/10.1007/978-3-319-73132-2_6</u> 

# **6. An Introduction to Classes** 

Joe Pitt-Franci ~~s~~ <u>1</u> and Jonathan Whitele ~~y~~ <u>1</u> 

- (1) University of Oxford, Oxford, UK 



**Joe Pitt-Francis Email:** <u>joe.pitt-francis@cs.ox.ac.uk</u> 

One of the key features of the C++ programming language is that it is _object-oriented_ . Up until now we have largely ignored this feature, making only passing reference to it in earlier chapters. For the remainder of this book, we focus on object-orientation, allowing readers to utilise this feature in their C++ programs. 

## **6.1 The** **_Raison d’Être_ for Classes** 

At the end of Chap. 5 we introduced the concept of a module. We explained that modules are useful for code reuse, and therefore allow rapid code development for programs that require the functionality provided by the module, even if the programmer has no understanding of the operations that a module performs. This may be highlighted by using the example of a module for solving linear systems that was introduced in Chap. <u>5. Three advantages of having this module available</u> are given below. 

- Linear algebra lies at the heart of numerical analysis, and so numerical analysts use linear solvers in many programs that they write. A module allows them to reuse this code rather than write new functionality for solving linear systems each time they write a new program. 

- There are many different linear algebra techniques for solving linear systems. It is possible to include many different techniques in a module, and to specify which technique is to be used as part of the interface to the module. 

- Other scientists with little mathematical expertise may have to write programs which require the solution of a linear system. A module allows them to do so without learning the mathematical techniques that underpin linear algebra algorithms. 

Modules are clearly very useful when writing scienti�ic computing programs. But, as we now explain, the use of modules may cause problems. 

### **6.1.1 Problems That May Arise When Using Modules** 

Suppose that the linear solver that we discussed in the previous section has been written so that the solution of this linear system is calculated using the GMRES algorithm.1 This technique for solving linear systems requires several instances of a calculation of the scalar product between two vectors. Implementation of this technique would, therefore, probably include a function being written to calculate the scalar product of two vectors of a given length. Use of this function would not be restricted to users of the module for solving linear systems: another part of the code may use this function to calculate, for example, the normal derivative of a function of two or more variables. Suppose whoever was using the scalar product function to calculate a normal derivative decided to change the inputs to the scalar product function. This would inadvertently cause the linear solver to stop functioning correctly. The linear solver module could then _not_ be treated as a “black box”. 

Another drawback of using standard modules is the way in which data is stored. There is only ever one copy of a particular module and one copy of any data associated with it. If that data is changed for the module to ful�il a particular purpose, then it will be changed for all future uses. Consider a linear solver which has had its functionality extended so that it is able to deal with singular matrices. Such a linear solver will need to have access to the _null space_ (or kernel) of the singular matrix or matrices in question. Suppose we use the extended 

linear solver to solve a singular linear system. The linear system will then solve the singular system subject to knowing and storing the null space of this system. If we were to subsequently use the module to solve another nonsingular linear system, we would have to remember to specify the null space as being empty or the linear solver would attempt to �ind the solution of the nonsingular system subject to the previously speci�ied null space. 

In the next section, we explain how _classes_ allow us to write code including all the features of modules, but without the drawbacks identi�ied above. 

### **6.1.2 Abstraction, Encapsulation and Modularity Properties of Classes** 

The shortcomings of modules, described in the previous section using the example of a module for solving a linear system, could be overcome if we could write a “module” that: 

1. 

contains all the functions needed to solve the system; 2. 

does not allow these functions to be accessed by any other part of the program except through the interface; 3. 

can not itself access any other part of the program; and 4. 

also contains all the data needed to solve the system. 

This is possible through the use of _classes_ , and the speci�ications described above—that is, the compartmentalisation of all of the resources needed—are known as the _encapsulation_ feature of classes. The variables/data and functions associated with a class are known as _class members_ , and the functions more speci�ically as _methods_ . We are now in a position to describe some of the technical terms from Sect. <u>1. 1. 1.</u> 

Classes allow _modularity_ , which includes placing similar functionality in a few �iles. Classes allow us to go further than this: access controls allow us to control which resources are available outside of the class, and which are hidden from users. Hiding parts of 

the code may—at �irst sight—seem to have the undesirable effect of preventing a user from accessing the full functionality of the software. As we shall see later in this chapter, this is certainly not the consequence: it actually has the more desirable effect of preventing users from inadvertently corrupting data. Furthermore, combining functionality in this way allows us to associate data with the functionality. 

The concept of _abstraction_ is that the particulars of an idea should not be important. Classes allow us to hide the irrelevant details of functionality from users who need not know about them. For example, a reader of this book does not need to know _how_ a compiler translates a C++ code into a machine readable executable �ile, but only how to _instruct_ the compiler to perform this task. Abstraction allows emphasis to be placed on the qualities or properties that characterise the objects in how they act and the type of information that they carry. 

A further property of classes is _inheritance_ which allows easy code reuse, extensibility and polymorphism. Inheritance will be discussed in Chap. <u>7</u> . 

## **6.2 A First Example Simple Class: A Class of Books** 

The �irst simple class that we develop is a class of books. 

### **6.2.1 Basic Features of Classes** 

Each book has the following attributes: 

- an author; 

- a title; 

- a format; 

- a price; 

- a year of publication; and 

- a publisher. 

These attributes can be associated with each instance of a book by �irst saving the �ile below as `Book.hpp` . As explained earlier, these attributes are known as _class members_ . 



The �ile above is known as the _header �ile_ associated with the class: the extension `.hpp` indicates that this �ile is a header �ile associated with a C++ program. At this stage, it is suf�icient to know that the word `public` that is used in line 5 of this �ile allows us to access all variables associated with the class. We will give more precise details on what are known as _access privileges_ later in this chapter. Note the semi-colon that is required after the closing curly bracket at the end of this �ile. A common mistake made by novice programmers is to miss this semicolon at the end of the class de�inition. 

The class of books may then be used as shown in the code below. Note that when header �iles that we have written are included the names of these �iles are enclosed within quotation marks, in contrast to the system header �iles such as `iostream` , `fstream` and `cmath` that we have used earlier. The compiler does not distinguish between included �iles with quotation marks and those with angle brackets, but a common coding convention encourages programmers to use quotation marks and angle brackets to make the distinction between local include �iles and those from external libraries, respectively. 



The class of books written here allows us to associate data with each instance of the class. As such, we can think of this class as allowing us to de�ine a new data type and line 6 of the code above as declaring an instance of that class, in this case called `my_favourite_book` . The class members can all be accessed as shown in lines 8–18 of the code above—that is, the string `my_favourite_book.author` is the class member `author` associated with the instance of the class called `my_favourite_book` . 

### **6.2.2 Header Files** 

It doesn’t matter if we include header �iles such as `iostream` , `string` , etc. more than once. But we should be very careful not to include �iles such as `Book.hpp` in the form that it was written in the previous section more than once, as this can cause problems. We will see later on in this book when we are working with several different classes that it is easy to inadvertently include header �iles more than once. To avoid this code being included twice, we adapt it so that the header �ile for a class called `ExampleClass` is of the form shown below. 

Initially `EXAMPLECLASSHEADERDEF` will _not_ be de�ined. The “ `ifndef` ” in line 1 is a contraction of **if n** ot **def** ined. The �irst line of code below therefore instructs the computer to include the code between here and the `#endif` (line 18 of the code) _only if_ the _macro_ `EXAMPLECLASSHEADERDEF` is _not_ de�ined. The �irst time this code is included this macro will not be de�ined, and so all of the code in the listing below will be read. Note that when this code is included, the �irst task that is performed is to de�ine the macro `EXAMPLECLASSHEADERDEF` (line 7 of the code). As `EXAMPLECLASSHEADERDEF` is now de�ined, if this code were to be included a second time all code between the `#ifndef EXAMPLECLASSHEADERDEF` statement (line 1) and `#endif` (line 18) will now _not_ be included. We therefore see that the `#ifndef` , `#define` and `#endif` statements may be used to ensure that the contents of a header �ile are not included more than once. 



### **6.2.3 Setting and Accessing Variables** 

In the class of books we developed in the previous section, all class members were variables, such as strings, double precision �loating point numbers, or integers. Classes are, however, much more powerful 

than this: we will now show how functions may also be de�ined as class members, known as class _methods_ . 

Suppose we want to check that the year of publication of an instance of the class `Book` always takes a valid year. Assuming that no book in our catalogue was published before the invention of the printing press, and has already been published or will be in the near future, then we may write a function known as a _member method_ , called `SetYearOfPublication` , that allows us to set this variable and check that the integer value for year of publication falls within a sensible range (after the invention of the printing press and not too far in the future). As we are writing a method that allows us to check that a valid year of publication is assigned, it seems sensible to force the user of the class to use this method to set this variable. This may be implemented by setting the member `yearOfPublication` to be a _private variable_ . Private variables may only be accessed by other class members: making `yearOfPublication` a private variable therefore prevents us from accessing this variable through code such as line 14 in Listing <u>6.1. However, it can be set through the member method</u> `SetYearOfPublication` , which we will make a public member of this class. Access privileges—that is, the use of `public` and `private` members—will be discussed more fully in Sect. 6.2.5. 

Now that we have made `yearOfPublication` a private member, we cannot directly access this member from outside the class. We therefore need to write a public method that allows us to access this member—this class member will be called `GetYearOfPublication` . We are also going to slightly modify the name `yearOfPublication` to `mYearOfPublication` , where the pre�ix “m”—with the “m” pertaining to “my”—reminds us that this variable is private to the class. We now present code that implements this discussion. First we need a new header �ile `Book.hpp` , given below. 

In the code below, all members that follow `public` and precede `private` (lines 9–12) may be accessed from outside the class. As `mYearOfPublication` comes after `private` it is only accessible to class members. We will discuss access privileges more fully in Sect. 6.2.5. Note the methods declared in lines 11 and 12 of this code. We have speci�ied that the method `SetYearOfPublication` accepts 

an integer argument and returns no value, that is, it is a void function. The method `GetYearOfPublication` returns an integer, but does not require any input arguments as it can access all class members including `mYearOfPublication` . The keyword `const` after the declaration of this method is a signal to the compiler that we want to ensure that the instance of the class will remain constant throughout the execution of the method. That is, the method `GetYearOfPublication` should have changed nothing inside the class. We now need to tell the computer what these methods do. This is given in the code in Listing <u>6.3, which should be saved as</u> `Book.cpp` . We have used an `assert` statement to check that the year of publication does fall within a sensible period when it is set. Note that the header �ile required for `assert` statements should be included in this �ile. 





In the code above, line 4 requires more explanation. In common with functions introduced in Chap. <u>5, the</u> `void` at the start of this line indicates that this method does not return any variable. The remainder of this line indicates that this method: (i) is associated with a class called `Book` ; (ii) is called `SetYearOfPublication` ; and (iii) requires one integer input argument which will be termed `year` . Inside this method we �irst check that the input year is appropriate through an assertion, before allocating it to the `mYearOfPublication` of a book. The method `GetYearOfPublication` , which is written in lines 10– 13, allows us to access the variable `mYearOfPublication` from outside the class, without allowing us to change this value to what may be an incorrect value. 

Code that uses this updated class is given below, and should be saved as `UseBookClass.cpp` . Using access privileges to ensure that variables may only be set through a class member that provides a check on the accuracy of data is very good programming practice, and should be used whenever possible. 



Note that in line 17 of the code above we need to acknowledge that the class member `GetYearOfPublication` is a function or method by including empty brackets after using this class method, even though no input arguments are required. 

The �iles `Book.hpp` and `Book.cpp` together form valid C++ code for a class of books. The code in Listing <u>6.4</u> above is a valid C++ use of this class. So far in this book we have only needed to compile one �ile. Now, however, we need to think a bit more about how to compile the multiple �iles that arise from using classes. 

### **6.2.4 Compiling Multiple Files** 

In Sect. 1. 3. 3 we compiled a single C++ �ile into an executable program using the single compilation step below. 



What really happens in this process is that the C++ �ile is �irst compiled to another �ile called `HelloWorld.o` , and known as an _object �ile_ , which is a machine-readable �ile. In a second step, the object 

�ile is compiled into the executable �ile and the intermediate object �ile is deleted. What we are actually doing when using the compilation command above is to combine the two compilation steps given below. 



The �irst of these commands creates an object �ile called `HelloWorld.o` from the C++ �ile `HelloWorld.cpp` through the use of the `-c` compiler �lag. The second command creates an executable �ile `HelloWorld` from the object �ile `HelloWorld.o` . Up until this point, we have used a one line compilation command, allowing us to completely ignore the existence of object �iles. When compiling multiple �iles we do, however, need to be aware of the existence of these �iles. 

Before we can compile the �ile `UseBookClass.cpp` in Listing <u>6.4,</u> we �irst need to compile the `Book` class to create an object �ile `Book.o` associated with this class. This is done, as above, by using the `-c` option when compiling: 



This produces an object �ile `Book.o` . We can now compile `UseBookClass.cpp` into an object �ile and then _link_ the two object �iles to make an executable. The two compilation commands are now 



As in the above “HelloWorld” example, it is possible to skip one step in the compilation process so that we do not have to explicitly produce the intermediate �ile `UseBookClass.o` . 



The code may be run as before by typing 



at the command line. 

### **_6.2.4.1 Using Make�iles to Compile Multiple Files_** 

Suppose we have code that uses several classes stored in several �iles. We would rather not compile _all_ of these classes separately every time one �ile is modi�ied slightly. This may be avoided by the use of a `Makefile` —using this approach only the necessary compilation is carried out. The following is a Make�ile for code `UseClasses.cpp` that uses two classes, `Class1` and `Class2` . 



If the �ile above is saved as `Makefile` , then to generate an up-todate executable �ile `UseClasses` we simply type “ `make UseClasses` ” at the command line. 

Using this approach only the necessary compilation will be carried out. Line 10 of this `Makefile` tells the compiler that the executable �ile `UseClasses` requires three �iles: `Class1.o` , `Class2.o` and `UseClasses.o` . Line 11 gives the rule for compiling the executable �ile from its dependencies. Line 1 tells the compiler that the �ile `Class1.o` depends on the two �iles `Class1.cpp` and `Class1.hpp` . Only if one or both of these �iles have been changed since the last time this class has been compiled will this class be recompiled using the rule given on Line 2. Similar remarks hold for the class `Class2` . Note that in line 7, the recompilation of `UseClasses.o` depends not only on the 

relevant C++ �ile, but also on the classes’ header �iles—so that a change in either class interface will result in a recompilation of the �ile which uses its functionality. Finally, having worked through all the steps described, a new executable `UseClasses` will be created only if one or more of the �iles listed on line 10 have changed as a consequence of this compilation process. 

The compilation procedure is illustrated in Fig. <u>6.1. In this �igure,</u> the thin lines with arrows represent some of the code dependencies described above that are encapsulated within the `Makefile` . Many of the integrated development environments described in Sect. <u>1. 3. 1</u> will automatically generate Make�iles. 

### **6.2.5 Access Privileges** 

In Sect. 6.2.3, we brie�ly discussed access to class members. There are three degrees of access to class members: 

- `private` —these class members are only accessible to other class members, unless `friend` (which will be introduced in Sect. <u>6.3) is</u> used; 

- `public` —these class members are accessible to everyone; `protected` —these class members are accessible to other class members, to derived classes (which will be introduced in Chap. <u>7),</u> and to friends. 

The reserved keywords `private` , `public` and `protected` may be used as often as desired, with the default being `private` . For example in the class below, `member1` and `member3` are private members, `member2` and `member4` are public members, and `member5` is a protected member. 



**_Fig. 6.1_** The compilation process 



**6.2.6 Including Function Implementations in Header Files** We saw in Sect. <u>6.2.4</u> that it can be inconvenient to have to compile multiple classes. When working on large projects that require the use of multiple classes it can be dif�icult to keep track of the class members and their access privileges (stored in the header �ile) and the 

implementations of the member functions (stored in the `.cpp` �ile). If functions associated with a class require only a few lines of code then it may be more convenient to include the implementation of these functions in the header �ile. This may be done as shown below, where we implement the functions that are members of our class `Book` in the header �ile for this class, thus combining the �iles in Listings <u>6.2</u> and 6.3 into a single �ile `Book.hpp` . 



### **6.2.7 Constructors and Destructors** 

Each time an object of the class `Book` is created the program calls a function that allocates space in memory for all the variables used. This function is called a _default constructor_ and is automatically generated. This default constructor can be overridden if desired—for example we may wish to set all the string variables in our class of books to 

“ `unspecified` ” so that it will be clear when accessing this object that these strings have not yet been properly assigned. An appropriate header �ile for this class is shown below. Note that when overriding the default constructor this function has the same name as the class, takes no arguments, has no return type and must be a `public` member of the class. 



The methods associated with this class are given in the �ile below. 



The code below demonstrates how to use the overridden default constructor. 



The code above will print “ `The author is unspecified` ”. We will see in Chap. 10 that, if any memory management such as allocating memory dynamically is required by a class, then it is _essential_ to change the behaviour of the automatically generated default constructor: if not, the default constructor will not allocate any 

memory. We can change the behaviour of the automatically generated default constructor either by overriding it with a default constructor of our own (as in the example of `Book` , above) or by providing some other constructor (which we will discuss shortly). This is because the automatically generated default constructor is _only available_ if no other constructors have been provided by the programmer. 

Another constructor that is automatically generated is a _copy constructor_ . This constructor requires as input another instance of the class, and creates a copy of this instance of the class. In common with default constructors, copy constructors may also be overridden. Note that the argument to a copy constructor has to be a _reference_ to another instance of the class, rather than that object itself. This is because, by default, all method arguments are called by copy. Were we to miss the fact that this constructor takes a reference argument, then we would need to use a copy constructor in the call—the very machinery that we are de�ining here. It is also a good idea to declare the argument to a copy constructor as `const` which is an instruction to the compiler to ensure that the object argument `otherBook` to the copy constructor in the code in Listing <u>6.6</u> will remain constant during this operation. That is, the constructor will have no hidden side-effects on the instance of the class that it is copying. 

Furthermore, in addition to the default and copy constructors, we may write our own customised constructor that takes any inputs that we feel are appropriate, and we may write as many of these constructors as we like. For example, we may want to specify a book’s title when creating an object. We now demonstrate how to write a constructor such as this, and how to override a copy constructor. First, we need an appropriate header �ile: one is shown in Listing 6.6. Line 10 of this header �ile declares an overridden copy constructor, and line 11 explains that there will be a constructor that accepts a string as input. As we have provided a constructor ourselves the automatically generated default constructor is _not_ available: we may, however, supply a default constructor ourselves. 

The methods associated with this class are given in the �ile in Listing <u>6.7. Lines 14–22 are the overridden copy constructor, where all</u> class members are set to be the same as the instance of the class that 

we wish to copy. Lines 25–28 represent the specialised constructor that sets the title of the book to a speci�ied string. 

The code in Listing <u>6.8</u> �irst creates an instance of the class `Book` , called `good_read` , and sets the class members associated with `good_read` . Line 15 demonstrates how to use the overridden copy constructor to create another instance of the class `Book` , called `another_book` , that is initialised with class members taking identical values to those of `good_read` . Line 17 uses the constructor that sets the title when the instance of the class is declared: an instance of the class called `an_extra_book` is declared, with title set to “ `The Magician’s nephew` ”. 

Destructors are also automatically written, and free memory allocated for an object when it goes out of scope. We will see later when writing classes of vectors and matrices that there are situations— speci�ically where the constructor has performed dynamic allocation of memory—where the automatically generated destructor _should_ be overridden. This allows us to adhere to the tip introduced in Sect. <u>4. 3. 3,</u> which advised programmers to ensure that any line of code where memory is dynamically allocated using `new` has a corresponding line where the memory is freed up using `delete` . 







### **6.2.8 Pointers to Classes** 

We may declare a pointer to an instance of a class as we show in the code below. In line 6 of this code we declare a pointer, `p_book_i_am_reading` , to an instance of the class `Book` described earlier in this chapter, and allocate memory for this instance through the use of `new` . In line 8, we use `*p_book_i_am_reading` to denote the contents of the memory whose address is stored by the pointer. By placing this in brackets, we may access the class members as shown in earlier sections of this chapter. Line 9 is a more convenient way of accessing a class member associated with a pointer to a class in which the forward arrow, `->` , means “de-reference and then access the member”. 



In the code above, note that we have followed the advice given in Sect. 4. 3. 3—which we shall repeat many times in this book—to always write a `delete` statement to match a `new` statement. 

## **6.3 The** **`friend` Keyword** 

When developing a program, we may wish to access private members of a class from outside the class. One way of doing this is to create a new public method that accesses the private member in the same way as we did in Sect. <u>6.2.3</u> . Another way is to write a free function that is a _friend_ of the class: such functions may access all members of the class, including private variables. This is demonstrated in the class that we write below. First, we write the header �ile. 



The constructor, member function and friend function are then implemented using the code below. Note that as the friend function `GetMaximum` is not a member of the class, we do not include `ExampleClass::` in line 25 of the code as we would do when writing a method that is a member of the class. 



Code that uses the friend function of the class above is shown below. 



## **6.4 A Second Example Class: A Class of Complex Numbers** 

In the class of books that we have developed, all class members were quite simple, being either variables—such as strings or integers—or straightforward methods. We now develop a class of complex numbers, allowing some more advanced features of classes—such as operator overloading—to be showcased through a scienti�ic computing example. It is worth pointing out, before developing the class, that C++ does already have a complex number type which is based on templates (see Chap. <u>8). We are developing a complex number class here solely for</u> illustration. If you need to use complex numbers we recommend you use the of�icial C++ class (which we will revisit in Sect. <u>9. 5).</u> 

A complex number has a real part and an imaginary part. A class of complex numbers will therefore contain class members that represent both of these quantities. It seems sensible to override the default constructor to set both the real and imaginary part of a complex number to zero in the absence of any speci�ied value. We would also like a constructor to be available that allows us to set the complex number `z = x + iy` , where `x` and `y` are double precision �loating point variables, using statements of the form shown below. 



In addition, we may also include class members that are methods that calculate both the modulus and the argument of this complex number. A further method that may be of use is raising the complex number to a speci�ied power. 

### **6.4.1 Operator Overloading** 

If we have declared `a` , `b` , `c` and `d` to be integer variables then we may easily relate these variables through statements such as those below. 



We would also like to write statements such as these if `a` , `b` , `c` and `d` were complex numbers rather than integers. Before we can do this, we need to de�ine: (i) what the assignment operator (equals) means for complex numbers; (ii) what the _unar_ _~~y~~_ <u>2</u> minus operator means—i.e. what is meant by the expression “ `-a` ” if `a` is a complex number; and (iii) what the _binar_ _~~y~~_ <u>3</u> addition operator means—that is, what `a+b` means for complex numbers `a` and `b` . De�ining these operators for classes is known as _operator overloading_ . We will explain how this is done in C++ below. 

### **6.4.2 The Class of Complex Numbers** 

In light of the discussion above, we will write a class of complex numbers with the following members. 

- A double precision �loating point variable `mRealPart` containing the real part of the complex number. 

- A double precision �loating point variable `mImaginaryPart` containing the imaginary part of the complex number. 

- An overridden default constructor `ComplexNumber()` that initialises the real part and the imaginary part to zero. 

- A constructor `ComplexNumber(double x, double y)` that initialises the real part to `x` and the imaginary part to `y` . 

- A method `CalculateModulus()` that returns a double precision �loating point variable containing the modulus (or magnitude) of the complex number. 

- A method `CalculateArgument()` that returns a double precision �loating point variable containing the argument (or phase) of the complex number. 

- A method `CalculatePower(double n)` that returns the complex number calculated when raising the original complex number to the power `n` . 

- Overloading of the assignment operator. 

- Overloading of the unary subtraction operator. 

- Overloading of the binary addition and subtraction operators. Overloading of the output stream ( ) insertion operator which gives control of the output format for complex numbers. 

A suitable header �ile for this class is shown below. This should be saved as `ComplexNumber.hpp` . We have made the data associated with each complex number—i.e. the real part and the imaginary part— private members of this class to prevent inadvertent corruption of these members. These members can, of course, be accessed by the methods of the class. 



Code for the class members that are methods is shown in Listing 6.10, and should be saved as `ComplexNumber.cpp` . 

In the code in Listing <u>6.10</u> we have written two constructors. The �irst of these (lines 6–10) overrides the automatically generated default constructor, and initialises both the real part and the imaginary part of the complex number to zero if no values are speci�ied. The second constructor (lines 13–17) accepts two double precision �loating point variables, sets the real part of the complex number to the �irst of these, and the imaginary part of the complex number to the second of these. Readers who have followed the discussion of constructors for the class of books will need no more discussion on the implementation of these constructors. We have not de�ined a new copy constructor because the automatically generated copy constructor behaves correctly. 

We now turn our attention to the third method in the code below, the method for calculating the modulus of a complex number in lines 21–25. As this method returns the modulus of the complex 

number, which is a double precision �loating point variable, we begin line 21 with the word `double` to re�lect this. This is then followed by the text `ComplexNumber::CalculateModulus()` to indicate that: (i) it is a member of the class `ComplexNumber` ; and (ii) the method is called `CalculateModulus` . The text `()` indicates that no arguments are required. Recall that member methods can access all class members, and so there is no need to specify either the real part or the imaginary part of the complex number in the list of arguments. Line 21 then concludes with the reserved keyword `const` to ensure that both the real part and the imaginary part of the complex number whose modulus is being calculated are left unchanged by this method. A simple calculation is then performed to return the modulus of this number. The fourth method in the code above, lines 29–32, uses very similar ideas to calculate the argument of a complex number. Readers should work through this method to ensure that they understand exactly why the function has been written in this way. 







Much of the discussion on the methods `CalculateModulus` and `CalculateArgument` applies to the �ifth method in lines 37–47 of the code, namely the function `CalculatePower` , which is used to return the `n` th power of a given complex number. We perform this calculation by �irst writing the complex number in polar form, that is, _z_ = _r_ e = _r_ . We may then write _z_ , which has real part _r_ cos( _n_ ), 

and imaginary part _r_ sin( _n_ ). This method requires some different 

features to the methods of this class already described, which we now explain. In line 37, we specify that the type of variable returned is of type `ComplexNumber` : that is, methods can be used to return an instance of a class as well as simpler variable types such as `double` . This method also requires input of the exponent to which we raise the complex number: this is speci�ied by the “ `double n` ” in brackets at the end of line 37. Inside the method, the �irst two lines of code calculate the modulus and argument of the original number using the two class members `CalculateModulus` and `CalculateArgument` —this demonstrates how to call these methods from within the class. The next two lines then perform the calculations required on both the modulus and argument of the complex number to raise it to the power of `n` . Having set both the real part and the imaginary part of the resulting complex number, this complex number is then returned. 

In lines 50–56, we overload the assignment operator. Note that the argument to the assignment operator is a reference to another instance of the class, rather than the object itself. This is because, by default, all method arguments are called by copy, necessitating the overhead of the use of the copy constructor in making the assignment. The use of the `const` keyword guarantees that the assignment operator will not alter the contents of the object argument `z` . The remainder of the method for assignment uses an entity called `this` which does not appear to have been declared. For the purpose of this book, the reader need only know that `this` is a pointer to the complex number that is returned: it is the contents of `this` which is returned. 

The unary subtraction operator is overloaded in lines 59–65. Line 59 explains that: (i) the return type is a `ComplexNumber` ; (ii) the method is a member of the class `ComplexNumber` ; (iii) de�ines the operator “ ”; (iv) the function requires no input arguments (as speci�ied by the empty brackets); and (v) the original complex number is left unchanged (through use of `const` ). An instance of the class `ComplexNumber` , called `w` , is then declared in line 61, and the real part and imaginary part of `w` are set to the negative of those of the original complex number in lines 62 and 63. Finally, the complex number `w` is returned. 

The binary addition operator is de�ined in lines 68–75. We begin as usual in lines 68–69 by specifying the return type, the class that the function is a member of, the operator and the input argument. There is only one input argument which is that to the right of the `+` operator— the class itself is the left operand. We declare an instance of a complex number (line 71), perform the required addition (lines 72–73), and then return the result of this addition (line 74). A similar function overloads the binary subtraction operator in lines 78–85. 

The �inal operator is de�ined in lines 88–103. This is the output stream ( ) insertion operator. The syntax here is different: the operator is not a member method of the class, but is an external function. This operator uses the `friend` keyword introduced in Sect. 6.3. By using the `friend` keyword for the operator in line 21 of the header �ile for complex numbers, we are telling the computer that, although this operator is not a class member, this operator may access 

all class members—including private members. When this operator is de�ined in lines 88–103 of the listing above, we see that we do not make it a class member through `ComplexNumber::` . The function de�ining this operator takes an output stream (such as `std::cout` or an output stream to a �ile) and inserts characters into it using the complex number `z` . 

We now demonstrate use of the class of complex numbers in the following code. Recall from earlier that when member methods are called that require no arguments we still need to acknowledge that they are functions by using empty brackets, for example `z1.CalculateModulus()` in line 9 of the code below. Note that we can declare an array of complex numbers: this is shown in line 25 of the listing below where we create an array of complex numbers with two entries. In lines 26–27, we set the �irst element of this array to the complex number `z1` , and the second element of this array to the complex number `z2` . In lines 28 and 29, we show how to access a friend function of an entry of an array, through printing the complex number that is the second entry of the array of complex numbers to screen. 

The �iles `ComplexNumber.hpp` and `ComplexNumber.cpp` given in Listings <u>6.9</u> and 6.10 may be downloaded from <u>http:// www. springer. com/ book/ 9783319731315.</u> 



## **6.5 Some Additional Remarks on Operator Overloading** 

In Sect. 6.4.1, we introduced the concept of operator overloading. This concept was demonstrated in Sect. <u>6.4.2</u> using the example class of complex numbers. In this example class, we demonstrated how to overload the assignment operator, and both unary and binary addition and subtraction operators. Many more operators may be overloaded, as will be demonstrated in later chapters. In Sect. 8. 1, we show how the 

square bracket operator may be overloaded. In Sect. 8. 3. 2, we show how the “less than” operator can be overloaded: extending this to the “greater than” operator, the “less than or equals to” operator, the “greater than or equals to” operator, the “not equal to” operator, and the equality operator then follows the same pattern. In Sect. 10. 3. 4, we demonstrate how to overload the round bracket operator. 

## **6.6 Tips: Coding to a Standard** 

Many programming organisations and projects use coding standards in an attempt to ensure that the software written is of an appropriate quality. A famous C++ coding style called JSF (Joint Strike Fighter) was drafted for an international aviation project and has now been adopted by many commercial software houses. Some organisations use automatic checks to ensure that their code complies to the standard (to the extent that employees are reprimanded if their work falls short), while other organisations use the standard as a guideline. 

Coding standards are basic rules for programming. Some rules dictate how programs should be laid out (in terms of where comments, new lines and spaces should appear). Other rules are about the naming of variables, classes, functions and methods. Still other rules outlaw various programming practises which, although legal in the language, are considered dangerous (such as returning a pointer to locally allocated memory). The reasons for adopting coding standards are various, but it is generally believed that they promote code which is more reliable, portable, maintainable, readable and extensible. 

We believe that a few simple coding rules make programs much more readable (and therefore more maintainable). For this reason, we have used a small set of coding standard rules throughout this book. We don’t always follow these rules rigidly, especially when we present small fragments of programs, but once you are familiar with some of the rules we are using then our presentation of code should make more sense. 

1. 

Code within blocks (such as those introduced in Sect. <u>5. 1, as well as</u> functions, loops, branches of `if` statements, and other places which may have curly brackets) is indented. The curly brackets ({ and }) are 

y 

y ) y ({ }) 

always used, even in single-statement blocks (see Sect. 2. 1. 1), and they appear on a line of their own. 2. 

Lines of code which are too long to �it comfortably within the width of an editor are split across multiple lines with a suitable indentation. 3. 

Names for variables and functions are meaningful (e.g., `local_index` or `numberOfNodes` ) but are not so verbose that they become too long and unwieldy. 

4. 

Variables are declared close to where they are used, rather than at the beginning of a function. This is so that the context is clear (see Sect. 5. <u>1). Loop counter variables are declared in the context of the loop, that</u> is, we write 



#### rather than 



5. 

Locally declared variable names have underscores (e.g., `total_sum` ). 6. 

Where types are pointers or references the “ `*` ” or “ `&` ” character is written adjacent to the native type, with no space between, that is, 



rather than 



As explained in Sect. 4. 1. 2, a consequence of this rule is that each pointer variable declaration should appear on its own line. 7. 

Pointer names begin with “p” (e.g., `p_return_result` or `pLastResult` ). One exception to this rule is when the pointer is used for an array of values stored in dynamically allocated memory. 8. 

Function names are in camel-case (i.e., where capital letters begin each word) and the �irst word is a verb, to indicate what it is that they _do_ (e.g. `GetSize()` or `InitialisePreconditioner()` ). This applies to class methods as well as to regular functions. 9. 

Names of arguments to functions (and class methods) are in also camel-case, but they begin in lower-case (e.g., `firstDimension` ). The same format is also applied to member data of classes, but the following rule helps us to distinguish them. 10. 

Class data which have access controls are also in camel-case with “m” (for “my”) to denote “private” or “protected” (e.g., `mSize` or `mpQuadraticMesh` where the latter is a private pointer). Since it is advisable for member data to be private, this naming convention allows us to distinguish, in the body of a class method, between the method arguments and the class variables. 11. 

Class names are also in camel-case (as are function names), but they can be distinguished by the context (e.g., `FiniteElementSolver` or `PopSinger` ). 12. 

There should be lots of descriptive comments as discussed in Sect. 5. 10. 

## **6.7 Exercises** 

In all of the exercises below, test your code using suitably chosen test cases. 

**6.1** The �iles `ComplexNumber.hpp` and `ComplexNumber.cpp` given in Listings <u>6.9</u> and <u>6.10</u> may be downloaded from <u>http:// www. springer. com/ book/ 9783319731315. Extend this</u> class to include the following features. 

1. 

Methods called `GetRealPart` and `GetImaginaryPart` that allow us to access the corresponding private members. In the class of complex numbers, the members representing the real and imaginary parts of the complex number—called `mRealPart` and 

`mImaginaryPart` —are private members. These members may be set through using a constructor, but there is no way to access them. 2. 

Friend functions `RealPart` and `ImaginaryPart` so one may either write `z.GetImaginaryPart()` or `ImaginaryPart(z)` . 3. 

An overridden copy constructor. 4. 

A constructor that allows us to specify a real number in complex form through a constructor that accepts one double precision �loating point variable as input, sets the real part of the complex number to the input variable, and the imaginary part to zero. 5. 

A `const` method `CalculateConjugate` which returns the complex conjugate `x - iy` of a complex number `x + iy` . 6. 

A method `SetToConjugate` which has a void return type and sets the complex number `x + iy` to its complex conjugate `x - iy` . 7. 

Write code to dynamically allocate memory for a 3 3 matrix of complex numbers. Extend this code to calculate the exponential of the matrix, where the exponential of a matrix _A_ is given by 



where, in practice, the in�inite sum above is truncated at a suitably large value of _n_ . Having allocated the memory for this array dynamically what should you now do? See Sect. 4. 3. 3 if you don’t know. 

8. 

Test the class to ensure that special cases give sensible results. For example (0+0 _i_ ) should equal zero for most values of _n_ , but any number raised by _n_ = 0 should return 1. 

## **6.2** Develop a class of matrices of double 

precision �loating point variables that has the features listed below. 

1. 

An overridden default constructor that initialises all entries of the matrix to zero. 2. 

An overridden copy constructor. 

3. 

A constructor that speci�ies the four entries of the matrix and allocates these entries appropriately. 4. 

A method (function) that returns the determinant of the matrix. 5. 

A method that returns the inverse of the matrix, if it exists. 6. 

Overloading of the assignment operator, allowing us to write code such as `A = B;` for instances of the class `A` and `B` . 7. 

Overloading of the unary subtraction operator, allowing us to write code such as `A = -B;` for instances of the class `A` and `B` . 8. 

Overloading of the binary addition and subtraction operators, allowing us to write code such as `A = B + C;` or `A = B - C;` for instances of the class `A` , `B` and `C` . 

9. 

A method that multiplies a matrix by a speci�ied double precision �loating point variable. 

## **Footnotes** 

<u>1</u> 

The Generalised Minimal RESidual technique—commonly known as GMRES—is an iterative technique for solving linear systems. See, for example, Trefethen and Bau [4] for more details. <u>2</u> 

A unary operator has one input, hence `-a` is the unary minus operator applied to `a` . <u>3</u> 

A binary operator has two inputs, hence `a+b` is the binary addition operator applied to `a` and `b` . 

© Springer International Publishing AG, part of Springer Nature 2017 Joe Pitt-Francis and Jonathan Whiteley , _Guide to Scienti�ic Computing in C++_ ,  Undergraduate Topics in Computer Science <u>https://doi.org/10.1007/978-3-319-73132-2_7</u> 

# **7. Inheritance and Derived Classes** 

Joe Pitt-Franci ~~s~~ <u>1</u> and Jonathan Whitele ~~y~~ <u>1</u> 

(1) University of Oxford, Oxford, UK 



**Joe Pitt-Francis** 

**Email:** <u>joe.pitt-francis@cs.ox.ac.uk</u> 

In Sect. 6. 1. 1, we explained how object-oriented programming allowed for a more reliable programming paradigm than was possible using modules. One reason for this, which we touched on brie�ly, is the availability of _inheritance_ . Inheritance allows us to extend the functionality of a class by introducing a new class, known as the _derived class_ , that contains all the features of the original class, known as the _base class_ . 

## **7.1 Inheritance, Extensibility and Polymorphism** 

Perhaps the most important feature of object-oriented programming is _inheritance_ . This concept allows the functionality of classes to be built into a “family tree”. The data, operation and functionality of a given class (the base class, sometimes called the parent class) may be directly reused, extended and modi�ied in another class (the derived or child class). The operation of one base class can be inherited by several derived classes ~~.~~ <u>1</u> In turn, these derived classes may become the base classes of further inheritance, giving rise to further generations. 

Suppose we have written a class that allows us to solve linear systems. Suppose further that we now want to write a class for solving linear systems that may be used only when the matrix in the linear 

system is symmetric and positive de�inite, thus allowing us to solve the system using the very effective conjugate gradient technique discussed in Sect. <u>A. 2. 3. Much of the functionality required—such as specifying</u> the vectors, matrix and tolerance, and providing a function for calculating the scalar product between two vectors—will already be implemented in the class that has been written to solve more general linear systems. Inheritance allows us to write a new class for solving a special category of linear systems that uses—or inherits—all features of the class for solving general linear systems. If we wanted to extend the functionality of the class that uses the conjugate gradient scheme to include Successive Over–Relaxation (SOR),2 we simply inherit again so that the SOR variant is a grandchild derived class of the original. 

Inheritance gives rise to two important concepts �irst mentioned in Sect. 1. 1. 1: _extensibility_ and _polymorphism_ . Extensibility is the idea, not just that the code can be extended, but that it can be extended easily, and without changing any of the original functional behaviour of the base class. Polymorphism is the ability to perform the same operations on a wide variety of different types of objects. So, for example, the `Solve` method of the generic linear solver outlined above will perform a certain set of operations. This method of the base class is then rede�ined in a derived class for symmetric, positive de�inite matrices, without changing its arguments. At run-time, the program is able to detect which object it has and therefore which version of `Solve` to run. This version of polymorphism is also known as dynamic polymorphism or run-time polymorphism. 

## **7.2 Example: A Class of E-books Derived from a Class of Books** 

We now demonstrate the basic features of inheritance through extending the class of books developed in Sect. <u>6. 2. Suppose the owner</u> of a bookshop also runs a website where she not only sells traditional (paper) books, but also electronic e-books. The advantage of the e-book over a traditional book is that it does not need to be parcelled up and sent through the mail. The e-book may be delivered by giving the customer access to a private URL from which they may download it. 

The bookseller may wish to update her computer system so that a URL attribute is added to each instance of her e-books. She could do this by deriving a class `Ebook` from the class `Book` given in Listings <u>6. 6</u> and 6. <u>7. The class</u> `Ebook` will have the same members as the class `Book` , but with two differences. The �irst difference is that the class member `format` will be set to “electronic”. The second difference is that instances of the class `Ebook` will have an additional class member `hiddenUrl` that contains the private URL. The header �ile for this class is given below. 

As the class `Ebook` is derived from the class `Book` , we include the header �ile for the class `Book` in the header �ile for the class `Ebook` below. Line 7 of this listing speci�ies that the class `Ebook` is indeed derived from the class `Book` , and the word “ `public` ” in this line has the effect that: 

1. 

public members of `Book` are public members of `Ebook` ; 2. protected members of `Book` are protected members of `Ebook` ; and 3. private members of `Book` are hidden from `Ebook` , and so may not be used by the derived class. 

This is known as _public inheritance_ . We will discuss access privileges for derived classes in more detail in Sect. <u>7.3.</u> 



Based on the discussion above, all public and protected members of the class `Book` de�ined in Listing <u>6. 6</u> are available to instances of the class `Ebook` . This has the possibly unintended effect that the member `mYearOfPublication` is not directly available to the derived class `Ebook` , as this member is private and therefore not available to the derived class. This member is, however, still available indirectly through the public methods of the base class `SetYearOfPublication` and `GetYearOfPublication` —as these members are public they are available to the derived class, and can be used to access the member `mYearOfPublication` . The other difference between the derived class and the parent class is that we have declared two additional members in the listing above: an overridden default constructor, and a string member representing the hidden URL. 

The overridden default constructor is given below, where the format is set to “electronic” as required. Note the syntax for overridden default constructors below: this allows the default constructor for the base class `Book` to be called �irst, setting the author, the title, and the publisher to “unspeci�ied”. The format is then set to “electronic” inside the overridden default constructor for the derived class. 



Example code using the class `Ebook` is given below. Note that the member `format` of an instance of the class `Ebook` is automatically set to `electronic` . 



Figure <u>7.1</u> shows, in schematic form, a representation of how the class `Ebook` relates to its parent class `Book` . This representation is given in the _Uni�ied Modelling Language_ ( _UML_ ) format where each class is 

shown as a box. Space inside each box is divided into three components: the class name, a list of the data contained in the class and a list of the class methods. A `+` sign signi�ies data and methods which are public. Private data or methods ( `mYearOfPublication` in this case) carry a `−` sign, while protected members would be given a `#` sign. 



**_Fig. 7.1_** An inheritance graph, showing that Ebook is derived from the Book base class 

The arrow between the boxes shows the child–parent inheritance relationship. The reason for the repetition of “ `+ Book()` ” in the base class is to show that `Book` has three different constructors: the default constructor, the copy constructor and a specialised `Book` constructor for setting the `title` attribute. These three constructors were 

introduced in Sect. <u>6. 2. 7.</u> `Ebook` has only one constructor which is the overridden default (no argument) constructor given above which sets the `format` attribute. 

## **7.3 Access Privileges for Derived Classes** 

When developing a class, we specify all class members as being public, protected or private members. When a class is derived from this base class, we need to know what access privileges the members of the base class have in the derived class. In the class `Ebook` that we derived from the class `Book` in Sect. <u>7.2, we used public inheritance in line 7 of</u> Listing <u>7.1. There are two other types of inheritance:</u> _protected inheritance_ ; and _private inheritance_ . These three different types of inheritance determine the access privileges of the base class members in the derived class. In Table 7.1, we state these access privileges. 

**_Table 7.1_** Access privileges for derived classes 

|**Access privilege in base**<br>**class**|**Type of**<br>|**inheritanc**<br>|**e**<br>|
|---|---|---|---|
||**Public**|**Protecte**<br>**d**|**Privat**<br>**e**|
|Public|Public|Protecte<br>d|Privat<br>e|
|Protected|Protect<br>ed|Protecte<br>d|Privat<br>e|
|Private|Hidden|Hidden|Hidde<br>n|



## **7.4 Classes Derived from Derived Classes** 

We may derive classes from classes that are themselves derived classes, as discussed in Sect. <u>7.1. If</u> `Class2` is derived from `Class1` , we may derive a new class `Class3` from `Class2` in exactly the same way as in Sect. 7.2, as shown in the header �ile for `Class3` shown below. 



## **7.5 Run-Time Polymorphism** 

Polymorphism may be used when a number of classes are derived from the base class, and for some of these derived classes we want to override one—or more—of the methods of the base class. Suppose we have developed a class of guests who stay at a hotel. This class will include members such as name, room type, arrival date, number of nights booked, and a member method that computes the total bill. It is likely that the hotel has negotiated special nightly rates for individuals from particular organisations. To re�lect this, the method that computes the total bill must act differently on guests from these organisations. This may be incorporated into software in a very elegant manner through the use of _virtual methods_ where the method does different things for different derived classes. This is implemented by the use of the `virtual` keyword, shown in the header �ile for the class of hotel guests shown below. The `virtual` keyword is a signal to the compiler that a method has the potential to be overridden by a derived class. 



The implementation of the method `CalculateBill` is given in the listing below, where the total bill is given by multiplying the number of nights that a guest stayed in the hotel by a nightly rate of £50, and adding the telephone bill to this �igure. Even though this method is a virtual method, it is written in exactly the same way as if it were not declared as virtual. 



Suppose now that the hotel have negotiated a deal with a company that reduces the room rate to £45 for the �irst night that a guest stays, and £40 for subsequent nights, and offers free telephone calls. This may be implemented by deriving a class `SpecialGuest` from the class `Guest` as shown below. 



The method `CalculateBill` for this derived class is then implemented using the code below. 



Note that declaring the member method `CalculateBill` as virtual in the class `Guest` does not require that the method must be overridden (rede�ined) in derived classes: it simply gives us the option to override it. 

The real power of run-time polymorphism can be seen when we use only pointers to the _base class_ in a family tree of objects. It might not be obvious what the exact type of each object in our program is, but the run-time system is able to �ind out. In the following code, there are three pointers to `Guest` objects, but one of them is in actuality a `SpecialGuest` and therefore has a reduced bill. One might imagine a larger-scale program running over an array of `Guest` pointers— representing those guests who are checking out—each of which has their own mechanism for calculating the bill. The programmer does not need to be aware which of these `Guest` objects might be actually be a <u>3</u> `SpecialGuest` ~~.~~ 



## **7.6 The Abstract Class Pattern** 

Suppose we want to write an object-oriented program for calculating the numerical solution of initial value ordinary differential equations of the form 



where _f_ ( _t_ , _y_ ) is a given function, and _T_ , _Y_ are given values. Many methods exist for calculating the numerical solution of equations such as these, for example, the forward Euler method, Heun’s method, 

various Runge–Kutta methods, and various multistep methods. One way of implementing these numerical methods would be to write a class called `AbstractOdeSolver` that has members that would be used by all of these numerical methods, such as variables representing the stepsize and initial conditions, a method that represents the function _f_ ( _t_ , _y_ ) on the right-hand side of the equation above, and a virtual method `SolveEquation` for implementing one of the numerical techniques described above. We would then implement each of the numerical methods using a class derived from `AbstractOdeSolver` , and overriding the virtual function `SolveEquation` . The derived classes would then contain members that allow a speci�ic numerical algorithm to be implemented, as well as the members of the base class `AbstractOdeSolver` that would be required by all of the numerical solvers. 

Using the class structure described above, the base class `AbstractOdeSolver` would not actually include a numerical method for calculating a numerical solution of a differential equation, and so we would not want to ever create an instance of this class. We can automatically enforce this by making `AbstractOdeSolver` an _abstract class_ . This is implemented by setting the virtual functions `SolveEquation` and `RightHandSide` to be _pure virtual functions_ as shown in lines 15 and 16 of the listing for `AbstractOdeSolver.hpp` below. We indicate that these functions are pure virtual functions by completing the declaration of these members with “ `= 0` ” as shown in the listing below. Should we mistakenly attempt to create an instance of the class `AbstractOdeSolver` we would get a compilation error. An investigation into pure virtual functions is made in Exercise <u>7.2.</u> 



A class is an abstract class if it contains one or more pure virtual methods. We do not discuss implementation of the class `AbstractOdeSolver` or the derived classes further here: these classes are developed in the exercises at the end of this chapter. 

## **7.7 Tips: Using a Debugger** 

In Sect. 1. 7 we gave a few tips about how to debug your code using simple techniques such as printing information out to the screen, and we also promised to give a little more information on using a debugger to inspect your code. There is a wide-range of open source and commercial tools to support you, should you wish to do this. 

The easiest debuggers to use are those which are integrated with your development environment (such as Visual Studio or Eclipse). These integrated debuggers allow you to set breakpoints (places where you wish to temporarily pause execution) by clicking and selecting individual lines of code in your editing window. In the case of Eclipse, the debugging options basically provide a point and click front-end 

interface on top of a less user-friendly text-based debugger such as `gdb` . 

The next level of sophistication is a graphical standalone debugger. Many of those available are actually a front-end to a text-based debugger, whereas some, such as `ups` are completely self-contained debuggers. A popular open source graphical front-end debugger is `ddd` which is a graphical interface to `gdb` , although it can also interface with a range of low-level debugging tools for a variety of programming languages. There are many other graphical front-end debuggers available such as `KDbg` and `Xxgdb` . 

The lowest level of sophistication is the text-based debugger. The most widely used of these is the open source GNU debugger `gdb` , but many commercial compilers offer their own debugging environments. 

All the debugging tools mentioned will allow you to walk through the code line by line, function call by function call, or to the next break point. If your program aborts with a _segmentation fault_ , then the debugger will stop at the place where the fault happened, allowing you to see the line which caused the error. At any stage in execution, you will be able to inspect the values of the program variables and classes. You will also be able to inspect the _back-trace_ (or _stack_ ) which shows the function calling sequence which led from the `main` function to a particular line of code. 

Our advice is to debug your code with a graphical front-end to `gdb` , such as the popular `ddd` . Such tools are easy to download and install. The fact that they have a graphical interface with a built-in help system will allow you to rapidly see what the capabilities are. We also need to stress at this point that debuggers do not cope well with optimised code. Before you load the program into the debugger, you must remember to �irst compile your code with the “ `-g` ” �lag (see Sect. 1. 3. 3). 

## **7.8 Exercises** 

**7.1** In this question, we will develop classes to describe the students at a university. 1. 

Write a class of students at the university that has the following public members: 

- a string for the student’s name; 

- a double precision �loating point variable that stores the library �ines owed by the student; 

- a double precision �loating point variable that stores the tuition fees owed by the student; 

- a method that returns the total money owed by the student, that is, the sum of the library �ines and tuition fees associated with a given student; 

- a few constructors that take different arguments. 

2. 

The library �ines owed by the students must be a nonnegative number. Enforce this by making a student’s library �ines a private member of the class. Write one method that allows the user to set this variable only to nonnegative values, and another method that can be used to access this private variable. Both methods should be public members of the class. 3. 

Students at the university are either graduate students or undergraduate students. All undergraduate students are full-time students. Graduate students may be full-time students or part-time students. Derive a class of graduate students from the class of students that you have already written with an additional member variable that stores whether the student is full-time or part-time. 4. 

Graduate students do not pay tuition fees. Use polymorphism to write a method that calculates the total money owed by a graduate student. This will require the method for calculating the total money owed to be a virtual function of the parent class. 5. 

Ph.D. students are a special class of graduate students who do not pay library �ines. Derive a class of Ph.D. students from the class of graduate students. Write a method that calculates the total money owed by a Ph.D. student. 

**7.2** This exercise is an investigation into proper use of the `virtual` keyword and into safe ways of making _abstract_ classes. 

The following program presents a small hierarchy of classes using the _abstract class pattern_ described in Sect. 7.6. There is an abstract class `AbstractPerson` , which is intended never to be instantiated, and two derived classes, `Mother` and `Daughter` . The code in the `main` function demonstrates the power of polymorphic inheritance. It shows that it is possible to have a variety of objects of the same family stored as pointers to a generic abstract type, each of which could be a different concrete class. The `AbstractPerson` class promises a `Print` method, but it is only at run-time that the system inspects the class pointed to by `p_mother` and works out which `Print` method to invoke. 



#### 1. 

Copy, save, compile and run the above program. The output from the `Print` method calls in lines 25 and 26 ought to be: 



2. 

Investigate what happens if you remove the `public` keyword from the inheritance declaration of either derived class (lines 9 and 15). This will make the base class inaccessible from the derived class. 3. 

Investigate what happens if you remove either of the `virtual` keywords in lines 6 and 12. Also investigate adding the `virtual` keyword on line 18. How does the output change after each of these changes? 

#### 4. 

What happens if you use the code fragment below to instantiate an instance of the abstract class in the main function? 



5. 

The _preferred method_ of making an abstract class with a pure virtual method (so that it cannot be instantiated) is to give no implementation of that method in the class. This is done by replacing line 6 with the rather strange syntax which was introduced in the `AbstractOdeSolver` of Sect. <u>7.6:</u> 



#### 6. 

After making the `Print` method of `AbstractPerson` pure virtual as above, repeat the exercise in part 3 of removing the virtual keywords in lines 6 and 12. 

7. 

Also after making the method `AbstractPerson::Print()` pure virtual as above, repeat the exercise in part 4 of attempting to instantiate an instance of the abstract class. 

## **7.3** 

In Sect. 7.6, we discussed how abstract classes could be used to write a library for calculating the numerical solution of initial value ordinary differential equations, i.e. ordinary differential equations of the form 



for some user speci�ied function _f_ ( _t_ , _y_ ), where _y_ = _Y_ at _t_ = _T_ for an initial value _Y_ at some initial time _T_ . We want to calculate a numerical solution in the time interval _T_ < _t_ < _T_ where _T_ is the �inal 

time. To solve this equation numerically, we require the user to specify an integration step size, which we denote by _h_ . A large variety of numerical methods exist for solving equations such as these and in Sect. 7.6 we explained that, as these methods all required very similar inputs, they could be coded very effectively using an abstract class pattern. We will base the library developed in this exercise on the abstract class in Listing 7.2: you should save this �ile, and ensure that you understand how the class members relate to the discussion above. 

In this exercise, we will develop the library to allow you to solve initial value ordinary differential equations using two methods: the forward Euler method; and a Runge–Kutta method. Using a step size _h_ , we de�ine the points by 



where _h_ is chosen so that _t_ = _T_ . The numerical solution at these are points is denoted by . These values of _y_ determined by the numerical technique chosen. For the forward Euler method, we set = . For is given by 



For the fourth order Runge–Kutta method, we set . For , we calculate using the following formulae: 



More details on numerical methods for initial value problems may be found in Kreyszig, [2]. 

1. 

Write the methods associated with the class `AbstractOdeSolver` and save these as the �ile `AbstractOdeSolver.cpp` . Note that you do not have to write the pure virtual functions, as the “ `= 0` ” when they are declared in the �ile `AbstractOdeSolver.hpp` means that these are already written. 2. 

Derive a class called `FowardEulerSolver` that allows the user to specify the function `RightHandSide` , and contains a method `SolveEquation` that uses the forward Euler method to calculate the values of _y_ as described above, and writes the values of _t_ and _y_ to 

�ile. You may want to refer back to Sect. <u>5. 7</u> to remind yourself how to allow a user to specify a function. 3. 

Test the class `FowardEulerSolver` using the initial value ordinary equation 



for the time interval , and with initial condition at . This equation has solution . Investigate how the 

choice of step size affects the accuracy of the solution. 

#### 4. 

Repeat the two sub-parts above using the fourth order Runge–Kutta . method to calculate the values of _y_ 

## **Footnotes** 

##### <u>1</u> 

A feature of C++ is that it also allows _multiple inheritance_ , not available in other object-oriented languages, where derived classes may inherit from more than one base class. This feature causes some seasoned C++ programmers dif�iculty, and hence is beyond the scope of this book, although we do brie�ly discuss this topic in Appendix <u>B.</u> 

<u>2</u> 

SOR is an iterative technique for solving linear systems: see, for example, Iserles [1]. 

##### <u>3</u> 

The advanced programmer can test if a `Guest` is a `SpecialGuest` using a feature called _dynamic casting_ . 

© Springer International Publishing AG, part of Springer Nature 2017 Joe Pitt-Francis and Jonathan Whiteley , _Guide to Scienti�ic Computing in C++_ ,  Undergraduate Topics in Computer Science <u>https://doi.org/10.1007/978-3-319-73132-2_8</u> 

# **8. Templates** 

Joe Pitt-Franci ~~s~~ <u>1</u> and Jonathan Whitele ~~y~~ <u>1</u> (1) University of Oxford, Oxford, UK 



**Joe Pitt-Francis Email:** <u>joe.pitt-francis@cs.ox.ac.uk</u> 

If we want to write a function that returns the larger of two numbers, and we want this function to be used for both integer variables and double precision �loating point variables, then we could use function overloading and write two functions: one for integer variables and the other for double precision �loating point variables. Both of these functions would require only a few lines of code, and it would not be dif�icult to maintain both functions. For larger functions maintaining more than one function to do the same operations may be problematic. This may be avoided by the use of _templates_ , a feature of the C++ language that allows very general code to be written. 

We begin this chapter by discussing templates and the �lexibility that they permit. One library associated with C++ is the _Standard Template Library_ (STL) : we conclude this chapter by giving a brief survey of this library, and other functionality that has been introduced in recent C++ standards. 

## **8.1 Templates to Control Dimensions and Verify Sizes** 

Many scienti�ic computing applications are underpinned by vectors and matrices. We have seen earlier that these are represented in C++ by arrays. Under normal circumstances there is no check, when we 

attempt to access elements of an array, that the index is a valid index. For example, in the code fragment below we attempt to access the element with index 7 when the array only has 5 elements. Although this is clearly an error, it may not trigger a compiler or run-time error. The most likely outcome when code including these lines is executed is a segmentation fault or an incorrect answer. 



If this fragment is part of a large program, it could be dif�icult to locate this error. It would be therefore be useful if we could use arrays with an additional feature that a check for validity of the index is performed each time an element of the array is accessed. This may be achieved using the class shown below, which is referred to as a _templated class_ . 



The class in the listing above allows us to declare instances of `DoubleVector` , specifying the length of the array. The entries of the array are private members of this class and so can’t be accessed in the normal way that we would access elements of an array. Instead we access members of this class by overloading the square bracket operator. Overloading this operator allows us to check that the index is a valid index before returning the variable requested. 

Use of the class above is demonstrated in the code below. Note (in line 6) how using this class requires us to declare the array `v` as an instance of a `DoubleVector` , with the size of this array being enclosed within pointed brackets. Subsequently this array is accessed in exactly the same way as a normal array, but with the additional feature that a check is carried out on the index every time an element of the array is accessed through the overloading of the square bracket operator. 



## **8.2 Templates for Polymorphism** 

There are very good reasons in C++, and many other programming languages, for distinguishing between integer variables and �loating point variables. For example, the argument(s) used to access an element of an array may only take integer values which provides one level of validation that the index is correct. Furthermore, integers may be stored much more ef�iciently than �loating point variables. One slight drawback in having to distinguish between these variables is that if we want to write a function that is valid for all numerical variables—that is, both integers and �loating point variables—we have to write more than one instance of the same function. Templates, however, provide a way around this. 

The program below demonstrates how a function `GetMaximum` that returns the maximum of two numbers, either integers or �loating point variables, may be written. The code is very similar to the code that we would write to calculate the maximum of two numbers, although there are two important differences. The �irst difference is 

that the function prototype in line 3 of the listing speci�ies that the function is de�ined for a general class `T` , and that the return type and both function arguments will be instances of the same class `T` . To call the function, we have to put the data type used in angled brackets as is shown in lines 7 and 8 of the listing. The function `GetMaximum` demonstrates _polymorphism_ , because it can perform the same operation on different types of input argument. This type of polymorphism is also called static polymorphism or compile-time polymorphism, because when the compiler sees line 7 or 8 of the listing it makes a speci�ic version of `GetMaximum` ready for the `int` or `double` type. 



## **8.3 A Brief Survey of the Standard Template Library** 

The Standard Template Library (STL) contains many commonly used patterns that may be reused for different types of objects. In this survey, we give a summary of the features available that are particularly relevant to writers of scienti�ic software. 

Containers, such as random-access vectors and sets, are dynamic arrays where the STL is responsible for memory management. We now demonstrate how these two containers may be used. Other containers that are available in the STL are maps, multimaps, multisets, lists and deques (double-ended queues, pronounced “decks”). There are also many more algorithms that may be performed on these containers other than those presented here. Some of these other containers and algorithms do not have application in scienti�ic computing software and so we do not discuss them here. Nevertheless, it is useful for readers to be aware that they exist. 

### **8.3.1 Vectors** 

The STL vector class is a very useful container because it is an _extensible_ class which has a similar interface to the regular C++ array. The fact that it is extensible means that its size is not �ixed (either at compile time or at the time that it is created) and that it will grow to accommodate new items as necessary. One can either declare an empty STL vector of minimal capacity which then grows by adding new items to it, or one can exploit ef�iciency savings by knowing the maximum size at compile time or run time. 

If you explore available STL containers, you will notice that the interface for the STL vector is very similar to the interface for the other basic container types _deque_ and _list_ . This is a good example of object _abstraction_ , because the details which distinguish these container types from each other are not exposed to the user. The main differences between these types of containers are in the ef�iciency which STL guarantees for various operations: it is possible to retrieve an item from an STL vector via its index in a single operation, but this is not possible from an STL list. It is generally only ef�icient to insert and delete elements to the back of a vector object and to the front or back of a deque. The list type allows ef�icient constant time insertion and deletion anywhere in the container. 

The use of the vector container is shown in the listing below. Several features of the STL are included in this listing which we now highlight. 

- To use the vector container, we must include the `vector` header �ile (line 2). For some algorithms that may be used on STL vectors, such as sorting, we must include the `algorithm` header �ile (line 3). 

- In line 8, we declare a vector of strings called `destinations` . Note that we do not have to state the size of the vector: the STL will handle this for us. We can write 



   - if we wished 

- to begin with a vector of 50 empty strings rather than an empty vector. 

- In line 9, we _reserve_ 6 elements. This sets the vector’s _capacity_ without changing the number of items in the vector. Although this line is unnecessary, it may produce ef�iciency savings in more memoryintensive code because it establishes that 6 items can be stored in the vector without having to reallocate any memory later. 

- In line 10, we introduce our �irst entry to the vector, the string “ `Paris` ”. The member function `push_back` appends a copy of this string to the current vector, which is currently empty. 

- In line 11, we append another entry to the end of the vector, that is, the second entry of this vector is “New York”. 

- In line 12, we append a further entry to the vector, that is, the third entry of this vector is “Singapore”. 

- In lines 13 and 14, we demonstrate the use of the member function `size` for accessing the number of elements of the vector. 

- In lines 17–20, we show that entries of the vector may be accessed in the same way as for a standard vector. 

- Lines 22–26 demonstrate how to access entries of the vector using an _iterator_ . The iterator is declared in line 22, where we de�ine what type of vector the iterator is associated with, that is, in this case a vector of strings. In line 23, we construct a `for` loop that iterates from the start of the vector to the end of the vector using this iterator. The entries are printed using line 25, which prints out the contents of the vector entry that the iterator is pointing at. Note the use of the overloaded `*` operator which looks like a pointer de-reference. 

- In line 28, we add a string to the _start_ of a vector by using the `insert` method, and inserting at the start of the vector using the `begin` method: all subsequent entries are now moved one place back. 

- In line 29, we add a string to the vector, and place it in the second position: all subsequent entries are again moved one place back. In line 30, we add another entry to the end of the vector. We then print out the number of entries of the vector, and the entries, using lines 31–38. 

- In lines 40 and 41, we erase all entries of the vector that appear after the third entry, and then print out the number of entries of the vector, and the entries, using lines 42–49. 

- In line 51, we use the algorithm `sort` : this algorithm will sort a vector of strings into alphabetical order and requires the header �ile `algorithm` as described above. This is veri�ied by printing the entries of the vector using lines 52–59. 





### **8.3.2 Sets** 

A set is an STL container where new entries are only stored if they are distinct from the entries already stored. The machinery for maintaining the distinctness of the entries is _abstracted_ from the user. One might implement a set as an unordered list of elements, so that each insertion requires a membership test that may involve an equality check with all elements of the existing set. One might make a more ef�icient implementation using an _ordered_ list, so that membership tests involve fewer equality checks against existing members. The STL set actually uses a more ef�icient structur ~~e~~ <u>1</u> so that it is able to guarantee the ef�iciency of all possible set operations. It is only possible to make an ef�icient set implementation if the elements of the set can be ordered. We will demonstrate the set container by using the class of points in two dimensions whose members have coordinates that take integer values. As the items in a set have to be comparable, we need to de�ine an ordering on points in two dimensions, which we do by overloading the “less than” operator for these points. If we are comparing two points and , which represent the points ( ) and ( ), we 

say that if , and if . Only if we say that if , and if . If and then the points and are identical: the set would only store one instance of these two. 

The class `Point2d` representing the class of points in two dimensions is given in the listing below. This class has two member 

variables, `x` and `y` , that store the _x_ - and _y_ -coordinates. There is also a constructor that allows us to initialise the coordinates, and an overloaded “less than” operator that allows us to order points in two dimensions as described above. 



In the listing below, we create a set of instances of the class `Point2d` . When using the set container, we must include the `set` header �ile (line 1). In line 7 we create a set, made up of instances of the class `Point2d` , that is called `points` . In lines 9–12, we attempt to insert four points into this set using the `insert` method associated with sets. Two of these points—the origin and the point `(0, 0)` —are identical, and so only one is stored. This is seen in lines 14 and 15 where we print 

out the size of the set, which is 3. Note how the iterator may be used in lines 17–21 of the code to print the member variables of the class of points in line 20. 



## **8.4 A Survey of Some New Functionality in Modern C++** 

At the close of Chap. 4 we thought it pertinent to give you an indication that some features of C++ have moved on since the �irst edition of this book was written. In Sect. <u>4. 4</u> we introduced two of the new smart pointer constructs which have been implemented in compilers that conform to modern C++ standards. This enabled us to indicate that, whereas in former days all dynamically allocated memory was the responsibility of the programmer, there are now ways to ensure that certain pointers are not aliased (via the `unique_ptr` type) and to automatically garbage collect certain variables (via `shared_ptr` ). 

Now, towards the close of this chapter, we would like to introduce a selection of some of the other features available in modern C++ standards such as C++11. With the exception of smart pointers, we have deferred writing about any of these new features until now because most of the features are _templated_ over a type. By introducing modern C++ features here we only intend to scratch the surface. As in Sect. 8.3, this section is intended only as a brief survey of some of the available features. We have deliberately selected those features which we have found most helpful in the years since we wrote the �irst edition of this book—in the belief that these features will prove useful to other computational scientists. 

Note that with a current version of the GNU C++ compiler, all code fragments in this section require that the compiler is explicitly told that it is compiling code that conforms to a newer standard of C++ than its default. This may mean invoking 



or something similar on the command-line. 

### **8.4.1 The** **`auto` Type** 

After reading Sect. <u>8.3</u> you may have been left believing that templates are all double colons and angle brackets. Worse, that whenever you want to iterate over a vector or set which you have created, then you will need to remember the exact form of the iterator type. The good news is that much of the writing of these types can now be simpli�ied via _automatic type inference_ . This not only saves on writing, but it also makes templated code more readable, by removing some of the lengthy type names. This relies on one simple rule. 

**Rule** : if the type of a new variable can be inferred by the compiler at the point of its initialisation then the type may be replaced by `auto` . 

For example, in the code fragment below, there is enough information for the compiler to infer that `i` ought to be an integer variable: at its initialisation it is given the value 1 (an integer). Meanwhile the variable `x` which is initialised to a �loating point value is 

given the inferred type `double` . Note that each of these two lines contain both the `auto` type and an assignment. Neither of these lines can itself be split across two lines, because if the type is separated from the initialisation then the type can no longer be inferred. 



It is worth pointing out that the full power of automatic type inference is not demonstrated by the above example and, furthermore, that inferring simple types as in this example is potentially dangerous because the programmer may �ind unexpected behaviour if the compiler infers a different type to the type presumed by the programmer. For example, the code below will print to console that `x` contains the value 22 which may not be what the programmer intended. This is because, on line 1, the compiler will infer that the type of `x` ought to be `int` . A programmer, reading line 2, may assume that `x` ought to be of type `double` , but at this point it’s too late—the type is �ixed. The programmer could repair this issue either by initialising the value of `x` to 22.0 or by using `double` as the explicit type for `x` . 



The real power of the `auto` keyword comes in places where the onus used to be on the programmer to write out a lengthy type name. For example in Listing 8.3, loops beginning at lines 23, 35, 46 and 56 all rely on a `const_iterator` which is declared once globally in line 22. This was largely done to keep the code compact. Note though that the style of globally declaring a loop iterator in Listing <u>8.3</u> is in direct contravention to point 4 in our tips on coding style (given in Sect. 6. 6). In the code below we have indicated how the code in any of these `for` loops over the vector `destinations` may be replaced concisely with one which has a locally-declared iterator of type `auto` . 



### **8.4.2 Some Useful Container Types with Uni�ied Functionality** 

Modern C++ provides `std::array` which is a useful replacement for the small size, statically allocated array (as found in Sect. <u>1. 4. 5). The</u> idea behind this array type is to provide a uniform way to access and use arrays. It is templated by the type of object it contains and its size. In terms of access to its elements it can behave exactly like the old style plain array: the element index in square brackets is used to read or write individual elements. This is demonstrated below where an oldstyle array and a new-style array are created on lines 1 and 2 respectively. In the assert statement on line 3, elements of the two arrays are compared using the same syntax. 



However, there are two main ways in which the new `std::array` is very different to the old array. In both of these respects it behaves a lot more like a �ixed-size version of `std::vector` . The �irst difference is that many of the vector functions, such as `begin()` and `size()` , are available in the templated array class. The second difference is that arrays can now be passed into functions as �irst-class objects. That is, whereas old-style arrays are always sent to functions as pointers (a fact we exploited in Sect. <u>5. 2. 4) the new type can either be copied or sent as</u> a reference. 

Because the new-style array is built around the same infrastructure as the previous STL structures it interacts with many of them in the way one might expect. Many structures may be initialised using the 

_initialiser list_ style (a list of elements in curly braces). One can also convert between many of the structures by copying data between objects. 

In the code below, after initialising an array in line 1, we then copy the array contents into both a vector and a set in lines 2–4. Note that the syntax for the two operations is that same but that the data are converted to different underlying representations. Finally the representation is tested in line 5, where we expect that the set, which has no duplicates, will contain fewer members. 



Modern C++ also contains a light-weight mixed-type _tuple_ . This allows us to put pieces of data together in one place in a modular way, so that it is similar to a small class with no methods. The tuple is a generalisation of the existing STL data structure `pair` (which was restricted to having exactly two pieces of data). An example of the use of a tuple is given below. The new tuple `explorer` is required to represent information about a book via two strings and a number. It is clear from lines 4 and 5 that access to the member data in the tuple is possible (though the syntax may look a little strange). Finally in line 7 we tidy up some of this new strange syntax by using the keyword `auto` which enables us to initialise a reasonably complicated mixed-type tuple in a single line. 



### **8.4.3 Range-based** **`for` Loops** 

A very useful feature of modern C++ is the range-based loop. This is sometimes known in other languages as a “for each” loop but, as we will see later, “for each” has a reserved meaning in modern C++. The rangebased loop provides the programmer with a way of iterating over each and every member of a particular container (array or vector, for example) without having to worry about how many members there are, or about the exact mechanism of iteration. 

The most simple way to demonstrate this is with an iteration over an intialiser list. Here the variable `even` , which is local to the `for` loop takes on all the values in the given list up to, and including the value 8: 



The range-based loop is available for all structures which might be iterated over: arrays, vectors, sets, maps and so on. In each case the meaning of the range-based loop is to iterate over the container in the same way that the container’s regular iterator might behave (but with a far more compact syntax). If we use a range-based loop on a `std::set` then we expect to see each element of the set exactly once, but with no guarantee on the order in which they appear. If we use a range-based loop on a `std::vector` then we will see each item according to their position in the vector. 

We can now re-visit the example code for the STL vector type in Listing <u>8.3</u> and again re-write those loops which are iterating over the members of the vector and printing them out. Note that in the code below we have taken advantage of the array initialiser in lines 8–9 in order to rapidly �ill the vector `destinations` with content. 

In lines 11–15 we show the normal usage for a range-based loop over a vector. On each iteration of this loop the variable `city` , which is local to the loop, is assigned a value which is a _copy_ of an item in the vector. This means that the content of the underlying vector cannot be changed: any modi�ications to the copied string in the variable `city` will stay local to the loop. If, on the other hand, we intended to change the contents of `destinations` , then we would do so by using a 

reference to the items. The use of a reference in a range-based loop is demonstrated in lines 16–21. Here each of the city names in the vector is modi�ied using simple string concatenation. Finally, in line 23, we show that a combination of a range-base loop, the `auto` keyword, and writing the loop without braces leads to a highly compact way to express the same code. The loop in line 23 is equivalent to that in lines 11–15. If we wanted to make modi�ications to the vector then we could insist that the local variable were a reference by writing `auto&` instead of `auto` for the type name. 



### **8.4.4 Mapping Lambda Functions** 

We close this survey with the “for each” function, which is intended to take a function and apply it to every member of a container (for example a vector). This type of functionality is called a “map” in some languages. It works by taking as arguments the beginning and end of a range to be iterated over, and the function that should be applied. In the most straightforward form the “function” might just be the name of function which has been de�ined elsewhere, but it becomes more powerful when the function can be declared locally: inside the current scope, or even within the `for_each` function itself. The local declaration of a function is known as a _lambda closure_ by computer scientists. 

In the following code fragment, we apply functions which double each element of a vector. The �irst time this happens is on line 7 where the function name `twice` appears in the third argument. Now this `twice` function might have been declared externally (as indicated by the comment on line 4) but, instead, it is declared on line 6. Square brackets here indicate that what follows is a function, with round brackets around the argument, braces around the function body, and a �inal semicolon. We have used `auto` for the type of `twice` because its real type is a function from `int&` to `void` . Lines 10–11 show that the function does not need a name. Instead we can just declare the form and de�inition of the function in place. This is a very compact form, but perhaps renders the code less readable. 



## **8.5 Tips: Template Compilation** 

In Sect. 8.1 we presented a templated class `DoubleVector` in which the size of the vector is speci�ied at compile time. Since the size of the vector in `UseDoubleVector.cpp` (Listing <u>8.2) is known at compile</u> time, the memory allocation is static. 

When building a program to use a templated class such as `DoubleVector` we might follow the pattern laid down in Sect. 6. 2. 4. 1 of placing the _de�inition_ of the class in the �ile `DoubleVector.hpp` and the _implementation_ of the class in the �ile `DoubleVector.cpp` . We would write a main program to test it and write the rules for compilation into a `Makefile` . There is an unfortunate snag with this plan, because when we instantiate a vector ( , say) 

in our main program and compile it, the compiler has no access to the implementation from `DoubleVector.cpp` . The compiler needs to compile code from the `DoubleVector.cpp` �ile, in which all the instances of `DIM` are replaced by “5”. 

There are three strategies which can be used to overcome this _template instantiation_ problem. 

1. 

Each �ile which uses the class may include the implementation of the entire class through the use of `#include "DoubleVector.cpp"` . This means the code compilation may be slower since the entire class must be compiled every time it is used. It also means that care must be taken to ensure that the �ile `DoubleVector.cpp` is included at most once. (The `#define` mechanism introduced in Sect. 6. 2. 2 may be suitably adapted for this purpose.) 

2. 

A similar solution is to place the entire class in the �ile `DoubleVector.hpp` , as we did for `DoubleVector` in Listing <u>8.1</u> of Sect. 8.1. This, again, has the disadvantage that the entire class must be compiled every time it is used. 3. 

A more advanced solution to the problem is _explicit instantiation_ . If it is known that we only use `DoubleVector` with a small set of sizes, then we can force the compiler to produce exactly the ones which are needed as it compiles `DoubleVector.cpp` into the object �ile `DoubleVector.o` . This is done by making an unnamed instance of the class of each required size in the �ile `DoubleVector.cpp` , as the code fragment below illustrates. 



## **8.6 Exercises** 

**8.1** The probability of rain for each of the next `N` days is to be stored in a double precision �loating point array of size `N` . As the entries of this array are probabilities they should all take values between 0 and 1 inclusive. However, as they have been calculated using a numerical algorithm, these probabilities are only correct to within an absolute error of : that is, in reality these 



numbers may be between and 

inclusive. Using the ideas presented in Sect. <u>8.1,</u> use templates so that when accessing an individual entry of the array: 

1. 

the value stored by the array is returned if it is between 0 and 1 inclusive; 2. 

the value 0 is returned if the value stored is between and 0 

inclusive; 3. 



the value 1 is returned if the value stored is between 1 and 

inclusive; and 4. 

an assertion is tripped otherwise. 

**8.2** Use templates to write a single function that may be used to calculate the absolute value of an integer or a double precision �loating point number. 

**8.3** Use the class of complex numbers given in Sect. <u>6. 4</u> to create an STL vector of complex numbers. Investigate the functionality of the STL demonstrated in Sect. 8.3.1 using this vector of complex numbers. Note that when you add an object to an STL vector it is a _copy_ which is added, so it is imperative that the copy constructor is working as expected. 

**8.4** Modify the example of an STL set given in Sect. <u>8.3.2</u> so that the coordinates of the point are now given by double precision �loating point variables. You will now need to think a bit more carefully about what it means for two coordinates to be equal: see the tip on comparing two �loating point numbers given in Sect. <u>2. 6. 5.</u> 

## **8.5** Use the container 



(a mapping 

from keys of type `string` to values of type `int` ) 

to represent a phone book. If you have access to a compiler which is compatible with C++11 or higher then you might consider some of the following ideas. 

1. 

Use an _initialiser list_ to populate the phone book with a small list of name-number pairs. See Sect. 8.4.2 for examples of structures initialised in this way, but be aware that a _map_ needs to be initialised with a list of lists. 

2. 

Write a `for` loop to iterate over the contents of the phone book and output all name-number pairs. Try this with the range-based loop that was introduced in Sect. <u>8.4.3.</u> 

3. 

Write out the entire contents of the phone book using a `std::for_each` loop and a lambda function, in a similar manner to the loops shown in Sect. 8.4.4. 

4. 

Write functionality to get all names from the map and store them in a vector. 

5. 

Write functionality to get all the numbers from the map into a vector. Then use `std::set` to detect whether two or more people share the same number. 

6. 

Write the “reverse” map to look up a name when given a number. If you have two people who share the same number then you may �ind that `std::multimap` is useful. 

7. 

Re-write the map so that, instead of each name mapping to a single number value, it maps to a `std::tuple` consisting of a number and an email address. See Sect. 8.4.2 for example use of _tuples_ . 

## <u>1</u><sup>**Footnotes**</sup> 

The STL set is implemented as a tree structure known as a _red-black search tree_ . 

© Springer International Publishing AG, part of Springer Nature 2017 Joe Pitt-Francis and Jonathan Whiteley , _Guide to Scienti�ic Computing in C++_ ,  Undergraduate Topics in Computer Science <u>https://doi.org/10.1007/978-3-319-73132-2_9</u> 

# **9. Errors, Exceptions and Testing** 

Joe Pitt-Franci ~~s~~ <u>1</u> and Jonathan Whitele ~~y~~ <u>1</u> 

- (1) University of Oxford, Oxford, UK 



**Joe Pitt-Francis Email:** <u>joe.pitt-francis@cs.ox.ac.uk</u> 

In Sect. 1. 6 we introduced the concept of an assert statement. This is a way of forcing your program to terminate execution, should something unexpected happen. The program which motivated the use of assertion in Sect. <u>1. 6</u> was one which calculated the square root of a number entered at the command-line. Here is a version of that program where the assertion has been removed by turning it into a comment. 



What happens when a user ignores the request and enters a _negative_ number at the command line? Without the assert statement on line 10 it is likely that the program will complete without error. This is because 

the computer’s �loating point unit renders the result of some calculations such as `sqrt(-1.0)` as “not a number” or `nan` for short. 



Other examples of �loating point operations which produce the answer `nan` include `0.0/0.0` and `log(0.0)` . Some calculations such as `1.0/0.0` will resolve to a �loating point representation of in�inity ( `inf` ) . In a scienti�ic program, once one variable has been set to `nan` or `inf` then this value is likely to propagate to later parts of the calculation. It is normally best to check for this sort of error at the earliest possible stage so that computation is not wasted. In this context, it would be prudent to check in any piece of code that uses division, square root, logarithms etc. that the values of all the arguments are in a sensible range. As we have already seen, assertions are one method of checking such arguments. In this chapter, we will see that exceptions are another method of checking that are more �lexible in some ways. We will also introduce techniques for testing software, to allow software to be developed in a sustainable manner with as few errors as possible. 

## **9.1 Preconditions** 

Every section of a program (where a “section” could be a function, method, block, `for` -loop iteration body etc.) can be thought of as having the task to produce a _postcondition_ when given a valid _precondition_ . The postcondition of the program above (the thing which it is tasked to do) is that it prints the square root of a given number. It does this subject to the precondition that the number is nonnegative. Consider a method which �inds all the roots of a function _f_ ( _x_ ) in the half-open range . This method might need to assume as a precondition that the function _f_ is continuous and differentiable over the same range . More trivially, it might also need to 

assume that or . What should happen if ? If the precondition for correct functionality is not met 

then what should happen? Before we answer this question, we will �irst consider a speci�ic case. 

### **9.1.1 Example: Two Implementations of a Graphics Function** 

In a particular graphics library, there is a function for rendering a 2-D annulus. This function takes four input arguments: the inner radius, the outer radius and the number of radial and axial segments. The speci�ication of the library says that the outer radius must be bigger than the inner radius and both should be nonnegative. It also says that the segment numbers must be strictly positive. The speci�ication further says that it is valid to give the inner radius as zero, in which case the annulus will be rendered as a 2-D disk with no hole. 

There is a cautionary story about a professor who wrote a program for his students which used this graphics function to draw disks. He misread the speci�ication and set the radius values the wrong way round so that the outer value was 0.0 and the inner value was 1.0. Without realising his mistake, he distributed the program source code to his students, some of whom began to complain that it would not run. 

The problem was that the students whose code would not run were using a different implementation of the library. The two different implementations of the same speci�ication were dealing with errors in different ways. The implementation of this function in the graphics library as used by the professor contained a check for his type of error which silently �ixed the problem by interchanging values in a manner similar to the code given below. 



Meanwhile, the students who complained that the program was not running properly were using a library implementation in which the annulus function terminated on reaching this type of error. The listing below shows that this termination behaviour can easily be implemented by checking the precondition with an assertion. 



The “helpful” implementation, as used by the professor, was in reality making a bug in his code invisible—only for it to become embarrassingly visible in the other implementation. Both implementations are _correct_ in the sense that they follow the speci�ication and perform the correct operations provided that the preconditions are met. Unfortunately, the library speci�ication left the handling this kind of error open to interpretation. 

## **9.2 Three Levels of Errors** 

Some of the most important decisions that a programmer has to make are about how errors should be treated. What should happen if the user misreads a prompt and enters some invalid input? What should happen if the application writer accidentally permutes the input arguments of a library function? What should happen if some numerical scheme has generated `inf` or `nan` because of divergence? 

The answer to all these questions is the same: “It depends”. It’s good to treat errors differently depending on their severity, both in terms of how likely they are to happen and in terms of how easy it might be to �ix the problem and carry on. The dif�icult balance of knowing how severe an error might be is illustrated by the `RenderAnnulus` story in Sect. 9.1.1 where the programmers of different library implementations chose to deal with the same error in completely different ways. One set of programmers decided the error was trivial to �ix, while the other set decided to abort the program. 

We propose a strategy for handling errors which is built on a framework of three levels of errors. 1. 

If the error can be �ixed safely, then _�ix_ it. If need be, warn the user. 2. 

If the error could be caused by some reasonable user input then throw an _exception_ up to the calling code, since the calling code should have enough context to �ix the problem. 

3. If the error should not happen under normal circumstances then trip an _assertion_ . 

These three basic levels could be further re�ined. You may distinguish between errors that trip assertions (which are normally removed in optimised code) and errors that should halt the program under all circumstances. At the other end of the scale, you might distinguish between error �ixes which are silent and those which should warn the user that something has been changed. 

The _exception_ level of error is a compromise between patching the problem to carry on, and stopping completely. It is used in 

circumstances where the caller of a function may have enough information to be able to deal with the error. For example, a nonlinear Newton root �inder may diverge and hence signal an error, but the programmer may know that the original task in question can still be solved by calling the same function with a different initial guess, or by calling it with a damping factor, or by calling a bisection root �inder. The logic would be to �irst try the Newton solver, but if that function signalled an error then to �ind the root using a more expensive bisection routine. 

## **9.3 Introducing the Exception** 

An exception in C++ is a way of interrupting the normal �low of control of a program and _throwing_ a bundle of information back to the calling code. This bundle of information is encapsulated inside an object. We de�ine in this section a class called `Exception` , but objects of any class may be thrown between functions to signal an error. 

The use of exceptions requires the keywords `try` , `throw` and `catch` . 

- `try` is used in the calling code and tells the program to execute some statements in the knowledge that some error might happen. 

- `throw` is used when the error is identi�ied. The function called will encapsulate information about the error into an `Exception` object and throw it back to the caller. 

- `catch` is used in the calling code to show how to attempt to �ix the error. Every block of code that has the `try` keyword must be matched by a `catch` block. 

- Exceptions which are not caught by the calling code may cause the program to halt. 

When an error occurs we want the code to “throw” two pieces of information: a one-word summary of the problem type and a more lengthy description of the error. We write a class `Exception` (shown below) to store these two pieces of information, and with the ability to print this information when required. 





## **9.4 Using Exceptions** 

In Listing 3. 4, we read from a named �ile `Output.dat` . We assumed that this �ile existed and tripped an assertion if it did not. In the code below, we present a more sophisticated program for opening a �ile which uses exceptions to attempt to �ix the problem. If the �ile cannot be opened by the `ReadFile` function, an exception is thrown. This is caught by code that prompts the user to enter an alternative �ile name. Note that `ReadFile` takes the name of the �ile as a C++ string which is 

converted to a C string on line 8 (using `c_str` which was introduced in Sect. 1. 4. 8). 



## **9.5 Testing Software** 

It is often the case that you need to take a program which has been developed in the past and seek to extend its functionality, perhaps to address some new research question. Assuming that you are able to understand the working of the original code because it is welldocumented (as suggested in the tips given in Sect. <u>5. 10) and has a</u> literate coding style (as suggested in the tips given in Sect. 6. 6), there is still a potential pitfall. Suppose you add the new functionality, use it to solve your new research problem, but later discover that the original functionality of the code has changed. Perhaps you are no longer able to reproduce the results which are needed for a publication. This pitfall may have been avoided had an appropriate software testing strategy been used for the original code. 

For reasons including those given above, it is universally accepted that software should always be tested to give con�idence in the output when a code is executed. There is, however, less agreement on how much effort should be put into testing, and on the methodology to be used for testing software. One reason for the absence of a uni�ied view is that the rigour required depends on many characteristics of the software which we now explain with the aid of examples. 

Suppose we have a �ile that contains many matrices that are 

believed to represent rotations, that has been generated from a piece of software. If **Q** is one of these matrices, then **Q** must be an orthogonal matrix and so we must have **QQ I** , where **I** is the identity 

matrix, and . Suppose further that a colleague wants to use 

this �ile, provided he or she can be reasonably certain that the matrices are indeed orthogonal. If we were to allow this colleague to use this �ile of matrices then we should �irst check that the matrices really are orthogonal. We may check this by writing a short program that reads these matrices in and checks that they are orthogonal (subject to rounding errors) by printing to screen any warnings that a matrix isn’t orthogonal. In this case it can be argued that this rudimentary method for testing the software is appropriate, as we are checking that the �ile that we share with our colleague does indeed contain matrices that represent rotations. Nevertheless we should be aware of the limitations of testing software in such an unsophisticated manner. This method 

does not ensure that the original software is error free; all we have done is to con�irm that the given �ile does indeed contain orthogonal matrices. For example, if the �ile is believed to represent 1000 distinct matrices we have not checked that there really are 1000 matrices, or that they are distinct—we may only have 500 distinct matrices, or we may have one matrix that has been printed 1000 times. It is also possible that an error exists in the software used to generate the matrices, and that a subsequent execution of the software generates some matrices that are not orthogonal. Many other potential sources of error also exist. 

Consider, by contrast, a piece of software containing many lines of code that controls a mechanical ventilator in the clinical setting. It is clearly of critical importance that as many errors as possible are eradicated from the software before it is used, and so much more rigorous testing of the code is required. Furthermore, it is likely that the software may be updated for future generations of ventilators. It is surprisingly easy to break the original functionality of software when making what appears to be a small extension. It is therefore extremely useful to be able to test the whole code after making even a small modi�ication to this code. The basic technique of testing software described above for the �ile of matrices is not appropriate in this case, and more sophisticated techniques should be used. The testing of _safety-critical software systems_ is a research topic in its own right. 

The two examples above illustrate that the effort that should be dedicated to testing software depends on many factors. The �irst, simpler case required nothing more than a short, disposable C++ program that may easily be written by a competent programmer and requires no more discussion. The second case requires far more attention to the testing strategy. We will now describe some common testing strategies. 

### **9.5.1 Unit Testing** 

An effective technique for testing software, that is particularly useful for software that may be extended in the future, is known as _unit testing_ . When using this technique, a collection of tests are written, known as _unit tests_ . Each unit test is designed to test a particular section of the code, for example a single method of a class. Each test should then be 

executed when new functionality is added; should a test fail then it is clear that the new functionality has broken an existing part of the original functionality. 

Unit testing is particularly effective when: (i) each unit test covers only a very small number of lines of the original code; and (ii) each line of the original code is covered by at least one test. Whenever we add a small amount of new functionality we can then re-run each test. If we have broken any existing functionality at least one test would hopefully fail (as each line of code is covered by at least one test). Furthermore, as each test covers only a few lines of code, knowing which tests had failed should help us pinpoint the lines of code where the original functionality had been broken. 

In the previous paragraph we explained that, when using unit testing, should existing functionality be broken then at least one test will “hopefully” fail. The reader may expect that, rather than one test hopefully failing, at least one test would _de�initely_ fail. Unfortunately this assumes that we fully understand the algorithm being used by the software, and have written our unit tests to cover every possible cause of this algorithm failing. For effective unit testing, all possible scenarios must be tested. Suppose, for example, we are writing a graphics application. As part of this application we may want to know where two lines in the ( _x_ , _y_ )-plane intersect. This can easily be done by solving two simultaneous equations to calculate the coordinates of the points where the lines meet. We should obviously write a test to check that these coordinates are accurately calculated for two example lines with a unique point of intersection. Despite having written a test that has passed in the example case, there are possibilities where this method does not behave as expected. First, suppose the two lines are identical. They will then intersect at every point. A method written to calculate the intersection of these lines will either fail, or will return one point on the line. A second case is when the lines are parallel, but don’t intersect. Any method used to calculate the intersection of these lines would not be able to give a correct answer. To fully test this code we should write tests that cover all possibilities highlighted here. If we don’t do this then it is possible that the errors described here may occur, and will propagate into other parts of the code. This may cause other tests to fail, identifying that a problem exists. However the cause of the failing 

test will not be as clearly located, and may require many tedious and frustrating hours of debugging to pinpoint. We therefore encourage programmers to write tests that cover all possible scenarios. 

One highly recommended strategy for writing unit tests is to write the tests for new functionality _before_ adding this new functionality. This test will clearly fail initially. All tests—including the new test—are then run when the new functionality has been added, ensuring that both the new functionality has been correctly implemented and that the existing software has not been broken. This method of software development is known as _test driven development_ . 

Several C++ testing framework libraries exist, such as `CxxTest` , `Boost.Test` and `googletest` . These are designed to help you structure your testing, and we recommend using one of these libraries when writing a suite of tests. 

### **9.5.2 Extending Software** 

It is very rare that a software package is written from scratch. It is more common for existing software to be extended. For example, you may be expected to extend the functionality of software written by a colleague. Alternatively you may develop software that is underpinned by libraries from external sources. Even if the existing software is believed to be reliable, the user should at least test their own implementation of the functionality offered. This can be done by simply testing all functionality of the software, without understanding the implementation of the functionality—this is known as _black box testing_ . This is appropriate for well-supported, mature libraries, that are widely accepted to be robust and reliable. There are, however, potential pitfalls associated with black box testing. Suppose we are using some externally written software that contains the functionality to solve a linear system. When using black box testing, we would simply check that this functionality works for a given linear system. However, if we had taken a course in linear algebra, we would know that there is no solution to some linear systems, and a non-unique solution to other linear systems. To limit errors from the externally written software propagating into the code we develop, we may want to know how the software handles these cases; this will depend on the implementation of the functionality for these special cases. In these cases we would 

deliberately test the externally written software by choosing one example linear system with no solution, and one example linear system with a non-unique solution. In this case we may also investigate the algorithm that underpins the functionality of the system, allowing us to understand how the given software handles these systems of equations. This variety of testing is known as _white box testing_ . 

We now explain how both black box testing, white box testing and test driven development may be carried out. We illustrate the concepts discussed above using the `CxxTest` library, applied to the class of complex numbers developed in Sect. <u>6. 4. We focus on the principles of</u> testing, thus allowing the reader to apply these principles to other testing libraries. As such, we do not focus heavily on the details of using `CxxTest` ; a user guide for this library may be found at http:// www. <u>cxxtest. com.</u> 

### **9.5.3 Black Box Testing** 

We illustrate black box testing using the class of complex numbers developed in Sect. 6. 4. As explained earlier, when using black box testing we check that the functionality works correctly without inspecting the implementation. In Listing 9.3 we have written a suite of tests for some of the public methods contained in the header �ile for this class (given in Listing <u>6. 9); we leave the remainder of the black box</u> testing of these public methods as an exercise. As explained earlier, we use the C++ testing framework library `CxxTest` for writing these tests. We reiterate that we are focusing on how suitable tests may be written, rather than explaining how to use the `CxxTest` library. Nevertheless, a few comments on this library are necessary to allow the reader to understand the tests written. First, lines 5–6 and 78 may be considered to be a wrapper that allows us to use the functionality of this library (after it has been installed). Within this wrapper we have written a collection of unit tests: `TestDefaultConstructor` (line 8); `TestCustomisedConstructor` (line 17); `TestCalculatePower` (line 36); and `TestAgainstStdLibrary` (line 61). Within these tests, we test that a �loating point variable resulting from a calculation is equal to the true value, subject to ignoring the effects of rounding errors as described in Sect. 2. 6. 5. If, for example, we were using 

assertions to check that two double precision variables `x` and `y` differed by less than some value `epsilon` , we would write 



or, slightly more compactly 



To write this as a test using the `CxxTest` library, rather than an assert statement, we would use the specially de�ined `CxxTest` assertion 



which, rather than acting as an assertion, would simply report a failure if `x` and `y` differ by at least some value `epsilon` . Many other test assertions are offered by the `CxxTest` library. When the tests have been written, the library may then be used to generate a test runner that may be compiled so that the tests may be executed. This executable would then report which tests had passed, and which tests had failed. Further details on the features available, and instructions on how to install and use these libraries may be found at http:// www. cxxtest. com. We now explain why the tests given in Listing <u>9.3</u> are suitable for black box testing of both constructors, and the members `CalculateModulus` , `CalculateArgument` and `CalculatePower` . 

We begin by testing the default constructor. This constructor was written with the intention that both the real part and the imaginary part of a complex number created using this constructor should be initialised to zero. A suitable test for this constructor is to check that an instance of a complex number created using this constructor has zero modulus. Clearly this assumes that the method `CalculateModulus` correctly calculates the modulus of this complex number. As such, this test may be considered to also test the method `CalculateModulus` , albeit with a particularly simple input. This test may be found in 

lines 8–15 of the listing. Line 8 de�ines a test called `TestDefaultConstructor` . Line 12 then de�ines an instance of a complex number that is created using the default constructor, and line 13 calculates the modulus of this complex number. Finally, in line 14, we use the function `TS_ASSERT_DELTA` to test that the calculated modulus really is within of the true value of zero 

remembering, as discussed in Sect. <u>2. 6. 5, that two �loating point</u> numbers that should (mathematically) be equal may differ slightly due to rounding errors. 

The test between lines 17 and 34 is intended to test the customised constructor. This constructor allows an instance of a complex number to be generated initialising the real and imaginary parts to speci�ied values (lines 21–23). As the real and imaginary parts of the complex number are private members with no methods that allow us to access these members, we may only con�irm the real and imaginary parts of the complex number are correctly initialised by con�irming that both the modulus (lines 26–28) and the argument (lines 31–33) of the complex number are correct. We note that this test also allows testing of the members `CalculateModulus` and `CalculateArgument` . It is also worth noting that, as we are treating the class as a black box, we have not copied code from the original class and we are instead calculating the modulus and argument via independent means. 

Our next test is to test the member `CalculatePower` (lines 36– 60). In this test we use the customised constructor to create a complex number with non-zero real and imaginary parts (lines 40–42), and calculate the modulus and argument of this number (lines 43 and 44). We test `CalculatePower` by raising the original complex number to the power of 2, and calculating the modulus and argument of this squared complex number (lines 48–50). We then use properties of complex numbers to check that the modulus of the squared complex number is correct (lines 54 and 55) and that the argument of the squared complex number is correct (line 59). 

Our �inal test in this section is to test some of our functionality against a trusted complex number class `std::complex` (lines 61–77). The C++ library version of `std_z` , is initialised on line 64. Note 

that the `std::complex` is templated with a �loating point number type in angle brackets. Here we use `double` , to match the type of the private data in our own class, but the class also allows for complex numbers with are stored as `float` . Notice that the syntax of the functions on `std_z` is completely different to our own. Despite this, the mathematical speci�ication is the same and, consequently, we may perform the same tests on them in tandem. 





Using the black box testing above has given us some con�idence that the members of the class of complex numbers that have been tested have been implemented correctly. Note, however, that we have only used arbitrary choices to test these members. Were we to consider the implementation of these members we may discover some cases that could give unexpected results. We now discuss such an instance when describing white box testing. 

### **9.5.4 White Box Testing** 

In the class of complex numbers, the real part and the imaginary part of an instance of a complex number are both private members of this class. This made it dif�icult to black box test the customised constructor of this class in Sect. 9.5.3, where we create an instance of the class of complex numbers and simultaneously initialise both the real part and imaginary part to speci�ied values. The dif�iculty arose because, within the test we wrote, we were unable to access the private members of the class, and were therefore unable to test directly that these had been set to the correct values. Instead, we tested these values were correct indirectly by testing that the modulus and the argument of the complex number were correct. This, however, relies on the public methods used to calculate the modulus and the argument of a complex number being correct. Should the test of the customised constructor fail, we would not know whether the test failed because of an error in the customised constructor, or in one of the methods used to calculate the modulus and the argument of a complex number. This may be avoided by white box testing where, in contrast to black box testing, we inspect the implementation of the functionality offered by the class of complex numbers. We simply make the test suite in Listing <u>9.3</u> (which is a class) a friend of the class of complex numbers, allowing us to access—and test for correctness—the real and imaginary parts of a complex number. In Listing 9.4 we have given an example white box style test of the default constructor. This test may be used to replace the original test (lines 8–15 in Listing <u>9.3) provided that the test suite itself is given</u> access to the private members of the complex number class via “ `friend class ComplexNumberTestSuite;` ”. 



A second use of white box testing may be illustrated by creating an instance of the class of complex numbers using the default constructor. This default constructor will set both the real and the imaginary part of this complex number to zero. The modulus of this complex number is clearly zero. However, the argument of this complex number is given by `atan2(0.0,0.0)` . Mathematically, this is . As 0 / 0 is not 

de�ined, it is not immediately clear what the result of `atan2(0.0,0.0)` is. To �ind out, we visit the C++ reference page at <u>http:// www. cplusplus. com/ reference/ cmath/ atan2/ , where we</u> discover that a _domain error_ occurs ~~.~~ <u>1</u> This is to be avoided, and so we should update the method `CalculateArgument` given in Listing <u>6. 10</u> to take account of this special case. An appropriate course of action, that is followed by the scienti�ic computing environment M�����, is to set the argument of the complex number zero to 0. We leave the implementation, and testing, of this as an exercise. 

### **9.5.5 Test Driven Development** 

We have already recommended using test driven development to extend software. When using this technique we �irst write the tests that are required to test the new functionality, forcing us to be very clear about what we expect our modi�ied software to achieve. These new tests will clearly fail initially, as the new functionality does not yet exist. The new functionality will usually �irst require some refactoring of existing code, for example modifying an existing constructor to take account of extra data that is now associated with a class to implement the new functionality. If you have a well written and maintained suite of tests you can then run these tests to ensure that you haven’t broken any 

existing functionality. The new functionality is then added, and the tests originally written are run to ensure that the new functionality behaves as expected. 

For some applications of complex numbers—for example: the calculation of powers of complex numbers; investigation of the stability of a numerical method for solving initial value ordinary differential equations; and integration of complex numbers around poles—it is convenient to have access to the modulus and argument of a complex number. Rather than calculate these quantities every time they are used by using the methods `CalculateModulus` and `CalculateArgument` that already exist within the class of complex numbers, we could modify the class so that the class contains the private members `mModulus` and `mArgument` to represent these quantities. Should we do this, we would then have to decide whether to introduce the members `mModulus` and `mArgument` instead of the existing members `mRealPart` and `mImaginaryPart` , or in addition to these existing members. 

If we modify the class of complex numbers so that we include the private members `mRealPart` , `mImaginaryPart` , `mModulus` and `mArgument` we will have to modify other methods in the class so that all of these members are speci�ied whenever an operation is performed on an instance of the class. If we decide to only include the members `mModulus` and `mArgument` we will have to modify other methods in the class to specify these members, rather than `mRealPart` and `mImaginaryPart` , whenever an operation is performed on an instance of the class. Whatever choice is made, much of the existing functionality of the class will need to be altered. That is, we will have to refactor the code. This illustrates the importance of having a collection of well written unit tests that each cover a small fraction of the whole functionality. Should any of the existing functionality be broken when the code is refactored, at least one test should fail. The location of the error(s) should then be highlighted. 

We leave the implementation of this new functionality as an exercise. 

## **9.6 Tips: Writing Appropriate Tests** 

In this chapter we have attempted to convince you that an appropriate a collection of unit tests will increase the reliability and longevity of your software. These unit tests should each test a very small part of your code, and each line of software should be covered by at least one test. This testing strategy is, however, underpinned by the assumption that the tests are suitable. The following tips may help you to write appropriate tests, and to get the most out of this technique. 

1. 

Use a C++ testing framework library, such as `CxxTest` , `Boost.Test` or `googletest` . This will help you structure your tests. 2. 

Add one or more tests for every new piece of functionality, no matter how small the added functionality is. 3. 

Make tests de�initive—they should either pass or fail. However, beware of �loating point tolerances and allow for rounding errors in calculations. 

4. 

Remember to write tests for _corner cases_ . These are test inputs which may be rare, but might cause problems—collinear triangles, singular matrices, the complex number etc. 

5. 

Rather than spreading test input parameters randomly or evenly, it is more ef�icient to concentrate on the boundary between types of input. For example, if a test input `p` is supposed to be a probability (0 `p` 1) then check that `p` 1 gives the correct answer, but that `p` 1.0001 gives an error. 6. 

Review your tests from time to time. Add new tests as necessary and remove only those which you know to be redundant. 7. 

Automate your testing, so that you do not have to remember to run the tests or remember to check the results. 

**9.7 Exercises** 

**9.1** Extend the `Exception` class given in Listings 9.1 and <u>9.2</u> by creating two inherited classes `OutOfRangeException` and `FileNotOpenException` . Each of these two new inherited classes will derive from the `Exception` class in a similar manner to the way the `Ebook` class derived from the `Book` class in Sect. <u>7. 1. The constructors for each of the two</u> classes should take only the `probString` argument to set the `mProblem` member. Each constructor should ensure that the `mTag` member is automatically set in a similar manner to the way the `format` member was set in the constructor of the `Ebook` class. Write a catch block which is able to catch a generic exception but can also differentiate between these two types of error. 

## **9.2** 

An earlier tip in Sect. 4. 3. 2 showed how it was possible for bad memory allocation to terminate your program. If you want your program to continue through a memory allocation error there are two ways to cope with the exception: to turn the exception off (and check the value of the pointer) or to catch the exception. Here is some code which demonstrates how to turn off the exception message but still detect bad allocation of memory, without terminating the program. 



The proper way to deal with this issue is, of course, to catch the exception. Rewrite the code fragment above so that there is a `try` block around the line of code which attempts to allocate a large vector to `p_x` and demonstrate that you can catch this exception. [ _Hint: The name of the exception class which you need to catch is not_ `Exception` . _It is_ `std::bad_alloc` .] 

**9.3** In Exercise 7. 3 in Chap. 7, we developed a library for solving initial value ordinary differential equations. Let us suppose that the solution of the ordinary differential equation represents a probability of some event happening as time evolves. The true solution of this equation should therefore be nonnegative, and no greater than one. Of course, due to both rounding errors and errors induced by the numerical approximation used to calculate the numerical solution, this numerical solution may violate these restrictions slightly. In this exercise, we will suggest how to extend the library developed in Sect. <u>7. 3</u> to handle these requirements in a way that is consistent with the discussion of dealing with errors given in Sect. <u>9.2.</u> 

We will assume that an acceptable value for the absolute error is . When solving the differential equation, we therefore won’t be 

concerned if the solution for a value of _y_ in Exercise <u>7. 3</u> lies in the interval . Under these circumstances, we would simply 

write the value 0.0 to �ile containing the solution at each time _t_ instead of the value _y_ . Similarly, if the solution lies in the interval 



. we would write 1.0 to �ile rather than the value _y_ 

This is an instance of an error of type #1 in the list given in Sect. 9.2. Now suppose the value of _y_ lies further outside the range of 

acceptable values than can be attributed to rounding error. The most likely cause of this error is a step size _h_ that is too large. Under these circumstances, an exception should be thrown explaining this. The code that calls the library for solving initial value ordinary differential equations would then know to reduce the step size: a suitable new step size would be half of the step size currently being used. This is an instance of an error of type #2 in the list given in Sect. <u>9.2.</u> 

It is, of course, possible that an error has been made elsewhere in the library or in the code used to call the library. Under these circumstances persisting with making the step size smaller may not solve the problem. We therefore want to terminate the code if the step size _h_ falls below some critical value. This is an instance of an error of type #3 in the list given in Sect. 9.2. 

Incorporate the error handling procedure described above into the library for solving initial value ordinary differential equations developed in Exercise <u>7. 3</u> in Chap. 7. Test this error handling using the example initial value problem 



with initial condition when , for the time interval . Investigate how different values of the step size _h_ affect 

the error handling implemented. 

**9.4** In Sect. <u>9.5</u> we discussed how unit tests could be written for the class of complex numbers developed in Sect. <u>6. 4. In this exercise we will</u> complete the set of unit tests that we started in Sect. <u>9.5.3.</u> 

1. 

Extend the unit tests given in Listing <u>9.3</u> so that all the public methods in the class of complex numbers—listed in the header �ile given in Listing <u>6. 9—are tested using black box testing.</u> 2. 

The default constructor for the class of complex numbers initialises both the real and imaginary parts of an instance of a complex number to zero. We noted in Sect. 9.5.4 that the method 

`CalculateArgument` , as implemented in Listing <u>6. 10, will give a</u> domain error when applied to the complex number zero. By using white box testing, as described in Sect. 9.5.4, we suggested a suitable �ix for this problem. Implement this �ix, and write a test to ensure you have implemented this �ix correctly. 

3. 

Suppose we are writing a piece of software for investigating the stability of a given numerical method for solving an initial value system of ordinary differential equations. This software will require us to evaluate polynomial functions of a given complex number, and to con�irm that the modulus of a complex number is less than unity. We decide to implement this additional functionality by �irst modifying the class of complex numbers so that the class also contains the private members `mModulus` and `mArgument` that represent the modulus and argument of an instance of a complex number. In Sect. <u>9.5.5</u> we explained that we could add these members either in addition to the members `mRealPart` and `mImaginaryPart` , or instead of these existing members. 

In this exercise you should use test-driven development to implement the new functionality. First decide whether or not to include the existing members `mRealPart` and `mImaginaryPart` in addition to the new members `mModulus` and `mArgument` , and refactor the existing code as necessary. Having done that, introduce new functionality that uses the new members `mModulus` and `mArgument` to evaluate polynomial functions of a given complex number, and to determine whether the modulus of a complex number is less than unity. 

## **Footnotes** 

<u>1</u> 

If you were to use the C version of the trigonometry functions, rather than the C++ one, then you will �ind that `atan2(0.0,0.0)` gives no error and is de�ined to be 0. 

© Springer International Publishing AG, part of Springer Nature 2017 Joe Pitt-Francis and Jonathan Whiteley , _Guide to Scienti�ic Computing in C++_ ,  Undergraduate Topics in Computer Science <u>https://doi.org/10.1007/978-3-319-73132-2_10</u> 

# **10. Developing Classes for Linear Algebra Calculations** 

Joe Pitt-Franci ~~s~~ <u>1</u> and Jonathan Whitele ~~y~~ <u>1</u> 

(1) University of Oxford, Oxford, UK 



**Joe Pitt-Francis Email:** <u>joe.pitt-francis@cs.ox.ac.uk</u> 

In this chapter, we will apply the ideas introduced earlier in this book to develop a collection of classes that allow us to perform linear algebra calculations. We will describe the design of a class of vectors in the body of this chapter. The exercises at the end of the chapter will focus on developing this class further, developing a companion class of matrices, and developing a linear system class that allows us to solve matrix equations. 

## **10.1 Requirements of the Linear Algebra Classes** 

As explained above, we will develop a class of vectors called `Vector` , a class of matrices called `Matrix` and a linear system class called `LinearSystem` . The vector and matrix classes will include constructors and destructors that handle memory management. These classes will overload the assignment, addition, subtraction and multiplication operators, allowing us to write code such as “ `u = A*v;` ” where `u` and `v` are vectors, and `A` is a matrix: these overloaded operators will include checks that the vectors and matrices are of the correct size. The square bracket operator will be overloaded for the 

vector class to provide a check that the index of the array lies within the correct range, and the round bracket operator will be overloaded to allow the entries of the vector or matrix to be accessed using M����� style notation, indexing from 1 rather than from zero. 

The remainder of this chapter will focus on the development of a class of vectors. The header �ile for this class is given in Listing <u>10.1,</u> and the implementation of the methods is given in Listing <u>10.2. The two</u> variables that each instance of the class are built upon are a pointer to a double precision �loating point variable, `mData` , and the size of the array, `mSize` . We have made both of these private members of the class. We clearly need to write methods to both access and set values of the array. We shall insist that the size of the array is set through a constructor. As such, we shall not allow the user to change this variable through any method, but will write a public method that allows us to access the size of a given vector. 









The �iles required for the vector class are given above. These �iles may be downloaded from <u>https:// www. springer. com/ 9783319731315.</u> Subsequent sections of this chapter provide a commentary on why we have chosen to write the methods in the way in which they appear. 

## **10.2 Constructors and Destructors** 

In the tip given in Sect. 4. 3. 3, we encouraged the reader to ensure that, when dynamically allocating memory, every `new` statement was matched by a `delete` statement. We explained that if this is not done, then the code may consume large amounts of the available memory. Eventually the computer will run out of memory, preventing the code (and any other application running) from proceeding any further. We have repeated this tip on several occasions. Writing appropriate constructors and destructors for the vector and matrix classes allows us to automatically match a `delete` statement (through the calling of a destructor when the object goes out of scope) with every `new` statement (hidden from the user of the class in a constructor). We now describe appropriate constructors and a destructor for the class of vectors. 

### **10.2.1 The Default Constructor** 

We want a constructor for the `Vector` class to allocate the memory required to store a given vector when it is called. The default constructor takes no arguments, and therefore this constructor has no way of knowing how many entries the vector requires. As such, it cannot allocate an appropriate size to the vector, and so we ensure that a default constructor is never used by not supplying a default constructor. The automatically generated default constructor will not be available to the user because we are supplying an alternative specialised constructor. 

### **10.2.2 The Copy Constructor** 

Let us suppose we have an instance of the class `Vector` called `u` . If we were to use the automatically generated copy constructor to create another vector called `v` , then this constructor would _not_ perform the 

tasks that we require of the copy constructor. The member `mSize` would be correctly set. However, the automatically generated copy constructor would not allocate any memory for the new copy of the data, and so it would be impossible for the entries of the vector to be copied correctly. What would actually happen is that the pointer `mData` in the original vector `u` would be assigned to the pointer `mData` in the new vector `v` . As no new memory would be allocated, this would have the effect that `v` would simply become a different name for the original vector `u` : there would only be one vector stored, and changing the entries of `v` would therefore have the unintended effect of changing those of `u` , and vice versa. A further complication of not overriding the default copy constructor would be that, because two vectors alias their `mData` pointers with the same piece of memory, both vectors would attempt to de-allocate it (by calling `delete` in their destructor, see Sect. 10.2.4) when they went out of scope. 

What we actually want to happen when the copy constructor is called is for the member `mSize` of the new vector `v` to be set to the same value as for the original vector `u` . Memory should then be allocated for the new vector so that `v` has the same number of entries as `u` , and the entries of `u` then copied into the correct position in the new vector `v` . We therefore override the automatically generated copy constructor so that it sets the size of `v` to the size of `u` , allocates memory for the vector `v` of the correct size, and then copies the entries of `u` into `v` . 

### **10.2.3 A Specialised Constructor** 

We have supplied no de�inition for the default constructor to ensure that it is never used, and have overridden the copy constructor so that if we already have a vector we may create a copy of that vector. We also include a constructor that requires a positive integer input that represents the size of the vector. This constructor sets the member `mSize` to this value, allocates memory for the vector, and initialises all entries to zero. 

### **10.2.4 Destructor** 

The automatically generated destructor will delete the pointer `mData` and the integer `mSize` when an instance of the class `Vector` goes out of scope, but will not free the memory allocated to this instance of the class: this would be similar to not providing a matching `delete` statement for a `new` statement. We therefore override the automatically generated destructor to free the memory allocated for an instance of the class `Vector` when it goes out of scope. 

## **10.3 Accessing Private Class Members** 

In Sect. 10.1 we explained that we were going to make both the size of the vector, `mSize` , and the pointer to the entries of the vector, `mData` , private members of the class. This has the advantage that we can only set the size of the vector through the constructor (ensuring that this member is a positive integer, and preventing us from inadvertently changing it while a code is being executed), and allows us to perform a validation that the index of an entry of a vector is correct before attempting to access that entry. In this section, we explain how we have written the methods that allow us to access these private members. 

### **10.3.1 Accessing the Size of a Vector** 

The size, or length, of a vector is accessed through the public method `GetSize` . This member takes no arguments, and returns the private member `mSize` . 

### **10.3.2 Overloading the Square Bracket Operator** 

We overload the square bracket operator so that, if `v` is a vector, then `v[i]` returns the entry of `v` with index `i` using zero-based indexing. This method �irst checks that the index falls within the correct range— that is, a nonnegative integer that is less than `mSize` —and then returns a reference to the value stored in this entry of the vector. 

### **10.3.3 Read-Only Access to Vector Entries** 

The overloaded square bracket operator can be used for both reading data from the vector and for changing entries of the vector, through a reference. Since we may need to guarantee that some functions which 

read from a vector do not change it, we also supply a read-only `const` version. This public method `Read` is similar to the square bracket operator. It uses zero-based indexing and �irst checks that the index falls within the correct range and then returns a copy of the value stored in this entry of the vector. 

### **10.3.4 Overloading the Round Bracket Operator** 

The round bracket operator is overloaded to allow us to access entries of a vector using one-based indexing. We have chosen the round bracket operator for this purpose as this allows similar notation to that employed by Fortran and M�����, both of which use one-based indexing. In common with the overloaded square bracket operator described in Sect. <u>10.3.2, this method �irst validates the index before</u> returning the appropriate entry of the vector. 

## **10.4 Operator Overloading for Vector Operations** 

Readers with experience of programming in M����� will appreciate the feature of this system that allows the user to write statements such as “ `v = -w;` ” and “ `a = b + c;` ” where `v` , `w` , `a` , `b` , `c` are vectors of a suitable size. We will allow similar looking code to be written for the vectors developed in this chapter through operator overloading: i.e. we will de�ine the assignment operator, and various unary and binary operators. This will be very similar to the operator overloading for complex numbers in Sect. <u>6. 4. An additional feature required for the</u> class being written here is a check that the vectors are all of the correct size: this will be enforced using `assert` statements. 

### **10.4.1 The Assignment Operator** 

The overloaded assignment operator �irst checks that the vector on the left-hand side of the assignment statement is of the same size as the vector on the right-hand side. If this condition is met, the entries of the vector on the right-hand side are copied into the vector on the left-hand side. 

### **10.4.2 Unary Operators** 

The overloaded unary addition and subtraction operators �irst declare a vector of the same size as the vector that the unary operator is applied to. The entries of the new vector are then set to the appropriate value before this vector is returned. Note that in the example statement “ `v = -w;` ” above, it is the assignment operator’s responsibility to check that sizes of `v` and `w` match and the unary subtraction need do no error checking. 

### **10.4.3 Binary Operators** 

The overloaded binary operators �irst check that the two vectors that are operated on are of the same size. If they are, a new vector of the same size is created. The entries of this new vector are assigned, and this new vector is then returned. In the example statement “ `a = b + c;` ” above, it is the binary addition operator’s responsibility to check that the sizes of the vectors `b` and `c` match, but the assignment operator’s responsibility to check that the result can safely be assigned to `a` . 

## **10.5 Functions** 

A function to calculate the _p_ -norm of a vector is included in our class of vectors. See Sect. A. 1. 5 for a de�inition of the _p_ -norm of a vector. This implementation allows the user to call the function with an optional argument _p_ : if this is not speci�ied the default value 

(corresponding to the Euclidean norm) will be used. 

### **10.5.1 Members Versus Friends** 

We note that most functionality in the class is given via member methods and member operators. In order to calculate the 2-norm of a vector or to inspect its size, we must write “ `u.CalculateNorm();` ” or “ `u.GetSize();` ”, respectively. This may be considered a clumsy syntax by some users, especially those with experience of M�����, and so we provide an alternative `length` function to complement the `GetSize` method. The length function is declared as a _friend_ within the 

class which enables it to read the private `mSize` member. Note that whereas many of the members of the class are declared `const` at the end of the signature—to ensure they do not change the class itself—the length function guarantees that the vector which it is given as an argument will remain constant through making the argument a constant reference variable. 

## **10.6 Tips: Memory Debugging Tools** 

We stressed in a previous tip (Sect. 4. 3. 3) that every `new` should be matched with a `delete` . This is especially important when a program allocates memory within a loop. If a long-running program repeatedly allocates memory without de-allocating it, then eventually that program will unnecessarily occupy all the available memory of the computer. This problem—known as a _memory leak_ —will eventually cause the program to fail. 

There are memory-related problems other than memory leakage. The following code illustrates some common memory errors. The loop in lines 8–11 has an incorrect upper bound and thus the program attempts to write to `x[10]` which does not match the 10 elements allocated to `x` in line 3. The variable `z` is never initialised, which means that the �low of the program at the `if` statement on line 15 is unpredictable. The second `delete` statement—on line 23—is in error since it attempts to de-allocate memory which has already been de– allocated on the previous line. Finally, the memory for `y` which was allocated on line 4 is never deleted. 



The four problems in the program above will not prevent the code from being compiled. The program may also run as expected until the �inal `delete` statement, but crash at that point. So, in this program, most of the memory errors are undetectable in normal circumstances. 

These errors can be detected with a memory debugging tool such as the open source programs _Valgrind_ or _Electric Fence_ . These tools run an executable �ile while inspecting all the memory access calls. Some tools (such as Electric Fence) do this by replacing the usual memory libraries with ones which intercept the calls. Others tools (such as Valgrind) run the program inside a virtual machine and externally monitor the memory accesses—a slower process, but one which does not require recompilation of the program. 



**_Fig. 10.1_** Class collaboration diagram for PosDefSymmLinearSystem 

On running the program given in Listing <u>10.3</u> through Valgrind all four memory problems are detected. A summary of the Valgrind output is given below. 



## **10.7 Exercises** 

The exercises in this chapter guide you to build on the `Vector` class with an additional `Matrix` class. These classes are then combined into a `LinearSystem` class (or, in the �inal exercise, an alternative class derived from it) which has a method for solving systems of the form **Ax** = **b** for **x** . Example solutions for these classes are given in Sect. C. 1. Figure <u>10.1</u> illustrates a typical solution to these exercises with a collaboration diagram for all the classes produced by these exercises. This diagram uses the same UML syntax as Fig. 7. 1, as described in Sect. 7.2. 

The �iles `Vector.hpp` and `Vector.cpp` given in Listings <u>10.1</u> and <u>10.2, as well as the example</u> `Matrix` and `LinearSystem` classes given in Sect. <u>C. 1, may be downloaded from https:// www. springer. com/ 9783319731315.</u> 

## **10.1** Write a suitable suite of tests to black box test the class of vectors. 

**10.2** Make any improvements you might deem appropriate to the class of vectors. You might be helped in this task by the following list. 

- The assertions for the round bracket operator are almost identical to those of the square bracket operator and those of the `Read` method. Rewrite the `Read` method and one of these operators in such a way that they call the remaining operator (with a suitable offset, as necessary) and all the checks are given in one place. 

- There are many assertions in the class as it stands. These mean that it is very easy to write programs which terminate with a run–time error. Can you turn any of the assertions into exceptions or warnings (see Chap. <u>9)?</u> 

- Write an output operator for vectors using the pattern given in Sect. 6. 4 for the `operator` in the complex number class. 

**10.3** In this exercise, we will develop a class of matrices called `Matrix` for use with the class of vectors developed in this chapter. The class of matrices should include the features listed below. Your class should have private members `mNumRows` and `mNumCols` that are integers and store the number of rows and columns, and `mData` that is a pointer to a pointer to a double precision �loating point variable, which stores the address of the pointer to the �irst entry of the �irst row. See Appendix A for details of the linear algebra that underpins these operations. Use a 

## suitable testing strategy when developing this class. 

1. 

An overridden copy constructor that copies the variables `mNumRows` and `mNumCols` , allocates memory for a new matrix, and copies the entries of the original matrix into the new matrix. 2. 

A constructor that accepts two positive integers— `numRows` and `numCols` —as input, assigns these values to the class members `mNumRows` and `mNumCols` , allocates memory for a matrix of size `mNumRows` by `mNumCols` , and initialises all entries to zero. 3. 

An overridden destructor that frees the memory that has been allocated to the matrix. 4. 

Public methods for accessing the number of rows, and the number of columns. 5. 

An overloaded round bracket operator with one-based indexing for accessing the entries of the matrix so that, provided `i` and `j` are valid indices for the matrix, `A(i, j)` may be used to access `mData[i-1] [j-1]` . 

6. 

Overloaded assignment, unary and binary operators to allow addition, subtraction and multiplication of suitably sized matrices, vectors and scalars. You should use `assert` statements to ensure the matrices and vectors are of the correct size. 7. 

A public method that computes the determinant of a given square matrix. 

## **10.4** In this exercise, we will develop a class called `LinearSystem` that may be used to solve 

linear systems. Assuming the system is nonsingular, a linear system is de�ined by the size of the linear system, a square matrix, and vector (representing the right-hand side), with the matrix and vector being of compatible sizes. The data associated with this class may be speci�ied through an integer variable `mSize` , a pointer to a matrix `mpA` , and a pointer to the vector on the right-hand side of the linear system `mpb` . We suggest only allowing the user to set up a linear system through the use of a constructor that requires speci�ication of the matrix and vector: the member `mSize` may then be determined from these two members. If you do not wish to provide a copy constructor, then the automatically generated copy constructor should be overridden and made private to prevent its use. As with the class of vectors, we recommend that use of the automatically generated default constructor is prevented by providing a specialised constructor but no default constructor. A public method `Solve` should be written to solve this linear system by Gaussian elimination with pivoting, as described in Sect. <u>A. 2. 1. 3. This method should</u> 

return a vector that contains the solution of the linear system. 

Test your class using suitable examples. We suggest that you write a set automated tests in a testing framework such as `CxxTest` . An outline model test-suite for testing the linear algebra classes is given in Listing <u>C. 5</u> in Section <u>C. 1. When considering what to test think about</u> the following. 

- How you might test the various constructors. 

- How you will black box test solving problems when the matrix is poorly conditioned. 

- How to test that the Gaussian Elimination routine is performing pivoting when small values appear on the diagonal. How to test various `Matrix` and `Vector` methods. 

## **10.5** Derive a class called 

`PosDefSymmLinearSystem` (or similar) from the class `LinearSystem` that may be used for the solution of positive de�inite symmetric linear systems. Make the method `Solve` a virtual method of the class `LinearSystem` , and override this method in the class 

`PosDefSymmLinearSystem` so that it uses the conjugate gradient method for solving linear systems described in Sect. <u>A. 2. 3. If you declared</u> `LinearSystem` member data as `private` in the previous exercises, then this should now be declared `protected` . Your class 

`PosDefSymmLinearSystem` should perform a 

check that the matrix used is symmetric: testing that the matrix is positive de�inite would be rather dif�icult and so we don’t suggest performing a check for this property. Test your class using suitable examples. 

© Springer International Publishing AG, part of Springer Nature 2017 Joe Pitt-Francis and Jonathan Whiteley , _Guide to Scienti�ic Computing in C++_ ,  Undergraduate Topics in Computer Science <u>https://doi.org/10.1007/978-3-319-73132-2_11</u> 

# **11. An Introduction to Parallel Programming Using MPI** 

Joe Pitt-Franci ~~s~~ <u>1</u> and Jonathan Whitele ~~y~~ <u>1</u> 

(1) University of Oxford, Oxford, UK 



**Joe Pitt-Francis Email:** <u>joe.pitt-francis@cs.ox.ac.uk</u> 

This chapter serves as an introduction to the _Message Passing Interface_ (MPI), which is a widely used library of code for writing parallel programs on distributed memory architectures. It is not intended that you will learn much about parallel programming from reading this chapter—we would recommend that you use a dedicated textbook (such as those listed in the Further Reading section at the end of this book [9, 10]) or tutorial if you wish to gain a detailed knowledge. However, this chapter should give you a _basic guide_ to compiling and running parallel programs written using MPI. If you are likely to use a scienti�ic library built on MPI (such as PETSc1 ~~)~~ then what you learn here in this chapter should help to demystify some of the library calls, and enable you to begin to edit parallel programs written by other programmers. 

## **11.1 Distributed Memory Architectures** 

There are several ways of classifying parallel computers and parallel programs but the most basic one is that of _shared memory_ versus _distributed memory_ machines. In the shared memory architecture several processing units (often called “cores” nowadays), share access to a common pool of memory, as shown in Fig. 11.1. This architecture 

has the advantage that a part of a program running on one core can easily communicate with another, since it can read or write in the memory space of the other part of the program. Programming for shared memory can be quite easy and the programs are generally very quick, but historically shared memory machines have been expensive, require specialised hardware, and physical constraints limit the total number of cores. This situation is, however, now changing as most new desktop computers have two or more cores. 



**_Fig. 11.1_** A shared memory parallel architecture: the processors/cores are co-located and share a common memory 



**_Fig. 11.2_** A distributed memory parallel architecture: each processor has sole access to its local memory and the machines are connected on the same network 

The other main architecture commonly used for parallel programming is the distributed memory architecture (see Fig. <u>11.2) ,</u> where each processing unit has a local memory space where it can read and write with ease, but the memory of other processors is completely hidden. The processors are connected—allowing data to be communicated between processors—on a network which could be a dedicated fast switch network (in the case of a cluster computer) or could be the wider Internet. The existence of the network between the 

processing units means that programming for this architecture is likely to be more complicated, and that programs that rely heavily on communication between processors are likely to be slower. However, as we shall now explain, distributed memory programs are versatile. 

The versatility of distributed memory programs is evidenced by the fact that it is possible to take a program intended for a distributed memory architecture and run it on a shared memory architecture. In this case, the individual parts of the parallel program will have separate memory spaces within the shared memory system (so that they cannot directly access each others’ memory), but will be able to communicate via the memory system. Communication is therefore much faster than over a network. Distributed memory programs can readily be executed on shared memory machines and are fast, but are also memory-hungry. The reverse is not true: you cannot, in general, run a shared memory program on a distributed memory cluster ~~.~~ <u>2</u> 

You can even run distributed memory programs on a computer with a single processor. All the parallel processes will be run as what are known as individual _threads_ , and will communicate via the memory system with the operating system responsible for context switching between the threads. There is no performance advantage to doing this, since there is an overhead to run many threads on a single processor. The advantage is that you can write and debug a program on a lowpowered laptop, tune it on a shared memory desktop, and then deploy exactly the same program on a supercomputer. 

## **11.2 Installing MPI** 

MPI is actually a set of standards for performing distributed computing. The MPI-1 standard documents the primary core of MPI (basic pointto-point and collective communication) while the MPI-2 standard adds other useful but advanced features such as parallel �ile access (through the input and output operations provided by MPIIO) and remote memory access (one-sided communication). Because MPI is a set of open standards there are various implementations available to choose from. The most commonly used are the MPICH and Open MPI implementations. The current versions of MPICH and Open MPI 

(formerly LAM/MPI) both implement all the functionality in both the MPI-1 and MPI-2 standards. 

Both MPICH and Open MPI are open source projects, under active development and freely available to download. They may be run on a wide variety of machine architectures, operating systems and communication infrastructures. The Open MPI library implementation is currently available from major Linux distribution repositories and is therefore easy to install on Linux systems. It is con�igured so that it can be used either on a stand-alone system (in the manner of a sharedmemory system) or across standard Ethernet using the secure shell `ssh` protocol. 

## **11.3 A First Program Using MPI** 

Just as in Sect. 1. 2, we introduce the MPI library by using a program that prints the text “Hello World” to the screen. This time, it runs and prints in parallel. This simple example C++ MPI program is shown below. 

Before explaining the purpose of the individual statements in this program, we need to explain what we mean by the term _process_ . Loosely speaking a process is a part of a parallel program that may be executed independently of the other parts, provided that data can be communicated through MPI calls when required. As such, a process can be thought of as a component of the program that can be executed on one of the processors shown in Fig. 11.2. (However, we make a distinction between processes and physical processors—or cores— because it is possible to run multiple processes on a single processor.) If a code has _p_ processes, then each process is given a `rank` which is a unique integer in the range 0 rank < _p_ . 



There are several lines of the program above which mention MPI. The �irst of these is the extra include on line 2 which allows the program to see the full functionality of the MPI library. Subsequently, there are `MPI::Init` and `MPI::Finalize` statements on lines 6 and 12 which start and stop the parallel part of the code. All MPI calls must lie between these two statements. The method `Get_size` allows us to access the number of processes taking part in the program execution, and the method `Get_rank` allows us to identify the process which is executing a given statement. The `COMM_WORLD` object represents a communications group involving _all the processes_ running the current calculation. It is possible to split this communication group up into smaller groups so that subsets of the processes can share private data. 

It should be noted that all the calls to MPI in program above use calls to speci�ic C++ bindings to the MPI library. So `Finalize` is a function in the MPI _namespace_ (see Sect. B. 4) and `Get_size` is a method of the communication object `COMM_WORLD` . Some C++ programmers prefer not to use these bindings, but opt instead for the plain C functions `MPI_Init` , `MPI_Get_size` , etc. which have a slightly different syntax. Both versions are valid in C++ programs and can even be mixed. 

### **11.3.1 Essential MPI Functions** 

The functions `MPI::Init` and `MPI::Finalize` on lines 6 and 12 of Listing <u>11.1</u> are required calls in any MPI program. On line 6, `MPI::Init` is able to promote the program from a single executable to a parallel program running as several processes. In order to do this, it needs to know how many processes to launch and on which machines they should be run—as we shall see in Sect. 11.3.2 this is information that can be made available via command-line arguments. `MPI::Init` inspects the command-line arguments provided by `argc` and `argv` , acting on any it recognises. 

Some MPI implementations of `MPI::Init` update their arguments by removing those which have been acted upon. Therefore, if you want an MPI program to read some speci�ic arguments from the commandline for use in your calculation, the best place to do this is _after_ `MPI::Init` since, at that point, all MPI-speci�ic arguments have been read and updated as necessary. 

The `MPI::Finalize` makes sure that the program closes down neatly, closing any remote connections and terminating all processes. 

### **11.3.2 Compiling and Running MPI Code** 

So far when we have compiled C++ programs we have included code either from standard locations (through including �iles such as `cmath` ) or from other parts of our own code (such as `Book.hpp` ). MPI, as a _third-party library_ , is not part of the standard C++ distribution. 

Normally when you compile against a third-party library, you would have to include extra compiler �lags specifying the location of the header �iles, the location of the libraries themselves, and names of some of the library dependencies. This can be a little onerous. Added to this, on some large computing facilities there may be several versions of MPI available which make it possible to accidentally compile some of your program with one version, and the remainder of the program with another, possibly incompatible, version. To ameliorate these dif�iculties, the MPI distributions have provided “wrapper compilers” for C++ (as well as for C and Fortran). The wrapper compiler automatically adds the correct compiler �lags when it calls the actual compiler. The C++ MPI compiler on most systems will be called `mpiCC` , `mpic++` or 

`mpicxx` . It is probably the case that it exists with more than one synonym. 

The standard Linux distribution of the Open MPI package has an `mpiCC` compiler which is a wrapper to the GNU `g++` C++ compiler. To ensure that this compiler is installed, open a terminal window and type “ `which mpiCC` ” followed by return. Hopefully the computer will respond by reporting the location of this compiler, for example, 



To compile the code given in Listing <u>11.1, open a terminal window and</u> create a directory where code may be saved. Move into this directory, and save the code as “ `MpiHelloWorld.cpp` ”. The MPI wrapper compiler may have some compiler �lags of its own, but most �lags are passed on to the normal `g++` compiler. In the same directory type, 



It is possible (but uninteresting) to run the executable which you have just produced as a standalone program. That is, without any of the MPI machinery and with no code run in parallel. If this is the case then `Get_size` will return 1, and, because there is only one process, `Get_rank` on that process will return 0. Just as in array numbering, the process rank numbering starts at zero, so each process is given a unique integer rank in the range 0 rank < _p_ , where _p_ is the total 

number of processes. 



To run in parallel either on the same machine or across a network or cluster, use the `mpirun` command (also known as `mpiexec` on some MPI implementations). This command will, if necessary, launch a 

service (called a daemon) on all the machines involved in the calculation. It will then make sure that copies of the executable can be run on every machine. 

To run the program locally, use the “number of processes” `-np` �lag. 



To run the program across a network you can give a list of machines in a _host �ile_ , or alternatively list the machine names on the commandline. It is imperative that you have an account on the remote machines, that you are able to connect via `ssh` (preferably without being prompted for a password), that the machines have the same MPI implementation installed on them, and that they are capable of running the executable �ile which you are sending. In the example below, ranks 0 and 2 of a 3-process job are launched on remote machines. The rank 1 process will run on the local machine, from where the job has been launched. Note that in this case buffered output from the local machine has appeared on the screen before output which has been sent from the remote machines ~~.~~ <u>3</u> 



If you are running your program on a large cluster or a supercomputer, then it is likely that the program will be launched from a script via a queueing system. In this case, the locations of the processors available to you will be determined by the job queue manager. You should obtain detailed instructions from the system administrators about which arguments to give to the `mpirun` command in your script. 

## **11.4 Basic MPI Communication** 

While the parallel “Hello World” program used the MPI libraries, it did not make any use of the communication features offered by these libraries. More speci�ically, it did not do any _message passing_ , which is the main feature of MPI. In this section, we give a brief survey of some of the common communication patterns available in the MPI library through providing a sample of the large range of available function calls. 

### **11.4.1 Point-to-Point Communication** 

The essential part of MPI functionality is being able to send a single message between processes, where one process _sends_ while another process _receives_ . These two functions are called `Send` and `Recv` . Their function prototypes are: 



The `Send` method takes data on the current process from the location given by the pointer `buf` . These data are assumed to be in contiguous memory (as an array of `count` variables), but `buf` may be a pointer to a single variable. Note the `const` keyword next to the buffer argument: MPI is making a guarantee not to alter your data during the message sending. The `datatype` �ield tells the system what the type of the data is (so that the correct number of bytes are sent in the correct format). The last two arguments of the `Send` method give the destination process number (this is the _rank_ of the process we wish to send to) and a _tag_ . The message tag can be any nonnegative integer value and its purpose is to allow the user to easily identify the context of a message. Negative tag values are reserved by the library for special values such as `MPI::ANY_TAG` which is introduced below. 

The `Recv` method has the same basic arguments: a pointer to a buffer in which to store the message, an integer `count` that gives the expected number of items in the message, the data-type for these items, 

the rank of the source process which is sending the message and the tag value of a message. The receiver is allowed to use wild-cards for either the source of the message, or the message tag, or both. The wild-card `MPI::ANY_SOURCE` <u>4</u> is useful if, for example, we wish to receive all the results of one phase of computation (tagged with `phase_1_tag` , for example) before moving on to the next phase. Messages sent with the next tag ( `phase_2_tag` ) can then be queued until the receiving process is ready for them. The wild-card `MPI::ANY_TAG` is useful if we know which process is sending the data, but do not know what the tag will be. 

The corresponding MPI `Datatype` signatures for the types introduced in Chap. <u>1</u> are `MPI::BOOL` , `MPI::CHAR` , `MPI::INT` and `MPI::DOUBLE` ~~.~~ <u>5</u> There is no MPI type for strings because `std::string` is a C++ class rather than a plain data-type. It is possible to send entire C++ classes in MPI messages by using advanced programming features to introduce user-de�ined data-types, but this is not recommended. Classes can readily be transferred by packing the raw data into a message at one end and unpacking it into a waiting class at the other end. 

The following code fragment illustrates sending one message consisting of two �loating-point numbers from process 0 to process 1. Note that code involving point-to-point communication is necessarily nonsymmetric: both processes are running exactly the same program with the same code, but parts of the program which are intended only for one process are placed in speci�ic blocks guarded by their process rank. 



### **_11.4.1.1 Blocking and Buffered Sends_** 

The default means of sending point-to-point messages with `Send` and `Recv` represents one combination in a spectrum of available communication protocols. Both functions are known as _blocking_ functions because they do not allow the execution of the program to continue until it is safe to do so. The `Send` method not only guarantees that it will not change the contents of the data buffer, but that any subsequent changes to the data buffer will not affect the message that is being sent. So if computation is allowed to proceed from a `Send` call it either means that the message has already been delivered or that the data has been copied into another buffer ready for delivery. 

The default `Send` is a compromise between the safety of waiting to be sure that a message has been delivered and the ef�iciency of getting on with other tasks after sending the message immediately. The other send functions have similar function prototypes, but slightly different names. We brie�ly describe these send functions below: the interested reader should consult a dedicated MPI programming book (such as [9, 10]) for more details. 

The very safest, but possibly most inef�icient, means of sending a message is to use a _blocking_ synchronous send, `Ssend` . This function 

guarantees not to continue until the message has been delivered. This is a little like delivering a message by telephone conversation, because we cannot get on with our lives until the call has been made and the information has been relayed. 

- A slightly more con�igurable version is `Bsend` , the _buffered_ send. Like the plain `Send` , it allows the program to continue when safe, but this may happen faster since the message is copied to a separate buffer. This buffer must be supplied and con�igured by the user. At the top end of the spectrum, the most ef�icient means of sending a message is the _immediate_ send `Isend` , which returns control to the program immediately, whether the message has been delivered, buffered or not yet acted on. This is a little like communicating via SMS text message in which we are able to press “send” and get on with other things safe in the knowledge that the recipient will get the information some time soon. Because it may be dangerous to overwrite the original data contained in the message, MPI provides functions for testing whether or not the message has been delivered. The `Isend` command gives back a handle (called an 

- `MPI::Request` ) which has a `Wait` method: this method instructs execution to “wait here” until the message has been sent. There are a few other �lavours of `Send` including compatible combinations: an immediate send can make use of a user-supplied buffer using the buffered non-blocking combination `Ibsend` . 

The default `Recv` function is also one of a spectrum of functions. It is technically a _blocking_ function, because execution cannot continue until a suitable message has been received. There is also a _non blocking_ immediate receive `Irecv` together with some utilities for probing whether there are any queued messages which match certain sources or tags. This means that your program, rather than waiting for messages to be received, could get on with useful work, occasionally going back to check for new information. 

### **11.4.2 Collective Communication** 

Code for point-to-point communication is not symmetric: one process sends while another receives. MPI provides specialised collective calls in which all the processes take part by executing the same commands. 

There are several major different �lavours of these communication patterns: the combined send-receive (where every process sends a message to another, while also receiving a remote message); one-tomany operations such as _broadcast_ where data from one process are sent to the entire group; and many-to-one operations such as _reduction_ in which an operation is used to combine results from all processes into a single result. 

These collective calls have the advantage that they can be highly tuned in an MPI implementation to �it the local architecture. The broadcast of a single number to all _p_ processes from process 0 could be achieved by sending _p_ − 1 messages from process 0, one message to each of the recipients. However, if process 0 sends to only two processes who each send to two more, then the information is broadcast to all recipients in about log _p_ rounds of message sending. If 

a supercomputer consists of several multicore computers connected by Ethernet, then the broadcast algorithm can be tuned to minimise the number of Ethernet messages while possibly increasing the number of faster messages between cores in the same machine. 

### **_11.4.2.1 Barrier_** 

The simplest collective method is `Barrier` . It says that every process should wait here until all processes are ready to proceed. Barriers are useful when you are timing certain parts of the code, printing out information to the console, or debugging the code. In the following code example there is a `Barrier` at line 3, the purpose of which is to ensure that all processes have completed writing their output (from line 1) before they are permitted to proceed. 



### **_11.4.2.2 Combined Send and Receive_** 

There are many cases when we might wish to send and receive many point-to-point messages at the same point in a computation, and where 

#### every process should be involved. 

For example, consider solving a partial differential equation (PDE) using a �inite difference scheme over a regular grid (such a grid is illustrated in two dimensions in Fig. <u>12. 2) where the value of a variable</u> at one position on the grid depends on the value of that variable at a few neighbouring grid points. A similar example from a different �ield is that of image processing: many image processing �ilters, such as edge detection or blurring, are implemented as weighted averages of image intensities over a small patch of neighbouring pixels. Such problems may be readily parallelised by dividing the grid or image into a number of identical vertical (or horizontal) strips and assigning one strip to each parallel process. Each process can compute its partition independently, except at the edges where information at grid-points or pixels assigned to the neighbouring process is required. A way to provide this information is to keep a local copy of the required neighbouring grid-point data and to update these data from the neighbouring process by message-passing. The local copy of remote neighbouring data is called _halo data_ and the message passing process is called _halo exchange_ . 



**_Fig. 11.3_** Halo exchange between processes 

Halo exchange is demonstrated in Fig. <u>11.3</u> using the example of an image processing �ilter. This �ilter produces an image where the image intensity in the processed image at a given pixel is the average of the image intensities in the original image at �ive pixels: the pixel of interest; the pixel to the left; the pixel to the right; the pixel directly above; and the pixel directly below. The pixels allocated to process `n` are those in the shaded area in Fig. 11.3. We may calculate the processed image at the pixels represented by open circles in this shaded region using only pixel intensities stored by process `n` . Before we may calculate the �iltered image at the pixels represented by solid circles on the left edge of process `n` , however, we require access to the pixels represented by solid circles on the right edge of the pixels stored by process `n-1` : these pixels are referred to as the halo, and we need to copy these to process `n` before we can calculate the whole processed image. Similarly, the nodes along the left-hand boundary of process `n` must be copied to process `n-1` before the processed image may be calculated. This procedure of sending edge data in both directions between processes `n` and `n-1` is known as halo exchange. For the same reasons, two-way halo exchange is also required between processes `n` and `n+1` . 

The partitioning of data between processes should ideally minimise the amount of data that has to be passed in halo exchanges: this is important when �ine-tuning your code to produce optimum ef�iciency, but is beyond the scope of this book. 

For these types of problem, a more sophisticated version of pointto-point message passing is the combined send and receive, called `Sendrecv` . Its function prototype is: 



Note that the ten arguments are divided into two sets of �ive: a set of send arguments about the outgoing message and a set of receive arguments about the incoming message. These are similar to the arguments given to the point-to-point versions in Sect. 11.4.1 and they are interpreted relative to the _local process_ : if each process is sending to the rank above, by symmetry, each must be receiving from the rank below. It is possible to mix the types of messages (both in terms of `DataType` and the length of the messages) so that, for example, oddranked processes are sending integer messages to the process above, but even-ranked processes are sending double precision �loating point data. In this circumstance, on any given process the types of send and receive data will differ. As with the `Recv` functions, we can use the wild-cards for the source process identity and the received message tag. 



**_Fig. 11.4_** Message passing between processes in a ring using combined send-receive 

The following code shows all processes communicating in a ring. Each process (with rank given by the variable `rank` ) sends a message to its right-hand neighbour ( `rank` + 1). Modular arithmetic—see Sect. 1. 4. 3—ensures that the `left_rank` and `right_rank` variables are set inside the range rank < num_procs so that the top-most 

process is able to send a message to the rank 0 process. This message passing is illustrated schematically in Fig. <u>11.4</u> for four processes: the arrow indicates the direction in which the message is passed. 



There are cases, such as the halo exchange situation outlined above, where _nearly every_ process will send halo data from the right-hand edge of its domain up to the next process to become a left-hand halo, but the top-most process does not need to send any data and the bottom-most process needs no left-edge halos. This is illustrated in Fig. <u>11.5</u> where four processes are taking part in the communication with the arrows indicating the direction in which information is passed. In a separate send-receive event the left-edges would also be sent down the chain to become right-edge halos, but again there is no need to send data from the bottom-most process. For this reason, MPI provides a special process name `MPI::PROC_NULL` which means that this process does not participate with a send and/or receive. This process name is illustrated in the following code, which is similar to the previous `Sendrecv` example, except that there is no closed loop: the top-most process does not send to process 0. 



**_Fig. 11.5_** Message passing between processes in a chain using combined send-receive. On process 3 the message destination is set to `PROC_NULL` 



### **_11.4.2.3 Broadcast and Reduce_** 

The collective operations broadcast and reduce are primarily one-tomany and many-to-one operations. In a broadcast ( `Bcast` ) operation, data from one process are shared with all other processes in the communication group. In a reduction operation all the data is concentrated to a single process. This reduction operation is likely to be of one of a standard set available for numerical data ( `MPI::MAX` , `MPI::MIN` , `MPI::SUM` , and `MPI::PROD` ). There are other prede�ined reduction operations available including some bit-wise operations, and there is also opportunity to de�ine extra operations. The prototype signatures of the broadcast and reduce operations are given below. Note that the argument `root` is the _source_ of the broadcast but the _destination_ of the reduction. MPI also provides a many-to-many reduction operation `Allreduce` which may be thought of as a reduction operation followed by a broadcast to all processes. 



An example reduction operation is given in Sect. <u>11.5.1</u> where the partial sums of a series are summed together in a single reduction step. For now, here is a broadcast example in which one process—process 0 —mimics throwing three dice by generating integer random numbers from 1–6 inclusive, and broadcasts the results of all three throws. Each process then adds their own rank to the value shown on the �irst die, and a reduction operation reports on the maximum value attained after this operation. 



### **_11.4.2.4 Scatter and Gather_** 

The scatter and gather operations are extensions to broadcast and reduction operations. They are the most advanced operations which we cover in this book, and we do so because the gather operation is useful for taking data which has been distributed across processes and 

_concentrating_ it onto a single process. For example, if a vector is split across processes in a similar manner to a PETSc vector we might wish to write it to a �ile using a single write operation using only one <u>6</u> process ~~.~~ 

The scatter operation `Scatter` is similar to the broadcast operation in that it is one-to-many with one process being responsible for sending the message to all other processors. Unlike the broadcast operation, where the same entries of data (of size `count` ) are sent to all processes, the �irst `count` elements are send to the �irst process, the next `count` to the next and so on. MPI also provides a scatter for variable sized data (where the `count` size can be different for different destinations) which is called `Scatterv` . 

The gather operation is similar to the reduce operation in that it is many-to-one with each process contributing some data to the result. The difference is that the data is not reduced but rather it is _concatenated_ . If each process contributes `count` elements of data, then the gathering process must have space to store `count` multiplied by `num_procs` elements. There is a variable-sized data version of the gather, `Gatherv` in which the numbers of elements contributed per process may be different. MPI also provides `Allgather` and `Allgatherv` in which the result of the gather ends up on all the processes involved in the communication. These may be thought of as a regular `Gather` or `Gatherv` operation followed by a broadcast. 

Below are the prototype signatures of the scatter and gather operations. For completeness we also give the signature of `Allgatherv` since we will demonstrate the use of `Allgather` and `Allgatherv` in Sect. <u>11.5.2.</u> 



Most of the arguments in the above methods should be readily understood, since they are similar to the arguments of the previous less advanced methods. The argument `root` always refers the scatterer (sender) or to the gatherer (receiver). In most cases, the _types_ and _counts_ of the send and receive data should be identical, with the counts referring to the size of the array sent to (or received from) each process. In the variable size gather, the `int` array arguments `recvcounts` and `displs` are used to communicate the variable data counts and displacements for each process (so `recvcounts[rank]` should be equal `sendcount` for that process). The value `displs[rank]` contains the index in the gathered array `recvbuf` where the data from process `rank` should begin. There is some redundancy between the counts and displacements since one might expect the displacement of each process’ data to be equal to the sum of the counts of the data from lower ranked processes. However, this redundancy allows there to be gaps in the gathered data. 

## **11.5 Example MPI Applications** 

In this section, we give two examples of parallel programs written with MPI. The designs of the parallel algorithms shown here are not unique to the problems which they solve. In general, the choice of parallel algorithm depends on how it relates to an equivalent sequential 

algorithm (if there is one) and how the data is partitioned. One usually seeks to partition the data and computation between the processes in such a way that communication between processes is minimised and that the processes are given an equivalent amount of computational work. The task of giving the processes the same amount of work is known as _load balancing_ . 

However, merely giving each process a similar amount of work is no guarantee of a successful parallel algorithm if the combined computational load of parallel processes is much more than that of the sequential program, or if communication dominates the program. The measures of success in producing parallel programs are _parallel speedup_ and _parallel ef�iciency_ . The _parallel speedup_ is the ratio of the time it takes to run the code sequentially on a certain problem to time it takes to run on _p_ processes . In an ideal case, a problem can 

be partitioned such that it is well load balanced with minimal extra overhead, so we expect _S_ . Parallel ef�iciency scales this value by _p_ : 



so that _E_ is generally in the range from 0 to 1 with 1 being 

the ideal value. It is uncommon, but not unusual, for a particular problem to scale in parallel such that _E_ > 1. This fortunate situation normally arises when a given problem has memory constraints when run on a small numbers of processes and it is known as _super-linear speedup_ . 

### **11.5.1 Summation of Series** 

The summation of a series can be taken as an _abstraction_ of a range of problems in which it is moderately easy to partition work between processes and there is minimal communication. Such problems are termed _embarrassingly parallel_ . In the following example, the calculation is trivial but this case is representative of tasks which are possibly more labour intensive, such as Monte Carlo integration (see Exercise <u>11.4).</u> 

Consider the problem of summing a series, such as the approximation to 



credited to Gottfried Wilhelm Leibniz. Given that we cannot compute the sum to in�inity, we approximate this summation with a �inite sum from to for some value _max_ (which may be 

assumed to be divisible by the number of processes, _p_ ). In dividing the _max_ contributions between the processes evenly, we might choose to allocate this work in blocks, so that the �irst _max_ / _p_ contributions to the series go to process zero, and so on, or we might distribute in such a way as to interleave processor contributions. In the following example, the contributions are interleaved. Note that the only parallel communication needed in this code is a reduction operation, which combines the subtotals from the processes into a grand total for the entire calculation on process 0. 



**11.5.2 Parallel Linear Algebra** 

In this section, we give an outline of the operations required for performing parallel linear algebra operations. It is beyond the scope of this book to provide a complete parallel linear algebra library, but we outline some of the issues arising when we design such a system. A fundamental question to ask is how matrices and vectors might be partitioned across the processes. We choose to use the matrix-row partitioning (which will be described later) favoured by the PETSc library—although other parallel linear algebra systems, such as Mondriaan, use more sophisticated techniques. 

We begin by discussing parallel implementation of the product between a matrix and a vector of suitable sizes. Using the matrix-row partitioning scheme, the matrix-vector product **v** = **Au** where **A** is a matrix, and **u** , **v** are vectors of length _N_ , can be partitioned in 

such a way that the �irst _N_ / _p_ rows of matrix **A** are only known to process 0, as are the �irst _N_ / _p_ elements of the vectors **u** and **v** . If we are performing a simple matrix-vector calculation using row-wise partitioning over 3 processes then it can be see from the schematic 



that in order for process 0 to compute the �irst _N_ / _p_ elements of **v** it is required to know only the �irst _N_ / _p_ rows of **A** (which are held locally) and _all_ the elements of **u** (most of which are not local to process 0). More generally, in order to solve the linear system **Ax** = **b** using an iterative approach (such as the conjugate gradient method described in Sect. A. 2. 3) there are a limited number of operations which will be needed: 

- scalar-vector multiplication—an operation on locally-held data; vector-vector addition and subtraction—operations on locally-held data; 

- a vector Euclidean norm—a sum of squares on local data, followed by a global sum of squares (a parallel reduction), followed by a squareroot; and 

- matrix-vector multiplication—in which, as outlined above, data from the vector must be communicated between all the processes. 

We illustrate an implementation of this fashion of parallel linear algebra by giving a bare-bones working `MpiVector` class. This class contains the features listed below, which will aid building a parallel conjugate gradient solver. 

- On constructing a vector of size _N_ , the components are automatically distributed between _p_ processes. Each process is assigned _N_ / _p_ elements. This division may be rounded down so that there will be a shortfall in cases where _p_ does not divide _N_ . This shortfall is picked up by the top–most process. Each process holds `mSize` elements corresponding to indices in the range `mLo mHi` . 

- There is an overloaded `[]` operator for accessing elements of the vector. This operator converts between a _global index_ into the vector and the _local index_ into the process’ private data. Any out-of-range indexing trips an assertion. 

- Helper methods `GetHi` and `GetLo` enable the caller to probe the range of locally held data, thus ameliorating the fact that the partitioning code is hidden from the caller which would make it easy to trip index violation assertions. 

- There is a `CalculateNorm` method which calculates the 2-norm (see Sect. A. 1. 5) by calculating a local sum of squares, using reduction to sum the local sums into a global sum, and taking the square root. Note the use of `Allreduce` which ensures that the result of the reduction (and therefore of the norm) is available to all processes. There is a method `UpdateGlobal` for _gathering_ all elements of the vector from the remote processes. 

The method `UpdateGlobal` uses more than one gather operation as introduced in Sect. 11.4.2.4, and gathers the entire vector into private storage on every process. The �irst two gather operations assemble information about the number of locally held data and their 

displacements. These operations are here to illustrate a common use of �ixed- and variable-sized gathers but they are redundant for multiple reasons: (i) the sizes and displacements are �ixed in constructor and do not need to be re-calculated on every communication, (ii) the sizes and displacements are not independent—one can be calculated from the other, (iii) the algorithm for calculating sizes and displacements in the constructor is quite simple and could be repeated here. 





**11.6 Tips: Debugging a Parallel Program** 

We have discussed debugging sequential code in Sects. <u>1. 7</u> and 7. 7. Message passing clearly introduces the potential for different errors to be inserted into your code. We discuss some methods for debugging parallel programs below. 

### **11.6.1 Tip 1: Make an Abstract Program** 

As with sequential programming, it is very rare for a programmer to begin building a parallel program from scratch. In many cases, you may be given a sequential program which has been written by someone else, or you may be starting from your own program. At such times, it is hard to see the communication patterns underlying the parallel code—they can easily get lost in the details of the calculations. 

Our advice is to �irst take the time to design a rough idea of the communication patterns needed in your new parallel program, and then start afresh. Write a simpli�ied _abstract program_ which concentrates on the communication, but neglects the main calculation. This will give you the opportunity to ensure the safe working of the parallel communication in the absence of details of the particulars. Once the message passing is working correctly, it can easily be integrated into the main code. 

### **11.6.2 Tip 2: Datatype Mismatch** 

In the following code, copied incorrectly from Listing <u>11.2, the process</u> 0 block has been amended so that the type of the data is now `int` and the message is sent as `MPI::INT` . However, this change has not been re�lected in the code for the receiving process where the message is received as `MPI::DOUBLE` . 



The message passing in this program may work correctly—in terms of the communication pattern—but the data received on process 1 will probably be incorrect. This may be because of mismatches in the _size_ of the data (on most architectures `int` uses 32 bits whereas `double` uses 64 bits) or it may be due to errors in the _conversion_ of the data. 

Problems where message data types (or sizes) do not match can be hard to see, especially when the send and receive components are in separate methods or in separate �iles. 

### **11.6.3 Tip 3: Intermittent Deadlock** 

_Deadlock_ is the technical term for the situation in which all processes are waiting for some event to happen before proceeding but no process can supply that event because they are waiting for another process. This situation is illustrated simply by four cars arriving simultaneously at a junction where the traf�ic signals have failed: with nothing to tell them how to proceed all four drivers play safe and wait for someone else to make the �irst move. In most cases, it is possible to �ind code which causes deadlock by heavily instrumenting the program, that is, by printing out lots of information and �lushing the output. We will 

deliberately induce deadlock in Exercise <u>11.2</u> by never receiving any sent messages so that eventually the sender is not able to proceed because it is unable to send any more messages. 

Problems involving _intermittent deadlock_ are harder to diagnose. These are situations where the program deadlocks on some runs of the code but runs normally on others. Perhaps the program runs without encountering problems with some trivial example test input, but when it is fed with the real-life input it then deadlocks. When this happens, it is an indication that the problem is to do with the size or timing of messages. In Exercise <u>11.2</u> we demonstrate that small amounts of data can be buffered—which hides the fact that a non-buffered blocking send would produce deadlock—but large amounts of data cannot be buffered. In other words, for a given program there may be sizes and timings of messages where deadlock happens, and some where it does not happen. 

In such situations, a good strategy is to concentrate on those situations most likely to deadlock. We make our program less ef�icient and more likely to deadlock by removing buffering and asynchronous messages: replacing all instances of `Send` with `Ssend` . Once all message passing is synchronous it is likely that the intermittent deadlock has become predictable deadlock, allowing us to identify the problem and debug the code. A program can also be made “more synchronous” by splitting calculation steps up with barriers. The program can later be made more ef�icient as necessary. 

### **11.6.4 Tip 4: Almost Collective Communication** 

It is common to treat process zero as a “master process”, orchestrating the tasks of the other processes, reducing data for output to the screen, and gathering information from all processes for output to a single �ile. In these circumstances, it is usual to have some blocks of code or some methods which are only executed by the master process and some which are only executed by the “slave processes”. 

In Sect. 11.4.2.4, we gave the example of an output pattern in which all data was _concentrated_ onto a single process before being written to disk. In this case, process zero may execute a block of code consisting of receives and writes to disk via an `ofstream` , whereas the other processes execute a block consisting of the matching send commands. 

When debugging parallel code, it is usually a good idea to add barriers in order to break the program into manageable sections. However, if we were to add barriers into the slave processes’ block of sending code, this would be a recipe for instant deadlock. Since all processes _except one_ are executing this code, then any collective communication on `MPI::COMM_WORLD` cannot complete. If collective communication is necessary in this code, then a new communication group (including all processes in `MPI::COMM_WORLD` except rank zero) must be created. New communication groups can be created using relevant MPI functions such as `MPI_Comm_split` (see MPI documentation for more details). 

## **11.7 Exercises** 

**11.1** Amend the `MpiHelloWorld` program in Listing 11.1 so that the processes print in reverse rank order. You can do this with a down-loop over processes and a barrier. Beware that if your implementation of MPI buffers output then you might not be able to verify that your process is working correctly! 

Assuming that your loop for output is correct, now modify it to do _round robin_ �ile output. Instead of writing process ranks to `std::cout` each process in turn should: open a named �ile, write the rank information to it and close the �ile. The second process to write (and those subsequent) should not open the �ile until the previous process has closed it and should open the �ile in append mode (see Sect. 3. 2). 

Investigate the `MPI::Wtime` method (which returns a highprecision time, with units of seconds, since some �ixed point of time in the past) and use it to time the program on each process. Use `Reduce` to compute the average duration of the program over all processes. 

**11.2** The MPI standard allows the `Send` library call to behave either like a buffered send or like a blocking send. In practice, all implementations of the MPI standard treat `Send` the same way. If the message is small enough (and there is space), then it is copied into a private buffer, and the MPI library is delegated to ensure that the message is delivered and the program �low continues— similar to `Bsend` . If the message is large (or if that private buffer is full), then delivery of the message must wait until the recipient is ready for it, so the program �low waits—similar to `Ssend` . 

Write an MPI program where the master process has one loop which attempts to send larger messages each time, and then prints how big the message was. We suggest that you double the size of the message on each iteration. All other processes should do nothing. We suggest that you have an array of length _at least_ a million items, to make sure that there is always something to be sent. Eventually you should observe deadlock. 

**11.3** Write an MPI code following the instructions below. This code is to be executed with only two processes, and tests the use of MPI for transferring vectors of data between processes. 

De�ine an array `V[10][10]` to store the entries of a matrix. The process with rank 0 initialises its copy of the array to 



while the process with rank 1 initialises its copy of the array to 



This choice provides a convenient way of identifying, from the value of the entry of `V` , where it has come from in the original arrays, and from which process: the three-digit value `xyz` will be row `y` , column `z` from process `x` . 

- Transfer the data stored in the �irst row of the matrix stored by process 0 into the corresponding positions in the matrix stored by process 1. This involves process 0 sending the data using `Send` , and process 1 receiving the data using `Recv` . One way of doing this on the sending side is to �irst copy the data into a buffer vector of suitable length and then send this vector. Similarly, on the receiving side receive it into a buffer vector of suitable length and then copy it into the appropriate part of `V` . Print out the contents of the array `V` stored by process 1 to check that you have correctly sent the data. Repeat the transfer of the �irst row of data without copying into a buffer on the sender or copying from a buffer on the receiver. Repeat the transfer of data sending both the row with index 5 and the row with index 8 between the processes. Transfer the �irst _column_ of data between the processes. 

**11.4** The aim of this exercise is to get you started on writing algorithms with collective communications. The exercise asks you to develop a parallel algorithm for calculating an approximation to using Monte Carlo integration. Suppose we want to approximate the integral 



where _f_ ( _x_ ) is a continuous function de�ined at all points in the closed interval . If are independent random variables uniformly distributed on the interval , where _N_ is suf�iciently large, then Monte Carlo integration allows us to approximate the integral by 



Noting that 



we will use Monte Carlo integration to estimate through 

approximating the integral on the right-hand side of this equation. Sequential code for this is given below. 

The random numbers are generated through the random number generator `rand` (line 18), and seeded through `srand` (line 11). The random number generator requires the `cstdlib` header to be included. The random number generator is seeded differently on every run: in this exercise you will develop this code to run on a distributed memory machine through use of MPI statements, and you don’t want a set of parallel computers to all work on the same set of “random” numbers. 



Compile the program and it should print out an answer similar to 



In the exercises below, we will add MPI function calls to enable this code to be run in parallel. 1. Add MPI function calls so that `n_points` function evaluations are performed on each of the MPI processes. 2. Estimate through reducing the result of function evaluations ( `sum` ) from each processor to a global sum on process 0 and scaling appropriately. This is similar to the summation of a series in Sect. 11.5.1. 3. 

Amend the code so that process 0 selects a value of `n_points` for each of the processes at the beginning program. Pass these values out in a scatter operation. 

**11.5** Write classes to enable parallel linear algebra based on the row-wise matrix partitioning —and the `MpiVector` class—given Sect. 11.5.2. Your goal for this exercise should be to perform a matrix-vector multiplication in parallel. 1. 

Add as much functionality and overloaded operators from the `Vector` class given in Sect. <u>10. 1</u> to `MpiVector` as you wish. Include any improvements which you may have made to `Vector` as part of Exercise <u>10. 2.</u> 

2. 

The `MpiVector` constructor contains an assertion that the ideal local size (number of local vector elements) should be nonzero. This guards against the case when the number of processes is larger than `vecSize` , in which case the current code in the constructor would assign the entire vector to the top-most process. Fix this situation so that when there are fewer vector elements than processes every process is assigned either one or zero elements. 3. 

Make it possible to set elements on remote processes. A suitable scheme would be to construct the vector in “set up” mode, during which requests to add values to remote elements are stored for later. A user is able to call a method `FinishSetUp` which communicates the stored data between processes, puts the vector in a “usable” mode and bars future attempts to set remote data. 4. 

Remove some of the redundant calculations performed by `UpdateGlobal` mentioned in Sect. 10. 1. 5. 

Write an output method which uses `UpdateGlobal` such that one process is able to print the entire vector to screen or to �ile. 6. 

The `UpdateGlobal` method relies on memory for the private data member `mGlobalData` being allocated in the constructor. Since the `mGlobalData` is only required for output or for a matrix-vector product, the memory for `mGlobalData` ought to be allocated on demand. Make sure that there is also a method for de-allocating this memory when it is no longer needed. 7. 

Write an `MpiMatrix` class using the scheme outlined in Sect. <u>10. 1. It is</u> important that you treat the partition on the number of matrix rows in exactly the same way as the vector partition, so that local sizes are always compatible. Perform a matrix-vector multiplication in parallel and output the solution. 

## **Footnotes** 

<u>1</u> 

The Portable Extensible Toolkit for Scienti�ic Computing (PETSc, pronounced “pet see”) is a library providing functionality for the solution of linear and nonlinear systems of equations on both sequential and parallel architectures. 

<u>2</u> 

There are several programming libraries which allow the programmer access to a _distributed shared memory_ computer where machines over a network act as if they were part on one contiguous system. There has, however, not been wide-spread use of these libraries at the time of writing. 

##### <u>3</u> 

MPI implementations vary in how they return console input from the individual processes to the console from which the program was launched. Even when `flush` is called on the `cout` stream it may still be the case that the MPI machinery is buffering output. 

##### <u>4</u> 

`MPI::ANY_TAG` and `MPI::ANY_SOURCE` are C++ names for these wild-card values. Many codes use the interchangeable C names: `MPI_ANY_TAG` and `MPI_ANY_SOURCE` . 

##### <u>5</u> 

Note that these are the C++ object names for these types—they are also called synonymously by their C names: `MPI_BOOL` , `MPI_CHAR` , `MPI_INT` and `MPI_DOUBLE` . 

##### <u>6</u> 

There are a few standard ways of getting data to �ile from a parallel program: _concentration_ , where one process does all the writing, as suggested above; _round-robin_ where processes take it in turns to open and close the same �ile; _parallel �ile libraries_ such as MPI’s MPIIO; and _separate �iles_ where 

each process writes data to different places to be re-assembled later. The choice of output method is largely dependent on the data structure and size. 

© Springer International Publishing AG, part of Springer Nature 2017 Joe Pitt-Francis and Jonathan Whiteley , _Guide to Scienti�ic Computing in C++_ ,  Undergraduate Topics in Computer Science <u>https://doi.org/10.1007/978-3-319-73132-2_12</u> 

# **12. Designing Object-Oriented Numerical Libraries** 

Joe Pitt-Franci ~~s~~ <u>1</u> and Jonathan Whitele ~~y~~ <u>1</u> 

(1) University of Oxford, Oxford, UK 



**Joe Pitt-Francis Email:** <u>joe.pitt-francis@cs.ox.ac.uk</u> 

Having developed classes that underpin linear algebra operations in Chap. <u>10</u> we now demonstrate how to construct object-oriented libraries for scienti�ic computing applications that utilise the functionality of these classes. We use the speci�ic example of developing a library that uses the �inite difference method to solve boundary value, second order differential equations. 

We begin by developing a library for problems in one spatial dimension that are linear, constant coef�icient, second order, boundary value ordinary differential equations. That is, equations of the form 



(12.1) where _A_ ( 0), _B_ , _C_ , _X_ , _X_ (with ) are given constants, _f_ ( _x_ ) is a given function, and suitable boundary conditions are given at and . We choose to use the �inite difference method to underpin 

the library as this method for calculating the numerical solution of differential equations is the simplest to explain, and a method that many readers will be familiar with. This allows us to focus on the 

_implementation_ of this method, without a need to explain more technical aspects of the method from a mathematical viewpoint as would be the case with more sophisticated techniques such as the �inite element method. Having discussed how to develop a library for this class of equations we conclude this chapter by brie�ly touching upon how a library for computing the numerical solution of Poisson’s equation may be constructed. For ease of explanation, we limit ourselves to a two-dimensional rectangular domain, and apply only Dirichlet boundary conditions, that is, the following partial differential equation: 



where _X_ , _X_ , _Y_ , _Y_ are speci�ied constants with 



is a speci�ied function, and _u_ is speci�ied at 

each point on the boundary. As partial differential equations may be beyond the mathematical scope of some readers, this section is entirely self-contained: the remainder of this chapter may be read independently of the material in Sect. <u>12.3.</u> 

The emphasis of this chapter is to explain the object-oriented structure that may be used when developing a library for solving differential equations. We describe the functionality required from the classes that we use, but give very little detail on the implementation of these classes: implementation of the ideas presented uses C++ techniques introduced in earlier chapters, and is the focus of the exercises at the end of the chapter. The mathematical theory of the �inite difference method is not discussed in much detail. Readers unfamiliar with this technique should consult a suitable text such as Iserles [1], Kreyszig [2], or Süli and Mayers [3]. 

## **12.1 Developing the Library for Ordinary Differential Equations** 

When developing software, it is useful to know precisely what type of problems are to be solved using this software. We therefore begin by 

de�ining two exemplar model problems that contain all features commonly seen in linear, constant coef�icient, boundary value ordinary differential equations. We then explain the mathematical theory behind the �inite difference method for these boundary value problems, before concluding this section by explaining how to utilise the theory when developing the library. 

### **12.1.1 Model Problems** 

We use two example model problems to motivate the development of the library. These model problems have a known solution and can therefore be used to give some veri�ication of the correctness of the output of the library. The �irst model problem is very simple, whilst the second model problem is more complicated and uses all the features that we will include in our library for ordinary differential equations. 

**_Model Problem 1_** _._ 

The �irst model problem is the following boundary value problem: 



This problem has solution 



This is a very simple problem—we have the minimal number of terms in the differential equation, and only very simple Dirichlet (i.e., nonderivative) boundary conditions. 

**_Model Problem 2_** _._ 

The second model problem is a more complicated differential equation, with one Dirichlet boundary condition, and one Neumann (derivative) boundary condition. This model problem satis�ies the following equation and boundary conditions: 



This differential equation has solution 



### **12.1.2 Finite Difference Approximation to Derivatives** 

We now de�ine the notation used for the �inite difference approximations to the �irst and second derivative of a function of one variable. Where we de�ine a derivative at _N_ distinct points, we will denote these points using subscripts starting at 1 and ending at _N_ for consistency with the overloaded parenthesis operators used when writing the classes of vectors and matrices developed in Chap. <u>10.</u> Let us suppose that a function _u_ is de�ined on the interval . Suppose further that there is a collection of points that satisfy 



We will refer to the points as the _�inite difference grid_ , and the individual points as _nodes_ . The nodes and are referred to as the _boundary nodes_ of the �inite difference grid, whilst all other points are referred to as _interior nodes_ . We may evaluate the function _u_ at each node , which we denote by : 



The �irst derivative of a function at a given node may be thought of as being the “slope” of the function at that point: i.e. the ratio of the change in _u_ to the change in _x_ . In Fig. 12.1 we motivate three different approximations to the �irst derivative at which are de�ined in 

Table 12.1. Note that not all of these approximations are de�ined at the boundary nodes of the �inite difference grid, that is, at and 





**_Fig. 12.1_** Backward �inite difference ( _broken line_ ), forward �inite difference ( _dotted line_ ), and central �inite difference ( _dot-dashed line_ ) approximations to the �irst derivative of the function represented by _the solid line_ at the point 



**_Table 12.1_** Numerical �inite difference approximations to the �irst derivative at 

|**Type**|**Formula**|**Range**|
|---|---|---|
|Backwa<br>rd|||
|Forward|||
|||− 1|



|**Type**|**Formula**|**Range**|
|---|---|---|
|Central|||
|||− 1|



A numerical approximation to the second derivative, not de�ined at the boundary nodes of the �inite difference grid, and , is 



which may be written 



(12.2) where 













This approximation to the second derivative follows from Taylor series expansions: see, for example, Kreyszig [2]. We note that when there is a uniform spacing between the nodes, that is, 



, for some constant _h_ , then the 

approximation to the second derivative given in Eq. (12.2) may be simpli�ied to the more familiar formula 



When developing our classes we will use the approximation given in Eq. (12.2) as it allows more generality. 

### **12.1.3 Application of Finite Difference Methods to Boundary Value Problems** 

We now explain how the �inite difference approximations given in Sect. 12.1.2 may be used to calculate a numerical solution of the model problems given in Sect. 12.1.1. For both problems we use the �inite difference grid with _N_ nodes described in Sect. 12.1.2. There are therefore _N_ unknown values of _u_ to determine. We will demonstrate 

how to set up a linear system of size _N_ that allows us to calculate these values. 

### **_12.1.3.1 Model Problem 1_** 

Substituting the approximation to second derivative given by Eq. (12.2) into the differential equation at the interior nodes of the �inite difference grid yields 



(12.6) The boundary conditions imply that 



(12.7) 

Equations (12.6) and (12.7) may be combined and written as the linear system **Au** = **b** , where **A** is a _N N_ matrix, and **u** and **b** are vectors of 

length _N_ . The entries of **A** , **u** and **b** are then given by 





Now that we have written the model problem as a linear system, we may use the methods associated with the vector, matrix and linear system classes to solve this system and calculate the values of . 

### **_12.1.3.2 Model Problem 2_** 

We now write model problem 2 in matrix form. At the interior nodes of the �inite difference grid, we use a central approximation to the �irst derivative, as de�ined in Table 12.1, and the approximation to the second derivative given by Eq. (12.2). The differential equation may then be approximated by, for 



(12.8) The boundary condition at may be implemented in the same way as the Dirichlet boundary conditions in model problem 1, that is, we write 



(12.9) The Neumann (derivative) boundary condition at requires a bit more thought. We see from Table 12.1 that the only one of these approximations to the �irst derivative that is de�ined at the node _x_ is 

the forward approximation. We therefore use this approximation and implement this boundary condition by setting 



(12.10) : De�ining, for the quantities 



we may write Eqs. (12.8)–(12.10) as the linear system **Au** = **b** , where the entries of **A** and **b** are given by 



As with model problem 1 we may now use the linear system class already written to solve this linear system. 

### **12.1.4 Concluding Remarks on Boundary Value Problems in One Dimension** 

We have now explained how to write the �inite difference approximation to a linear, constant coef�icient, second order boundary value problem in matrix notation, thus allowing the classes of vectors, matrices and linear systems developed in Chap. <u>10</u> to be used to calculate the �inite difference approximation. In the next section, we will describe an object-oriented structure that allows a very general library for solving such problems to be developed. We should, however, discuss the limitations of this library. 

Suppose we want to solve the following equation: 



This has solution _u_ = sin _x_ , and it may be thought that the library we are writing may be used to solve this problem. However _u_ = _A_ sin _x_ , where _A_ is any constant value, satis�ies the differential equation and both boundary conditions: that is, the solution is not unique. 

The equation above has a non-unique solution. It is also possible that an equation of the form Eq. (12.1) has no solution. For example, consider the equation 



It can be shown that this equation, together with these boundary conditions, has no solution. 

Proof of existence and uniqueness of solutions to boundary value differential equations is beyond the scope of this book. Nevertheless, the reader should be aware when using this library that some equations have solutions that are not unique, and solutions do not exist for other equations. 

## **12.2 Designing a Library for Solving Boundary Value Problems** 

To calculate a numerical solution of the boundary value ordinary differential equations discussed above, we may specify the problem by specifying individually: (i) the ordinary differential equation and the interval on which the solution is valid; (ii) the boundary conditions; and (iii) the �inite difference grid. Classes will be written for these three entities, called `SecondOrderOde` , `BoundaryConditions` and `FiniteDifferenceGrid` . These will then all be members of a class `BvpOde` that encapsulates a boundary value ordinary differential equation, and contains all the functionality required for the numerical solution of the differential equation. We now discuss the individual classes. 

### **12.2.1 The Class** **`SecondOrderOde`** 

To specify the ordinary differential equation, we need to specify the coef�icients on the left-hand side of Eq. (12.1), the function on the righthand side of this equation, and the interval on which the equation is valid. These will all be made members of the class `SecondOrderOde` . To ensure that all of these are speci�ied, we will only allow a user to use a constructor that speci�ies all of these members. In the exercises at the end of this chapter, we will discuss developing other constructors. A header �ile for this class is given below. 



**12.2.2 The Class** **`BoundaryConditions`** On the left boundary, we may specify either the value of the function _u_ (a left Dirichlet boundary condition), or the derivative (a left 

Neumann boundary condition). It is important to note that there must be _either_ a left Dirichlet boundary condition _or_ a left Neumann boundary condition: we must have one of these boundary conditions 

but we cannot have both. Similarly, on the right boundary we must have _either_ a right Dirichlet boundary condition _or_ a right Neumann boundary condition. In the class `BoundaryConditions` , we will declare class members `mLhsBcIsDirichlet` , `mRhsBcIsDirichlet` , `mLhsBcIsNeumann` , `mRhsBcIsNeumann` that are Boolean variables, thus allowing us to check that we have precisely one boundary condition on the left–hand boundary, and precisely one boundary condition on the right boundary. The default constructor should be overridden to set these variables to the value “ `false` ” in the absence of any other instruction. Whatever type of boundary conditions are set, values for these are needed at either end of the interval. These class members are called `mLhsBcValue` and `mRhsBcValue` . Finally, we require methods to set these values, and set the appropriate Boolean variable to the value “ `true` ”. The method `SetLhsDirichletBc` takes a double precision �loating point variable as input. It sets the member variable `mLhsBcValue` to this input, and sets the Boolean variable `mLhsBcIsDirichlet` to the value `true` . The methods `SetRhsDirichletBc` , `SetLhsNeumannBc` and `SetRhsNeumannBc` perform similar tasks. 

The header �ile `BoundaryConditions.hpp` is shown below. 



### **12.2.3 The Class** **`FiniteDifferenceGrid`** 

The �inite difference grid requires access to the interval on which the equation is valid, given in the class `SecondOrderOde` . To create a uniform grid, we also need speci�ication of the number of nodes. To ensure that the number of nodes is speci�ied, we only allow use of a constructor that sets this through a constructor argument. A vector of uniformly spaced nodes can then be generated. We create a class `Node` that stores the coordinate of each node. Header �iles for the classes `FiniteDifferenceGrid` and `Node` are given below. 





### **12.2.4 The Class** **`BvpOde`** 

Now we have described the classes `SecondOrderOde` , `BoundaryConditions` and `FiniteDifferenceGrid` we may develop the class `BvpOde` . We only allow this class to be instantiated through a constructor that speci�ies: (i) an instance of the class `SecondOrderOde` ; (ii) an instance of the class `BoundaryConditions` ; and (iii) the number of nodes to be used in the �inite difference grid. Once these entities have been speci�ied we 

then create an instance of the class `FiniteDifferenceGrid` , a vector that will contain the solution, a vector that will be on the right– hand side of a linear system, and a matrix associated with the linear system. Methods will then be written to populate both the matrix and the vector associated with the linear system, and to apply the boundary conditions, as discussed in Sect. <u>12.1.3. Finally, methods will be written</u> to solve the linear system, and to write the solution to �ile. A header �ile `BvpOde.hpp` is given below. 





### **12.2.5 Using the Class** **`BvpOde`** 

When using the classes introduced above, we would like to write code such as that in Listing 12.6 to calculate a numerical solution of the model problems given in Sect. 12.1.1. This will form the basis for the exercises at the end of this chapter. 



**12.3 Extending the Library to Two Dimensions** In this section, we assume that the reader is familiar with partial differentiation: that is, if a differentiable function _u_ ( _x_ , _y_ ) depends on the variables _x_ and _y_ then _partial derivatives_ with respect to both _x_ and _y_ may be calculated. Readers unfamiliar with partial differential equations may wish to skip this section or consult a suitable text on mathematical methods such as Kreyszig [2]. 

In the previous section, we designed a library for calculating the �inite difference solution of linear, constant coef�icient, second order, boundary value ordinary differential equations. We will now explain how a library may be developed for the �inite difference solution of Poisson’s equation in two spatial dimensions on a rectangular domain, with Dirichlet boundary conditions, that is, equations of the form 



where _X_ , _X_ , _Y_ , _Y_ are speci�ied constants, _f_ ( _x_ , _y_ ) is a speci�ied 

function, and boundary conditions for _u_ are given at each point on the boundary of the rectangular domain speci�ied. 

### **12.3.1 Model Problem for Two Dimensions** 

As with ordinary differential equations earlier in this chapter, we will use a model problem to demonstrate the implementation of the �inite difference method. The model problem that we will use is 



(12.11) 















This model problem has solution 



### **12.3.2 Finite Difference Methods for Boundary Value Problems in Two Dimensions** 

To de�ine the �inite differences that approximate the partial derivatives of a function in two dimensions, we �irst need to de�ine a �inite difference grid. We have already stated that we are assuming that the function _u_ that is to be determined satis�ies a partial differential equation de�ined on the region . We now suppose that there are points , and such that 



The nodes of the �inite difference grid are then the points ( The boundary nodes are the nodes where or . All other nodes are 

interior nodes. An example mesh on the square 0 < _x_ < 1, 0 < _y_ < 2 is shown in Fig. 12.2, where the �illed circles denote the boundary nodes, and the open circles denote the interior nodes. 



**_Fig. 12.2_** A suitable �inite difference grid in two dimensions. Boundary nodes are denoted by a _�illed circle_ , interior nodes by a _hollow circle_ 



**_Fig. 12.3_** Node _i_ and points used to calculate �inite difference approximations in two dimensions 

Numbering of the nodes for a �inite difference grid is slightly more complicated in two dimensions than it was in one dimension. For the �inite difference grid in one dimension all nodes could be numbered consecutively, allowing the �inite difference approximations to be written down in an intuitive way. To write down �inite difference approximations in two dimensions, we will adopt the “compass point” notation shown in Fig. 12.3. The node immediately above node _i_ in the computational mesh is denoted by _i_ , _N_ , where “ _N_ ” corresponds to north. The other nodes that are adjacent to node _i_ are the _east_ , _south_ and _west_ nodes, denoted by “ _i_ , _E_ ”, “ _i_ , _S_ ” and “ _i_ , _W_ ” respectively. 

Provided _i_ is an interior node, the four adjacent nodes shown in Fig. <u>12.3</u> all exist. Finite differences to the derivatives that appear in Poisson’s equation are given below. 

(12.16) 







We will now explain how these �inite difference approximations may be used to set up a linear system to calculate the numerical solution of Poisson’s equation. 

**12.3.3 Setting Up the Linear System for the Model Problem** We will now apply the theory developed in Sect. <u>12.3.2</u> to the model problem described in Sect. <u>12.3.1. Using the �inite difference grid</u> described in Sect. <u>12.3.2, we have</u> _M_ nodes in the _x_ -direction, and _N_ nodes in the _y_ -direction: that is, a total of _M N_ nodes. Each of these 

nodes has an unknown value of _u_ , and so our linear system comprises _M N_ equations, with each equation being associated with one node of 

the mesh. 

At interior nodes we may substitute the �inite difference approximations given in Eqs. (12.16) and (12.17). Substituting these approximation into Eq. (12.11) and rearranging yields 



(12.18) where 



The value of _u_ at each boundary node is given by the appropriate equation from Eqs. (12.12)–(12.15). This may be incorporated into the linear system by the equation 



(12.19) where _i_ is a boundary node, and _b_ is the value that _u_ takes at that node. 

Equations (12.18) and (12.19) fully de�ine the linear system. We may now use the functionality of the classes of vectors, matrices and linear systems developed in Chap. <u>10</u> to calculate the value of the �inite difference approximation to _u_ at each node. 

### **12.3.4 Developing the Classes Required** 

We give only minimal guidance on developing the classes required for calculating a numerical solution of Poisson’s equation. Designing and implementing these classes is left as an exercise (Exercise <u>12.4). Our</u> suggestions are given below. 

Creating an instance of the class `FiniteDifferenceGrid` should require the use of a constructor that speci�ies the number of nodes in the _x_ direction and the number of nodes in the _y_ direction. The grid should consist of a vector of boundary nodes that are all instances of the class `BoundaryNode` (discussed below) and a vector of interior 

nodes that are all members of the class `InteriorNode` (also discussed below). Each of the nodes in the mesh should have a global numbering that will refer to the row number of the matrix that will . correspond to the unknown value of _u_ at that node, _u_ 

- An instance of the class `BoundaryNode` will have an integer representing the global numbering, and a double precision �loating point variable that represents the value of _u_ at that node from the boundary conditions. 

- An instance of the class `InteriorNode` will have an integer representing the global numbering, and the global numbers of the north node, east node, south node and west node: see Fig. <u>12.3</u> for a de�inition of these nodes. 

The classes described above, together with a class for encapsulating the partial differential equation that is similar to `SecondOrderOde` in Sect. 12.2, should enable code to be written to calculate the numerical solution of Poisson’s equation. 

## **12.4 Tips: Using Well-Written Libraries** 

In Chap. <u>10</u> we developed a linear system class that was based on classes of vectors and matrices. These classes allowed us to perform various linear algebra operations. In this chapter, we utilised these classes to allow us to develop libraries for calculating the numerical solution of boundary value ordinary differential equations. 

Although the classes developed in Chap. <u>10</u> do have suf�icient functionality for the purpose of this chapter, we would recommend that a reader who requires a linear algebra library should consider using one of the many high quality, open-source libraries that are available. (Indeed, in Sect. 1. 1. 2, we gave the fact that there is a wealth of numerical libraries for scienti�ic computing as one of the reasons for learning C++.) Libraries for linear algebra usually include signi�icantly more functionality than that developed here including, for example: sparse matrices; a wide variety of iterative linear solvers; a wide variety of preconditioners; interfaces with other packages; and support for parallelisation. Indeed, as linear algebra is such a fundamental topic at the core of scienti�ic computing, it is unlikely that any functionality 

required will not be included in a widely used library. Furthermore, such libraries have the advantage of being well-tested, optimised code and can, as such, be treated as a black box. 

One open-source library that is of particular use is the Portable Extensible Toolkit for Scienti�ic Computing (PETSc, pronounced “pet see”) which is available for download from https:// www. mcs. anl. gov/ <u>petsc/. Libraries such as PETSc include an extremely large amount of</u> functionality for systems of both linear and nonlinear equations, with support for parallel implementation on distributed memory architectures through the MPI library. 

We conclude this section by reminding the reader of our the remarks in Sect. <u>1. 1. 4. We explained in that section that this book</u> focuses on aspects of the C++ programming language that are commonly needed when writing software for scienti�ic computing applications. As such, we haven’t touched on the functionality of the language that is rarely required in this �ield. Should readers wish to develop their C++ skills to use more advanced features we have given a list of suitable references in the Further Reading at the end of this book [5–10]. 

## **12.5 Exercises** 

**12.1** Develop the classes described in Sect. 12.2 for second order, constant coef�icient, linear boundary value ordinary differential equations. Test these libraries using the model problems described in Sect. <u>12.1.1. The code in Listing 12.6</u> which produces output �iles that can be readily plotted may be used as a framework. Example solutions for this problem are given in Sect. C.2: these �iles, together with the header �iles given in 

## this chapter, may be downloaded from <u>http:// www. springer. com/ book/ 9783319731315.</u> 

Make sure that the `BvpOde` method `WriteSolutionFile` does not attempt to write a �ile if `mFilename` is uninitialised or set to an empty string. (This may be achieved by setting `mFilename` to a safe value in the constructor.) 

**12.2** Extend the library developed in Exercise 12.1 so that the user may specify a nonuniform �inite difference grid. Allow this to be done through a method `SetGrid` of the class `FiniteDifferenceGrid` that allows a mesh to be speci�ied as a vector of ordered nodes. Ensure that the boundary nodes have the same value as `mXmin` and `mXmax` in the class `SecondOrderOde` . 

**12.3** Some programmers may feel that the constructor given in Listing 12.1 is inadequate. They may argue that it would be easy to incorrectly assign one of the coef�icients of the equation. One way around this would be to force the user to use a default constructor. Additional class members, such as a Boolean variable `mCoeffOfUxxIsSet` could be deployed. The default constructor would be overridden so that 

these variables were set to `false` when the constructor was called. A method called `SetCoefficientOfUxx` would then be written, which would have as input the coef�icient of . This method would assign the coef�icient correctly and set the Boolean variable `mCoeffOfUxxIsSet` to `true` . Before the methods that calculate the numerical solution are called a check would be carried out to ensure that all required data has been assigned. Design, and implement, classes to specify the differential equation in this way. 

**12.4** If you understand the theory for �inite difference methods for Poisson’s equation given in Sect. <u>12.3.2, develop a library for solving such</u> equations. Test this library using the model problem described in Sect. <u>12.3.1.</u> 

**12.5** Exercise 12.1 asks you to develop the classes described in Sect. <u>12.2</u> and to test these libraries using the model problems described in Sect. <u>12.1.1. For this purpose Listing 12.6</u> gives a program `Driver.cpp` . This way of “testing” is not ideal because it relies on the manual step of 

## checking that the data in the output �iles matches the expected solution. 

Automate the process of testing the classes described in Sect. <u>12.2</u> by rewriting the testing functionality within a testing framework such as `CxxTest` . For each model problem you should produce a testing function which runs the problem, reads the output �ile back into a suitable data structure, and tests that the solution is correct: that is, the solution is close to the analytic form given in Sect. <u>12.1.1. Think about</u> what the expected error might be for this numerical scheme. An example solution to this problem is given in Listing <u>C. 9</u> in Sect. <u>C. 2.</u> 

## **Appendix A** 

## **Linear Algebra** 

This appendix summarises the linear algebra that underpins the classes of vectors and matrices developed in this book. We present little more than the algorithms used: a reader interested in a deeper understanding of this theory should consult a textbook such as one of those listed in the Further Reading section at the end of this book. 

### **A.1 Vectors and Matrices** 

For the purpose of this book, a vector is a one-dimensional array and a matrix is a two-dimensional array: it is—of course—possible to work only with matrices, with vectors having either only one column or only one row. For consistency with the classes of vectors and matrices developed, we treat vectors and matrices as separate entities in this discussion. 

In this Appendix, we use mathematical rather than C++ notation for vectors and matrices.We will use italics to denote a scalar. Vectors will be denoted by lower case bold font letters. Individual entries of a vector will be denoted by italics indexed by subscripts. For example, **v** represents a vector, and the entry of **v** with index _i_ is denoted by . For 

consistency with C++ coding, we index the vectors and matrices in this Appendix so that the indices begin from 0. We assume that all vectors are column vectors: that is, a vector **v** of length _N_ is the vector 



If a row vector is required, it is denoted using the transpose superscript, that is, . Matrices will be denoted by upper case bold 

font letters, with italics indexed by subscripts used to denote the entries of the matrix. The �irst index corresponds to the row number 

and the second index corresponds to the column number. Using this notation, if **A** is a matrix, then the entry of **A** that appears in the row with index _i_ and the column with index _j_ is denoted by . Where 

required for clarity, we will separate the indices by a comma, for . example 

A square matrix of size _N_ has both _N_ rows and _N_ columns. The identity matrix of size _N_ is a square matrix, denoted by , with entries given by 



### **A.1.1 Operations Between Vectors and Matrices** 

_Linear combinations of vectors_ . Suppose , where **u** , **v** , **w** are all vectors of length _N_ , and are scalars. The entries of **w** are given by 



_Linear combinations of matrices._ Suppose , where **A** , **B** , **C** are all matrices with _M_ rows and _N_ columns, and are scalars. The entries of **C** are given by 



_Multiplication of a matrix by a vector._ Suppose **A** is a matrix with _M_ rows and _N_ columns, and **u** is a vector of length _N_ . If **v** = **Au** , then **v** is a vector of length _M_ with entries given by 



Similarly, if **s** is a vector of length _M_ and , then **t** is a vector of 

length _N_ with entries given by 



_Multiplication of a matrix by a matrix._ Suppose **A** is a matrix with _L_ rows and _M_ columns, and **B** is a matrix with _M_ rows and _N_ columns. If the matrix **C** satis�ies **C** = **AB** , then **C** has _L_ rows and _N_ columns, and has entries given by 



_The transpose of a matrix._ Suppose **A** is a matrix with _M_ rows and _N_ columns. If the matrix **B** satis�ies , then **B** has _N_ rows and _M_ columns with entries given by 





A matrix **A** is said to be symmetric if 

### **A.1.2 The Scalar Product of Two Vectors** 

Suppose **v** and **w** are both vectors of length _N_ . The _scalar product_ between **v** and **w** , denoted by , is given by 



(A.1) 

### **A.1.3 The Determinant and the Inverse of a Matrix** 

The simplest way to specify the determinant of a square matrix of general size is to use recursion. <u>1</u> Suppose **A** is a square matrix of size _N_ . The determinant of **A** , denoted by , may be written 



where the square matrix , of size , is the matrix **A** with row _i_ and column _j_ removed. This de�inition allows us to express the determinant of a square matrix of size _N_ as a sum of determinants of square matrices of size . This process may be repeated 

recursively until the determinant is expressed as a sum of determinants of square matrices of size 1. To complete this de�inition, we need to de�ine the determinant of a square matrix of size 1: under these conditions . We leave it to the reader to verify that this 

de�inition is consistent with the commonly used expressions for the determinant of matrices of sizes 2 and 3. 

If the determinant of a square matrix **A** of size _N_ is nonzero, then **A** — is said to be _invertible_ : a unique inverse matrix—denoted by exists, and satis�ies 



For the square matrix **A** of size 2 given by 



then provided the determinant, given by is nonzero, exists and is given by 



### **A.1.4 Eigenvalues and Eigenvectors of a Matrix** 

Suppose **A** is a square matrix of size _N_ . The scalar is said to be an eigenvalue of **A** if 



If is an eigenvalue of _A_ then a family of nonzero vectors <u>2</u> **v** that satisfy exists: each **v** in this family is then said to be an . _eigenvector_ corresponding to the eigenvalue 

### **A.1.5 Vector and Matrix Norms** 

Suppose **v** is a vector of length _N_ . The _p_ -norm of **v** , denoted by , is given by 



(A.2) Taking the limit as , this de�inition yields 



Of most use is the 2-norm: this is known as the Euclidean norm, and corresponds to the length of the line that represents a vector in two or three dimensions. Using Eq. ( <u>A.1</u> ), and Eq. ( A.2 ) with , we see that we may write the 2-norm as 



The _p_ -norm of a matrix **A** , denoted by , is given (in terms of the vector _p_ -norm) by 



In common with vector norms, the most commonly used norm is the 2- norm. It can be shown that the eigenvalues of the matrix are all real and nonnegative. Let be the largest of these eigenvalues. Then 



### **A.2 Systems of Linear Equations** 

Many algorithms in scienti�ic computing require the solution of linear systems of the form **Ax** = **b** , where: (i) **A** is a square, invertible matrix of size _N_ ; (ii) the vectors **x** , **b** are both of length _N_ ; (iii) **A** , **b** are known; and (iv) **x** is to be calculated. Clearly **x** satis�ies . However, 

calculating is extremely computationally expensive for large _N_ and this approach is rarely used to solve systems of linear equations. Instead a plethora of techniques are available: we list three relatively simple methods below. 

### **A.2.1 Gaussian Elimination** 

Readers may remember being taught how to solve two simultaneous linear equations for unknown values of _x_ and _y_ at school. When using this technique, the �irst step is to eliminate one of the variables resulting in a single linear equation for a single variable that can easily be solved. The value of this variable is then substituted back into one of the original equations to allow the value of the other variable to be calculated. Gaussian elimination is a systematic extension of this technique when solving a system of _N_ linear equations for _N_ unknowns. There are two versions of Gaussian elimination: with or without pivoting. We now describe both of these versions. 

### **_A.2.1.1 Gaussian Elimination Without Pivoting_** 

The original system of equations may be written 



Let us �irst assume that . This is a very restrictive assumption: in Sect. <u>A.2.1.3</u> we introduce _pivoting_ , which allows us to deal with the case . The assumption allows us to eliminate from 

all but the �irst equation: this is achieved by subtracting a suitable multiple of the �irst equation, and results in the following system: 



where: 



Assuming now that , we may repeat this process to eliminate 



from all but the �irst two equations: 



where: 



Providing that at all steps we have , we 

may continue in this fashion until we have generated an upper : triangular matrix 



Solving this upper triangular system is a straightforward task: we start with the last equation in this system and work our way backwards. The �irst two steps in this procedure are 



. A general formula exists for calculating Assuming that we have already calculated , we may calculate by 



(A.3) 

This completes the description of the Gaussian elimination algorithm without pivoting. A very important point to note is that there is no need 

to store all the matrices generated during this algorithm: only the most recently generated version is required, and all earlier matrices may be discarded. 

### **_A.2.1.2 LU Decomposition_** 

The Gaussian elimination process described above may be used to factorise **A** as the product of a lower triangular matrix **L** and an upper triangular matrix **U** , that is, **A** = **LU** . De�ining the matrices 

by 



we may write 



or, equivalently, 



We �irst note that the inverses of the matrices , are simply 



These matrices are all lower triangular. It is trivial to prove that the product of lower triangular matrices is also lower triangular. Writing 



we see that we have **A** = **LU** with **L** a lower triangular matrix and **U** an upper triangular matrix. An explicit representation of **L** exists: direct calculation may be used to verify that 



**_A.2.1.3 Gaussian Elimination with Pivoting_** The Gaussian elimination technique described above required that at each step. Clearly this algorithm would fail for a nonsingular 

matrix such as 



where 



and so , violating one of the assumptions made in Sect. <u>A.2.1.1</u> . 

We can, however, proceed further: in this case we would simply interchange the last two rows of both and . This is known as 

_pivoting_ . Even if is not zero it may be advisable to use pivoting. In Eq. ( <u>A.3</u> ) we see that calculating the value of requires us to divide by . If is small then the division by a small number may 

introduce numerical errors in the calculation of . To avoid both of these problems, we recommend pivoting at each step: when constructing , �ind the row _n_ with the largest absolute value of , and then interchange row _k_ and row _n_ . It 

is relatively simple to include this in our Gaussian elimination algorithm: at step _k_ we are working with the linear system 



To interchange rows _k_ and _n_ in this system of equations, we simply : multiply both sides of this equation by the matrix 



where is a square matrix of size _N_ with entries given by 



For example, if we wanted to interchange the row with index 2 and the row with index 4 in a square matrix of size 5, then the matrix would be given by 



The key point to note when modifying the _LU_ - factorisation algorithm described in Sect. <u>A.2.1.1</u> to take account of pivoting is that Gaussian elimination with pivoting would give exactly the same results if all the rows were interchanged �irst, and then Gaussian elimination with no pivoting were carried out. Denoting the product of all the matrices representing row interchanges by **P** , we see that the _LU_ -decomposition algorithm now reduces to a factorisation of the matrix **PA** : that is, forming 



### **A.2.2 The Thomas Algorithm** 

The Thomas algorithm may be used for matrices with a speci�ic structure. Suppose our matrix **A** has structure 



where the entries of **A** satisfy 



This condition is satis�ied, for example, for an implicit �inite difference discretisation of the heat equation in one spatial dimension with Dirichlet boundary conditions at both ends of the spatial domain. De�ining 



then the linear system may be solved using the explicit recurrence relation 



### **A.2.3 The Conjugate Gradient Method** 

The matrices arising in many scienti�ic computing applications—for example, �inite element, �inite difference and �inite volume discretisations of partial differential equations—often have a large number of rows and columns, but very few nonzero elements in each row of the matrix. Such matrices are termed _sparse matrices_ . 

It is often the case that storing every element of a sparse matrix would exceed the memory limitations of a computational architecture, but storing only the nonzeros of this matrix is possible within the 

constraints of available memory. This poses a logistical challenge for the solution of linear systems described by this matrix: the _LU_ - factorisation of a sparse matrix described in Sect. <u>A.2.1.1</u> does not result in sparse matrices _L_ and _U_ , and so these matrices will suffer from the memory limitations described earlier. To circumvent this problem, iterative techniques may be used for the solution of sparse linear systems, where successive iterates of the solution of the linear system are generated until for some user-speci�ied tolerance . This branch of numerical linear algebra is a large subject in its own right and we only touch brie�ly upon it here, giving one algorithm for a very speci�ic class of matrices, namely symmetric, positive de�inite matrices. 



A matrix **A** is said to be _positive de�inite_ if, and only if, for all vectors **x** of the correct size the following two conditions are met: 



If a matrix **A** is positive de�inite and symmetric, then we may solve the linear system using the _conjugate gradient method_ , given by Algorithm 1. 

## **Appendix B** 

## **Other Programming Constructs You Might Meet** 

Below we brie�ly describe some programming constructs that other programmers may include in their C++ code. Many of these are constructs that were originally designed for the C programming language. As C++ was developed from C, much of the C language is legal C++, although the modi�ications developed for the C++ language are generally superior. 

### **B.1 C Style Output** 

We devoted the whole of Chap. <u>3</u> to describing the C++ machinery for input and output. To explain the corresponding machinery in C would require a similar amount of space, and so we only touch upon C style output here, limiting ourselves to describing output to the console. Nevertheless, this should give the �lavour of C style output commands, allowing the reader to at least recognise them should they see them. 

In the code below, we show how to use C style output to print a double precision �loating point variable to the screen in both normal and scienti�ic notation, and how to print an integer to the screen. C style output requires the whole of the output to be enclosed within double quotation marks. When a variable is to be printed it is represented by `%f` for a double precision �loating point variable, `%i` for an integer variable, and `%e` for a double precision �loating point variable in scienti�ic notation. Finally, the variables to be printed are included in an ordered list at the end of the statement. Note that the included �ile for C style printing is `<stdio.h>` —standard input and output which provides basic functionality similar to `<iostream>` in C++. 



Other C variations on `printf` which you might meet are `fprintf` for printing to �ile, in which the �irst argument is a �ile pointer of type `FILE*` and `sprintf` for printing to a string. 

### **B.2 C Style Dynamic Memory Allocation** 

In Sect. 4. 2 we explained how the C++ keywords `new` and `delete` could be used to allocate memory dynamically for arrays, and then free the memory when it was no longer needed. C also allows this, through the use of `malloc` (“memory allocate”) and `free` . As with C style output above, we only touch brie�ly on the use of these functions to allow the reader to recognise them should they come across them. In the code below, we declare a pointer to a double precision variable, `vector` , in line 6. In line 7, we then use the `malloc` function to allocate memory for 100 entries of the array `vector` , all of the same size as a double precision �loating point variable. In lines 8–13, we use these entries in the same way as a C++ array. Finally, in line 14, we free the memory allocated to this array through the use of the C function called `free` . 



### **B.3 Ternary ?: Operator** 

In Sect. 2. 1. 3 we saw that the keywords `if` and `else` could be used to execute one set of statements if a condition was met, and a different set of instructions if the condition is not met, as in the code fragment below. 



The ternary <u>3</u> ?: operator has identical effect to the `if–else` statements above: the code above may be written identically as 



Although the code written above is shorter than the original `if` – `else` statements we do not recommend it. The use of `if` and `else` makes the code much more readable, especially by anyone who is not an expert in C++ programming. 

### **B.4 Using Namespace** 

You may �ind it tedious to have to write `std::` before `cout` and other functionality of the C++ language. There is a way around this—we may use the `using` statement once in the code as shown below. 



At �irst sight, the code above may appear to make a programmer’s life a little easier. Both `string` and `cout` have been used here without being preceded by the slightly clunky `std::` . This approach does, however, introduce a subtle problem. Suppose we declared a variable called “ `vector` ”. It would then be unclear whether an instance of the word “ `vector` ” is referring to this variable, or the STL vector introduced in Chap. <u>8</u> , which the `using` statement now allows us to refer to as `vector` rather than `std::vector` . As such, we do not recommend use of the `using` keyword. 

### **B.5 Structures** 

A _structure_ is a collection of variables that are combined together. Structures can be thought of as very simple classes, but without the ability to declare functions, access privileges, or any other properties of classes other than variables. An example of a structure is shown below. Note how the variables are accessed in exactly the same way as classes 

(using “.” for a member or “ `->` ” to access a member by de-referencing a pointer). 



### **B.6 Multiple Inheritance** 

As mentioned in Sect. <u>7. 1</u> C++, unlike many other object-oriented languages, allows _multiple inheritance_ in which a derived class can be derived from multiple base classes. That is, classes may have more than one parent. 

Suppose we require a class of matrices so that we can calculate the determinant of given matrices, calculate the eigenvalues of these matrices, and calculate the norm of these matrices. One colleague may have a class of matrices, `MatrixDet` , that calculates the determinant of a matrix, but doesn’t have the functionality for calculating the eigenvalues or the norm of a matrix. Another colleague may have a class of matrices, `MatrixEigsNorm` , that does allow us to calculate the eigenvalues and norm of a matrix, but not the determinant. The functionality required is therefore all available, but not in the same class. It would therefore be convenient to merge the two classes to create a new class that contains all the functionality required. This is 

possible through _multiple inheritance_ . Below we show how to perform multiple inheritance to generate a new class `MatrixCombined` . 



If the class `MatrixDet` has no member with the same name as a member of the class `MatrixEigsNorm` then multiple inheritance is an ideal solution to this problem. Suppose both classes have a method called `ZeroEntries` . Provided this member is made a virtual function in both the class `MatrixDet` and the class `MatrixEigsNorm` we may prevent ambiguity through either de�ining a new function in the class `MatrixCombined` , or by explicitly identifying which function is to be used in the calling code. For example: 



### **B.7 Class Initialisers** 

In many cases, the constructor of a class is a simple piece of code involving a list of assignments. For example, the default constructor for the `Book` class in Sect. <u>6. 2. 7</u> set all the string �ields to “unspeci�ied” and the default constructor of the `ComplexNumber` class in Sect. <u>6. 4</u> set the real and imaginary components to zero. 



In cases where a constructor makes assignments it is more ef�icient to use C++ _initialisers_ . These are comma-separated lists of member variables and values which appear after the constructor’s signature (and a colon) but before the main body of the constructor code. Compilers for C++ are able to optimise a list of initialised values more completely than a block of code containing assignment statements. It must be noted that some compilers insist that the initialisers are ordered exactly as they appear in the de�inition of the class. An example constructor for the class of complex numbers given in Sect.  6. 4 that uses class initialisers is shown below. 



## **Appendix C** 

## **Solutions to Exercises C.1 Matrix and Linear System Classes** 

The code below is example solutions for the `Matrix` and `LinearSystem` classes developed in the Exercises at the end of Chap. 



<u>10</u> . 





















### **C.2 ODE Solver Library** 

The code below is example solutions for the classes developed in the Exercises at the end of Chap. <u>12</u> . 

















## **Further Reading** 

In earlier chapters we have touched on a few issues that are beyond the scope of this book. When discussing these issues we have directed the interested reader towards a selection of various resources: these are listed below thematically. For the “Mathematical Methods and Linear Algebra” theme, the most comprehensive reference for the basic material is that written by Kreyszig. The other references given are suitable for more advanced numerical concepts. For the “C++ Programming” theme, the website <u>http:// www. cplusplus. com</u> provides extensive practical guidance, whilst the texts listed focus on advanced features of the language. In the “Message–Passing Interface” theme the texts give an accessible tutorial–based overview of MPI-1 and MPI-2, respectively. The differences between these two MPI standards are discussed in Sect. <u>11. 2</u> . 

## **Mathematical Methods and Linear Algebra** 

1. Iserles, A.: A First Course in the Numerical Analysis of Differential Equations, 2nd edn. Cambridge University Press, Cambridge (2009) 

2. Kreyszig, E.: Advanced Engineering Mathematics, 9th edn. Wiley Inc, New York (2006) 

3. Süli, E., Mayers, D.F.: An Introduction to Numerical Analysis. Cambridge University Press, Cambridge (2006) 

4. Trefethen, L.N., Bau, D.: Numerical Linear Algebra, Society for Industrial and Applied Mathematics (1997) 

## **C++ Programming** 

5. Cline, M.P., Lomow, G., Girou, M.: C++ FAQs, 2nd edn. Addison-Wesley, Boston (1998) 

6. Meyers, S.: Effective C++, 3rd edn. Addison-Wesley, Boston (2005) 

7. Stroustrup, B.: The C++ Programming Language, 3rd edn. AT&T (2000) 

8. The Website, http:// www. cplusplus. com 

## **The Message–Passing Interface (MPI)** 

9. Gropp, W., Lusk, E., Skjellum, A.: Using MPI: Portable Parallel Programming with the Message-Passing Interface, 2nd edn. Massachussetts Institute of Technology Press, Massachussetts (1999) 

10. Gropp, W., Lusk, E., Thakur, R.: Using MPI-2: Advanced Features of the Message-Passing Interface. Massachussetts Institute of Technology Press, Massachussetts (1999) 

## **Index** 

### **A** 

Abstraction 

Access privileges, _see_ Classes Addresses of variables 

`AND` , _see_ Logical operators 

Arrays 

irregularly sized one-based indexing safe dynamic allocation sending to functions static allocation of memory 

initialising 

zero-based indexing 

ASCII character variables `assert` 

Assertions 

### **B** 

Black box testing, _see_ Testing software Blocks Boolean variables 

### **C** 

C programming language C style dynamic memory allocation `free malloc` C style output C++ �ile extensions C++11, _see_ Modern C++ `catch` , _see_ Exceptions `cerr cfloat cin` Classes abstract classes access privileges use for validating data class initialisers class members constructors copy constructor customised constructor default constructor overriding derived classes destructors `friend` keyword header �iles including only once members methods multiple inheritance pointers to setting and accessing variables 

Closing the �ile handle `cmath` Coding standards Commenting code Compiling code at the command line C++11 compiler �lags linking Make�iles multiple �iles object �ile template compilation Complex numbers `const` Constructors, _see_ Classes `cout` **D** Debugging code Destructors, _see_ Classes Distributed memory architectures Division of integers Documenting code `double` Dynamic allocation of memory, _see_ Pointers Dynamic casting **E** `else` Encapsulation Exception `catch` three levels of error `throw try` Extensibility 

### **F** 

Finite difference approximations application to boundary value problems Floating point variables comparing two �loating point variables `DBL_EPSILON` double precision Flow of control Flushing output `for` Fortran `fprintf free` , _see_ C programming language `friend` , _see_ Classes `fstream` Function overloading Function pointers, _see_ Functions Function prototypes, _see_ Functions Functions class members default values for function arguments function pointers function prototypes recursive functions return type returning a pointer sending arrays to use of arguments that are pointers 

### **G** 

Global variable, _see_ Variables GNU Octave Guard **I** `if` Indenting code 

In�inity Inheritance abstract classes base class child class derived classes parent class private inheritance protected inheritance public inheritance Input command line from console from �ile rewinding a �ile strings Input stream variable `int` Integer variables long integers short integers signed integers unsigned integers Integrated development environments Interpreted languages `iostream` **K** Keywords **L** Linear algebra conjugate gradient method Gaussian elimination no pivoting pivoting linear systems LU decomposition 

parallel Thomas algorithm Linear algebra algorithms Local variable, _see_ Variables Logical operators `AND NOT OR` 

### **M** 

Make�iles, _see_ Compiling code `malloc` , _see_ C programming language Mathematical operations absolute value arccos arcsin arctan ceiling cosh cosine exponential �loor logarithm raising variables to a given power shorthand sine sinh square root tangent tanh M ����� Matrices determinant eigenvalues inverse norm operations between 

positive de�inite symmetric transpose Message Passing Interface (MPI) `Allgatherv Allreduce Barrier Bcast` broadcast `Bsend` collective communication broadcast combined send and receive halo exchange reduction communication blocking buffered point-to-point compiling debugging executing remote machines `Gather` gather `Ibsend` input and output installing MPI `Irecv Isend` process rank `Recv` reduce running code `Scatter` scatter 

`Send Sendrecv Ssend` Modern C++ `array auto` compilation mapping lambda functions range-based `for` loops smart pointers `shared_ptr unique_ptr` Modularity Modules Multiple inheritance **N** Namespace `NOT` , _see_ Logical operators Not–a–number Numerical libraries PETSc **O** Object–oriented numerical libraries ordinary differential equations partial differential equations Object-orientation Object-oriented numerical libraries Operator overloading `OR` , _see_ Logical operators Ordinary differential equations Output appending to existing �ile formatting redirected to �ile scienti�ic notation 

setting precision of to console to �ile Output stream variable 

### **P** 

Partial differential equations Pointer Aliasing, _see_ Pointers Pointer de-reference, _see_ Pointers Pointers array of `delete` keyword dynamic allocation of memory `new` keyword pointer aliasing pointer de–reference pointer variables shared pointers smart pointers to classes Polymorphism run–time static, _see_ Templates templates, _see_ Templates Postcondition Precondition `printf` Python 

### **R** 

Recursive functions, _see_ Functions Reference variables Relational operators equal to equality versus assignment greater than greater than or equal to less than 

less than or equal to not equal to Reserved words **S** 

Scienti�ic notation, _see_ Variables Scope Shared memory architectures Shared pointers, _see_ Pointers `sprintf` Standard Template Library (STL) abstraction `algorithm` container deque iterator list `push_back set vector` vectors Statements `stdio.h` Strings Structures `switch` **T** Templates for polymorphism Standard Template Library, _see_ Standard Template Library (STL) validation of index to array Ternary `?:` operator Test driven development, _see_ Testing software Testing software black box testing test-driven development white box testing 

`throw` , _see_ Exceptions `try` , _see_ Exceptions Type conversion 

### **U** 

Uni�ied modelling language 

### **V** 

Variables constant variables declaring variables global variable initialising variables local variable scienti�ic notation Vectors norm operations between scalar product Virtual methods pure virtual method `void` 

### **W** 

`while` White box testing, _see_ Testing software 

## **Footnotes** 

<u>1</u> 

This recursion may be mapped directly into recursive functions (discussed in Sect. <u>5. 8</u> ) when programming. However, it is generally more ef�icient to hard-code commonly used determinants for small matrices such as and . 

<u>2</u> 

A vector **v** satis�ies **v** = **0** if, and only if, all entries of this vector take the value 0: **v** is then said to be a _zero vector_ . If not, **v** is said to be a _nonzero vector_ . 

<u>3</u> 

A ternary operator has three inputs.