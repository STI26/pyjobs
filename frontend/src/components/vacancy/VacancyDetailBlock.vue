<template>
  <!-- vacancy info -->
  <div class="vacancy-block">
    <!-- header -->
    <div class="vacancy-block__header">
      <small v-if="isOwner" class="vacancy-block__header_edit">
        <router-link :to="{ name: 'VacancyEdit' }">
          Редактировать
        </router-link>
        <a href="#" @click.prevent="deleteVacancy(vacancy.id)">Удалить</a>
      </small>
      <h6>{{ vacancy.position.toUpperCase() }}</h6>
      <p>
        Зарплата:
        <span v-if="vacancy.salary">от ${{ vacancy.salary }}</span>
        <span v-else>з/п не указана</span>
      </p>
      <p>Описание:</p>
      <p>{{ vacancy.description }}</p>
    </div>
  </div>
  <!-- /vacancy info -->
</template>

<script>
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

export default {
  props: {
    vacancy: {
      type: Object,
      requred: true
    },
    isOwner: {
      type: Boolean,
      requred: true
    }
  },
  setup: () => {
    const router = useRouter()
    const store = useStore()

    const deleteVacancy = id => {
      store
        .dispatch('deleteVacancy', id)
        .then(response => {
          router.push('/')
        })
        .catch(error => {
          console.warn(error.response)
        })
    }

    return {
      deleteVacancy
    }
  }
}
</script>

<style lang="scss" scoped>
.vacancy-block {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 2rem;

  & > * {
    width: 100%;
    padding: 1rem 0;
    border-top: 1px solid rgb(172, 172, 172);
  }

  &__header {
    &_edit {
      display: flex;
      justify-content: space-between;
    }
    h6 {
      font-weight: 500;
    }
  }
}
</style>
