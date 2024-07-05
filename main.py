from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine
import json

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/medecins/", response_model=schemas.MedecinBase)
def create_medecin(medecin: schemas.MedecinBase, db: Session = Depends(get_db)):
    return crud.create_medecin(db,medecin)

##@app.post("/villes/", response_model=schemas.VilleBase)
def create_ville(ville: schemas.VilleBase, db: Session = Depends(get_db)):
    return crud.create_ville(db,ville)


@app.get("/medecins/", response_model=list[schemas.Medecin])
def read_medecins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    list_medecins = crud.get_medecins(db, skip=skip, limit=limit)
    return list_medecins

@app.get("/specialites/", response_model=list[schemas.SpecialityBase])
def read_specialities(db: Session = Depends(get_db)):
    list_specialities = crud.get_specialities(db)
    return list_specialities

@app.get("/villes/", response_model=list[schemas.Ville])
def read_villes(db: Session = Depends(get_db)):
    list_ville = crud.get_villes(db)
    return list_ville

@app.get("/{speciality}/medecins", response_model=list[schemas.Medecin])
def get_docs_by_speciality(speciality:int, db: Session = Depends(get_db)):
    list_medecins = crud.get_docs_by_speciality(speciality,db)
    return list_medecins  

@app.patch("/medecins/{medecin_id}",response_model=schemas.Medecin)
def update_doc(medecin:dict,medecin_id:int, db: Session = Depends(get_db)):
    medecin = crud.update_medecin(medecin,medecin_id,db)
    return medecin

@app.delete("/medecins/{medecin_id}")
def delete_doc(medecin_id:int, db: Session = Depends(get_db)):
    resp = crud.delete_medecin(medecin_id,db)
    return resp

@app.get("/cabinets/",response_model=list[schemas.Cabinet])
def get_cabinets(db: Session = Depends(get_db),skip: int = 0, limit: int = 100,):
    list_cabinets = crud.get_cabinets(db, skip=skip, limit=limit)
    return list_cabinets