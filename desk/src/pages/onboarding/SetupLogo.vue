<template>
  <div class="flex flex-col gap-4">
    <div class="text-gray-700">
      {{ help }}
    </div>
    <img v-if="imageUrl" class="m-auto h-8" :src="imageUrl" />
    <FileUploader @success="(file) => update(file)">
      <template #default="{ error, openFileSelector }">
        <span>
          <Button
            label="Carregar Logo"
            :loading="r.loading"
            class="w-max"
            variant="outline"
            @click="openFileSelector"
          />
          <ErrorMessage class="mt-2" :message="error" />
        </span>
      </template>
    </FileUploader>
  </div>
</template>

<script setup lang="ts">
import { Ref, onMounted, ref } from "vue";
import { createResource, FileUploader } from "frappe-ui";
import { capture } from "@/telemetry";

const help =
  "ele será utilizado em vários locais, incluindo nas telas de login e de carregamento! \
  Uma imagem com fundo transparente e resolução de 160 x 32 funciona melhor!";
const imageUrl: Ref<string> = ref(null);

const r = createResource({
  url: "frappe.client.set_value",
  debounce: 1000,
  onSuccess(data) {
    imageUrl.value = data.brand_logo;
    capture("onboarding_logo_changed");
  },
});

function update(file) {
  r.submit({
    doctype: "HD Settings",
    name: "HD Settings",
    fieldname: "brand_logo",
    value: file.file_url,
  });
}

onMounted(() => capture("onboarding_logo_reached"));
</script>
