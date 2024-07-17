const app = require("./src/app");

const PORT = 8000;

app.set('port', PORT);
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});