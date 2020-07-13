const Tabbar = () => import('@/components/Tabbar/')

export default [
  {
    path: '/user',
    name: 'user',
    meta: {
      login: true,
      // keepAlive: true,
      showHeader: false
    },
    components: {
      default: () => import('@/views/user/user'),
      tabbar: Tabbar
    }
  },
  {
    path: '/withdraw',
    name: 'withdraw',
    meta: {
      showHeader: true,
      title: '提现查询'
    },
    components: {
      default: () => import('@/views/user/withdraw/withdraw')
    }
  },
  {
    path: '/fundDetail',
    name: 'fundDetail',
    meta: {
      showHeader: true,
      title: '资金明细'
    },
    components: {
      default: () => import('@/views/user/fundDetail/fundDetail')
    }
  },
  {
    path: '/myInvitation',
    name: 'myInvitation',
    meta: {
      showHeader: false
    },
    components: {
      default: () => import('@/views/user/myInvitation/myInvitation')
    }
  },
  {
    path: '/conttactCustomer',
    name: 'conttactCustomer',
    meta: {
      showHeader: true,
      title: '联系客服'
    },
    components: {
      default: () => import('@/views/user/conttactCustomer/conttactCustomer')
    }
  },
  {
    path: '/setting',
    name: 'setting',
    meta: {
      showHeader: true,
      title: '用户设置'
    },
    components: {
      default: () => import('@/views/user/setting/setting')
    }
  },
  {
    path: '/myTask',
    name: 'myTask',
    meta: {
      showHeader: false
    },
    components: {
      default: () => import('@/views/user/myTask/myTask')
    }
  },
  {
    path: '/myTeam',
    name: 'myTeam',
    meta: {
      showHeader: true,
      title: '我的团队'
    },
    components: {
      default: () => import('@/views/user/myTeam/myTeam')
    }
  }
]
