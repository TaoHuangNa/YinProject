<template>
  <div class="tab_home">
    <van-notice-bar
      left-icon="laba"
      text="恭喜 花不败 在10分钟前提现100.00元 恭喜 未来在哪里 在20分钟前提现650.00元 恭喜 敢问路在何方 在12分钟前提现8000.00元。"
    />
    <van-swipe :autoplay="3000"
               indicator-color="white">
      <van-swipe-item v-for="(banner, index) in bannerList"
                      :key="index">
<!--        <div class="bg" :style="{background-image: url(' + banner.image + ') no-repeat}"></div>-->
        <div class="bg" :style="{ 'background-image': 'url(' + banner.image + ')'}">
        </div>
<!--        <img :src="banner.image"-->
<!--             style="height:230px">-->
      </van-swipe-item>
<!--      <van-swipe-item>-->
<!--        <div class="bg">-->
<!--        <marquee style="color: #ffffff;" direction="left" behavior="scroll" scrollamount="10" scrolldelay="0" loop="-1" hspace="10" vspace="10">-->
<!--        &lt;!&ndash;&ndash;&gt;-->
<!--          &lt;!&ndash;&#45;&#45;&gt;&ndash;&gt;-->
<!--        </marquee>-->
<!--        </div>-->
<!--      </van-swipe-item>-->
    </van-swipe>
    <van-row class="order_status">
      <van-col span="6">
        <div class="order_status_icon" style="background: #f55315; color: #ffffff;" @click="$router.push({path: '/news'})">
          <van-icon class="iconfont icon-xinwen"/>
        </div>
        <div>通知公告</div>
      </van-col>
      <van-col span="6">
        <div class="order_status_icon" style="background: #f53952; color: #ffffff;" @click="$router.push({path: '/user/order/list/2'})">
          <van-icon class="iconfont icon-zhinanzhen"/>
        </div>
        <div>新手指南</div>
      </van-col>
      <van-col span="6" @click="$router.push({path: '/myInvitation'})">
        <div class="order_status_icon" style="background: #f59a08; color: #ffffff;" @click="$router.push({path: '/myInvitation'})">
          <van-icon class="iconfont icon-yqhy"/>
        </div>
        <div>邀请好友</div>
      </van-col>
      <van-col span="6">
        <div class="order_status_icon" style="background: #db3d3c; color: #ffffff;" @click="$router.push({path: '/member'})">
          <van-icon class="iconfont icon-ziyuan"/>
        </div>
        <div>开通会员</div>
      </van-col>
    </van-row>
    <van-row class="taskRow">
      <van-col span="12">
        <div class="order_status_icon" style="background: #2ee0f5;; color: #ffffff;" @click="toTask(0)">
          <van-icon class="iconfont icon-chepai" style="font-size: 20px;"/>&ensp;普通任务
        </div>
      </van-col>
      <van-col span="12">
        <div class="order_status_icon" style="background: #ff6ca5;; color: #ffffff;" @click="toTask(1)">
          <van-icon class="iconfont icon-feiji" style="font-size: 20px;"/>&ensp;会员任务
        </div>
      </van-col>
    </van-row>
    <van-row class="taskRow" style="background: #5c85fb; color: #ffffff;">
      <van-col span="6"><van-icon class="iconfont icon-ziyuan" style="font-size: 25px;"/></van-col>
      <van-col span="18" style="text-align: left;">今日任务数: {{this.homepage.tasks}}</van-col>
    </van-row>
    <van-row class="taskRow" style="background: #0ed4c5; color: #ffffff;">
      <van-col span="6"><van-icon class="iconfont icon-ziyuan" style="font-size: 25px;"/></van-col>
      <van-col span="18" style="text-align: left;">今日用户数: {{this.homepage.users}}</van-col>
    </van-row>
    <van-row class="taskRow" style="background: #ff655b; color: #ffffff;">
      <van-col span="6"><van-icon class="iconfont icon-ziyuan" style="font-size: 25px;"/></van-col>
      <van-col span="18"  style="text-align: left;">今日已完成: {{this.homepage.completes}}</van-col>
    </van-row>
    <van-row class="taskRow" style="background: #ffa72d; color: #ffffff;">
      <van-col span="6"><van-icon class="iconfont icon-ziyuan" style="font-size: 25px;"/></van-col>
      <van-col span="18" style="text-align: left;">今日排行榜: 3</van-col>
    </van-row>
  </div>
