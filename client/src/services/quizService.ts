import type { Quiz } from "@/types";
import { Service } from "./Service";

class QuizService extends Service<Quiz> {
    constructor (){
        super('/quiz')
    }
}

export const quizService = new QuizService()