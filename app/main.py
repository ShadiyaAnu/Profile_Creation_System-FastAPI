from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud, database, validations
from fastapi import HTTPException

app = FastAPI()

# Create tables in the database
models.Base.metadata.create_all(bind=database.engine)

@app.post("/profiles/", response_model=schemas.StudentProfileOut)
def create_profile(profile: schemas.StudentProfileCreate, db: Session = Depends(database.get_db)):
    validations.validate_password(profile.password)
    try:
        return crud.create_student_profile(db, profile)
        
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error creating profile. Email may already exist.")
    
