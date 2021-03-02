<template>
  <div>
    <Navbar :includeSidebarMenu=false />

    <main class="main-content">
      <router-view/>
    </main>

    <Footer />

  </div>
</template>

<script>
import Navbar from '@/components/bars/Navbar'
import Footer from '@/components/bars/Footer'
import { useStore } from 'vuex'

export default {
  components: {
    Navbar,
    Footer
  },
  setup: () => {
    const store = useStore()
    store.dispatch('autoLogin')
  }
}
</script>

<style scoped lang="scss"></style>
