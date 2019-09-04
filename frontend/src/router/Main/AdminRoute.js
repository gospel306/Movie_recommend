import AdminPage from '@/views/AdminPage'
import AdminUser from '@/components/admin/AdminUser'
import AdminMovie from '@/components/admin/AdminMovie'
import AdminCluster from '@/components/admin/AdminCluster'

export default [
    {
        path: '/admin',
        name: 'admin',
        component: AdminPage
    },
    {
        path: '/adminuser',
        name: 'adminuser',
        component: AdminUser
    },
    {
        path: '/adminmovie',
        name: 'adminmovie',
        component: AdminMovie
    },
    {
        path: '/cluster',
        name: 'cluster',
        component: AdminCluster
    }
]
