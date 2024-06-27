class Mail:
    def __init__(self):
        self.k = 0
        self.j = 0
        self.m = 0

    def validate_email(self, email):
        if len(email) >= 6:
            if email[0].isalpha():
                if ("@" in email) and (email.count("@") == 1):
                    if (email[-4] == ".") or (email[-3] == "."):
                        for i in email:
                            if i == i.isspace():
                                self.k = 1
                            elif i.isalpha():
                                if i == i.upper():
                                    self.j = 1
                            elif i.isdigit():
                                continue
                            elif i == "_" or i == "." or i == "@":
                                continue
                            else:
                                self.m = 1
                        if self.j == 1 or self.k == 1 or self.m == 1:
                            print("wrong Email 5")
                            return False
                    else:
                        print("wrong email 4")
                        return False
                else:
                    print("wrong email 3")
                    return False
            else:
                print("wrong email 2")
                return False
        else:
            print("wrong email 1")
            return False

    def check(self, email):
        if self.validate_email(email) is not False:
            return True


if __name__ == "__main__":
    mail = Mail()
    enter = input("Enter your Email:")
    mail.check(enter)
