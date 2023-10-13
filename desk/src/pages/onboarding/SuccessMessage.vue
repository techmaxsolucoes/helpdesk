<template>
	<div class="flex flex-col gap-4">
		<div>
			<div class="font-medium">Não se esqueça de curtir o nosso repositório no GitHub</div>
			<a class="text-sm text-gray-800" :href="github" target="_blank">
				{{ github }}
			</a>
		</div>
		<div>
			<div class="font-medium">
				Se você encontrar qualquer problema, registre ele no nosso gerenciador de tickets!
			</div>
			<a class="text-sm text-gray-800" :href="issues" target="_blank">
				{{ issues }}
			</a>
		</div>
		<div>
			<div class="font-medium">
				Para qualquer pergunta ou suporte, você pode nos encontrar no nosso portal de suporte!
			</div>
			<a class="text-sm text-gray-800" :href="support" target="_blank">
				{{ support }}
			</a>
		</div>
		<div>
			<div class="font-medium">Ou através do nosso email</div>
			<a class="text-sm text-gray-800" :href="'mailto:' + email">
				{{ email }}
			</a>
		</div>
	</div>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { capture } from "@/telemetry";

const github = "https://github.com/frappe/helpdesk";
const issues = "https://github.com/frappe/helpdesk/issues";
const support = "https://frappedesk.com/helpdesk";
const email = "hello@frappe.io";

onMounted(() => capture("onboarding_finished"));
</script>
