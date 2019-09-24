import MoviePage from '@/views/MoviePage'
import MovieSimilar from '@/components/movie/MovieSimilar'
import MovieBest from '@/components/movie/MovieBest'

export default [
    {
        path: '/search',
        name: 'moviesearch',
        component: MoviePage
    },
    {
        path: '/similar',
        name: 'moviesimilar',
        component: MovieSimilar,
        props: true
    },
    {
        path: '/best',
        name: 'moviebest',
        component: MovieBest,
    }
]
