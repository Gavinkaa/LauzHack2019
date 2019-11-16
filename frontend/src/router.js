import Vue from 'vue'
import Router from 'vue-router';
import Rooms from './components/Rooms.vue'
import Maps from './components/Maps.vue'
import Login from './components/Login.vue'
import Alerts from './components/Alerts.vue'

Vue.use(Router)


export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/login'
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/alerts',
            name: 'Alerts',
            component: Alerts
        },
        {
            path: '/rooms',
            name: 'Rooms',
            component: Rooms
        },
        {
            path: '/maps',
            name: 'Maps',
            component: Maps
        }
    ]
})