<!--
	Composant pour s'enregister
-->

<script>
	import Form from "@svelteschool/svelte-forms";

	let values;
</script>

<section class="section Register">
        <form method="post" action="">
                <Form bind:values>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">face</i>
                                <input
                                placeholder="Nom de famille ..."
                                type="text"
                                name="lastName" />
                        </div>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">face</i>
                                <input
                                placeholder="Prénom ..."
                                type="text"
                                name="firstName" />
                        </div>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">face</i>
                                <input
                                placeholder="Age ..."
                                type="text"
                                name="age" />
                        </div>      
                        <div class="input-field col s6">
                                <i class="material-icons prefix">account_circle</i>
                                <input
                                placeholder="Username ..."
                                type="text"
                                name="username" />
                        </div>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">lock</i>
                                <input
                                placeholder="Password ..."
                                type="password"
                                name="password" />
                        </div>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">home</i>
                                <input
                                placeholder="Adresse ..."
                                type="text"
                                name="adresse" />
                        </div>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">call</i>
                                <input
                                placeholder="Téléphone ..."
                                type="text"
                                name="teleĥone" />
                        </div>
                        <div class="input-field col s6">
                                <i class="material-icons prefix">mail</i>
                                <input
                                placeholder="Mail ..."
                                type="text"
                                name="mail" />
                        </div>      
                </Form>

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