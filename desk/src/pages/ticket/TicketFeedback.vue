<template>
  <Dialog
    :model-value="open"
    :options="{
      title: 'Pontue esse ticket!',
      actions: [
        {
          disabled: !preset,
          label: 'Enviar',
          theme: 'gray',
          variant: 'solid',
          onClick: () =>
            setValue.submit({
              fieldname: {
                status: 'Resolved',
                feedback: preset,
                feedback_extra: text,
              },
            }),
        },
      ],
    }"
    @update:model-value="() => $emit('update:open', !open)"
  >
    <template #body-content>
      <div class="space-y-4 text-base text-gray-700">
        <div class="space-y-2">
          <span> Selecionar pontuação </span>
          <span class="text-red-500"> * </span>
          <StarRating v-model:rating="rating" :static="false" />
        </div>
        <div v-if="options.data?.length" class="space-y-2">
          <span> Selecione uma opção </span>
          <span class="text-red-500"> * </span>
          <div class="flex flex-wrap gap-2">
            <Button
              v-for="o in options.data"
              :key="o.name"
              :label="o.label"
              :theme="preset === o.name ? 'blue' : 'gray'"
              variant="subtle"
              @click="preset = o.name"
            />
          </div>
        </div>
        <div class="space-y-2">
          <span> Outro </span>
          <FormControl
            v-model="text"
            type="textarea"
            placeholder="Conte-nos um pouco mais!"
          />
        </div>
      </div>
    </template>
  </Dialog>
</template>

<script setup lang="ts">
import { inject, ref, watch } from "vue";
import { createResource, createListResource } from "frappe-ui";
import { useError } from "@/composables/error";
import { StarRating } from "@/components";
import { ITicket } from "./symbols";

interface P {
  open: boolean;
}

interface E {
  (event: "update:open", open: boolean): void;
}

defineProps<P>();
const emit = defineEmits<E>();
const ticket = inject(ITicket);
const rating = ref(0);
const text = ref("");
const preset = ref(null);
const options = createListResource({
  doctype: "HD Ticket Feedback Option",
  fields: ["name", "label"],
  pageLength: 99999,
  onError: useError(),
});
const setValue = createResource({
  url: "frappe.client.set_value",
  debounce: 300,
  makeParams: (params) => {
    return {
      doctype: "HD Ticket",
      name: ticket.data.name,
      fieldname: params.fieldname,
      value: params.value,
    };
  },
  onSuccess: () => {
    emit("update:open", false);
    ticket.reload();
  },
  onError: useError(),
});
watch(rating, (r) => {
  preset.value = null;
  text.value = "";
  options.update({
    filters: {
      rating: r,
    },
  });
  options.reload();
});
</script>
