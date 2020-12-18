<template>
  <div>
    <Navbar :includeSidebarMenu=true />
    <Sidebar />

    <main class="main-content">
      <router-view/>
    </main>

  </div>
</template>

<script>
import Navbar from '@/components/bars/Navbar'
import Sidebar from '@/components/bars/Sidebar'
import { useStore } from 'vuex'

export default {
  components: {
    Navbar,
    Sidebar
  },
  setup: () => {
    const store = useStore()
    store.dispatch('autoLogin')
  }
}
</script>

<style scoped lang="scss">
main, footer {
  padding-left: 300px;
}
@media only screen and (max-width : 992px) {
  main, footer {
    padding-left: 0;
  }
}
.main-content {
  li {
    width: 100%;
    background-color: blue;
  }
}
</style>
