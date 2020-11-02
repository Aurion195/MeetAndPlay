import App from './App.svelte';

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

const app = new App({
	target: document.body,
	props: {
    name: 'world',
    hydrate: true,
    isLogged: false
	}
});

export default app;