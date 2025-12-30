import express from 'express';
import cors from 'cors';

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.json({ limit: '50mb' })); // Increased limit for base64 images

app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello from Node.js backend!' });
});

app.post('/api/chat', (req, res) => {
  const { message, image } = req.body;
  console.log('Received message:', message);
  if (image) {
    console.log('Received image (base64 string)');
  }
  
  res.json({ 
    reply: `Backend received your message: ${message}${image ? ' (with an image)' : ''}`
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

