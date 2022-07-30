from fastapi import FastAPI, Depends, status,HTTPException
from . import models, schemas
from . database import engine, SessionLocal
from sqlalchemy.orm import session
from geopy import Nominatim
from typing import List

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create the Address Book

@app.post('/address', status_code=status.HTTP_201_CREATED, tags=["Address Book"])
async def Create_addressbook(request:schemas.Address, db : session= Depends(get_db)):
    new_address=models.Address(First_name=request.First_name,Last_name=request.Last_name, Latitude=request.Latitude, Longitude=request.Longitude)
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address
# Update the address book

@app.put('/address/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["Address Book"])
async def Update_addressbook(id, request:schemas.Address, db : session= Depends(get_db)):
    address_updata = db.query(models.Address).filter(models.Address.id==id).first()
    if not address_updata:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Address {id} was not available')
    else:
        db.query(models.Address).filter(models.Address.id==id).update(request.dict())
    db.commit()
    db.refresh(address_updata)
    return address_updata

# Delete the address book

@app.delete('/address/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["Address Book"])
async def Delete_addressbook(id, db : session= Depends(get_db)):
    address_delete= db.query(models.Address).filter(models.Address.id==id).delete(synchronize_session=False)
    db.commit()
    if not address_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Address {id} was not available')
    return {"detial":f'Address {id} was deleted successfully'}

# Api user can retrieve the address of particuler location

@app.get('/address/{id}', status_code=status.HTTP_200_OK, tags=["Address Book"])
async def Retrieve_the_address_from_addressbook(id, db : session= Depends(get_db)):
    get_address = db.query(models.Address).filter(models.Address.id == id).first()
    if not get_address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Address {id} was not available')
    else:
        add1 = db.query(models.Address.Latitude).filter(models.Address.id==id).first()
        add2 = db.query(models.Address.Longitude).filter(models.Address.id==id).first()
        geolocator = Nominatim(user_agent='address/1')
        location = geolocator.reverse(f'{add1[0]},{add2[0]}')
        return {"address" : f"{get_address.First_name} {get_address.Last_name}, {location.address}"}
