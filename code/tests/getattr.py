class terminal:
    def attribute(self):
        x = getattr(self,'name',None)
        print(x)

test = terminal()
test.attribute()
print(type(test))
