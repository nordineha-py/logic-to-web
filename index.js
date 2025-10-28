import express from "express";

const app = express();
app.use(express.text()); // handle plain text requests (like "10000000")

// GET route — for quick testing in browser
app.get("/", (req, res) => {
  const now = new Date();
  const time = `${now.getHours().toString().padStart(2, "0")}:${now.getMinutes()
    .toString()
    .padStart(2, "0")}:${now.getSeconds().toString().padStart(2, "0")}`;
  res.send(`Logic-to-Web API active — current server time: ${time}`);
});

// Helper: Convert number to 8-bit binary
function to8BitBinary(n) {
  return n.toString(2).padStart(8, "0");
}

// Helper: Split a two-digit number into tens and ones
function splitDigits(value) {
  return [Math.floor(value / 10), value % 10];
}

// POST route — Build Logic sends binary signals here
app.post("/", (req, res) => {
  try {
    const code = req.body.trim();
    const now = new Date();
    const [hourTens, hourOnes] = splitDigits(now.getHours());
    const [minTens, minOnes] = splitDigits(now.getMinutes());
    const [secTens, secOnes] = splitDigits(now.getSeconds());

    let response = "00000000";

    switch (code) {
      case "10000000":
        response = to8BitBinary(hourTens);
        break;
      case "01000000":
        response = to8BitBinary(hourOnes);
        break;
      case "00100000":
        response = to8BitBinary(minTens);
        break;
      case "00010000":
        response = to8BitBinary(minOnes);
        break;
      case "00001000":
        response = to8BitBinary(secTens);
        break;
      case "00000100":
        response = to8BitBinary(secOnes);
        break;
      case "00000010":
        response = "11111111"; // Ping / test
        break;
      case "00000001":
        response = "00000000"; // Placeholder / reset
        break;
      default:
        response = "00000000"; // Fallback for unknown codes
    }

    res.type("text/plain").send(response);
  } catch (err) {
    console.error("Error processing request:", err);
    res.status(500).type("text/plain").send("00000000");
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Logic menu running on port ${PORT}`));
