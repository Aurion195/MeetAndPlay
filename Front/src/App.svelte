<script>
	import { Router, Link, Route } from "svelte-routing";
	import Navbar from "./home/Navbar.svelte"
	import ButtonEvent from "./home/ButtonEvent.svelte"
	import ProfilCard from "./home/ProfilCard.svelte"
	import CarouselEvenement from "./home/CarouselEvenement.svelte";
	import CarouselEvenementDetail from "./DetailsEvenement/CarouselEvenementDetail.svelte";
	import NavbarBack from "./home/NavbarBack.svelte";

	export let url = ''
</script>

<Router url="{url}">
	<Route path="/eventDetails" >
		<NavbarBack />
		<CarouselEvenementDetail />
	</Route>
	
	<Route path="/">
		<Navbar />
		<CarouselEvenement />
		<ButtonEvent />
		<ProfilCard />
	</Route>
</Router>