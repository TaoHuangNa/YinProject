import {
  Field,
  Button,
  CellGroup,
  Image,
  Toast,
  Notify,
  Tabbar,
  NavBar,
  TabbarItem
} from 'vant'

const vant = {
  install: function (Vue) {
    Vue.use(Field)
    Vue.use(Button)
    Vue.use(CellGroup)
    Vue.use(Image)
    Vue.use(Toast)
    Vue.use(Notify)
    Vue.use(Tabbar)
    Vue.use(NavBar)
    Vue.use(TabbarItem)
  }
}

export default vant
