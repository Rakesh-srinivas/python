class Car:
        def __init__(self,make,model,year):
            self.make = make
            self.model = model
            self.year = year

        def start_engine(self):
            print('Engine started..')

        def stop_engine(self):
            print('Engine stopped..')

        def drive(self):
            print(f"{self.make} {self.model} is being driven..")

    #craeting object instance of the class
            Car1 =Car('Toyota','Fortuner',2022)
            Car2 = Car('Mahindra','THAR',2021)
       
     #Accessing attributes of the object
            print(Car1.make)
            print(Car2.model)

    #calling methods of the object
            Car1.start_engine()
            Car2.drive()
