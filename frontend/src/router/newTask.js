// const Tabbar = () => import('@/components/Tabbar/')

export default [
  {
    path: '/newTask',
    name: 'newTask',
    meta: {
      login: true,
      keepAlive: true,
      showHeader: true,
      title: '发布任务'
    },
    components: {
      default: () => import('@/views/newTask/newTask')
      // tabbar: Tabbar
    }
  }
]
