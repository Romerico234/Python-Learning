import math
 
def get_station_data(filename:str):
    stations = {}
    with open(filename) as file:
        for row in file:
            parts = row.split(";")
            if parts[0] == "Longitude":
                continue
            stations[parts[3]] = (float(parts[0]), float(parts[1]))
 
    return stations
 
def distance(stations: dict, station1: str, station2: str):
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]
 
    # Note, that this
    # longitude2, latitude2 = stations[station2]
    # ...is equivalent to
    #
    # coordinates = stations[station2]
    # longitude2 = coordinates[0]
    # latitude2 = coordinates[0]
 
    x_as_km = (longitude1-longitude2) * 55.26
    y_as_km = (latitude1-latitude2) * 111.2
    return math.sqrt(x_as_km**2 + y_as_km**2)
 
def greatest_distance(stations: dict):
    longest = 0
    for start_station in stations:
        for end_station in stations:
            e = distance(stations, start_station, end_station)
            if e > longest:
                station1 = start_station
                station2 = end_station
                longest = e
 
    return station1, station2, longest