</template>

<script>
import {
  List,
  Swipe,
  SwipeItem,
  Tabbar,
  TabbarItem,
  Search,
  Panel,
  CouponCell,
  CouponList,
  Toast,
  Card,
  Grid,
  GridItem,
  Row,
  Col,
  Tag,
  NoticeBar
} from 'vant'
import scrollFixed from '@/mixin/scroll-fixed'
import { getBanner, homePage } from '@/api/loginapi'
    export default {
      name: 'home',
      mixins: [scrollFixed],

      data () {
        return {
          bannerList: [],
          isLoading: false,
          homepage: []
        }
      },

      created () {
        this.initViews()
        getBanner().then(res => {
          console.log(res)
          this.bannerList = res.data
        })

        homePage().then(res => {
          console.log(11111)
          console.log(res)
          this.homepage = res.data[0].ThreeData
        })
        // this.shopInfos = [{
        //   banner: [{
        //     url: '../../assets/images/head1.png'
        //   }]
        // }]
      },
      methods: {
        changeTabbar (o) {
          // goodsCategory({id: o.id}).then(res => {
          //   let categoryId = res.data.data.currentCategory.id;
          //   this.$router.replace({
          //     name: 'category',
          //     query: {itemClass: categoryId}
          //   })
          // })
        },
        initViews () {
        },
        // 进入任务页面
        toTask (val) {
          this.$router.push({
            name: 'getTask',
            query: {
              activeIndex: val
            }
          })
        }
      },
      components: {
        [Row.name]: Row,
        [Col.name]: Col,
        [Card.name]: Card,
        [Toast.name]: Toast,
        [CouponCell.name]: CouponCell,
        [CouponList.name]: CouponList,
        [Search.name]: Search,
        [Panel.name]: Panel,
        [List.name]: List,
        [Swipe.name]: Swipe,
        [SwipeItem.name]: SwipeItem,
        [Tabbar.name]: Tabbar,
        [TabbarItem.name]: TabbarItem,
        [Tag.name]: Tag,
        [Grid.name]: Grid,
        [GridItem.name]: GridItem,
        [NoticeBar.name]: NoticeBar
      }
    }
</script>

<style scoped lang="scss">
  @import '../../assets/scss/mixin';
  .order_status {
    background-color: #fff;
    text-align: center;
    padding: 10px 0;
    font-size: 12px;
    margin-top: 10px;

  > div {
  @include one-border;
  &::after {
     top: 50%;
     left: 50%;
     border-bottom: 0;
     border-right: 1px solid gray;
     height: 150%;
     transform: scale(0.5) translate3d(-50%, -50%, 0);
     transform-origin: 0 0;
   }
  &:last-child::after {
     border: 0;
   }
  }

  .order_status_icon {
    position: relative;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: inline-block;
  i {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate3d(-50%, -50%, 0);
    font-size: 24px;
    /*color: #000;*/
  }
  }
  }
.taskRow {
  background: #ffffff;
  text-align: center;
  font-size: 18px;
  height: 9vh;
  line-height: 9vh;
  margin-top: 10px;
}
.iconBg {
  font-size: 22px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
}
.bg {
  width: 100%;
  height: 140px;
  height: 24vh;
  /*background: url(../../assets/images/head1.png) no-repeat;*/
  background-size: 100% 24vh;
  font-size: 12px;
}
</style>
