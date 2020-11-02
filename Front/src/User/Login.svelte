<!--
	Composant pour se connecter
-->

<script>
	import Form from "@svelteschool/svelte-forms";

	let values;
</script>

<section class="section Login">
	<form method="post" action="">
		<Form bind:values>
			<div class="input-field col s6">
				<i class="material-icons prefix">account_circle</i>
				<input
				placeholder="Username ..."
				type="text"
				name="firstName" />
			</div>
			<div class="input-field col s6">
				<i class="material-icons prefix">lock</i>
				<input
				placeholder="Password ..."
				type="text"
				name="lastName" />
			</div>
		</Form>
		
		<button class="btn waves-effect waves-light" type="submit" name="action">Connexion
			<i class="material-icons right">send</i>
		</button>
	</form>
</section>

<style>
	.input-field {
                width: 50%;
                margin-left: 25%;
        }

	.btn {
		width: 10%;
                margin-left: 45%;
	}
</style>