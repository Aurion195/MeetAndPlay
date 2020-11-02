<!--
	Component pour la sélection des profils
-->
<script>
	//Declarations des variables
    	let continents = [] ;
	let prenom, activite_recente, jeux_favoris, nombre_victoire, age, note, niveaux, img ;
	let compteur = 0 ;

	//Fonction permettant de donner les valeurs en fonction de l'avancement
	//de la liste de profil
	function getData(indice) {
		prenom = continents[indice].prenom ;
		activite_recente = continents[indice].activité_recente ;
		jeux_favoris = continents[indice].jeu_favoris ;
		age = continents[indice].age ;
		note = continents[indice].note ;
		niveaux = continents[indice].niveau ;
		nombre_victoire = continents[indice].nombre_victoire;
		img = continents[indice].Img;
	}

	//Permet de récupérer tous les profils afin de les afficher
	const fetchImage = (async () => {
		const response = await fetch('http://localhost:5000/getallusers')
		const event = await response.json()
		continents = [... event]
		if(continents != null) {
			getData(compteur) ;
		}

		return  [... event]
	})()

	function ajout() {
		getData(compteur+1) ;
	}
</script>


<section class="section profil">
	{#await fetchImage}
	{:then continents}
	<!--
		Carousel pour afficher tous les profils
	-->
	<div class="demo" style="max-heigth:370px">
		<div class="slide-content">
			<section>
				<img class="evenement" src={img} width="600px" height="341px">
		    	</section>
		</div>
		<script>
			window.addEventListener("resize", function () {	
				const div = document.querySelector(".profil") ;
				const image = document.querySelector(".slide-content");
				const heigth = window.getComputedStyle(image).height;
				div.style.height = heigth
			});

			if(document.documentElement.clientWidth < 700) {
					const div = document.querySelector(".profil") ;
					const image = document.querySelector(".slide-content");
					const heigth = window.getComputedStyle(image).height;
					div.style.height = heigth
			}
		</script>
	</div>
	<!--
		Button pour afficher les profils, quand on clique sur un seul
		on continue la liste tant que l'utilisateur part ou qu'il continue
		envoie une liste du coup quand on aime ou quand on aime pas
	-->
	<div class="button">
		<div class="button gauche" on:click={ajout()}>
			<i class="medium material-icons">do_not_disturb_on</i>
		</div>
		<div class="button droite" on:click={ajout()}>
			<i class="medium material-icons">check_circle</i>
		</div>
	</div>
	<script>
		window.addEventListener("resize", function () {	
			const div = document.querySelector(".bandeauButton") ;
			const image = document.querySelector(".slide-content");
			const heigth = window.getComputedStyle(image).height;
			div.style.height = heigth
		});
	
		if(document.documentElement.clientWidth < 700) {
			const div = document.querySelector(".bandeauButton") ;
			const image = document.querySelector(".slide-content");
			const heigth = window.getComputedStyle(image).height;
			div.style.height = heigth
		}
	</script>
	<!--
		Tableau pour afficher les données relatives au profil
	-->
   	<div class="detailsProfil">
		<table>
			<tr>
				<td>prenom :</td>
				<td class="droite">{prenom}</td>
			</tr>
			<tr>
				<td>activite_recente :</td>
				<td class="droite">{activite_recente}</td>
			</tr>
			<tr>
				<td>jeux_favoris :</td>
				<td class="droite">{jeux_favoris}</td>
			</tr>
			<tr>
				<td>nombre_victoire :</td>
				<td class="droite">{nombre_victoire}</td>
			</tr>
			<tr>
				<td>Place restante :</td>
				<td class="droite">{age}</td>
			</tr>
			<tr>
				<td>note :</td>
				<td class="droite">{note}</td>
			</tr>
			<tr>
				<td>niveaux :</td>
				<td class="droite">{niveaux}</td>
			</tr>
		</table>
    	</div>
	{/await}
</section>

<style>
	.profil {
		margin-bottom: 2%;
		max-height: 341px;
	}

	.demo {
		margin: 0 auto;
		margin-top: 1%;
		height: 341px;
		max-height: 341px;
		width: 80vw;
		text-align: center;
	}
	
	.slide-content {
		display: inline;
		flex-direction: column;
		background-color: white;
    	}

	.slide-content img {
		width: 100%;
		height: auto;
		max-height: 341px;
		max-width: 80vw;
		object-fit: contain;
	}

	.button {
		width: 100%;
		display: flex;
	}

	.button .gauche {
		float: left;
		width: 30%;
		margin-left: 20%;
    	}

    	.button .droite {
		width: 30%;
		margin-left:10% ;
    	}
</style>

