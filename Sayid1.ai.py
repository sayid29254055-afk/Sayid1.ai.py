# Sayid1.ai.py
const axios = require("axios");
const fs = require("fs");

async function generateVoice(text) {
  const response = await axios({
    method: "POST",
    url: "https://api.elevenlabs.io/v1/text-to-speech/VOICE_ID",
    headers: {
      "xi-api-key": "YOUR_API_KEY",
      "Content-Type": "application/json"
    },
    data: {
      text: text
    },
    responseType: "arraybuffer"
  });

  fs.writeFileSync("voice.mp3", response.data);
}// server.js
const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

app.post("/ai-chat", async (req, res) => {
  const message = req.body.message;

  try {
    const response = await axios.post(
      "https://api.openai.com/v1/chat/completions",
      {
        model: "gpt-4.1-mini",
        messages: [{ role: "user", content: message }]
      },
      {
        headers: {
          Authorization: `Bearer YOUR_OPENAI_KEY`
        }
      }
    );

    res.json(response.data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("Server running");
});
