const http = require("http");
const fs = require("fs");

const HOST = "0.0.0.0";
const PORT = 8080;

const response = (_, res) => {
  const html = fs.readFileSync("index.html", "utf8");

  res.setHeader("Content-Type", "text/html");
  res.writeHead(200);
  res.end(html);
};

const server = http.createServer(response);
server.listen(PORT, HOST, () => {
  console.log(`[INFO] Server is running on http://${HOST}:${PORT}`);
});
