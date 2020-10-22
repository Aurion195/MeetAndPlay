<script>
import { onMount } from "svelte";


	let continents = [] ;
	onMount((async () => {
		const response = await fetch('http://localhost:8000/getallevent')
		const event = await response.json()
		continents = [... event.data]


		console.log(continents)
	  })) ;
</script>

<section class="zob">
	<ul>
	{#each continents as img}
			<li>
				<img src={img.img}>
			</li>
	{:else}
			<p>loading</p>
	{/each}
	</ul>
</section>