const SheetsAPIClass = require("./sheets-api")
const api = new SheetsAPIClass()

const http = require("http")

function jsonParser(blob) {
    let parsed = JSON.parse(blob);
    if (typeof parsed === 'string') parsed = jsonParser(parsed);
    return parsed;
}

function removeSlash(str) {// s/o chat gpt
    if (str.startsWith("/")) {
        str = str.slice(1);
    }
    if (str.endsWith("/")) {
        str = str.slice(0, -1);
    }
    return str;
}


api.init().then(() => {
    const server = http.createServer((req, res) => {
        if(req.method === "POST"){
            let postData=""
            req.on("data", chunk => {
                postData+=chunk.toString()
            })
            req.on("end", () => {
                let jsonData = jsonParser(postData)
                if(jsonData.date === "now") {
                    api.addDataForDay(removeSlash(req.url), jsonData.dataPlante).then((resultat) => {
                        console.log(removeSlash(req.url))
                        res.writeHead(200)
                        res.end(resultat)
                        console.log("dernière requête à " + (new Date()).toLocaleDateString("fr-FR") + ": " + resultat)
                    })
                }
                else {
                    api.addDataForDay(removeSlash(req.url), jsonData.dataPlante, jsonData.date).then((resultat) => {
                        console.log(removeSlash(req.url))
                        res.writeHead(200)
                        res.end(resultat)
                        console.log("dernière requête à " + (new Date()).toLocaleDateString("fr-FR") + ": " + resultat)
                    })
                }
            })
        }
        else {
            res.writeHead(405)
            res.end("IL FAUT UN 'POST' COMME DETAILLE DANS LE README DU GITHUB !")
        }
    })
    
    server.listen(42069)
    
    console.log("server started on port 42069")
})