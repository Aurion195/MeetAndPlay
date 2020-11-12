<script>
	//Permet de saisir un code client afin d'avoir -10%
	function codeClient() {
		alert("Pour bénéfécier de réduction veuillez saisir notre code partenaire : \n TMUJGA")
	}
</script>

<!--
	Component pour acheter un jeux de société
-->
<section class="section buttonEvent">
	<div class="button" on:click={codeClient}>
		<a class="waves-effect waves-light btn">Achat !</a>
	</div>
</section>

<style>
	.buttonEvent {
        	margin: 1% ;
    	}

    	.button {
        	text-align: center;
    	}
</style>