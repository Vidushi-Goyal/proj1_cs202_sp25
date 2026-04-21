#complete your tasks in this file
#task 1
from dataclasses import dataclass
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
    if rc.pop == 0:
        return 0.0
    emissions_per_person = rc.ghg_rate/rc.pop
    return emissions_per_person

def area(gr: GlobeRect) -> float:
#task 4: 8:00-10:00: finish assignment submit
