<template>
  <ul class="collection">
    <li v-for="resume of resumes" :key="resume.id" class="collection-item avatar">
      <div class="user-foto">
        <img v-if="resume.photo" :src="resume.photo" alt="avatar">
      </div>
      <span class="title">
        <router-link :to="{ name: 'ResumeDetail', params: { id: resume.id } }" v-slot="{ href }">
          <a :href="href">{{ resume.position }}</a>
        </router-link>
      </span>
      <p>
        <strong>{{ $t('components.resume.resumeListBlock.salary') }}: </strong>
        <span v-if="resume.salary">от {{ resume.salary }}</span>
        <span v-else>{{ $t('components.resume.resumeListBlock.noSalary') }}</span><br>
        <small class="custom-badge" v-for="skill of resume.skills" :key="skill.tag">{{ skill.tag }}</small><br>
        <span v-if="resume.last_work">
          <strong>{{ $t('components.resume.resumeListBlock.lastWork') }}: </strong>
          {{ `${resume.last_work.organization}(${resume.last_work.position})` }}
        </span>
      </p>
    </li>
  </ul>
</template>

<script>

export default {
  props: {
    resumes: {
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
  background: center / contain no-repeat url('../../assets/img/user-avatar.png');
  background-color: rgba(255,255,255,0.8);
  background-blend-mode: lighten;
  position: absolute;
  overflow: hidden;
  left: .8rem;
  top: .8rem;

  img {
    width: 100%;
    height: 100%;
  }
}
</style>
