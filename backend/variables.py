from typing import Annotated
from pydantic import BaseModel, Field
from uuid import UUID
from numpy.typing import NDArray
import numpy as np

class Car(BaseModel):
    brand: str = Field(description="The name of the brand", max_length=50)
    model: str = Field(description="Model of the car", max_length=50)
    type: str = Field(description="Type of the model", max_length=50)
    engine: str = Field(description="Used engine in the car", max_length=50)
    engine_type: str = Field(default=None, description="Type of the engine", max_length=50)
    engine_volume: float = Field(default=None, qt=0, description="Volume of the engine")
    engine_kilowatts: int = Field(default=None, qt=0, description="Kilowatts of the engine")
    engine_horsepower: int = Field(default=None, qt=0, description="Horsepower of the engine")
    valves: Annotated[NDArray[np.int32], 2] = Field(default=None, description="Number of cylinders per valve and amount of valves")

class Part(BaseModel):
    model_config = {"extra":"forbid"}
    uuid: UUID = Field(default=None, description="UUID of the part", max_length=36)
    price: float = Field(qt=0, default=0.0, description="The price of the part must be higher than 0.")
    amount: int = Field(qt=0, default=0, description="The amount of the part must be higher than 0.")
    name: str = Field(default=None, description="The name of the part.", max_length=50)
    description: str | None = Field(default=None, description="Description of the part can contain 500 characters at maximum", max_length=500)
    fits: Car
    special_info: list[dict[str, str]] = Field(default=None, description="Specific info about the part")

class ListedCar(Car):
    model_config = {"extra": "forbid"}
    uuid: UUID = Field(default=None, description="UUID of the part", max_length=36)
    price: float = Field(qt=0, default=0.0, description="The price of the car must be higher than 0.")
    mileage: float = Field(qt=0, default=0.0, description="The mileage of the car must be higher than 0.")
    description: str = Field(description="Description of the part can contain 500 characters at maximum", max_length=500)
    key_features: list[str]
    detail: list[str]
    motor: list[str]
    car_state: list[str]
    interior: list[str]
    exterior: list[str]
    infotainment: list[str]
    other: list[str]

class CarsFilter(BaseModel):
    pass

class BrakesSystem(BaseModel):
    brakes_system: bool = False
    brake_fluid: bool = False
    brake_pipes: bool = False

class Steering(BaseModel):
    steering: bool = False

class SpringAndDampers(BaseModel):
    spring_and_dampers: bool = False

class AxleSuspension(BaseModel):
    axle_suspension: bool = False

class Undercarriage(BaseModel):
    undercarriage: bool = False
    brakes_system: BrakesSystem
    steering: Steering
    spring_and_dampers: SpringAndDampers
    axle_suspension: AxleSuspension


class PartsFilter(BaseModel):
    model_config = {"extra":"forbid"}
    car: Car
    undercarriage: Undercarriage
    pass

class BaseUser(BaseModel):
    username: str
    email: str

class UserIn(BaseUser):
    password: str

class UserOut(BaseUser):
    pass