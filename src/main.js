import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App);
app.use(require('vue-cookies'));
app.mount('#app');
