$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(name) {
	$('#character').text(data.name);
});
