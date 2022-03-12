import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Carousel from '../views/CarouselTest.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/c',
    name: 'cc',
    component: Carousel
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
