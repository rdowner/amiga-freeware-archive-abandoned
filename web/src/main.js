import axios from 'axios'
import Vue from 'vue'
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import App from './App.vue'
import HomePage from './components/HomePage.vue'
import SearchPage from './components/SearchPage.vue'
import DiskPage from './components/DiskPage.vue'
import LibraryPage from './components/LibraryPage.vue'
import AboutPage from './components/AboutPage.vue'

Vue.config.productionTip = false;
Vue.use(VueRouter);
Vue.use(BootstrapVue);

axios.defaults.baseURL = 'https://w1rz82fujb.execute-api.us-east-2.amazonaws.com/prod';

const routes = [
    { name: 'home', path: '/', component: HomePage },
    { name: 'search', path: '/search', component: SearchPage },
    { name: 'library', path: '/libraries/:library', component: LibraryPage },
    { name: 'library_disk', path: '/libraries/:library/disks/:disk', component: DiskPage },
    { name: 'about', path: '/about', component: AboutPage }
];

const router = new VueRouter({
    mode: 'history',
    routes // short for `routes: routes`
});

new Vue({
    render: h => h(App),
    router
}).$mount('#app');
