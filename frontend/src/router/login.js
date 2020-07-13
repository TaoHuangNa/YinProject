export default [
  {
    path: '/login',
    name: 'login',
    meta: {
      showHeader: false,
      title: '登录'
    },
    component: () => import('@/views/login/login')
  },
  {
    path: '/login/forget',
    name: 'forget',
    meta: {
      showHeader: true,
      title: '重置密码'
    },
    component: () => import('@/views/login/forget')
  },
  {
    path: '/login/register',
    name: 'forget',
    meta: {
      showHeader: true,
      title: '注册账号'
    },
    component: () => import('@/views/login/register')
  }
]
