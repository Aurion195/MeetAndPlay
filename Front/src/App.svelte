<script>
	import { Router, Link, Route } from "svelte-routing";
	import Navbar from "./Utilitaire/Navbar.svelte"
	import ButtonEvent from "./home/ButtonEvent.svelte"
	import ProfilCard from "./home/ProfilCard.svelte"
	import CarouselEvenement from "./home/CarouselEvenement.svelte";
	import CarouselEvenementDetail from "./DetailsEvenement/CarouselEvenementDetail.svelte";
	import NavbarBack from "./Utilitaire/NavbarBack.svelte";
	import Login from "./User/Login.svelte";
	import ButtonInscription from "./DetailsEvenement/ButtonInscription.svelte";
	import CarouselJeuxAchat from "./home/CarouselJeuxAchat.svelte";
	import ButtonAchat from "./home/ButtonAchat.svelte" ;
import ButtonProfil from "./home/ButtonProfil.svelte";

	export let url = ''
</script>

<Router url="{url}">
	<Route path="/eventDetails" >
		<NavbarBack />
		<CarouselEvenementDetail />
		<ButtonInscription />
	</Route>
	
	<Route path="/Login" >
		<NavbarBack />
		<Login />
	</Route>

	<Route path="/">
		<Navbar />
		<CarouselEvenement />
		<ButtonEvent />
		<ProfilCard />
		<ButtonProfil />
		<CarouselJeuxAchat />
		<ButtonAchat />
	</Route>
</Router>