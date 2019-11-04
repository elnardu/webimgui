import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./registerServiceWorker";

import 'buefy/dist/buefy.css'

import { Slider, Field } from "buefy";
Vue.use(Slider); // used by components/Slider.vue

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
