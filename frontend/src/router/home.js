const Tabbar = () => import('@/components/Tabbar')

export default [
  {
    path: '/',
    name: 'home',
    components: {
      default: () => import('@/views/home/home'),
      tabbar: Tabbar
    },
    meta: {
      keepAlive: true,
      showHeader: false
    }
  },
  {
    path: '*',
    redirect: {
      name: 'home'
    }
  },
  {
    path: '/news',
    name: 'news',
    components: {
      default: () => import('@/views/home/news/news')
    },
    meta: {
      showHeader: true,
      title: '通知公告'
    }
  },
  {
    path: '/newsDetail',
    name: 'newsDetail',
    components: {
      default: () => import('@/views/home/news/newsDetail')
    },
    meta: {
      showHeader: true,
      title: '公告详情'
    }
  },
  {
    path: '/member',
    name: 'member',
    components: {
      default: () => import('@/views/home/member/member')
    },
    meta: {
      showHeader: true,
      title: '开通会员'
    }
  },
  {
    path: '/payMent',
    name: 'payMent',
    components: {
      default: () => import('@/views/home/payMent/payMent')
    },
    meta: {
      showHeader: true,
      title: '转账提交'
    }
  }
]
