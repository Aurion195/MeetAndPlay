<!--
	Components pour le button profil, quand on clique dessus on va sur 
	une nouvelle route afin de pouvoir sélectionner les joueurs avec qui
	on veut jouer
-->
<script>
	import { Router, Link, Route } from "svelte-routing";
</script>

<section class="section buttonEvent">
	<Link to="profilSelection">
		<div class="button">
			<a class="waves-effect waves-light btn">Choix du profil</a>
		</div>
   	</Link>
</section>

<style>
	.buttonEvent {
       		margin: 1% ;
   	}

   	.button {
       		text-align: center;
   	}
</style>