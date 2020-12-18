<template>
  <ul v-if="paginator.num_pages > 1" class="pagination">
    <li :class="[!paginator.previous ? 'disabled' : 'waves-effect']">
      <a href="#!" @click.prevent="addPageToUrl(paginator.previous)"><i class="material-icons">chevron_left</i></a>
    </li>
    <li
      v-for="n in paginator.num_pages"
      :key="n"
      :class="[paginator.current === n ? 'active' : 'waves-effect']"
    >
      <a href="#!" @click.prevent="addPageToUrl(n)">{{ n }}</a>
    </li>
    <li :class="[!paginator.next ? 'disabled' : 'waves-effect']">
      <a href="#!" @click.prevent="addPageToUrl(paginator.next)"><i class="material-icons">chevron_right</i></a>
    </li>
  </ul>
</template>

<script>
import { useRouter } from 'vue-router'

export default {
  props: {
    paginator: {
      type: Object,
      required: true
    }
  },
  setup: () => {
    const router = useRouter()
    const addPageToUrl = (page) => {
      if (!page) {
        return null
      }

      router.replace({
        name: router.currentRoute.value.name,
        query: { ...router.currentRoute.value.query, page }
      })
    }

    return {
      addPageToUrl
    }
  }
}
</script>
