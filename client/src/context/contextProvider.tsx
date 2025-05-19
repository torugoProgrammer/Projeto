import type { Question, User } from "@/types";
import type { AppContext } from "@/types/AppContext";
import { createContext, useContext, useState, type ReactElement } from "react";

const appContext = createContext({})

export function ContextProvider({children}: {children: ReactElement}) {
    const [user, setUser] = useState<User>()
    const [questions, setQuestions] = useState<Question[]>()
    return(   
        <appContext.Provider value={{user, setUser, questions, setQuestions}}>
            {children}
        </appContext.Provider>
    )
}
export const useAppContext = (): AppContext => useContext(appContext) as AppContext