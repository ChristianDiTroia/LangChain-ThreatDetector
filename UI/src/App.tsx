import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "./assets/vite.svg";
import TextInput from "./components/TextInput";

function Header({ className }: { className?: string }) {
  return (
    <>
      <div className={`w-[80vw] m-auto ${className}`}>
        <h1 className="font-bold italic text-3xl flex justify-center pt-4">
          Threat Detector
        </h1>
        <div className="border-b-2 my-4 flex justify-center" />
        <div className="flex justify-center">
          <div className="shadow-emerald">
            <img src={viteLogo} className="mx-4 " alt="Vite logo" />
          </div>
          <img src={reactLogo} className="mx-4 shadow-cyan" alt="React logo" />
        </div>
      </div>
    </>
  );
}

function App() {
  const [name, setName] = useState("");

  return (
    <>
      <Header />
      <div className="max-w-4xl my-10 mx-auto flex min-h-[50vh] justify-center p-4">
        <TextInput
          className="w-full"
          label="Demo Input"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </div>
    </>
  );
}

export default App;
