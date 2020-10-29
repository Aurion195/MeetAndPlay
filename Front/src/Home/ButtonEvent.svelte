<!--
	Component pour le button event, quand on clique dessus on va sur une nouvelle page
-->
<script>
	import { Router, Link, Route } from "svelte-routing";
</script>

<section class="section buttonEvent">
	<Link to="eventDetails">
		<div class="button">
			<a class="waves-effect waves-light btn">Plus d'information</a>
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