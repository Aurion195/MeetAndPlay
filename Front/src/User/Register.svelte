<!--
	Composant pour s'enregister
-->

<script>
        import axios from 'axios';
        import {fetchPost} from "./../Service/helper.js";

        const addUser = (async () => {
                const response =  await fetchPost("http://localhost:5000/register", values)
                                  .then(res => {
                                        if(res["Status"] === "OK") {
                                                alert("Vous vous êtes bien enregistré")
                                        }
                                 })
        })

       
        let values = {} ;
</script>

<section class="section Register">
        <form method="POST" on:submit={addUser}>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">face</i>
                                <input
                                placeholder="Nom de famille ..."
                                type="text"
                                name="nom"
                                bind:value={values.nom} />
                        </div>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">face</i>
                                <input
                                placeholder="Prénom ..."
                                type="text"
                                name="prenom"
                                bind:value={values.prenom} />
                        </div>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">face</i>
                                <input
                                placeholder="Age ..."
                                type="text"
                                name="age"
                                bind:value={values.age} />
                        </div>      
                        <div class="input-field col s6">
                                <i class="material-icons prefix">account_circle</i>
                                <input
                                placeholder="Username ..."
                                type="text"
                                name="username"
                                bind:value={values.username} />
                        </div>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">lock</i>
                                <input
                                placeholder="Password ..."
                                type="password"
                                name="password"
                                bind:value={values.password} />
                        </div>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">home</i>
                                <input
                                placeholder="Adresse ..."
                                type="text"
                                name="adresse"
                                bind:value={values.adresse} />
                        </div>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">call</i>
                                <input
                                placeholder="Téléphone ..."
                                type="text"
                                name="tel"
                                bind:value={values.tel} />
                        </div>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">mail</i>
                                <input
                                placeholder="Mail ..."
                                type="text"
                                name="mail"
                                bind:value={values.mail} />
                        </div>      
                <button class="btn waves-effect waves-light" type="submit" name="action">Connexion
			<i class="material-icons right">send</i>
		</button>
        </form>
</section>

<style>
	.section Register{
		margin: 25% auto;
	}

        .input-field {
                width: 50%;
                margin-left: 25%;
        }

        .btn {
		width: 10%;
                margin-left: 45%;
	}
</style>