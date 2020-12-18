<template>
  <component :is="layout">
    <router-view/>
  </component>
</template>

<style lang="scss">
@import '~materialize-css/dist/css/materialize.min.css';
@import '~material-design-icons/iconfont/material-icons.css';
@import 'assets/main.css';
</style>

<script>
import BaseLayout from '@/layouts/BaseLayout'
import AdvancedLayout from '@/layouts/AdvancedLayout'
import { computed } from 'vue'
import { useRoute } from 'vue-router'

export default {
  components: {
    BaseLayout,
    AdvancedLayout
  },
  setup: () => {
    const route = useRoute()
    const layout = computed(() => route.meta.layout || 'blank-layout')

    return {
      layout
    }
  }
}
</script>
