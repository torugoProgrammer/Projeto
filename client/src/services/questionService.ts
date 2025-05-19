import type { Question } from "@/types";
import { Service } from "./Service";

class QuestionService extends Service<Question>{
    constructor (){
        super('/question')
    }
    takeRandom(count: number) {
        return this.instance.get(`/random/${count}`)
    }
}

export const questionService = new QuestionService()