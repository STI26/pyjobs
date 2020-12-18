<template>
  <!-- user info -->
  <div class="user-block">
    <div class="user-block__info">
      <small v-if="isOwner" class="user-block__edit">
        <router-link to="/profile/edit" href="#">Редактировать</router-link>
      </small>
      <h3>{{ user.name }}</h3>
      <p>{{ user.age }} лет.</p>
      <p>Контакты: {{ user.email }}</p>
      <p>О себе:</p>
      <p>{{ user.bio }}</p>
    </div>
    <div class="user-block__photo">
      <img v-if="user.photo" :src="user.photo" alt="avatar">
    </div>
  </div>
  <!-- /user info -->
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
      requred: true
    },
    isOwner: {
      type: Boolean,
      requred: true
    }
  }
}
</script>

<style lang="scss" scoped>
.user-block {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 2rem;

  &__info {
    line-height: 1.1;
  }

  &__photo {
    height: 15rem;
    width: 15rem;
    overflow: hidden;
    background: center / contain no-repeat url('../../assets/img/user-avatar.png');
    background-color: rgba(255,255,255,0.8);
    background-blend-mode: lighten;

    img {
      max-height: 100%;
      max-width: 100%;
    }
  }
}
</style>
