from fastapi import FastAPI, Query, Path, Body, status
from typing import Annotated
from variables import Part, UserIn, UserOut, BaseUser, PartsFilter, ListedCar
from uuid import UUID


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#AUTH
@app.post("/login", response_model=UserOut)
async def login(user_in: UserIn)-> BaseUser:
    pass

#PART CRUDS
@app.get('/parts/{part_id}', status_code=status.HTTP_200_OK, response_model=Part)
async def get_part(part_id: Annotated[UUID, Path(min_length=36, max_length=36)]) -> Part:
    pass

@app.post('/parts/filtered', status_code=status.HTTP_200_OK,
          response_model=list[Part], response_model_exclude_none=True)
async def get_multiple_parts(offset: Annotated[int, Query(regex="^[0-9]+$")],
                             limit: int,
                             part_filter: Annotated[PartsFilter|None, Body(embed=True)] = None
                             ) -> list[Part]:
    pass

@app.post('/parts', status_code=status.HTTP_201_CREATED, response_model=list[Part])
async def add_parts(parts: list[Part]) -> list[Part]:
    pass

@app.put('/parts/{part_id}', status_code=status.HTTP_200_OK, response_model=Part)
async def update_part(part_id: Annotated[UUID, Path(min_length=36, max_length=36)], part: Part) -> Part:
    pass

@app.delete('/parts/{part_id}', status_code=status.HTTP_200_OK, response_model=Part)
async def delete_part(part_id: Annotated[UUID, Path(min_length=36, max_length=36)]) -> Part:
    pass

#CAR CRUDS
@app.get('/cars/{car_id}', status_code=status.HTTP_200_OK, response_model=ListedCar)
async def get_car(car_id: Annotated[UUID, Path(min_length=36, max_length=36)]) -> ListedCar:
    pass

@app.post('/cars', status_code=status.HTTP_201_CREATED, response_model=list[ListedCar])
async def add_cars(car: list[ListedCar]) -> list[ListedCar]:
    pass

@app.put('/car/{car_id}', status_code=status.HTTP_200_OK, response_model=ListedCar)
async def update_car(car_id: Annotated[UUID, Path(min_length=36, max_length=36)], car: ListedCar) -> ListedCar:
    pass

@app.delete('/car/{car_id}', status_code=status.HTTP_200_OK, response_model=ListedCar)
async def delete_car(car_id: Annotated[UUID, Path(min_length=36, max_length=36)]) -> ListedCar:
    pass

@app.get('/car/filter', )
async def get_parts_filtered(q: Annotated[str|None, Query(reqex="")] = None):
    pass

