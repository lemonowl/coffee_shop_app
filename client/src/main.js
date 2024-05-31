import { createApp } from 'vue';
import Toast, { useToast, POSITION, TYPE } from "vue-toastification";
import axios from 'axios';

import "./css/custom.css"
import router from "./router/index.js";

import Header from './components/common/Header.vue';
import Footer from './components/common/Footer.vue';
import App from './App.vue';

const app = createApp(App);

app.component('Header', Header);
app.component('Footer', Footer);

app.use(router);
app.use(Toast, {
  position: POSITION.BOTTOM_CENTER,
  toastDefaults: {
      [TYPE.ERROR]: {
          timeout: 3000,
      },
      [TYPE.SUCCESS]: {
          timeout: 1500,
      }    
  }
});

app.config.globalProperties.$axios = axios.create({
  withCredentials: true,
  headers: {
    "Content-Type": "application/json; charset=UTF-8",
  }
});
app.config.globalProperties.$toast = useToast();

app.mount('#app');