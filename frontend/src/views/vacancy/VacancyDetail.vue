<template>
  <div class="container">
    <div v-if="loading" class="progress">
      <div class="indeterminate"></div>
    </div>
    <div v-else-if="vacancy">
      <CompanyInfo :company="vacancy.company_info" :isOwner="isOwner" />
      <VacancyDetailBlock :vacancy="vacancy" :isOwner="isOwner" />
    </div>
    <p v-else>
      {{ $t('views.vacancy.vacancyDetail.noVacancy') }}
    </p>
  </div>
</template>

<script>
import { computed, onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useStore } from 'vuex'
import VacancyDetailBlock from '@/components/vacancy/VacancyDetailBlock.vue'
import CompanyInfo from '@/components/vacancy/CompanyInfo.vue'

export default {
  components: {
    VacancyDetailBlock,
    CompanyInfo
  },
  setup: () => {
    const vacancy = ref(null)
    const loading = ref(true)
    const store = useStore()
    const route = useRoute()
    const isOwner = computed(() => {
      return (vacancy.value && (store.getters.userid === vacancy.value.company_info.user_id))
    })

    onMounted(async () => {
      const id = route.params.id
      loading.value = true
      vacancy.value = await store.dispatch('getVacancy', id)
      loading.value = false
    })

    return {
      vacancy,
      isOwner,
      loading
    }
  }
}
</script>
