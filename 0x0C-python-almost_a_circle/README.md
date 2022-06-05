# Python - Almost a circle

## Description of the files inside this folder:

0. All your files, classes and methods must be unit tested and be PEP 8 validated.
1. Write the first class Base. This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs).
2. Write the class Rectangle that inherits from Base.
3. Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded).
4. Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
5. Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.
6. Update the class Rectangle by overriding the "__str__" method so that it returns "[Rectangle] (<id>) <x>/<y> - <width>/<height>".
7. Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y.
8. Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute.
9. Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes.
10. Write the class Square that inherits from Rectangle.
11. Update the class Square by adding the public getter and setter size.
12. Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes.
13. Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle.
14. Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square.
15. JSON is one of the standard formats for sharing data representation. Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries.
16. Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file.
17. Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string.
18. Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set.
19. Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances.

## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Python 3.8.10
- Style guidelines: [PEP 8](https://www.python.org/dev/peps/pep-0008/)


<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
