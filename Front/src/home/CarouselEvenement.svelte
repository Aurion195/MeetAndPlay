<script>
	import { onMount } from "svelte";
	import Carousel from '@beyonk/svelte-carousel'
	import { ChevronLeftIcon, ChevronRightIcon } from 'svelte-feather-icons'

	let carousels = {perPage: 1}
	function changed (event) {
		console.log(event.detail.currentSlide)
	}

	const fetchImage = (async () => {
		const response = await fetch('http://0.0.0.0:5000/getallevent')
		const event = await response.json()
		return  [... event]
	})()
</script>


<section class="section event">
	{#await fetchImage}
	{:then continents}
	<div class="demo">
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
		<br/>
		<script>
			window.addEventListener("resize", function () {
				const fleche = document.querySelectorAll(".control");

				fleche.forEach(element => {
					element.style.display = (document.documentElement.clientWidth < 700 ? "none" : "block") ;
				});
				
				const div = document.querySelector(".event") ;
				const image = document.querySelector(".slide-content img");
				const heigth = window.getComputedStyle(image).height;
				div.style.height = heigth
			});
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
</style>

