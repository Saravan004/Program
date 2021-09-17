class Person:  
      
    serial = 10   
    def __init__(self, name):  
        self.name = name  
        self.serial=Person.serial
        Person.serial+=1
        #print(Person.serial)
        #self.serial = 112
        #print(self.serial)
  
    def say_hi(self):  
        print('Hello, my name is', self.name)  
      
p = Person('Nikhil')  
p.say_hi() 
print(p.serial)
p1 = Person("dd")
p1.say_hi()
print(p1.serial)

__________---------------_________

#static and class methos
class Student:
    school = "Mithra" #static_variable
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):#find average
        return (self.m1 +self.m2 + self.m3)/3
    
    @classmethod   
    def info(cls):
        return cls.school
        
    @staticmethod
    def fact():
        print("Static method")
        
s1 = Student(12,13,14)
s2 = Student(10,9,8)

print(s1.avg())
print(Student.info())
Student.fact()

-------------------------------------------

#static method with inheritance
class Shipp:
	serial = 11
	@classmethod
	def _gen_(cls):
		result = cls.serial
		cls.serial+=1
		return result
	@staticmethod
	def _make_(owner_code, serial):
 		print("")
	@classmethod
	def empty(cls, owner_code):
		print("ww")
	@classmethod
	def create(cls, owner_code, items):
		print("ll")
	def __init__(self,owner_code, contents):
		self.owner_code = owner_code
		self.contents = contents
		self.bic = ShippingContainer._make_(owner_code=owner_code,serial = Shipp._gen_()

class Ref(Shipp):
	@staticmethod
	def _make_(owner_code, serial):
		print("")

r1 = Ref("MAE", ["dd"]

-----------------------------
         #static method with inheritance
class Shipp:
	serial = 11
	@classmethod
	def _gen_(cls):
		result = cls.serial
		cls.serial+=1
		return result
	@staticmethod
	def _make_(owner_code, serial):
 		print("")
	@classmethod
	def empty(cls, owner_code):
		return cls(owner_code, contents=[], **kwargs)
	@classmethod
	def create(cls, owner_code, items, **kwargs):
		cls(owner_code, contents=[], **kwargs)
	def __init__(self,owner_code, contents, **kwargs):
		self.owner_code = owner_code
		self.contents = contents
		self.bic = ShippingContainer._make_(owner_code=owner_code,serial = Shipp._gen_()

class Ref(Shipp):


 max= 5.0
 def __init__(self,owner_code,contnts, *, celsius, **kwargs):
	super().__init__(owner_code, contents, **kwargs)
	if celsius> Ref.max
		raise Valueerror("")
	self.celsius = celsuis
	@staticmethod
	def _make_(owner_code, serial):
		print("")

r1 = Ref("MAE", ["dd"]


--------------------------------
	 #Properties
	 
class Employee:
	def __init__(self, first, last):
		self.first = first
		self.last = last
	@property #invoke as attribute
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)
	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last
		
	@fullname.deleter
	def fullname(self):
	    self.first = None
	    self.last = None
emp_1 = Employee("JIm","Koya")
emp_1.first = "John"
#emp_1.fullname = "e ee"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname #print None

----------------------------------
class SimpleList:
	def __init__(self,items):
		self._items = list(items)
	def add(self,item):
		self._items.append(item)
	def __getitem__(self, index):
		return self._items[index]
	def sort(self):
		self._items.sort()
	def __len__(self):
		return len(self._items)
	def __repr__(self):
		return f'{type(self).__name__}({self._items!r})'

class SortedList(SimpleList):
	def __init__(self, items=()):
		super().__init__(items)
		self.sort()
	def add(self, item):
		super().add(items)
		self.sort()
class Intlist(SimpleList):
	def __int__(self, items=()):
		for x in items: self._validate(x)
		super().__init__(items)
	@staticmethod
	def_validate(x):
		if not isinstance(x, int):
			raise TypeError("")

class SortedIntlist(Intlist, SimpleList):
	pass

---------------------------------
---------------------------------
#Super

class Animal:
	@classmethod
	def description(cls):
		return "an animal"
class bird(Animal):
	@classmethod
	def description(cls):
		s= super().
		print(s)
		return s.description()+"ee"
class Flamingo(Bird):
	@classmethod
	def description(cls):
		return  super().description() + "and"


-------------------------
-------------------------
#hashable
@dataclass(eq=true, frozen=true)
class Location:
	name: str
	position: Position
hong_kong = Location("hong kong", earth(22.2, 113.3)
#cities = {hong_kong, stockolhm}

=========
@dataclass(eq=true, frozen=true)
class Location:
	name: str
	position: Position
	def __post_init__(self):
		if self.name == "":
			raise ValueError("dd")
#

============

============
class Position:
	def __init__(self, latitude, longitude):
		if not (-90 <= latitude <=+90):
			raise ValueError(f"l{longitude} out of range")
		if not(-180<=longitude<= +180):
			raise valueError(f"l{longitude} out of range")

		self._latitude = latitude
		self._longitude = longitude
 	@property
	def latitude(self):
		return self._latitude
		
	@property
	def longitude(self):
		return self._longitude
	@property
	def latitude_hemishpere(self):
		return "N" if self.latitude >= 0 else "S"

	def latitude_hemishpere(self):
		return "E" if self.latitude >= 0 else "W"	

	def __repr__(self):
	 	return f"position{self.latitude}{self.longitude}"
	
	def __str__(self):
		return f"{self.latitude}'s, {self.longitude}'E
	def __format__(self, format_spec):
		return "Formatted Position"	 









