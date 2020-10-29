<script>
	import Carousel from '@beyonk/svelte-carousel'
	import { ChevronLeftIcon, ChevronRightIcon } from 'svelte-feather-icons'

	//Declarations des variables
    let continents = [] ;
	let prenom; 
	let activite_recente;
	let jeux_favoris;
	let nombre_victoire;
	let age;
	let note; 
	let niveaux ;
	let carousels = {perPage: 1}

	//Dés que lon va changer de photo dans le caroussel, on va mettre à jour les données
	function changed (event) {
		prenom = continents[event.detail.currentSlide].prenom ;
		activite_recente = continents[event.detail.currentSlide].activité_recente ;
		jeux_favoris = continents[event.detail.currentSlide].jeu_favoris ;
		age = continents[event.detail.currentSlide].age ;
		note = continents[event.detail.currentSlide].note ;
		niveaux = continents[event.detail.currentSlide].niveau ;
		nombre_victoire = continents[event.detail.currentSlide].nombre_victoire;
    }

	const fetchImage = (async () => {
		const response = await fetch('http://localhost:5000/getallusers')
        const event = await response.json()
        continents = [... event]
		prenom = continents[0].prenom ;
		activite_recente = continents[0].activité_recente ;
		jeux_favoris = continents[0].jeu_favoris ;
		age = continents[0].age ;
		note = continents[0].note ;
		niveaux = continents[0].niveau ;
		nombre_victoire = continents[0].nombre_victoire;

		return  [... event]
	})()
</script>


<section class="section profil">
	{#await fetchImage}
	{:then continents}
	<div class="demo" style="max-heigth:370px">
		<Carousel on:change={changed} {...carousels}>		
            {#each continents as data}
				<div class="slide-content">
            		<section>
                		<img class="evenement" src={data.Img} width="600px" height="341px">
                    </section>
                </div>
			{/each}

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
		</Carousel>
	</div>
	<div class="button">
		<div class="button gauche">
			<i class="medium material-icons">do_not_disturb_on</i>
		</div>
		<div class="button droite">
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
    <div class="detailsProfil">
		<table>
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

