const { connectToDatabase } = require('./mongo');

module.exports = async (req, res) => {
  if (req.method !== 'GET') {
    res.status(405).json({ ok: false, error: 'Método no permitido. Usa GET para obtener datos.' });
    return;
  }

  const limit = Math.min(Number(req.query.limit) || 20, 100);

  try {
    const client = await connectToDatabase();
    const db = client.db();
    const collection = db.collection('records');
    const items = await collection.find({}).sort({ createdAt: -1 }).limit(limit).toArray();

    res.status(200).json({ ok: true, count: items.length, items });
  } catch (error) {
    console.error(error);
    res.status(500).json({ ok: false, error: error.message });
  }
};
