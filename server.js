const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const app = express();
const port = 3000; // You can change the port if necessary

app.use(bodyParser.json());
app.use(express.static('public'));

let books = [];

app.get('/api/books', (req, res) => {
    res.json(books);
});

app.post('/api/books', (req, res) => {
    const { title, author } = req.body;
    books.push({ title, author });
    res.json(books);
});

// Serve the index.html file at the root URL
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
