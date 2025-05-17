import { Button } from '@/components/ui/button'
import { useTheme } from '@/theme'
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/')({
  component: Index,
})

function Index() {
  const { setTheme, theme } = useTheme()

  function toggleTheme(){
    if (theme === 'light') setTheme('dark')
    if (theme === 'dark') setTheme('light')
  }

  return (
    <div className="p-2">
      <h3>Welcome Home!</h3>
      <Button variant='outline' onClick={toggleTheme}>Change Theme</Button>
    </div>
  )
}