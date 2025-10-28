import express from "express";

const app = express();
app.use(express.text()); // handle plain text body (like "10000000")

// Helper: Convert number to 8-bit binary
function to8BitBinary(n) {
  return n.toString(2).padStart(8, "0");
}

// Helper: Split two-digit number into tens and ones
function splitDigits(value) {
  return [Math.floor(value / 10), value % 10];
}

app.post("/", (req, res) => {
  const code = req.body.trim();
  const now = new Date();
  const [hourTens, hourOnes] = splitDigits(now.getHours());
  const [minTens, minOnes] = splitDigits(now.getMinutes());
  const [secTens, secOnes] = splitDigits(now.getSeconds());

  let response = "00000000";

  // Match the 8-bit input code
  switch (code) {
    case "10000000": response = to8BitBinary(hourTens); break;
    case "01000000": response = to8BitBinary(hourOnes); break;
    case "00100000": response = to8BitBinary(minTens); break;
    case "00010000": response = to8BitBinary(minOnes); break;
    case "00001000": response = to8BitBinary(secTens); break;
    case "00000100": response = to8BitBinary(secOnes); break;
    case "00000010": response = "11111111"; break; // optional: test or “ping ok”
    case "00000001": response = "00000000"; break; // optional: reset or placeholder
    default: response = "00000000";
  }

  res.send(response);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Logic menu running on port ${PORT}`));
