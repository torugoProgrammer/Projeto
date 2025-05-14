from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Quiz(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    start_time: datetime = Field(default_factory=datetime.now())
    end_time: Optional[datetime]
    
    question_one_id: int | None = Field(None, foreign_key='question.id')
    question_two_id: int | None = Field(None, foreign_key='question.id')

# class QuizDTO(SQLModel):
#     end_time: Optional[datetime]
#     question_one_id: int
#     question_two_id: int
    