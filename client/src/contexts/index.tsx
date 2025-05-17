import { ThemeProvider } from "@/theme";
import type { ReactElement } from "react";

export function ContextProvider({children}: {children: ReactElement}){
    return (
        <ThemeProvider>
            {children}
        </ThemeProvider>
    )
}