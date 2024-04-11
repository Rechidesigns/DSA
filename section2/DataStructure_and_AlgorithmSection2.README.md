# Algorithm Analysis

we can measure an algorithm by:

    a. Time Complexity: The amount of time taking by an algorithm to complete.

    b. Space Complexity: Is the amount of memory used by the algorithm while executing.


In algorithm, impute size matters:

a. Running time of algorithm is propotional

b. Increases with the size of the input


## Time Complexity
Measuring time Complexity 

a. Experimental Analysis

b. Theoretical Analysis

## Experimental Analysis

a. Run-time measured on various inputs: 
the runing time of an algorithm can be measured by executing the algorithm on various input


**Advantages**

b. High Programming languages provides time function.

c. Lapse time is computed

**Disadvantages**

a. Limited Input
b. Hardaware dependent
c. Software dependent
c. Operating system dependent
Easier than theoretical analysis
Difficult to predict precise running time

## Theoretical Analysis

The theoritical model is also known as mathematical model.
In theoritical, the analysis is performed directly on description of algorithm, or the operation or actural program or function.

**Advantages**

It is independent of the hardware system, eg CPU, Memory catching and software eg compilers, interpreters and gabage collectors. 

The theoritical analysis is independent on the operating system and the other applications runing along in the system.

Theoritical analysis also takes into account all the posible inputes.

**Content Execution Time**
The theoritical analysis, there is always a way to determine the cost of operation.

We assume that the parameter are basic operations based on constraints time.

**it has frequency of operations, the operations that are considered as parameters are**

    Declarations

    Assignment

    Arithmetic Operations

    Comparison Statemnts

    Accessing elements

    Calling function 

    Returning functions


## Algorithms Order of Growth

when we analyze algorithm we can classify them according to their performance as the size of the impute grows.

### here is the order of growth

**Constant  1**
Constant is when the program has no loops

**Logarithm  log(n)**
If it has some kind of loops where the size of the impute is divided into halfs after every Iteration then the order of growth will be logarithmic.

**Linear  n**
If it has just simple loop in a algorithm then the growth is linear.
If an algorithm has two loops but they are not nested

**n-log-n   n log(n)**
this technique uses devide and conquer.

**QuadraTIC   n²**
If it has two nested loops then the growth is quadratic.

**Cubic n³**
If the algorithm has three nested loops then the growth will be cubic.

**Exponential 2ᵑ**


## Asymptotic Analysis

### Big-Oh, Big-Ώ, Big-O

When analysimg algorithm, we use mathematical notations and decribe them using functions.

The runtime as usual depends on the growth as described in the order of growth.

The runtime of the algorithm grows propotionally with the inpute

**Asymtotic: Approaching a value with some limit**

## Types of Sceneros.

Best Case: Lower bond, here the inpute is easier.

Worst Case: Upper bond, where the inpute is worst difficult

Average Case: Is where the bound is between the best case and the worst case. meaning bwteen Lower and Upper bond.

In analysis of algorithm and in therms of performance we are not concernced anbout the best case, we are more bordered on the worst case. which guarantees that the running time of the algorithm is going to be bigger than the worst case or upper bond.

Sometimes the best and the worst case may be seen. but we should be more concerned on the worst case.

**In order to find th performance we use notations knowm as:**

    Big -Oh  O( ) Big O is used to describe the worst case and also the rate of growth related to the inpute size.

    Big - Omega Ώ( ) The Omega notation measures the lower bond of the asymptotic growth, it is used to describe the best case.

    Big - Theta 0( ) The Theta notation measures between the upper and lower bond asymtotic growth, also called a tigth bond.


