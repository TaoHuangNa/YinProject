<template>
  <van-tabbar v-model="active"
              active-color="#07c160"
              inactive-color="#000"
              @change="onChange">
    <van-tabbar-item name="home" icon="home-o">首页</van-tabbar-item>
    <van-tabbar-item name="search" icon="search">查询</van-tabbar-item>
    <van-tabbar-item name="mine" icon="user-o">我的</van-tabbar-item>
  </van-tabbar>
</template>

<script>
  // import homediv from '../home/home'
  // import searchdiv from '../search/search'
  import { Notify } from 'vant'
  export default {
    name: 'index',
    components: {
      // homediv,
      // searchdiv
    },
    data () {
      return {
        active: 'home'
      }
    },
    methods: {
      onChange (index) {
        Notify({ type: 'primary', message: index })
      }
    }
  }
</script>

<style lang="scss" scoped>
  .centdiv {
    text-align: center;
    padding: 10px;
  }
  .bottomDiv {
    width: auto;
    position: absolute;
    bottom: 15px;
    height: auto;
    margin: 10px 5px;
    text-align: center;
    font-size: 13px;
    color: #4e4e4e;
  }
  .imgDiv {
    width: auto;
    height: 100px;
    padding: 15px 0;
  }
  .h1Class {
    color: #0b73c5;
    font-size: 20px;
    float: left;
    height: 40px;
    width: 100%;
    text-align: center;
    font-weight: 700;
    line-height: 40px;
    white-space: nowrap;
    overflow: hidden;
  }
</style>
