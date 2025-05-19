import { useAppContext } from "@/context/contextProvider"

export default function InputCard() {
    const {setUser} = useAppContext()

    return (
        <div className="card flex justify-center items-center relative bottom-20 ">
            <div className="card-body bg-gray-400 w-3/4 text-xl">
                <p className="text-xl">Coloque seus dados:</p>

                <fieldset className="fieldset">
                    <legend className="fieldset-legend">Qual é o seu nome?</legend>
                    <input onChange={ev => setUser(prev => ({...prev, name: ev.target.value}))} type="text" className="input input-neutral bg-white" placeholder="Digite seu nome" />
                </fieldset>
                <fieldset className="fieldset">
                    <legend className="fieldset-legend">Qual é o seu cpf?</legend>
                    <input onChange={ev => setUser(prev => ({...prev, cpf: ev.target.value}))} type="text" className="input input-neutral bg-white" placeholder="Digite seu cpf" />
                </fieldset>
            </div>
        </div>
    )
}