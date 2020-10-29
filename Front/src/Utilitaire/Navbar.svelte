<!--Import Google Icon Font-->
<!--
	La navbar de l'écran d'accueil
-->
<script>
	import { Router, Link, Route } from "svelte-routing";
	
	document.addEventListener('DOMContentLoaded', function() {
		var elems = document.querySelectorAll('.sidenav');
		var instances = M.Sidenav.init(elems);
	});

	document.addEventListener('DOMContentLoaded', function() {
		var elems = document.querySelectorAll('.dropdown-trigger');
		var instances = M.Dropdown.init(elems);
	});
</script>

<nav>
	<div class="nav">
		<a data-target="mobile-demo" class="sidenav-trigger"><i class="material-icons">menu</i></a>
		<ul class="right hide-on-med-and-down">
			<li><a>Mon Profil</a></li>
			
			<li>
				<Link to="/">
					<a>Accueil</a>
				</Link>
			</li>
			<li><a href="collapsible.html">Notification</a></li>
			  <!-- Dropdown Trigger -->
			<li><a class='dropdown-trigger' data-target='dropdown1'>Plus d'option<i class="material-icons right">arrow_drop_down</i></a></li>

			<!-- Dropdown Structure -->
			<ul id='dropdown1' class='dropdown-content'>
			<Link to="/Login">
				<li>
					<a>Se connecter</a>
				</li>
			</Link>
			
			<Link to="/Logout">
				<li>
					<a>Se deconnecter</a>
				</li>
			</Link>
			<Link to="/Inscription">
				<li>
					<a>S'inscrire</a>
				</li>
			</Link>
			<li class="divider" tabindex="-1"></li>
			<Link to="Evaluer">
				<li>
					<a>Evaluer joueur</a>
				</li>
			</Link>
			</ul>
		</ul>
	</div>
</nav>

<ul class="sidenav" id="mobile-demo">
	<Link to="/Login"><li><a href="/Login">Se connecter</a></li></Link>
	<li><a href="#!">Se deconnecter</a></li>
	<li><a href="#!">S'inscrire</a></li>
	<li class="divider" tabindex="-1"></li>
	<li><a href="sass.html">Mon Profil</a></li>
	<li><a href="badges.html">Accueil</a></li>
	<li><a href="collapsible.html">Notification</a></li>
	<li><a href="#!">Evaluer joueur</a></li>
</ul>

<style>
	.dropdown-content {
		color: black;
	}
</style>