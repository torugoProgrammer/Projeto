import { Header, InputCard } from '@/components/ui'
import { useAppContext } from '@/context/contextProvider'
import { questionService } from '@/services/questionService'
import { useMutation } from '@tanstack/react-query'
import { createFileRoute, useNavigate } from '@tanstack/react-router'

export const Route = createFileRoute('/')({
  component: App,
})

function App() {
  const navigate = useNavigate()
  const {setUser, user, setQuestions} = useAppContext()
  const {mutateAsync, isPending} = useMutation({
    mutationFn: () => questionService.takeRandom(2)
  })
  
  const startQuiz = async () => {
    if (!user?.name || !user?.cpf) return
    await mutateAsync(undefined, {
      onSuccess({data}){
        setQuestions(data)
        navigate({ to: "/quiz" })
      },
      onError(){}
    })
  }

  return (
    <div className='h-screen w-full '>
      <Header />
      <InputCard />
      <div className="flex flex-col items-center justify-center">
        <div className="btn btn-outline btn-secondary bg border-neutral rounded-2xl border-1 btn-wide w-2/4 m-3 h-12 flex items-center justify-center ">
          <p>Exportar Dados</p>
        </div>
        <button onClick={startQuiz} className="btn btn-primary border-1 rounded-2xl w-2/4 flex justify-center center items-center h-12">
          {isPending && (  
            <span className='loading loading-spinner'></span>
          )}
          <p>Começar</p>
        </button>
      </div>
    </div>
  )
}