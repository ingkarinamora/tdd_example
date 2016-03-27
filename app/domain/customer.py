class Customer:
    def __init__(self, identifier_type, identifier, name):
        self.__identifier_type = identifier_type
        self.__identifier = identifier
        self.__name = name

    def identifier_type(self):
        return self.__identifier_type

    def identifier(self):
        return self.__identifier

    def name(self):
        return self.__name

    def __eq__(self, other):
        return self.__identifier == other.__identifier

