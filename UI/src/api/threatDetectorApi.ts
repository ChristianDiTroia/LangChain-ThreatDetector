import axios from "axios";

const threatDetectorClient = axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export async function fetchThreatAnalysis(text: string) {
    return await threatDetectorClient.post("/threat-analysis", { text: text })
    .then((response) => {
        console.log("Threat analysis response:", response.data);
        return JSON.stringify(response.data, null, 4);
    }).catch((error) => {
        console.error("Error fetching threat analysis:", error);
        return "Failed to fetch threat analysis.";
    });
}