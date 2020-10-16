<script>
	import Carousel from '@beyonk/svelte-carousel'
	import { ChevronLeftIcon, ChevronRightIcon } from 'svelte-feather-icons'
	let carousels = {perPage: 1}
	
	function changed (event) {
		console.log(event.detail.currentSlide)
        }
</script>

<div class="demo">
	<Carousel on:change={changed} {...carousels}>
		<span class="control" slot="left-control" display="flex">
			<ChevronLeftIcon />
        </span>
		<div class="slide-content">
            <section>
                <img class="evenement" src="img/evenement1.jpg" width="600px" height="341px">
            </section>
		</div>
		<div class="slide-content">
			<section>
                <img class="evenement" src="img/evenement2.jpg" width="600px" height="341px">
            </section>
		</div>
		<div class="slide-content">
			<section>
                <img class="evenement" src="img/evenement3.jpg" width="600px" height="341px">
            </section>
		</div>
		<div class="slide-content">
			<section>
                <img class="evenement" src="img/evenement4.jpg" width="600px" height="341px">
            </section>
        </div>
        <div class="slide-content">
			<section>
                <img class="evenement" src="img/evenement5.jpg" width="600px" height="341px">
            </section>
        </div>
        <div class="slide-content">
			<section>
                <img class="evenement" src="img/evenement6.jpg" width="600px" height="341px">
            </section>
        </div>
		<span class="control" slot="right-control">
				<ChevronRightIcon />
		</span>
		
    </Carousel>
	<br/>

	<div class="button">
		<a class="waves-effect waves-light btn">Plus d'information</a>
	</div>
</div>

<style>
	.demo {
        margin: 0 auto;
		margin-top: 1%;
		height: 230px;
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
</style>

