from fastapi import FastAPI, Query, Depends
from typing import Optional
from enum import Enum
from train_classes import TrainClass
from trains import Trains
from seats import Seats
from genders import Genders
import datetime
import random
from pydantic import BaseModel

app = FastAPI()


class TrainsSearchArgs:
	def __init__(
		self,
		location_from: str,
		location_to: str,
		train_class: TrainClass,
		has_comfort: Optional[bool] = None,
		date: Optional[datetime.date] = None
	):
		self.location_from = location_from
		self.location_to = location_to
		self.has_comfort = has_comfort
		self.train_class = train_class
		self.date = date or datetime.date.today()



@app.get("/trains")
def get_trains(
	search_args: TrainsSearchArgs = Depends()
):
    return search_args

@app.get("/trains/{train_id}")
def trains_id(train_id: int):
	train = [train for train in Trains.trains if train["id"] == train_id]

	if train:
		return train[0]

	if not train:
		return {"error": "Поезд не найден" }
	pass


class SUseradd(BaseModel):
	first_name: str
	last_name: str
	mail_address: str
	phone_number: str
	gender: Genders
	birthday: datetime.date

@app.post("/useradd")
def add_user(useradd: SUseradd):
	pass

