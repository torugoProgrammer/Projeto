import type { Dispatch, SetStateAction } from "react";
import type { User } from "./User";
import type { Question } from "./Question";

export interface AppContext {
    user: User,
    setUser: Dispatch<SetStateAction<User>>,
    questions: Question,
    setQuestions: Dispatch<SetStateAction<Question>>,
}