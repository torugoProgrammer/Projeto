import { useAppContext } from '@/context/contextProvider'
import { createFileRoute, useNavigate } from '@tanstack/react-router'
import { useState } from 'react'

export const Route = createFileRoute('/quiz')({
  component: RouteComponent,
})

function RouteComponent() {
  const [questionIndex, setQuestionIndex] = useState<number>(0)
  const { questions, setQuestions } = useAppContext()
  const navigate = useNavigate()
  
  const incorrectAnswers = questions[questionIndex].answersIncorrect.split(',')
  const correctAnswer = questions[questionIndex].answersCorrect
  
  const answers = [ 
    ...incorrectAnswers.map(answer => ({ text: answer, isCorrect: false })),
    { text: correctAnswer, isCorrect: true }
   ]
  console.log(answers);

  /*
    ['a', 'b', 'c', 'd'] // answers

    [
      {text: 'a', isCorrect: true},
      {text: 'b', isCorrect: false},
      {text: 'c', isCorrect: false},
      {text: 'd', isCorrect: false},
    ] // answers (modded)
  
    confirm() {
      ...
      answers.forEach(answer => answer.isCorrect ? setScore(1) : setScore(0))
    }
  */  
  
  const questionCard = ( 
    <div className='card rounded-3xl card-xs w-80 h-110 p-10 bg-indigo-400 flex items-center'>
      <fieldset className='fieldset font-bold '>
        <legend className='fieldset-legend border-1 rounded-2xl p-2'>
          Questão Número {questionIndex + 1}: <br /> {questions[questionIndex].question}
        </legend>
      </fieldset>
      <div className=''>
        {/* {answers}       */}
      </div>
      <button onClick={confirm} className='btn btn-outline'>confirm</button>
    </div>
  )

  function confirm() {
    if (questionIndex === 1) {
      setQuestions([])
      navigate({ to: '/' })
    } else setQuestionIndex(prev => prev + 1)
  }

  return (
    <div className='h-screen w-full p-3 flex justify-center items-center'>
      {questionCard}
    </div>
  )
}