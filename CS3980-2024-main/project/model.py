from pydantic import BaseModel

class Exercise(BaseModel):
    id: int
    name: str
    weight: float
    reps: int
    sets: int
    difficulty: str
    details: str

class ExerciseRequest(BaseModel):
    name: str
    weight: float
    reps: int
    sets: int
    difficulty: str
    details: str
