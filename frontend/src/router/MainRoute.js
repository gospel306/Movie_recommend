import MainPage from '@/views/MainPage.vue'
import MovieRoute from '@/router/Main/MovieRoute.js'
import UserRoute from '@/router/Main/UserRoute.js'
import AdminRoute from '@/router/Main/AdminRoute.js'
import AuthRoute from '@/router/Main/AuthRoute.js'
import ProfileRoute from '@/router/Main/ProfileRoute.js'

export default {
    path: '/',
    name: 'mainpage',
    component: MainPage,
    children: [
        ...MovieRoute,
        ...UserRoute,
        ...AdminRoute,
        ...AuthRoute,
        ...ProfileRoute,
    ]
}
