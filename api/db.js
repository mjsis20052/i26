const { connectToDatabase } = require('./mongo');

module.exports = async (req, res) => {
  if (req.method !== 'GET') {
    res.status(405).json({ ok: false, error: 'Método no permitido. Usa GET para probar la conexión.' });
    return;
  }

  try {
    const client = await connectToDatabase();
    const admin = client.db().admin();
    const info = await admin.serverStatus();

    res.status(200).json({
      ok: true,
      message: 'Conectado a MongoDB',
      uptime: info.uptime,
      host: info.host
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ ok: false, error: error.message });
  }
};
