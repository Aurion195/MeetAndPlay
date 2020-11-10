import App from './App.svelte';
import Navbar from'./Utilitaire/Navbar.svelte';
import { redirectGuard } from 'svelte-guard-history-router';

let isLoged = false ;

const app = new App({
	target: document.body,
	props: {
    isLogged: isLoged,
    session:false,
	}
});

export default app ;