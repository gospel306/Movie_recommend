import LoginPage from '@/views/LoginPage'
import SignUpPage from '@/views/SignUpPage'
import IndexPage from '@/views/IndexPage'
export default [
    {
        path: '/login',
        name: 'Login',
        component: LoginPage
    },
    {
        path: '/signup',
        name: 'SignUp',
        component: SignUpPage
    },
    {
        path: '/index',
        name: 'Index',
        component: IndexPage
    }
]
