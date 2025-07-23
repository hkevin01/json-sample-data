// Entry point for data processing
// ...existing code...

/**
 * Example function to load JSON data
 */
const fs = require('fs');
const path = require('path');

function loadSampleData(filename) {
    const filePath = path.join(__dirname, '../data', filename);
    return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
}

module.exports = { loadSampleData };
