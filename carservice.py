from sqlalchemy.orm import Session
from models import Car


def add_car(db: Session, name: str, model: str, year: int):
    car = Car(name=name, model=model, year=year)
    db.add(car)
    db.commit()
    db.refresh(car)
    return car


def get_car(db: Session, car_id: int):
    return db.query(Car).filter(Car.id == car_id).first()


def delete_car(db: Session, car_id: int):
    car = db.query(Car).filter(Car.id == car_id).first()
    if car:
        db.delete(car)
        db.commit()
        return True
    return False
