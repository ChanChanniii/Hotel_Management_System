class Credential:
    def __init__(self, username, password, role="admin"):
        self.username = username
        self.password = password
        self.role = role

    def matches(self, username, password):
        return self.username == username and self.password == password
