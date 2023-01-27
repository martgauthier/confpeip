const { GoogleSpreadsheet } = require('google-spreadsheet');

const HEADER_ROW = 3;
const CONFIG_FILE_PATH = './config/confpeip-gsheets.json';

module.exports = class SheetsAPI {
    constructor() {
        this.config = require(CONFIG_FILE_PATH);
        this.doc = new GoogleSpreadsheet(this.config.sheetfile_id);
    }

    async init() {
        this.doc.useServiceAccountAuth({
            client_email: this.config.client_email,
            private_key: this.config.private_key
        })

        await this.doc.loadInfo()
        
        this.sheets=this.doc.sheetsByTitle

        for(const sheetTitle in this.sheets) {
            await this.sheets[sheetTitle].loadHeaderRow(HEADER_ROW)
            this.sheets[sheetTitle].rows = await this.sheets[sheetTitle].getRows()
        }
    }

    async addDataForDay(sheetName, dataPlante, date=((new Date()).toLocaleDateString("fr-FR") + "-" + (new Date()).getHours().toString().padStart(2, "0"))) { //date au format 01/01/1970 pour le 1er janvier 1970
        if(!(Object.keys(this.sheets).includes(sheetName))){
            await this.sheets["TEMPLATE"].duplicate({
                title: sheetName
            })

            await this.doc.loadInfo()

            this.sheets=this.doc.sheetsByTitle

            for(const sheetTitle in this.sheets) {
                await this.sheets[sheetTitle].loadHeaderRow(HEADER_ROW)
                this.sheets[sheetTitle].rows = await this.sheets[sheetTitle].getRows()
            }
        }
        
        let rowIndex = -1
        for (let i = 1; i <=2100; i++) {//100 pour prendre un grand nombre de jours
            if(this.sheets[sheetName].rows[i].Date === date) rowIndex=i;
            //console.log(this.sans.rows[i])
        }
        if(rowIndex === -1) {
            return "date introuvable"
        }
        else {
            let row = this.sheets[sheetName].rows[rowIndex]
            
            //instanciation des données
            row["Température"]=dataPlante.temperature
            row["humidité air"]=dataPlante.humiditeAir
            row["humidité sol"]=dataPlante.humiditeSol
            if(dataPlante.etatPlante !== -1) row["note de l'état de la plante"]=dataPlante.etatPlante
            if(dataPlante.commText !== "null") row["Commentaire textuel (optionnel)"]=dataPlante.commText
            if(dataPlante.arrosage !== "Pas encore fait") row["A dû arroser"]=dataPlante.arrosage

            await row.save()
            return "reussi"
        }
    }
}