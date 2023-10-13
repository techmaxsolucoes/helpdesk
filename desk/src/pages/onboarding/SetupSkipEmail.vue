<template>
  <div class="flex flex-col gap-4 text-gray-800">
    {{ query }}
    <Button
      :label="isYes ? 'Não' : 'Sim'"
      class="w-max"
      variant="outline"
      @click="update(!isYes)"
    />
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import { createResource, Button } from "frappe-ui";
import { capture } from "@/telemetry";

const query =
  "Você sabia que o nosso sistema de suporte está desenhado para funcionar de \
  maneira independente, sem a necessidade de estar ligado com uma conta de email ? \
  Nosso portal de cliente está ajustado para ser uma solução autônoma, eliminando \
  a necessidade de configuração do email. Você gostaria que eu desabilitasse o fluxo \
  de configuração de email para você?";
const isYes = ref(false);

const r = createResource({
  url: "frappe.client.set_value",
  debounce: 1000,
  onSuccess(data) {
    isYes.value = data.skip_email_workflow;
    const cond = isYes.value ? "yes" : "no";
    const event = "onboarding_skip_email_" + cond;
    capture(event);
  },
});

function update(value: boolean) {
  r.submit({
    doctype: "HD Settings",
    name: "HD Settings",
    fieldname: "skip_email_workflow",
    value,
  });
}

onMounted(() => capture("onboarding_skip_email_reached"));
</script>
