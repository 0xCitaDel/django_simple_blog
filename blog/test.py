class Car:
    @classmethod
    def engine(cls):
        print('Engine')
        def view():
            print('View')
        view.mersedes = 22
        return view()

print(Car.engine.__dict__)