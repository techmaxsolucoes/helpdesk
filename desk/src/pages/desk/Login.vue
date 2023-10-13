<template>
	<div class="p-5">
		<div class="flex">
			<div>Conecte-se para acessar o Helpdesk</div>
			<div class="ml-2">
				<Button @click="login">Entrar</Button>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "Login",
	methods: {
		login() {
			window.location.replace("/login")
		},
	},
}
</script>

<style></style>
