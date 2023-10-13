<template>
  <div class="flex flex-col">
    <PageTitle title="Equipes">
      <template #right>
        <Button
          label="Nova equipe"
          theme="gray"
          variant="solid"
          @click="showNewDialog = !showNewDialog"
        >
          <template #prefix>
            <IconPlus class="h-4 w-4" />
          </template>
        </Button>
      </template>
    </PageTitle>
    <ListView
      :columns="columns"
      :resource="teams"
      class="mt-2.5"
      doctype="HD Team"
    />
    <Dialog
      v-model="showNewDialog"
      :options="{
        title: 'Nova equipe',
      }"
    >
      <template #body-content>
        <form class="space-y-2" @submit.prevent="newTeam.submit">
          <FormControl
            v-model="newTeamTitle"
            label="Título"
            placeholder="Vendas"
            type="text"
          />
          <Button
            :disabled="isEmpty(newTeamTitle)"
            class="w-full"
            label="Criar"
            theme="gray"
            variant="solid"
          />
        </form>
      </template>
    </Dialog>
  </div>
</template>
<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { createResource, usePageMeta, Dialog, FormControl } from "frappe-ui";
import { isEmpty } from "lodash";
import { AGENT_PORTAL_TEAM_SINGLE } from "@/router";
import { createListManager } from "@/composables/listManager";
import { useError } from "@/composables/error";
import PageTitle from "@/components/PageTitle.vue";
import { ListView } from "@/components";
import IconPlus from "~icons/lucide/plus";

const router = useRouter();
const showNewDialog = ref(false);
const newTeamTitle = ref(null);
const emptyMessage = "Nenhuma equipe encontrada!";
const columns = [
  {
    label: "Nome",
    key: "name",
    width: "w-80",
  },
  {
    label: "Regra de atribuição",
    key: "assignment_rule",
    width: "w-80",
  },
];

const teams = createListManager({
  doctype: "HD Team",
  fields: ["name", "assignment_rule"],
  auto: true,
  transform: (data) => {
    for (const d of data) {
      d.onClick = {
        name: AGENT_PORTAL_TEAM_SINGLE,
        params: {
          teamId: d.name,
        },
      };
    }
    return data;
  },
});

const newTeam = createResource({
  url: "frappe.client.insert",
  makeParams() {
    return {
      doc: {
        doctype: "HD Team",
        team_name: newTeamTitle.value,
      },
    };
  },
  validate(params) {
    if (isEmpty(params.doc.team_name)) return "O título é obrigatório!";
  },
  auto: false,
  onSuccess() {
    router.replace({
      name: AGENT_PORTAL_TEAM_SINGLE,
      params: {
        teamId: newTeamTitle.value,
      },
    });
  },
  onError: useError({ title: "Erro ao criar a equipe!" }),
});

usePageMeta(() => {
  return {
    title: "Equipes",
  };
});
</script>
