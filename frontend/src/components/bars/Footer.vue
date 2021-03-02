<template>
  <footer class="page-footer grey lighten-3">
    <div class="footer-copyright">
      <div>
        © 2021 Copyright Text
      </div>
      <div class="input-field language-menu">
        <select
          v-model="$i18n.locale"
          ref="languageMenuElem"
        >
          <option value="en">English</option>
          <option value="ru">Русский</option>
        </select>
      </div>
    </div>
  </footer>
</template>

<script>
import M from 'materialize-css'
import { onMounted, onUnmounted, onUpdated, ref } from 'vue'

export default {
  setup: () => {
    const languageMenuElem = ref(null)
    let languageMenuObj

    onMounted(() => {
      languageMenuObj = M.FormSelect.init(languageMenuElem.value, {})
    })

    onUpdated(() => {
      M.updateTextFields()
    })

    onUnmounted(() => {
      if (languageMenuObj && languageMenuObj.destroy) {
        languageMenuObj.destroy()
      }
    })
    return {
      languageMenuElem
    }
  }
}
</script>

<style lang="scss" scoped>
  .page-footer {
    padding-top: 0;
  }

  .footer-copyright {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
    overflow: visible !important;
    padding: 1rem 3rem !important;
  }

  .language-menu {
    margin: 0;
  }
</style>
