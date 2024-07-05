from sqlalchemy.orm import Session

import models, schemas


def get_medecin(db: Session, medecin_id: int):
    return db.query(models.Medecin).filter(models.User.id == medecin_id).first()


#def get_users(db: Session, skip: int = 0, limit: int = 100):
#    return db.query(models.User).offset(skip).limit(limit).all()


def create_medecin(db: Session, medecin: schemas.Medecin):
    #db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db_medecin=models.Medecin(**medecin.dict())
    db.add(db_medecin)
    db.commit()
    db.refresh(db_medecin)
    return db_medecin

def create_ville(db: Session, ville: schemas.Ville):
    #db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db_ville=models.Ville(**ville.dict())
    db.add(db_ville)
    db.commit()
    db.refresh(db_ville)
    return db_ville

def get_medecins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Medecin).offset(skip).limit(limit).all()

def get_specialities(db:Session):
    return db.query(models.Speciality).all()

def get_villes(db:Session):
    return db.query(models.Ville).all()

def get_docs_by_speciality(special_id,db:Session):
    return db.query(models.Medecin).where(models.Medecin.speciality_id==special_id).all()

def update_medecin(medecin,medecin_id,db:Session):

    db.query(models.Medecin).filter(models.Medecin.id==medecin_id).update(medecin,synchronize_session = False)
    db.commit()
    medecin= db.get(models.Medecin,medecin_id)
    return medecin

def delete_medecin(medecin_id,db:Session):

    a=db.query(models.Medecin).filter(models.Medecin.id==medecin_id).delete()
    db.commit()
    return a

def get_cabinets(db:Session, skip=0, limit=0):
    return db.query(models.Cabinet).offset(skip).limit(limit).all()