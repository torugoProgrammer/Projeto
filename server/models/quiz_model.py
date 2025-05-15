from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Quiz(BaseModel):
    id: int 
    start_time: datetime
    end_time: Optional[datetime]
    
    question_one_id: int 
    question_two_id: int 

class QuizDTO(BaseModel):
    end_time: Optional[datetime]
    question_one_id: int
    question_two_id: int
    