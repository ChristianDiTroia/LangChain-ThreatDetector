import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "./assets/vite.svg";
import TextInput from "./components/TextInput";
import Button from "./components/Button";
import { fetchThreatAnalysis } from "./api/threatDetectorApi";
import TextDisplay from "./components/TextDisplay";

function Header({ className }: { className?: string }) {
  return (
    <>
      <div className={`w-[80vw] m-auto ${className}`}>
        <h1 className="font-bold italic text-3xl flex justify-center pt-4">
          Threat Detector
        </h1>
        <div className="border-b-2 my-4 flex justify-center" />
        <div className="flex justify-center">
          <img
            src={viteLogo}
            className="mx-4 drop-shadow-[0_0_10px_#10b981]"
            alt="Vite logo"
          />
          <img
            src={reactLogo}
            className="mx-4 drop-shadow-[0_0_10px_#06b6d4]"
            alt="React logo"
          />
        </div>
      </div>
    </>
  );
}

function App() {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");

  return (
    <>
      <Header />
      <div className="max-w-[80vw] min-h-[50vh] my-10 mx-auto p-4">
        <div className="grid grid-cols-2 gap-4">
          <TextInput
            className="w-full"
            label="Input Text To Analyze Threat Level"
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <TextDisplay className="mt-8" value={output} />
        </div>
        <div className="w-full flex justify-center">
          <Button
            className="bg-emerald-500 shadow-2xl/50 rounded-2xl my-4"
            label="Perform Threat Analysis"
            onClick={async () => {
              fetchThreatAnalysis(input).then((data) => {
                setOutput(data);
              });
            }}
          />
        </div>
      </div>
    </>
  );
}

export default App;
