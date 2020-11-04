<!--
	Composant pour s'enregister
-->

<script>
        import {fetchPost} from "./../Service/helper.js";

        let selected = 0 ;
        let values = {} ;

        const addUser = (() => {
                fetchPost("http://localhost:5000/register", values)
                .then(res => {
                        if(res["Status"] === "OK") {
                                alert("Vous vous êtes bien enregistré")
                        }
                })
                .catch(err => {
                        alert("Nous n'avons pas réussi à vous enregistré")
                        console.log(err.message)
                })
        })

        function getImg() {
                if(selected == 1) {
                        console.log("Homme")
                }
                else {
                        console.log("femme")
                }
        }
</script>

<section class="section Register">
        <form method="POST" on:submit|preventDefault={addUser}>
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
                                <input type=number bind:value={values.age} min=0 max=100>
                                <input type=range bind:value={values.age} min=0 max=100>
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
                        <div class="input-field col s6">
                                <i class="material-icons prefix">favorite</i>
                                <input
                                placeholder="Jeux favoris"
                                type="text"
                                name="jeu_favoris"
                                bind:value={values.jeu_favoris}>
                        </div>
                        <div class="input-field col s6">
                                <div on:click={getImg}>
                                        <label>
                                                <input type=radio bind:group={selected} value={1}>
                                                Homme
                                        </label>
                                </div>
                                <div on:click={getImg}>
                                        <label>
                                                <input type=radio bind:group={selected} value={2}>
                                                Femme
                                        </label>
                                </div>


                        </div>
                <button class="btn waves-effect waves-light" name="action" type="submit">Connexion
			<i class="material-icons right">send</i>
		</button>
        </form>
</section>

<style>
	.section Register{
		margin: 25% auto;
	}

        .input-field {
                display: block;
                margin:auto;
                width: 70%;
        }

        .btn {
                display: block;
                margin:auto;
		width: auto;
	}
</style>