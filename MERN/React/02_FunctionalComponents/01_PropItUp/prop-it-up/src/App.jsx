
import PersonCard from './components/PersonCard'

function App() {
  return (
    <>
      <h1>Person Cards:</h1>
      <PersonCard firstName={"John"} lastName = {"Jones"} age = {34} hairColor = {"Black"}/>
      <PersonCard firstName={"Bob"} lastName = {"Smith"} age = {27} hairColor = {"Brown"}/>
      <PersonCard firstName={"Bill"} lastName = {"Jackson"} age = {41} hairColor = {"Blonde"}/>
      <PersonCard firstName={"Alexa"} lastName = {"Anderson"} age = {23} hairColor = {"Purple"}/>
    </>
  )
}

export default App
