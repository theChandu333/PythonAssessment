class Hello:
    a = 10
    _b = 20
    __c = 30

    def display(self):
        print(Hello.a)
        print(Hello._b)
        print(Hello.__c)

h = Hello()
h.display()

##############################################################################################

print(Hello.a)
print(Hello._b)
# print(Hello.__c)

###############################################################################################

class Hi:

    def display(self):
        print(Hello.a)
        print(Hello._b)
        # print(Hello.__c)

h = Hi()
h.display()

################################################################################################

class Hi_Hello(Hello):
    a = 10
    _b = 20
    __c = 30

    def display(self):
        print(Hello.a)
        print(Hello._b)
        # print(Hello.__c)

hh = Hi_Hello()
hh.display()

#####################################################################################################
