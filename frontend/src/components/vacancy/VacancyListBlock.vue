<template>
  <ul class="collection">
    <li
      v-for="vacancy of vacansies"
      :key="vacancy.id"
      class="collection-item avatar"
    >
      <div class="user-foto">
        <img v-if="vacancy.photo" :src="vacancy.photo" alt="avatar" />
      </div>
      <span class="title">
        <router-link
          :to="{ name: 'VacancyDetail', params: { id: vacancy.id } }"
          v-slot="{ href }"
        >
          <a :href="href">{{ vacancy.position }}</a>
        </router-link>
      </span>
      <p>{{ vacancy.company_name }}</p>
      <p>
        <strong>Зарплата: </strong>
        <span v-if="vacancy.salary">от {{ vacancy.salary }}</span>
        <span v-else>з/п не указана</span>
      </p>
    </li>
  </ul>
</template>

<script>
export default {
  props: {
    vacansies: {
      type: Array,
      required: true
    }
  }
}
</script>

<style lang="scss" scoped>
.collection-item {
  line-height: 2;
}
.custom-badge {
  border: 1px solid rgb(38, 166, 154);
  border-radius: 4px;
  padding: 3px;
  margin: 0 2px;
}
.user-foto {
  height: 50px;
  width: 50px;
  border-radius: 50%;
  background: center / contain no-repeat url('../../assets/img/company-logo.png');
  background-color: rgba(255, 255, 255, 0.8);
  background-blend-mode: lighten;
  position: absolute;
  overflow: hidden;
  left: 0.8rem;
  top: 0.8rem;

  img {
    width: 100%;
    height: 100%;
  }
}
</style>
