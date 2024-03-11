<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
<link rel="stylesheet" href="styles/style1.css">
<script>
	function preencher(json){
		alert(json.name)
		divDados = document.getElementById('dadosPokemon')

		// add the newly created element and its content into the DOM
		divDados.innerHTML = json.name
	}
	function BuscarDados(){
		selectPokemon = document.getElementById('pokemonid').value
		console.log(selectPokemon)
		
		fetch('https://pokeapi.co/api/v2/pokemon/'+selectPokemon)
    .then(response => response.json())
    .then(data => {
      pokemon = data;
      preencher(pokemon)
	  console.log(pokemon.abilities);
    })
    .catch(err => console.log(err));
	}
 // Ex
</script>
</head>
<body>
		<div id="pokedex">
			<select class="form-select" aria-label="Multiple select example" id="pokemonid">
			  <option selected>Selecione um Pokémon</option>
			  <option value="pikachu">Pikachu</option>
			  <option value="ditto">Ditto</option>
			  <option value="charmander">Charmander</option>
			</select>
			<input  type="button" onClick ="BuscarDados()" value="Buscar">
		</div>
		<div id="dadosPokemon"></div>
</body>
</html>