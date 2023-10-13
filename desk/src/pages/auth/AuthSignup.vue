<template>
  <div class="flex h-screen w-screen justify-center bg-gray-100">
    <div class="mt-32 w-full px-4">
      <img
        v-if="configStore.brandLogo"
        :src="configStore.brandLogo"
        class="m-auto h-8"
      />
      <Logo v-else class="mx-auto h-8" />
      <div class="mt-6 flex items-center justify-center space-x-1.5">
        <span class="text-3xl font-semibold text-gray-900">Signup</span>
      </div>
      <div class="mx-auto mt-6 w-full px-4 sm:w-96">
        <form method="POST" @submit.prevent="submit">
          <FormControl
            v-model="email"
            variant="outline"
            size="md"
            type="email"
            label="Email"
            placeholder="jose@exemplo.com"
            :disabled="authStore.signup.loading"
          />
          <FormControl
            v-model="firstName"
            variant="outline"
            size="md"
            type="text"
            label="Nome"
            placeholder="José"
            class="mt-4"
            :disabled="authStore.signup.loading"
          />
          <FormControl
            v-model="lastName"
            variant="outline"
            size="md"
            type="text"
            label="Sobrenome"
            placeholder="da Silva"
            class="mt-4"
            :disabled="authStore.signup.loading"
          />
          <ErrorMessage class="mt-2" :message="authStore.signup.error" />
          <Button
            variant="solid"
            class="mt-6 w-full"
            :loading="authStore.signup.loading"
          >
            Registrar
          </Button>
        </form>
      </div>
      <RouterLink :to="{ name: LOGIN }">
        <button class="mt-2 w-full py-2 text-base text-gray-600">
          Já tem uma conta? Entrar
        </button>
      </RouterLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { FormControl } from "frappe-ui";
import { LOGIN } from "@/router";
import { useAuthStore } from "@/stores/auth";
import { useConfigStore } from "@/stores/config";
import Logo from "~icons/logos/helpdesk";

const authStore = useAuthStore();
const configStore = useConfigStore();
const email = ref("");
const firstName = ref("");
const lastName = ref("");

function submit() {
  authStore.signup.submit({
    email: email.value,
    first_name: firstName.value,
    last_name: lastName.value,
  });
}
</script>
