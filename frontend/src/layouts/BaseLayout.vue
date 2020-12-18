<template>
  <div>
    <Navbar :includeSidebarMenu=false />

    <main class="main-content">
      <router-view/>
    </main>

  </div>
</template>

<script>
import Navbar from '@/components/bars/Navbar'
import { useStore } from 'vuex'

export default {
  components: {
    Navbar
  },
  setup: () => {
    const store = useStore()
    store.dispatch('autoLogin')
  }
}
</script>

<style scoped lang="scss"></style>
