#complete your tasks in this file
#task 1
from dataclasses import dataclass
import math
@dataclass(frozen=True)
class GlobeRect:
    lo_lat: float
    hi_lat: float
    west_long: float
    east_long: float

@dataclass(frozen=True)
class Region:
    rect: GlobeRect #is this correct
    name: str
    terrain: str
@dataclass(frozen=True)
class RegionCondition:
    region: Region #is this correct
    year: int
    pop: int
    ghg_rate: float

#Task 2
region_conditions = [
    RegionCondition(
    Region(GlobeRect(28.24,28.53,76.50,77.20),"Delhi","other"),2025,34670000,25000000.0
    ),

    RegionCondition(
        Region(GlobeRect(19.43,19.4,-99.13,-99.1),"Mexico City","other"),2025, 22700000,36600000.0
    ),

    RegionCondition(
        Region(GlobeRect(-10.0, -8.0, -150.0, -148.0),"Abyssopelagic Zone", "ocean"), 2025, 0,0.0
    ),

    RegionCondition(
        Region(GlobeRect(35.3,35.4,-120.9,-120.8),"Morro Bay","other"), 2025,10550,110000.0
    )

]


#task 3:

def emissions_per_capita(rc: RegionCondition) -> float:
    #Purpose Statement: Return the CO2 emission per person via taking each region's ghg_rate divided by the region's population.
    if rc.pop == 0:
        return 0.0
    emissions_per_person = rc.ghg_rate/rc.pop
    return emissions_per_person

#remember when using sin/cos/tan -> use rad
def area(gr: GlobeRect) -> float:
    #Purpose statement: Caluclate the area of based on the Globe Rect latitude and longitude in radians (in sqaure kilometes).
    earth_rad = 6378.1
    lo_lat_rad = math.radians(gr.lo_lat)
    hi_lat_rad = math.radians(gr.hi_lat)
    west_long_rad = math.radians(gr.west_long)
    east_long_rad = math.radians(gr.east_long)
    dist_west_east = east_long_rad - west_long_rad
    if dist_west_east < 0:
        dist_west_east += 2 * math.pi
    area_ft = (earth_rad**2) * abs(dist_west_east) * abs((math.sin(lo_lat_rad) - math.sin(hi_lat_rad)))
    return area_ft

def emissions_per_square_km(rc: RegionCondition) -> float:
    #Using the area function return the tons of Co2 equivalent per sqare kiolmeter by dividing the recions ghg rate by the area emission.
    area_emission = area(rc.region.rect)
    if area_emission == 0:
        return 0.0
    emissions_per_square = rc.ghg_rate/area_emission
    return emissions_per_square

def densest(rc_list: list[RegionCondition]) -> float:
    #finding the highest populated by density region, it will return the name of the region only. (using recursion)
    main_rc = densest_helper(rc_list[1:], rc_list[0])
    return main_rc.region.name
def densest_helper(rc_list: list[RegionCondition], best_so_far: RegionCondition) -> RegionCondition:
    if not rc_list:
        return best_so_far
    current = rc_list[0]
    current_area = area(current.region.rect)
    if current_area > 0:
        current_density = current.pop / current_area
    else:
        return 0.0
    best_area = area(best_so_far.region.rect)
    if best_area > 0:
        best_density = best_so_far.pop / best_area
    else:
        return 0.0
    if current_density > best_density:
        new_best = current
    else:
        new_best = best_so_far

    return densest_helper(rc_list[1:], new_best)




#task 4:
def project_condition(rc: RegionCondition,years: int) -> RegionCondition:
    #Returns a new RegionCondition with the projected state of the region's population based on the terrain.
    if rc.region.terrain == "ocean":
        rate = .0001
    elif rc.region.terrain == "mountain":
        rate = .0005
    elif rc.region.terrain == "forest":
        rate = -.00001
    else:
        rate = .00003

    compounding = ( 1 + rate )** years

    current_year = rc.year + years
    current_pop = int(rc.pop * compounding)
    current_ghg = rc.ghg_rate * compounding
    return RegionCondition(rc.region, current_year, current_pop, current_ghg)
