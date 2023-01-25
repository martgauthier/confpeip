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
        
        this.sans = {
            sheet: await this.doc.sheetsByIndex[0]
        }

        this.avec = {
            sheet: await this.doc.sheetsByIndex[1]
        }

        this.sans.sheet.loadHeaderRow(HEADER_ROW)
        this.avec.sheet.loadHeaderRow(HEADER_ROW)

        this.sans.rows = await this.sans.sheet.getRows()
        this.avec.rows = await this.avec.sheet.getRows()
    }

    async addDataForDay(dataSans, dataAvec, date=((new Date()).toLocaleDateString("fr-FR") + "-" + (new Date()).getHours().toString().padStart(2, "0"))) { //date au format 01/01/1970 pour le 1er janvier 1970
        let rowIndex = -1
        for (let i = 1; i <=2300; i++) {//100 pour prendre un grand nombre de jours
            if(this.sans.rows[i].Date === date) rowIndex=i;
            //console.log(this.sans.rows[i])
        }
        if(rowIndex === -1) {
            return "date introuvable"
        }
        else {
            let sansRow = this.sans.rows[rowIndex]
            let avecRow = this.avec.rows[rowIndex]
            
            //données "sans engrais"
            sansRow["Température"]=dataSans.temperature
            sansRow["humidité air"]=dataSans.humiditeAir
            sansRow["humidité sol"]=dataSans.humiditeSol
            if(dataSans.etatPlante !== -1) sansRow["note de l'état de la plante"]=dataSans.etatPlante
            if(dataSans.commText !== "null") sansRow["Commentaire textuel (optionnel)"]=dataSans.commText
            if(dataSans.arrosage !== "Pas encore fait") sansRow["A dû arroser"]=dataSans.arrosage

            //données "avec engrais"
            avecRow["Température"]=dataAvec.temperature
            avecRow["humidité air"]=dataAvec.humiditeAir
            avecRow["humidité sol"]=dataAvec.humiditeSol
            if(dataAvec.etatPlante !== -1) avecRow["note de l'état de la plante"]=dataAvec.etatPlante
            if(dataAvec.commText !== "null") avecRow["Commentaire textuel (optionnel)"]=dataAvec.commText
            if(dataAvec.arrosage !== "Pas encore fait") avecRow["A dû arroser"]=dataAvec.arrosage

            await sansRow.save()
            await avecRow.save()
            return "reussi"
        }
    }
}