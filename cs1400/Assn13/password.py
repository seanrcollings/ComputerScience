class Password:
    def __init__(self, password=None):
        self.__password = password
        self.__validators = [self.__isNone, self.__contains, self.__endsWith,
                             self.__tooShort, self.__containsNonAlphaNumeric,
                             self.__tooFewDigits]
        self.__errors = []

    def setPassword(self, newPassword):
        if self.__isValid(newPassword):
            self.__password = newPassword
            return True
        return False

    def __isValid(self, password):
        for validator in self.__validators:
            validator(password)
        if len(self.__errors) > 0:
            return False
        return True

    def getErrorMessage(self):
        return '\n'.join(self.__errors)

    def setErrorMessage(self, error):
        self.__errors = error

    # Validators
    def __isNone(self, password):
        if password is None or password == '':
            self.__errors.append('* The password cannot be left emtpy')

    def __contains(self, password, word='password'):
        if word in password:
            self.__errors.append('* Password cannot contain the word "{}"'.format(word))

    def __endsWith(self, password, ending='123'):
        if password.endswith(ending):
            self.__errors.append('* Password cannot end with "{}"'.format(ending))

    def __tooShort(self, password, length=8):
        if len(password) < length:
            self.__errors.append('* Password must be {} or more characters'.format(length))

    def __containsNonAlphaNumeric(self, password):
        for char in password:
            if not char.isnumeric() and not char.isalpha():
                self.__errors.append("* Password cannot contain non alphanumeric characters")
                break

    def __tooFewDigits(self, password):
        digits = ''
        for char in password:
            if char.isnumeric():
                digits += char

        if len(digits) < 2:
            self.__errors.append("* Password must contain at least 2 numbers")
