<template>
  <div class="container">
    <VacancyForm />
  </div>
</template>

<script>
import VacancyForm from '@/components/vacancy/VacancyForm'

export default {
  components: {
    VacancyForm
  }
}
</script>

<style lang="scss" scoped>
.container {
  padding: 2rem;
}
</style>
