# Session 12 assignment of EPAi4.0
Named Tuples
***
|Name|Email|Git ID|
|----|-----|-------|
|Rishik Dutta|rishikdutta1987@gmail.com|rishikd1987|

## File Name: session12.py
***
#### Brief Description:
Problem from previous session:
Objective 1: Create a `Polygon` Class where initializer takes in:
* number of edges/vertices
* circumradius
Class needs to provide these properties:
* # edges
* # vertices
* interior angle
* edge length
* apothem
* area
* perimeter
Class should provide these functionalities:
* a proper __repr__ function
* implements equality (==) based on # vertices and circumradius (__eq__)
* implements > based on number of vertices only (__gt__)
Objecttive 2: Implement a Custom Polygon sequence type where initializer takes in:
* number of vertices for largest polygon in the sequence
* common circumradius for all polygons
Following properties need to be provided:
* max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
Following properties need to be provided:
* functions as a sequence type (__getitem__)
* supports the len() function (__len__)
* has a proper representation (__repr__)
Current problem set:
* Goal 1: Refactor the `Polygon` class so that all the calculated properties are lazy properties,
i.e. they should still be calculated properties, but they should not have to get recalculated more than once
(since we made our `Polygon` class "immutable").

* Goal 2: Refactor the `Polygons` (sequence) type, into an **iterable**. Make sure also that the elements in the iterator are computed lazily - 
i.e. you can no longer use a list as an underlying storage mechanism for your polygons.
You'll need to implement both an iterable and an iterator.
#### Packages imported:
* math

## Code Descriptions
|Type|Name|Input parameters|Output parameters|Description|Dependency|
|----|-----|-------|-------|-------|-------|
|class|`Polygon`|-|-|Polygon class|- |
|constructor|__init__|Tuple of (edge,circumradius)|-|creates Polygon object - minimum 3 edges required|- |
|setter|edge|int|-|Setter for edge property / also sets all property values to None for lazy evaluation - interior angle, edge length, apothem, area, perimeter|- |
|setter|circumradius|int|-|Setter for circumradius property / also sets all property values to None for lazy evaluation - interior angle, edge length, apothem, area, perimeter|- |
|dunder method|__repr__|-|-|retruns a string representation of class object|- |
|function|interior_angle|-|-|Calculate interior angle|- |
|function|edge_length|-|-|Calculate edge length|- |
|function|apothem|-|-|Calculate apothem|- |
|function|area|-|-|Calculate area|- |
|function|perimeter|-|-|Calculate perimeter|- |
|dunder method|__eq__|-|-|Implements equality property based on edge and circumradius|- |
|dunder method|__gt__|-|-|implements 'greater than' property between 2 polygon objects|- |
|class|`Polygon_sequence`|-|-|Polygon Sequence class - `Iterable`|- |
|constructor|__init__|Largest_edge(int) and common circumradius(int)|-|creates Polygon sequence(Iterable)|- |
|dunder method|__iter__|-|-|returns PolySeqIter object (Iterator)|- |
|sub class|`PolySeqIter`|Largest_edge(int) and common circumradius(int)|-|Iterator|- |
|dunder method|__iter__|-|-|Iter function inside PolySeqIter class|- |
|dunder method|__next__|-|-|Iterates through the Polygon sequence...stops when it reaches largest edge|- |
|function|max_efficiency|-|-|prints polygon wth maximum area-perimeter ratio|- |
