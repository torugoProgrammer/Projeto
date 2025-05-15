from pydantic import BaseModel

class Question(BaseModel):
    id: int
    answersCorrect: str
    answersIncorrect: str
    question: str
    
class QuestionDTO(BaseModel):
    answersCorrect: str
    answersIncorrect: str
    question: str