const SheetsAPIClass = require("./sheets-api")
const api = new SheetsAPIClass()

const http = require("http")

api.init().then(() => {
    const server = http.createServer((req, res) => {
        if(req.method === "POST"){
            let postData=""
            req.on("data", chunk => {
                postData+=chunk.toString()
            })
            req.on("end", () => {
                let jsonData = JSON.parse(postData)
                if(jsonData.date === "today") {
                    api.addDataForDay(jsonData.sansEngrais, jsonData.avecEngrais).then((resultat) => {
                        res.writeHead(200)
                        res.end(resultat)
                        console.log("dernière requête à " + (new Date()).toLocaleDateString("fr-FR") + ": " + resultat)
                    })
                }
                else {
                    api.addDataForDay(jsonData.sansEngrais, jsonData.avecEngrais, jsonData.date).then((resultat) => {
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