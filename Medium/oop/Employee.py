class Employee:

    def __init__(self, first_name, last_name, nric):
        self.first_name = first_name
        self.last_name = last_name
        self.nric = nric

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getFullName(self):
        return '{} {}'.format(self.first_name,  self.last_name)

    def getNric(self):
        return self.nric
