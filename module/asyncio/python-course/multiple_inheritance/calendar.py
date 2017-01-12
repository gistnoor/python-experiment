class Calendar(object):
    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    date_style = "British"

    @staticmethod
    def leapyear(year):
        if  year % 4 == 0:
            if  year % 4 == 0:
                if  year % 400 == 0:
                    leapyear = True
                else:
                    leapyear = False
            else:
                leapyear = True
        else:
            leapyear = False        
        
        return leapyear

    def __init__(self, d, m, y):
        self.set_Calendar(d,m,y)

    def set_Calendar(self, d, m, y):
        if type(d) == int and type(m) == int and type(y) == int:
            self.__days = d
            self.__months = m
            self.__years = y
        else:
            raise TypeError("d, m, y have to be integer")

    def __str__(self):
        if Calendar.date_style == "British":
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__days, self.__months, self.__years)
        else:
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__months, self.__days, self.__years)

    def advance(self):
        max_days = Calendar.months[self.__months - 1]
        if self.__months == 2 and Calendar.leapyear(self.__years):
            max_days += 1
        if self.__days == max_days:
            self.__days = 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            else:
                self.__months += 1
        else:
            self.__days += 1

if __name__ == '__main__':
    x = Calendar(31,12,2012)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print("2012 was a leapyear:")
    x = Calendar(28,2,2012)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    x = Calendar(28,2,2013)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print("1900 no leapyear: number divisible by 100 but not by 400: ")
    x = Calendar(28,2,1900)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print("2000 was a leapyear, because number divisibe by 400: ")
    x = Calendar(28,2,2000)
    print(x, end=" ")
    x.advance()
    print("after applying advance: ", x)
    print("Switching to American date style: ")
    Calendar.date_style = "American"
    print("after applying advance: ", x)  
