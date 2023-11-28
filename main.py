from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Fruit, get_db, database

app = FastAPI()

# Define async functions for startup and shutdown events
async def connect_to_db():
    await database.connect()

async def disconnect_from_db():
    await database.disconnect()

# Event Handlers
app.add_event_handler("startup", connect_to_db)
app.add_event_handler("shutdown", disconnect_from_db)

@app.get("/fruits")
async def get_fruits(db: Session = Depends(get_db)):
    return db.query(Fruit).all()

@app.get("/fruits/{fruit_id}")
async def get_fruit(fruit_id: int, db: Session = Depends(get_db)):
    return db.query(Fruit).filter(Fruit.id == fruit_id).first()

@app.post("/add-fruit")
async def add_fruit(fruit: Fruit, db: Session = Depends(get_db)):
    db.add(fruit)
    db.commit()
    db.refresh(fruit)
    return fruit
