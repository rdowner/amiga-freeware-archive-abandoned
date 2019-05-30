import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'

Vue.config.productionTip = false

axios.defaults.baseURL = 'https://w1rz82fujb.execute-api.us-east-2.amazonaws.com/prod';

new Vue({
  render: h => h(App),
}).$mount('#app')
