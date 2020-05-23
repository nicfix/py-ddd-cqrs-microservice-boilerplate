class Pet(object):
    """The Pet Model."""

    id: str
    name: str
    age: int

    def __init__(self, id, name, age):
        """
        Create an instance of Pet.

        :param id: the pet's id
        :param name: the pet's name
        :param age: the pet's age
        """
        self.id = id
        self.name = name
        self.age = age
