import App from './App.svelte';
import Navbar from'./Utilitaire/Navbar.svelte';
import { redirectGuard } from 'svelte-guard-history-router';


const app = new App({
	target: document.body,
	props: {

	}
});

export default app ;