<script>
	import { Router, Link, Route } from "svelte-routing";
	import Navbar from "./Navbar.svelte"
	import ButtonEvent from "./ButtonEvent.svelte"
	import ProfilCard from "./ProfilCard.svelte"
	import CarouselEvenement from "./CarouselEvenement.svelte";

	export let url = ''
</script>

<main>
<Router url="{url}">
  <div>
	<Route path="eventDetails" component="{Navbar}">
	</Route>
	
	<Route path="/">
		<Navbar />
		<CarouselEvenement />
		<ButtonEvent />
		<ProfilCard />
	</Route>
  </div>
</Router>

</main>