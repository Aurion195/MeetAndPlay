import App from './App.svelte';
import Navbar from'./Utilitaire/Navbar.svelte';
import { redirectGuard } from 'svelte-guard-history-router';

if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('./Service-workers/service.js')
    .then((reg) => {
      // registration worked
      console.log('Enregistrement réussi');
    }).catch((error) => {
      // registration failed
      console.log('Erreur : ' + error);
    });
}
let isLoged = false ;

const app = new App({
	target: document.body,
	props: {
    isLogged: isLoged,
    session:false,
	}
});

export default app ;