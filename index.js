const express = require('express')
const {spawn} = require('child_process');
const app = express()
const port = 3000


app.get('/analises', (req, res) => {
 

  const tipo = req.query.tipo;
  const analise = req.query.analise;
  const pais = req.query.pais;


 var dataToSend;

 const python = spawn('/usr/bin/python3.8', ['analises.py',tipo,pais,analise], {
    detached: true
  },);
 
  //D:/Anaconda/python.exe
  
 python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  dataToSend = data.toString();
 });

 
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);

 
 res.send(dataToSend)
 });
 
})
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))