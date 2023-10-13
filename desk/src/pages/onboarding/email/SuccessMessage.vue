<template>
	<div class="flex flex-col items-center justify-center gap-4">
		<div class="text-7xl">
			{{ emoji }}
		</div>
		<div class="text-center text-base italic text-gray-900">
			{{ message }}
		</div>
	</div>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { capture } from "@/telemetry";

const emoji = "✔️";
const message =
	"Maravilha! Seu email está ativo. Você está pronto para explorar \
	o real potencial do nosso sistema de suporte!";

onMounted(() => capture("onboarding_email_finished"));
</script>
