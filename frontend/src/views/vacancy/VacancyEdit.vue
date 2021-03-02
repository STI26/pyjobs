<template>
  <div class="container">
    <div v-if="loading" class="progress">
      <div class="indeterminate"></div>
    </div>
    <div v-else-if="vacancy">
      <VacancyForm :dataForm="vacancy" />
    </div>
    <p v-else>
      {{ $t('views.vacancy.vacancyEdit.noVacancy') }}
    </p>
  </div>
</template>

<script>
import VacancyForm from '@/components/vacancy/VacancyForm'
import { onMounted, ref } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'

export default {
  components: {
    VacancyForm
  },
  setup: () => {
    const vacancy = ref(null)
    const loading = ref(true)
    const store = useStore()
    const route = useRoute()

    onMounted(async () => {
      const id = route.params.id
      loading.value = true
      vacancy.value = await store.dispatch('getVacancy', id)
      loading.value = false
    })

    return {
      loading,
      vacancy
    }
  }
}
</script>

<style lang="scss" scoped>
.container {
  padding: 2rem;
}
</style>
