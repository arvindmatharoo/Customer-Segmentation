from pydantic import BaseModel

class CustomerInput(BaseModel):
    recency : float
    frequency : float
    monetary : float

class SegmentOutput(BaseModel):
    cluster : int
    segment : str

# REcency Number of days since the customer last made a purchase (lower is better)
# Frequency Total Number of unique purchase transaction made by the customer (Higher the better)
# Monetory Total amount of moneyu spent by the customer over time (Higher the better)

