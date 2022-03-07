from pydantic import BaseModel, Field
from objectid import PydanticObjectId
from pydantic import BaseModel, Field
from typing import List, Optional, Union
import fastapi

from fastapi.encoders import jsonable_encoder

class IDTags(BaseModel):
    _idtags : Optional[List[str]] = []   

class Attributes(BaseModel):
    attributes : List[str] = [] 

class Collection(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    name: str
    attributes: Optional[List[str]] = []
    #attributes: List[Attributes] = []
    #_idtags = List[IDTags] = []

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data["_id"] is None:
            data.pop("_id")
        return data