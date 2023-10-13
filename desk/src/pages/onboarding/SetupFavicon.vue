<template>
  <div class="flex flex-col gap-4">
    <div class="text-gray-700">
      {{ help }}
    </div>
    <img v-if="imageUrl" class="m-auto h-8 w-8" :src="imageUrl" />
    <FileUploader @success="(file) => update(file)">
      <template #default="{ error, openFileSelector }">
        <span>
          <Button
            label="Carregar Favicon"
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
  "Um favicon melhora seu website, provendo uma pequena imagem que aparece \
  nas abas do navegador. Isso melhora significativamente o reconhecimento da sua marca, \
  adicionando profissionalismo, facilita a navegação, estabelece confiancça e \
  mantem a consistência da sua marca. Uau, esse é o poder de uma imagem!";
const imageUrl: Ref<string> = ref(null);

const r = createResource({
  url: "frappe.client.set_value",
  debounce: 1000,
  onSuccess(data) {
    imageUrl.value = data.brand_favicon;
    capture("onboarding_favicon_changed");
  },
});

function update(file) {
  r.submit({
    doctype: "HD Settings",
    name: "HD Settings",
    fieldname: "brand_favicon",
    value: file.file_url,
  });
}

onMounted(() => capture("onboarding_favicon_reached"));
</script>
