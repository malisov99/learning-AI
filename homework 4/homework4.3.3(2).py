from cars import AutonomousCar

car = AutonomousCar("NeoCAR", "T-20")

car.show_status()
car.drive_to("Центральный парк")
car.show_status()
car.charge()
car.show_status()