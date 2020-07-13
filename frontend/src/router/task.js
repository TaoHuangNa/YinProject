const Tabbar = () => import('@/components/Tabbar/')

export default [
  {
    path: '/task',
    name: 'task',
    meta: {
      login: true,
      keepAlive: true,
      showHeader: false
    },
    components: {
      default: () => import('@/views/task/task'),
      tabbar: Tabbar
    }
  },
  {
    path: '/getTask',
    name: 'getTask',
    meta: {
      login: true,
      showHeader: true,
      title: '任务中心'
    },
    components: {
      default: () => import('@/views/task/getTask/getTask')
    }
  },
  {
    path: '/pickTask',
    name: 'pickTask',
    meta: {
      login: true,
      showHeader: true,
      title: '领取'
    },
    components: {
      default: () => import('@/views/task/getTask/pickTask')
    }
  }
]
