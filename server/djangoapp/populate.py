from .models import CarMake, CarModel


def initiate():

    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes Benz", "description": "Luxury cars."},
        {"name": "Audi", "description": "Luxury cars. German technology"},
        {"name": "Kia", "description": "Affordable cars. Korean technology"},
        {"name": "Toyota", "description": "Affordable cars. Japanese tech."},
        {"name": "Ford", "description": "Affordable cars. American tech"},
        {"name": "Chevrolet", "description": "Affordable cars."},
        {"name": "Hyundai", "description": "Affordable cars. Korean tech."},
        {"name": "BMW", "description": "Luxury cars. German technology"},
        {"name": "Volkswagen", "description": "Affordable cars."},
    ]
    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data["name"], description=data["description"]
            )
        )

    # Create CarModel instances with the corresponding CarMake instance
    car_model_data = [
        {
            "name": "Pathfinder",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
        },
        {
            "name": "Qashqai",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
        },
        {
            "name": "XTRAIL",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
        },
        {
            "name": "A-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
        },
        {
            "name": "C-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
        },
        {
            "name": "E-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[1],
        },
        {
            "name": "A4",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2],
        },
        {
            "name": "A5",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2],
        },
        {
            "name": "A6",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[2],
        },
        {
            "name": "Sorrento",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[3],
        },
        {
            "name": "Carnival",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[3],
        },
        {
            "name": "Cerato",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[3],
        },
        {
            "name": "Corolla",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[4],
        },
        {
            "name": "Camry",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[4],
        },
        {
            "name": "Kluger",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[4],
        },
        {
            "name": "Fiesta",
            "type": "Hatchback",
            "year": 2023,
            "car_make": car_make_instances[5],
        },
        {
            "name": "Focus",
            "type": "Hatchback",
            "year": 2023,
            "car_make": car_make_instances[5],
        },
        {
            "name": "Ranger",
            "type": "Pickup",
            "year": 2023,
            "car_make": car_make_instances[5],
        },
        {
            "name": "Cruze",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[6],
        },
        {
            "name": "Colorado",
            "type": "Pickup",
            "year": 2023,
            "car_make": car_make_instances[6],
        },
        {
            "name": "Equinox",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[6],
        },
        {
            "name": "Sonata",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[7],
        },
        {
            "name": "Tucson",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[7],
        },
        {
            "name": "Santa Fe",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[7],
        },
        {
            "name": "X3",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[8],
        },
        {
            "name": "X5",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[8],
        },
        {
            "name": "X7",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[8],
        },
        {
            "name": "Golf",
            "type": "Hatchback",
            "year": 2023,
            "car_make": car_make_instances[9],
        },
        {
            "name": "Passat",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances[9],
        },
        {
            "name": "Tiguan",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[9],
        },
    ]
    for data in car_model_data:
        CarModel.objects.create(
            name=data["name"],
            type=data["type"],
            year=data["year"],
            car_make=data["car_make"],
        )
