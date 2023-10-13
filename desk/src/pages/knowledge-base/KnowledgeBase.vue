<template>
  <div class="flex flex-col">
    <PageTitle title="Base de conhecimento" />
    <div class="flex grow border-t">
      <KnowledgeBaseSidebar />
      <RouterView :key="$route.fullPath" v-slot="{ Component }">
        <component :is="Component" v-if="Component" />
        <EmptyMessage v-else message="Selecione a categoria!" />
      </RouterView>
    </div>
  </div>
</template>

<script setup lang="ts">
import { usePageMeta } from "frappe-ui";
import PageTitle from "@/components/PageTitle.vue";
import EmptyMessage from "@/components/EmptyMessage.vue";
import KnowledgeBaseSidebar from "./KnowledgeBaseSidebar.vue";

usePageMeta(() => {
  return {
    title: "Base de conhecimento",
  };
});
</script>
