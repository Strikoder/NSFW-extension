from pydantic import BaseModel

class PhotoRequest(BaseModel):
    photo_path: str


class Prediction(BaseModel):
    #for now
    pass