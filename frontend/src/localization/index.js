import { createI18n } from 'vue-i18n'
import en from './languages/english.json'
import ru from './languages/russian.json'

const messages = {
  en,
  ru
}

const i18n = createI18n({
  locale: navigator.language,
  fallbackLocale: 'en',
  messages
})

export default i18n
