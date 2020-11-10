<!--
	Composant pour se connecter
-->

<script>
import { fetchPost } from "../Service/helper";


	let values = {} ;

	const loginUser = (() => {
		fetchPost("http://localhost:5000/login", values)
		.then(res => {
			console.log(res)
			if(res.statusText === "OK") {
				alert("Vous vous êtes connecté");
			}
			else {
				alert("Vous n'avez pas réussi à vous connecter");
			}
		})
		.catch(err => {
			console.log(err)
			alert("Error : " + err.message);
		})
	});
	
</script>

<section class="section Login">
	<form method="POST" on:submit|preventDefault={loginUser}>
			<div class="input-field col s6">
				<i class="material-icons prefix">account_circle</i>
				<input
				placeholder="Username ..."
				type="text"
				name="username" 
				bind:value={values.username}/>
			</div>
			<div class="input-field col s6">
				<i class="material-icons prefix">lock</i>
				<input
				placeholder="Password ..."
				type="password"
				name="password" 
				bind:value={values.password}/>
			</div>
		
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
		width: auto;
                margin-left: 45%;
	}
</style>