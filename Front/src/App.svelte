<script>
	import { Router, Link, Route } from "svelte-routing";
	import Navbar from "./Utilitaire/Navbar.svelte"
	import ButtonEvent from "./Home/ButtonEvent.svelte"
	import ProfilCard from "./Home/ProfilCard.svelte"
	import CarouselEvenement from "./Home/CarouselEvenement.svelte";
	import CarouselEvenementDetail from "./DetailsEvenement/CarouselEvenementDetail.svelte";
	import NavbarBack from "./Utilitaire/NavbarBack.svelte";
	import Login from "./User/Login.svelte";
	import CarouselJeuxAchat from "./Home/CarouselJeuxAchat.svelte";
	import ButtonAchat from "./Home/ButtonAchat.svelte" ;
	import ButtonProfil from "./Home/ButtonProfil.svelte";
	import SelectionProfil from "./Profil/SelectionProfil.svelte";

	export let url = "";
</script>

<!--
	Permet de gérer les différentes routes afin de naviguer dans la PWA
-->
<Router url="{url}">
	<!--
		Route pour le détails des différents évenements
	-->
	<Route path="/eventDetails" >
		<NavbarBack />
		<CarouselEvenementDetail />
	</Route>
	
	<!--
		Route pour se connecter
	-->
	<Route path="/Login" >
		<NavbarBack />
		<Login />
	</Route>

	<!--
		Route pour séléctionner les profils
	-->
	<Route path="/profilSelection" >
		<NavbarBack />
		<SelectionProfil />
	</Route>

	<!--
		Route pour la page d'acceuil
	-->
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