<template>
  <div class="flex gap-2">
    <Button v-bind="primary" />
    <Dropdown :options="dropdownOptions">
      <Button theme="gray" variant="ghost">
        <template #icon>
          <IconMoreHorizontal class="h-4 w-4" />
        </template>
      </Button>
    </Dropdown>
    <Dialog v-model="showDeleteDialog" :options="deleteDialogOptions" />
  </div>
</template>

<script setup lang="ts">
import { computed, ref, toRef } from "vue";
import { Dialog, Dropdown } from "frappe-ui";
import IconEdit from "~icons/lucide/edit-3";
import IconMoreHorizontal from "~icons/lucide/more-horizontal";
import IconTrash from "~icons/lucide/trash-2";

const props = defineProps({
  status: {
    type: String,
    required: false,
    default: "Draft",
  },
});

const emit = defineEmits<{
  (event: "delete"): void;
  (event: "toggleEditMode"): void;
  (event: "toggleStatus"): void;
}>();

const status = toRef(props, "status");
const showDeleteDialog = ref(false);
const primary = computed(() => ({
  label: status.value === "Published" ? "Unpublish" : "Publish",
  theme: "gray",
  variant: "solid",
  onClick: () => emit("toggleStatus"),
}));
const dropdownOptions = [
  {
    label: "Editar",
    icon: IconEdit,
    onClick: () => emit("toggleEditMode"),
  },
  {
    label: "Deletar",
    icon: IconTrash,
    onClick: () => (showDeleteDialog.value = !showDeleteDialog.value),
  },
];
const deleteDialogOptions = {
  title: "Deletar",
  message: "Você tem certeza que deseja deletar? Essa ação não pode ser desfeita!",
  icon: {
    name: "alert-triangle",
    appearance: "warning",
  },
  actions: [
    {
      label: "Confirmar",
      theme: "red",
      variant: "solid",
      onClick: () => emit("delete"),
    },
  ],
};
</script>
