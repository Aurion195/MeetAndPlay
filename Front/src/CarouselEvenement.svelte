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
        
        <script>
                if(screen.width < 700) {
                        const boxes = document.getElementsByClassName('evenement');

                        for(let i = 0 ; i < boxes.length ; i++) {
                                boxes[i].width = 212;
                                boxes[i].height = 102;
						}
                }
        </script>
	<br/>
</div>

<style>
	.demo {
        margin: 0 auto;
		height: 230px;
		width: 80vw;
		text-align: center;
	}
	
	.control :global(svg) {
		width: 100%;
		height: 100%;
		color: #333;
		border: 2px solid #333;
		border-radius: 32px;
	}
	
	.slide-content {
		display: flex;
		flex-direction: column;
                height: 500px;
                width: auto;
                background-color: white;
    }
        
        @media(max-width:700px) {
                .demo {
                    margin-top: 10px;
		        	height: 110px;
		        	width: auto;
					text-align: center;
                }

				.control :global(svg) {
					width: 100%;
					height: 100%;
					color: #333;
					border: 2px solid #333;
					border-radius: 32px;
					display: none;
				}
	
				.slide-content {
					display: flex;
					flex-direction: column;
					height: auto;
					width: auto;
					background-color: white;
				}
        }
</style>

