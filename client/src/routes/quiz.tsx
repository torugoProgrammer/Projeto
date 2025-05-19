import { useAppContext } from '@/context/contextProvider'
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/quiz')({
  component: RouteComponent,
})

function RouteComponent() {
  const {questions} = useAppContext()
  console.log(questions);
  
  return (
  <div className='card bg-indigo-400 rounded-none '>
    <p>quiz</p>
  </div>
  )
}
