import LoginPage from '@/views/LoginPage'
import SignUpPage from '@/views/SignUpPage'
export default [
    {
        path: '/login',
        name: 'Login',
        component: LoginPage
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUpPage
    }
]
