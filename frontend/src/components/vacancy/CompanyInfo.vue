<template>
  <!-- company info -->
  <div class="company-block">
    <div class="company-block__info">
      <small v-if="isOwner" class="company-block__edit">
        <a class="modal-trigger" href="#company-modal">
          {{ $t('components.vacancy.companyInfo.edit') }}
        </a>
      </small>
      <h3>{{ company.name }}</h3>
      <p>{{ $t('components.vacancy.companyInfo.contacts') }}: {{ company.email }}</p>
      <p>{{ $t('components.vacancy.companyInfo.about') }}:</p>
      <p>{{ company.description }}</p>
    </div>
    <div class="company-block__photo">
      <img v-if="company.photo" :src="company.photo" alt="avatar">
    </div>
    <!-- Company modal form -->
    <CompanyForm :dataCompany="company"  />
  </div>
  <!-- /company info -->
</template>

<script>
import CompanyForm from '@/components/vacancy/CompanyForm'

export default {
  components: {
    CompanyForm
  },
  props: {
    company: {
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
.company-block {
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
    background: center / contain no-repeat url('../../assets/img/company-logo.png');
    background-color: rgba(255,255,255,0.8);
    background-blend-mode: lighten;

    img {
      max-height: 100%;
      max-width: 100%;
    }
  }
}
</style>
