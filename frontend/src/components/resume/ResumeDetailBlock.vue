<template>
  <!-- resume info -->
  <div class="resume-block">
    <!-- header -->
    <div class="resume-block__header">
      <small v-if="isOwner" class="resume-block__header_edit">
        <router-link :to="{ name: 'ResumeEdit' }">
          Редактировать
        </router-link>
        <a href="#" @click.prevent="deleteResume(resume.id)">Удалить</a>
      </small>
      <h6>{{ resume.position.toUpperCase() }}</h6>
      <p>
        Зарплата:
        <span v-if="resume.salary">от ${{ resume.salary }}</span>
        <span v-else>з/п не указана</span>
      </p>
    </div>
    <!-- skills -->
    <div class="resume-block__skills">
      Навыки:
      <span v-for="skill of resume.skills" :key="skill.tag">{{ skill.tag }}</span>
    </div>
    <!-- educations -->
    <EducationInfo :educations="resume.educations" />
    <!-- works -->
    <WorkInfo :works="resume.works" />
  </div>
  <!-- /resume info -->
</template>

<script>
import EducationInfo from '@/components/resume/EducationInfo'
import WorkInfo from '@/components/resume/WorkInfo'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

export default {
  components: {
    EducationInfo,
    WorkInfo
  },
  props: {
    resume: {
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

    const deleteResume = id => {
      store
        .dispatch('deleteResume', id)
        .then(response => {
          router.push('/')
        })
        .catch(error => {
          console.warn(error.response)
        })
    }

    return {
      deleteResume
    }
  }
}
</script>

<style lang="scss" scoped>
.resume-block {
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

  &__skills {
    span {
      border: 1px solid rgb(38, 166, 154);
      border-radius: 4px;
      padding: 3px;
      margin: 0 2px;
    }
  }
}
</style>
