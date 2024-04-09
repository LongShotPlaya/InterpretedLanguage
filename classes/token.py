from classes.location import Location

class Token:
    def __init__(self, content: str, value, type: str, location: Location):
        self.content = content
        self.value = value
        self.type = type
        self.location = location

    @staticmethod
    def invalid_token(content: str, location: Location):
        return Token(content, None, "invalid", location)
