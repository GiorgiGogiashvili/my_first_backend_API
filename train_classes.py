from enum import Enum

class TrainClass(str, Enum):
	express = "express"
	slow = "slow"
	passenger = "passenger"
