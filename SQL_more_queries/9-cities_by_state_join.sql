-- comments
SELECT cities.id, cities.name, states.name 
	FROM cities, states
	JOIN states ON cities.states_id = states.id;
	
