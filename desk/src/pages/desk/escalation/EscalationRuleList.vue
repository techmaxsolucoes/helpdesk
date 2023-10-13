<template>
  <div class="flex flex-col">
    <PageTitle title="Regras de escalonamento">
      <template #right>
        <Button
          label="Nova regra"
          theme="gray"
          variant="solid"
          @click="openDialog(null)"
        >
          <template #prefix>
            <LucidePlus class="h-4 w-4" />
          </template>
        </Button>
      </template>
    </PageTitle>
    <ListView
      :columns="columns"
      :resource="rules"
      class="mt-2.5"
      doctype="HD Escalation Rule"
    >
      <template #is_enabled="{ data }">
        <Badge :theme="data.is_enabled ? 'green' : 'red'" variant="subtle">
          {{ data.is_enabled ? "Abilitada" : "Desabilitada" }}
        </Badge>
      </template>
    </ListView>
    <EscalationRuleDialog
      v-if="showDialog"
      v-model="showDialog"
      :name="selectedRule"
    />
  </div>
</template>
<script setup lang="ts">
import { ref } from "vue";
import { usePageMeta, Badge } from "frappe-ui";
import { socket } from "@/socket";
import { createListManager } from "@/composables/listManager";
import { ListView } from "@/components";
import PageTitle from "@/components/PageTitle.vue";
import EscalationRuleDialog from "./EscalationRuleDialog.vue";

const showDialog = ref(false);
const selectedRule = ref(null);
const emptyMessage = "Nenhuma regra de escalonamento encontrada";
const columns = [
  {
    label: "Prioridade",
    key: "priority",
    width: "w-64",
  },
  {
    label: "Equipe",
    key: "team",
    width: "w-64",
  },
  {
    label: "Tipo de ticket",
    key: "ticket_type",
    width: "w-64",
  },
  {
    label: "Status",
    key: "is_enabled",
    width: "w-20",
  },
];

const rules = createListManager({
  doctype: "HD Escalation Rule",
  fields: ["name", "priority", "team", "ticket_type", "is_enabled"],
  auto: true,
  transform: (data) => {
    for (const d of data) {
      d.onClick = () => openDialog(d.name);
    }
    return data;
  },
});

usePageMeta(() => {
  return {
    title: "Regras de escolamento",
  };
});

function openDialog(rule: string | null) {
  selectedRule.value = rule;
  showDialog.value = true;
}

socket.on("helpdesk:new-escalation-rule", () => rules.reload());
socket.on("helpdesk:delete-escalation-rule", () => rules.reload());
</script>
