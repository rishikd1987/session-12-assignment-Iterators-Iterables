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
"""

class Polygon:
	def __init__(self,edge:int,circumradius:int):
		"""
			Constructor to create polygon class.
			Takes 2 parameters - number of edges and circumradius
		"""
		if edge<3:
			raise ValueError("Edge count should be more than 3 to be a valid polygon")
		self.edge = edge
		self.circumradius = circumradius

	def __repr__(self):
		"""
			prints a string representation of a class object
		"""
		return f"Polygon with {self.edge} edges and circumradius={self.circumradius}"

	def no_of_edges(self):
		"""
			outputs the number of edges
		"""
		return self.edge

	def no_of_vertices(self):
		"""
			prints number of vertices
		"""
		return self.edge

	def interior_angle(self):
		"""
			print out the interior angle of the polygon
		"""
		return ((self.edge-2)*180/self.edge)

	def edge_length(self):
		"""
			prints edge length of polygon
		"""
		return (2 * self.circumradius * math.sin(math.pi/self.edge))

	def apothem(self):
		"""
			prints apothem of the polygon
		"""
		return (self.circumradius * math.cos(math.pi/self.edge))

	def area(self):
		"""
			prints area of the polygon
		"""
		return (0.5 * self.edge * self.interior_angle() * self.apothem())

	def perimeter(self):
		"""
			prints perimeter of the polygon
		"""
		return (self.edge * self.edge_length())

	def __eq__(self, other):
		"""
			implements equality property based on edge and circumradius
		"""
		if not isinstance(other, Polygon):
			raise TypeError(f"{other} is not of type Polygon")
		if self.edge == other.edge and self.circumradius == other.circumradius:
			return True
		else:
			return False

	def __gt__(self, other):
		"""
			implements 'greater than' property between 2 polygon objects
		"""
		if not isinstance(other, Polygon):
			raise TypeError(f"{other} is not of type Polygon")
		if self.edge > other.edge:
			return True
		else:
			return False

class Polygon_sequence:
	def __init__(self,largest_edge,common_circumradius):
		"""
			constructor to create polygon sequence
		"""
		self.largest_edge = largest_edge
		self.common_circumradius = common_circumradius
		self.polygon_seq = [Polygon(x,self.common_circumradius) for x in range(3,self.largest_edge+1)]

	def __repr__(self):
		"""
			prints a string representation of a plygon_sequence class object
		"""
		return str(self.polygon_seq)

	def max_efficiency(self):
		"""
			prints polygon wth maximum area-perimeter ratio
		"""
		eff_list = [(x.area()/x.perimeter()) for x in self.polygon_seq]
		return self.polygon_seq[eff_list.index(max(eff_list))]

	def __len__(self):
		"""
			returns number of polygons in the sequence
		"""
		return len(self.polygon_seq)

	def __getitem__(self, item):
		"""
			implement slicing operation in polygon_sequence object
		"""
		return self.polygon_seq[item]














