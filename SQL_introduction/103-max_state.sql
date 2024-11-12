-- maximum temperature
SELECT `state`, max(`value`) FROM `temperature`
	GROUP BY `state`
	ORDER BY `state`;

