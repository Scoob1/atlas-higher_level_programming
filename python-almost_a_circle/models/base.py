#!/usr/bin/python3
"""
Base module
"""


class Base:
    """Base class for managing `id` attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance with an id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

            @staticmethod
            def to_json_string(list_dictionaries):
                """
                Return the JSON string representation of list_dictionaries
                """
                if not list_dictionaries or not isinstance(list_dictionaries, list):
                    return "[]"
                return json.dumps(list_dictionaries)
            
            @classmethod
            def save_to_file(cls, list_objs):
                """
                Write the JSON string representation of list_objs to a file
                """
                filename = f"{cls.__name__}.json"
                with open(filename, "w") as f:
                    if list_objs is None:
                        f.write("[]")
                    else:
                        list_dicts = [obj.to_dictionary() for obj in list_objs]
                        f.write(cls.to_json_string(list_dicts))
                        
                        @staticmethod
                        def from_json_string(json_string):
                            """
                            Return the list of the JSON string representation json_string
                            """
                            if not json_string or json_string == "":
                                return []
                            return json.loads(json_string)
                        
                        @classmethod
                        def create(cls, **dictionary):
                            """
                            Return an instance with all attributes already set"""
                            if cls.__name__ == "Rectangle":
                                dummy = cls(1, 1)
                            elif cls.__name__ == "Square":
                                dummy = cls(1)
                                dummy.update(**dictionary)
                                return dummy
                            
                            @classmethod
                            def load_from_file(cls):
                                """Return a list of instances"""
                                filename = f"{cls.__name__}.json"
                                try:
                                    with open(filename, "r") as f:
                                        list_dicts = cls.from_json_string(f.read())
                                        return [cls.create(**d) for d in list_dicts]
                                    except FileNotFoundError:
                                        return []
