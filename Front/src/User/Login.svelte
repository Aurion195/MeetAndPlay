<!--
	Composant pour se connecter
-->

<script>
	import { fetchPost } from "../Service/helper";
	
	//Déclaration des valeurs
	let values = {} ;

	//Permet de mettre la valeur du connecté dans le session storage
	function update() {
		sessionStorage.setItem("MeetAndPlay", '1');
	}

	//Permet de se connecter via un fetch post afin de cacher les valeurs
	const loginUser = (() => {
		fetchPost("http://localhost:5000/login", values)
		.then(res => {
			if(res.statusText === "OK") {
				update();
				alert("Vous vous êtes connecté");
			}
			else if(res.statusText === "KO") {
				alert("Vous n'avez pas rentrer le bon idientifiant")
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
		
		<button class="btn waves-effect waves-light" type="submit" name="action" href="/">Connexion
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