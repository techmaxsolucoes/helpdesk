<template>
	<div class="flex flex-col gap-2 text-gray-800">
		<div class="text-base text-gray-900">
			{{ text }}
		</div>
		<div class="text-base text-gray-900">
			{{ subText }}
		</div>
	</div>
</template>

<script setup lang="ts">
import { onMounted } from "vue";
import { capture } from "@/telemetry";

const text =
	"Nós estamos felizes que você está se juntando a nós e queira explorar um mundo mais eficiente de atendimento ao cliente. \
	Nós estamos aqui para revolucionar a maneira como você gestiona o suporte aos seus clientes, facilitando a gestão de tickets \
	e entregando um serviço de qualidade excepcional.";
const subText =
	"Mais uma vez, bem vindo ao TMX Helpdesk! Esperamos que a sua jornada seja leve e doce!";

onMounted(() => capture("onboarding_started"));
</script>
