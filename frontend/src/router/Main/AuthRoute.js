import LoginPage from '@/views/LoginPage'
import SignUpPage from '@/views/SignUpPage'
import Index from '@/components/common/Index'

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
        path: '/',
        name: 'Index',
        component: Index
    }
]
