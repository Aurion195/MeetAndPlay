<script>
	import Carousel from '@beyonk/svelte-carousel'
	import { ChevronLeftIcon, ChevronRightIcon } from 'svelte-feather-icons'

	//Declarations des variables
    	let continents = [] ;
	let title, description, requirements, prix, placeRestante, lieux ,date ;
	let carousels = {perPage: 1}

	//Fonction permettant d'assigner les variables en fonction des indices
	function getData(indice) {
		title = continents[indice].titre ;
		description = continents[indice].Description ;
		requirements = continents[indice].Requierement ;
		placeRestante = continents[indice].Placerestante ;
		lieux = continents[indice].Lieux ;
		date = continents[indice].Date ;
		prix = continents[indice].Prix;
	}
	//Dés que lon va changer de photo dans le caroussel, on va mettre à jour les données
	function changed (event) {
		getData(event.detail.currentSlide) ;
    }

	const fetchImage = (async () => {
		const response = await fetch('http://localhost:5000/getallevent')
        	const event = await response.json()
		continents = [... event]
		
		if(continents != null) {
			getData(0)
		}

		return  [... event]
	})()
</script>


<section class="section event">
	{#await fetchImage}
	{:then continents}
	<div class="demo">
		<div class="carrousel">
		<Carousel on:change={changed} {...carousels}>		
			<span class="control" slot="left-control">
				<ChevronLeftIcon />
			</span>

            		{#each continents as data}
				<div class="slide-content">
            				<section>
                				<img class="evenement" src={data.Img} width="600px" height="341px">
					</section>
                		</div>
			{/each}

			<span class="control" slot="right-control">
					<ChevronRightIcon />
			</span>
		</Carousel>
	</div>
	<div class="button">
		<a onclick="alerte()" href="/" class="waves-effect waves-light btn">S'inscrire</a>
	</div>
	<script>
		function alerte() {
			alert("Votre inscription est en cour merci pour votre confiance") ;
		}
	</script>
        <div class="detailsEvent">
        	<table>
                	<tr>
                    		<td>Description :</td>
                    		<td class="droite">{description}</td>
                	</tr>
                	<tr>
				<td>Requirements :</td>
				<td class="droite">{requirements}</td>
			</tr>
			<tr>
				<td>Prix :</td>
				<td class="droite">{prix}</td>
			</tr>
			<tr>
				<td>Place restante :</td>
				<td class="droite">{placeRestante}</td>
			</tr>
			<tr>
				<td>Lieux :</td>
				<td class="droite">{lieux}</td>
			</tr>
			<tr>
				<td>Date :</td>
				<td class="droite">{date}</td>
                	</tr>
            </table>
        </div>
	<script>
		window.addEventListener("resize", function () {
			const fleche = document.querySelectorAll(".control");

			fleche.forEach(element => {
				element.style.display = (document.documentElement.clientWidth < 700 ? "none" : "block") ;
			});
			
			const div = document.querySelector(".carousel") ;
			const image = document.querySelector(".slide-content");
			const heigth = window.getComputedStyle(image).height;
			div.style.height = heigth
		});

		if(document.documentElement.clientWidth < 700) {
			const div = document.querySelector(".carousel") ;
			const image = document.querySelector(".slide-content");
			const heigth = window.getComputedStyle(image).height;
			div.style.height = heigth
		}
	</script>
	</div>
	{/await}
</section>

<style>
	.event {
		margin-bottom: 2%;
	}

	.demo {
        	margin: 0 auto;
		margin-top: 1%;
		height: 341px;
		max-height: 341px;
		width: 80vw;
		text-align: center;
	}

	.control :global(svg) {
		width: auto;
		height: auto;
		color: #333;
		border: 2px solid #333;
		border-radius: 32px;
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

	.droite {
		margin: 0 auto ;
		margin-left: 10%;
		text-align: right;
	}
</style>

