import math

"""
	**---------------Assignment on Sequence Type---------------**
	Objective 1: Create a Polygon Class where initializer takes in:
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
	
	********************************************************************************************************
	The starting point for this assignment is the `Polygon` class and the `Polygons` 
	sequence type you created in the previous assignment.

	The code for these classes along with the unit tests for the `Polygon` class are below 
	if you want to use those as your starting point. But use whatever you came up with in the last project.
	You have two goals:
	Goal 1:
	Refactor the `Polygon` class so that all the calculated properties are lazy properties, 
	i.e. they should still be calculated properties, but they should not have to get recalculated more than once 
	(since we made our `Polygon` class "immutable").
	 
	Goal 2:
	Refactor the `Polygons` (sequence) type, into an **iterable**. 
	Make sure also that the elements in the iterator are computed lazily - 
	i.e. you can no longer use a list as an underlying storage mechanism for your polygons.
	
	You'll need to implement both an iterable and an iterator.
"""
class Polygon:
	def __init__(self,val):
		"""
			Constructor to create polygon class.
			Takes 2 parameters - number of edges and circumradius
		"""
		try:
			edge, circumradius = val
		except ValueError:
			raise ValueError("Please pass an iterable with 2 items - edge and circumradius")
		else:
			if edge<3:
				raise ValueError("Edge count should be more than 3 to be a valid polygon")
			self.edge = edge
			self.circumradius = circumradius


	@property
	def edge(self):
		"""
			outputs the number of edges
		"""
		return self._edge

	@property
	def circumradius(self):
		"""
			outputs the circumradius
		"""
		return self._circumradius

	@edge.setter
	def edge(self,e):
		self._edge = e
		self._interior_angle = None
		self._edge_length = None
		self._apothem = None
		self._area = None
		self._perimeter = None

	@circumradius.setter
	def circumradius(self,c):
		self._circumradius = c
		self._interior_angle = None
		self._edge_length = None
		self._apothem = None
		self._area = None
		self._perimeter = None

	def __repr__(self):
		"""
			prints a string representation of a class object
		"""
		return f"Polygon with {self.edge} edges and circumradius={self.circumradius}"

	@property
	def no_of_vertices(self):
		"""
			prints number of vertices
		"""
		return self._edge

	@property
	def interior_angle(self):
		"""
			print out the interior angle of the polygon
		"""
		if self._interior_angle is None:
			print("Calculating interior angle")
			self._interior_angle = ((self._edge-2)*180/self._edge)
		return self._interior_angle

	@property
	def edge_length(self):
		"""
			prints edge length of polygon
		"""
		if self._edge_length is None:
			print("Calculating edge length")
			self._edge_length = (2 * self._circumradius * math.sin(math.pi/self._edge))
		return self._edge_length

	@property
	def apothem(self):
		"""
			prints apothem of the polygon
		"""
		if self._apothem is None:
			print("Calculating apothem")
			self._apothem = (self._circumradius * math.cos(math.pi/self._edge))
		return self._apothem

	@property
	def area(self):
		"""
			prints area of the polygon
		"""
		if self._area is None:
			print("Calculating area")
			self._area = (0.5 * self._edge * self.interior_angle * self.apothem)
		return self._area

	@property
	def perimeter(self):
		"""
			prints perimeter of the polygon
		"""
		if self._perimeter is None:
			print("Calculating perimeter")
			self._perimeter = (self._edge * self.edge_length)
		return self._perimeter

	def __eq__(self, other):
		"""
			implements equality property based on edge and circumradius
		"""
		if not isinstance(other, Polygon):
			raise TypeError(f"{other} is not of type Polygon")
		if self._edge == other._edge and self._circumradius == other._circumradius:
			return True
		else:
			return False

	def __gt__(self, other):
		"""
			implements 'greater than' property between 2 polygon objects
		"""
		if not isinstance(other, Polygon):
			raise TypeError(f"{other} is not of type Polygon")
		if self._edge > other._edge:
			return True
		else:
			return False

class Polygon_sequence:
	def __init__(self,largest_edge,common_circumradius):
		self.largest_edge = largest_edge
		self.common_circumradius = common_circumradius


	def __iter__(self):
		return self.PolySeqIter(self.largest_edge,self.common_circumradius)

	class PolySeqIter:
		def __init__(self, largest_edge,common_circumradius):
			self.largest_edge = largest_edge
			self.common_circumradius = common_circumradius
			self.i = 3

		def __iter__(self):
			return self

		def __next__(self):
			if self.i > self.largest_edge:
				raise StopIteration
			else:
				result = Polygon((self.i,self.common_circumradius))
				self.i += 1
				return result

	def max_efficiency(self):
		"""
			prints polygon wth maximum area-perimeter ratio
		"""
		eff_list = [(x.area/x.perimeter) for x in list(self)]
		return list(self)[eff_list.index(max(eff_list))]


















