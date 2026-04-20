#complete your tasks in this file
#task 1
from dataclasses import dataclass
@dataclass(frozen=True)
class GlobeRect:
    low_lat: float
    high_lat: float
    west_long: float
    east_long: float

@dataclass(frozen=True)
class Region:
    rect: GlobeRect #is this correct
    name: str
    terrain: str #how to make this be in certain boundaries like "ocean","moutain","forest", or "other"
@dataclass(frozen=True)
class RegionCondition:
    region: Region #is this correct
    year: int
    pop: int
    ghg_rate: float

#Task 2



#task 3: finish by it infrastructure: so that when I come back

#task 4: 8:00-10:00: finish assignment submit
