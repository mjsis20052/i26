const { connectToDatabase } = require('./mongo');

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.status(405).json({ ok: false, error: 'Método no permitido. Usa POST para guardar datos.' });
    return;
  }

  const data = req.body;

  if (!data || typeof data !== 'object') {
    res.status(400).json({ ok: false, error: 'Body inválido. Envía un JSON con los datos a guardar.' });
    return;
  }

  try {
    const client = await connectToDatabase();
    const db = client.db();
    const collection = db.collection('records');
    const result = await collection.insertOne({ ...data, createdAt: new Date() });

    res.status(201).json({ ok: true, insertedId: result.insertedId });
  } catch (error) {
    console.error(error);
    res.status(500).json({ ok: false, error: error.message });
  }
};
