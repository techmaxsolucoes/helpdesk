<template>
  <div class="flex flex-col gap-4">
    <div class="text-gray-700">
      {{ help }}
    </div>
    <Button label="Vamos lá!" variant="outline" class="w-max" @click="next" />
  </div>
</template>

<script setup lang="ts">
import { Button } from "frappe-ui";
import { useOnboardingEmailStore } from "./data";

const { next } = useOnboardingEmailStore();
const help =
  "Você sabia que o nosso sistema de suporte se tonar mais poderoso quando \
	está integrado ao seu email? Com essa integração, você pode enviar e receber \
	emails diretamente da sua caixa de suporte! Isso facilita a comunicação e melhora \
  a produtividade. Você gostaria de configurar sua integração de email agora?";
</script>
