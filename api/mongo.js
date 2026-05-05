const { MongoClient } = require('mongodb');
require('dotenv').config();

const uri = process.env.MONGODB_URI;

if (!uri) {
  throw new Error('MONGODB_URI no está definida. Configura la variable de entorno en Vercel o en un archivo .env.');
}

let cachedClient = global._mongoClient;
let cachedPromise = global._mongoClientPromise;

if (!cachedClient) {
  cachedClient = new MongoClient(uri);
  cachedPromise = cachedClient.connect();
  global._mongoClient = cachedClient;
  global._mongoClientPromise = cachedPromise;
}

async function connectToDatabase() {
  return cachedPromise;
}

module.exports = { connectToDatabase };
