#!/usr/bin/node

const request = require('request');
const episodnber = process.argv[2];
const url_api = https:'//swapi-api.alx-tools.com/api/films/:id';

request(url_api + episodnber, function(err, response, body){
if (err) {
	console.log(err);
	else if (reponse.statusCode === 200){
		const responsejson = JSON.parse(body);
		console.log(responsejson.title);
	}
	else {
		console.log(`error code` + response.statusCode);
	}

}
});
