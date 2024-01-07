from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import carservice

app = FastAPI()


# Dependency to get the database session
def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/car/{car_id}")
def get_car_info(car_id: int, db: Session = Depends(get_db)):
    car = carservice.get_car(db, car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


@app.post("/add-car/")
def add_car_info(car_name: str, car_model: str, car_year: int, db: Session = Depends(get_db)):
    car = carservice.add_car(db, car_name, car_model, car_year)
    return car


@app.delete("/car/{car_id}")
def delete_car_info(car_id: int, db: Session = Depends(get_db)):
    success = carservice.delete_car(db, car_id)
    if not success:
        raise HTTPException(status_code=404, detail="Car not found")
    return {"message": "Car deleted successfully"}

