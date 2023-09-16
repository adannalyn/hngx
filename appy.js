const express = require('express');
const bodyParser = require('body-parser');
const { MongoClient, ObjectId } = require('mongodb');

const app = express();
const port = process.env.PORT || 3000;
app.use(bodyParser.json());

// MongoDB Atlas connection string (replace <password> with your actual password)
const uri = "mongodb+srv://chinyere:uqqzMpiisHWJDX0f@jobinairee.pgajtf0.mongodb.net/?retryWrites=true&w=majority";

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Function to connect to MongoDB Atlas
async function connectToMongoDB() {
  try {
    await client.connect();
    console.log("Connected to MongoDB Atlas");
    return client.db(); // Return the database object
  } catch (error) {
    console.error("Error connecting to MongoDB Atlas:", error);
    throw error;
  }
}

// CREATE: Adding a new person
app.post('/api/people', async (req, res) => {
  const db = await connectToMongoDB();
  const collection = db.collection('people');
  const personData = req.body;

  try {
    const result = await collection.insertOne(personData);
    if (result.insertedCount === 1) {
      res.status(201).json(result.ops[0]);
    } else {
      res.status(500).json({ error: 'Failed to create a person' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// READ: Fetching details of a person by ID
app.get('/api/people/:id', async (req, res) => {
  const db = await connectToMongoDB();
  const collection = db.collection('people');
  const personId = req.params.id;

  try {
    const person = await collection.findOne({ _id: ObjectId(personId) });
    if (!person) {
      res.status(404).json({ error: 'Person not found' });
    } else {
      res.status(200).json(person);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// UPDATE: Modifying details of an existing person by ID
app.put('/api/people/:id', async (req, res) => {
  const db = await connectToMongoDB();
  const collection = db.collection('people');
  const personId = req.params.id;
  const updatedData = req.body;

  try {
    const result = await collection.updateOne(
      { _id: ObjectId(personId) },
      { $set: updatedData }
    );
    if (result.matchedCount === 0) {
      res.status(404).json({ error: 'Person not found' });
    } else {
      res.status(200).json({ message: 'Person updated successfully' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// DELETE: Removing a person by ID
app.delete('/api/people/:id', async (req, res) => {
  const db = await connectToMongoDB();
  const collection = db.collection('people');
  const personId = req.params.id;

  try {
    const result = await collection.deleteOne({ _id: ObjectId(personId) });
    if (result.deletedCount === 0) {
      res.status(404).json({ error: 'Person not found' });
    } else {
      res.status(204).send(); // No content (successful deletion)
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the Express server after connecting to MongoDB
async function startServer() {
  try {
    const db = await connectToMongoDB();

    // Start the Express server
    app.listen(port, () => {
      console.log(`Server is running on port ${port}`);
    });
  } catch (error) {
    console.error("Failed to start the server:", error);
  }
}

startServer();
