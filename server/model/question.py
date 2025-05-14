from sqlmodel import SQLModel, Field

class Question(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    answersCorrect: str
    answersIncorrect: str
    question: str
    
# class QuestionDTO(SQLModel):
#     answersCorrect: str
#     answersIncorrect: str
#     question: str