#github link
#https://github.com/Arhin4242
 #list of available cars and their prices in Dollars
car_dict ={
"Toyota":{
"Vios":{
        "available":False,
     "price":4700 
},
 "Camry":{
     "available":True,
     "price":8000
},
"Corolla":{
    "available":False,
    "price":6500
},
"RAV4":{
       "available": True,
       "price":7200
},
"Fortuner":{
   "available":True,
   "price":13000
 },
"Yaris":{
    "available":True,
    "price":5000
},
"Prado":{
    "available":True,
    "price":15000 
},
"Land Cruiser":{
   "available":True,
   "price":30000
},
"Prius":{
   "available":False,
   "price":4800
}},
"Nissan":{
"Altima":{
   "available":True,
   "price":6000
},
"Titan":{
   "available":False,
   "price":10000
},
"Maxima":{
   "available":True,
   "price":9000
},
"GT-R":{
   "available":True,
   "price":5800
},
"Sylphy":{
    "available":False,
    "price":4800
},
"Mercedes-Benz":{
"AMG GT":{
    "available":False,
    "price":150000
},
"C300":{
    "available":False,
    "price":15500
},
"CLA250":{
    "available":True,
    "price":27000
    },
 "G WAGON":{
     "available":False,
     "price":300000
     },
"S350":{
      "available":True,
      "price":280000
      },
"S500":{
       "available":False,
       "price":400000
       },
"S400":{
        "available":False,
        "price":320000
        },
"Hyundai":{
"Elantra":{
    "available":True,
    "price":7500
    },
 "Sonata":{
     "available":True,
     "price":6500
     },
"Accent":{
    "available":False,
    "price":5000
    },
"KIA":{
"Morning":{
    "available":True,
    "price":4800
    },
"Sorento":{
    "available":False,
    "price":6500
    },
"Sportage":{
    "available":True,
    "price":10000
    },
"Tesla":{
"Model S":{
    "available":True,
    "price":250000
    },
"Cybertruck":{
    "available":True,
    "price":540000
    },
"Model Y":{
    "available":False,
    "price":320000
    },
"Honda":{
"Accord":{
     "available":True,
     "price":15000
     },
"Civic":{
     "available":True,
      "price":12000
    }}}}}}}}
#get user input for car brand
car_brand=input('Enter your car brand:')
if car_brand in car_dict:
    car_model = input("Enter your car model:")
    if car_model in car_dict[car_brand]:
        available =car_dict[car_brand],
        [car_model],[available]
        if available:
            price=car_dict[car_brand][car_model]["price"]
            print(f"The {car_brand} {car_model} is available and it's price is GHc{price}")
        else:
            print(f"Sorry the {car_brand}{car_model} is not available.")
       
       
