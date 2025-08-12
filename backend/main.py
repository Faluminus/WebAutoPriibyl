from fastapi import FastAPI, Query, Path, Body, status
from fastapi.responses import JSONResponse
from typing import Annotated
from variables import *
from uuid import UUID

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#------------------------------------------- CLASSIC USER --------------------------------------------

#                                        *****FORM USER****
@app.post("/form", status_code=status.HTTP_200_OK)
async def create_form(form: Form) -> JSONResponse:
    return JSONResponse({"status": "OK"})

#                                           *****AUTH****
@app.post("/login", response_model=UserOut)
async def login(user_in: UserIn)-> BaseUser:
    pass

#                                      *****PART CRUDS USER****
@app.get('/parts/{part_id}', status_code=status.HTTP_200_OK, response_model=PartDetail)
async def get_part(part_id: Annotated[UUID, Path(min_length=EXACT_LENGTH_UUID, max_length=EXACT_LENGTH_UUID)]) -> PartDetail:
    pass

@app.post('/parts/filtered', status_code=status.HTTP_200_OK,
          response_model=list[ListedPart], response_model_exclude_none=True)
async def get_multiple_parts(offset: Annotated[int, Query(regex="^[0-9]+$")],
                             limit: Annotated[int, Query(regex="^[0-9]+$")],
                             searched_part: Annotated[str, Query(max_length=MAX_LENGTH_PART_NAME)],
                             part_filter: Annotated[PartsFilter|None, Body(embed=True)] = None
                             ) -> list[ListedPart]:
    pass

#                                      *****CAR CRUDS USER****
@app.get('/cars/{car_id}', status_code=status.HTTP_200_OK, response_model=ListedCar)
async def get_car(car_id: Annotated[UUID, Path(min_length=EXACT_LENGTH_UUID, max_length=EXACT_LENGTH_UUID)]
                  ) -> ListedCar:
    pass

@app.get('/car/filter', status_code=status.HTTP_200_OK,)
async def get_multiple_cars(offset: Annotated[int, Query(regex="^[0-9]+$")],
                             limit: Annotated[int, Query(regex="^[0-9]+$")],
                             searched_car: Annotated[str, Query(max_length=MAX_LENGTH_CAR_NAME)],
                             car_filter: Annotated[PartsFilter|None, Body(embed=True)] = None
                             ) -> list[ListedCar]:
    pass


#------------------------------------------ ADMIN ENDPOINTS ------------------------------------------------

#                                      *****CAR CRUDS ADMIN****
@app.delete('/car/{car_id}', status_code=status.HTTP_200_OK, response_model=ListedCar)
async def delete_car(car_id: Annotated[UUID, Path(min_length=EXACT_LENGTH_UUID, max_length=EXACT_LENGTH_UUID)]
                     ) -> ListedCar:
    pass

@app.put('/car/{car_id}', status_code=status.HTTP_200_OK, response_model=ListedCar)
async def update_car(car_id: Annotated[UUID, Path(min_length=EXACT_LENGTH_UUID , max_length=EXACT_LENGTH_UUID)]
                     , car: ListedCar) -> ListedCar:
    pass

@app.post('/cars', status_code=status.HTTP_201_CREATED, response_model=list[ListedCar])
async def add_cars(car: list[ListedCar]) -> list[ListedCar]:
    pass

#                                      *****PART CRUDS ADMIN****
@app.delete('/parts/{part_id}', status_code=status.HTTP_200_OK, response_model=PartDetail)
async def delete_part(part_id: Annotated[UUID, Path(min_length=EXACT_LENGTH_UUID, max_length=EXACT_LENGTH_UUID)]
                      ) -> PartDetail:
    pass

@app.post('/parts', status_code=status.HTTP_201_CREATED, response_model=list[PartDetail])
async def add_parts(parts: list[PartDetail]) -> list[PartDetail]:
    pass

@app.put('/parts/{part_id}', status_code=status.HTTP_200_OK, response_model=PartDetail)
async def update_part(part_id: Annotated[UUID, Path(min_length=EXACT_LENGTH_UUID, max_length=EXACT_LENGTH_UUID)],
                      part: PartDetail) -> PartDetail:
    pass
#                                      *****FORM CRUDS ADMIN****
@app.delete('/form/delete', status_code=status.HTTP_200_OK)
async def delete_form(form: Form) -> JSONResponse:
    pass
