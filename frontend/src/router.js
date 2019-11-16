import Vue from 'vue'
import Router from 'vue-router';
import Maps from './components/Maps.vue'
import Login from './components/Login.vue'
import Alerts from './components/Alerts.vue'

Vue.use(Router)

const router = new Router({
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
            path: '/maps',
            name: 'Maps',
            component: Maps
        }
    ]
});


router.beforeEach((to, from, next) => {
    if (router.app.connected === false && to.name !== 'Login') {
        next('/login')
    } else {
        next()
    }
})

export default router;