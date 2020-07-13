<template>
  <div>
    <van-row class="home-top">
      <van-row class="home-top-base">
        <van-col span="6" class="base-logo"></van-col>
        <van-col span="15" class="base-nick">
          <div>{{this.userdata.username}}</div>
          <div>{{this.userdata.name}}</div>
        </van-col>
        <van-col span="3" style="margin-top: 15px;text-align: end;">
          <router-link :to="{name: 'setting'}"><van-icon name="set" style="font-size: 20px;" /></router-link>
          <!--<van-icon class="iconfont icon-feiji" style="font-size: 20px;"/>-->
        </van-col>
      </van-row>
      <van-row class="home-top-acc">
        <div class="acc-lave">账户余额：<span style="color: #c51f1fab;">{{this.userdata.balance}}</span><van-button type="primary" style="float: right;" size="mini" @click="toOrderDetail(task.tasks_id)">提现</van-button></div>
        <van-row class="acc-list">
          <van-col span="6">
            <div style="text-align: center; color: #f1bd01;font-size: 12px;">{{this.userdata.task_reward}}</div>
            <div style="font-size: 12px; text-align: center;">任务奖励</div>
          </van-col>
          <van-col span="6">
            <div style="text-align: center; color: #f1bd01;font-size: 12px;">{{this.userdata.commission}}</div>
            <div style="font-size: 12px; text-align: center;">套餐提成</div>
          </van-col>
          <van-col span="6">
            <div style="text-align: center; color: #f1bd01;font-size: 12px;">{{this.userdata.team_income}}</div>
            <div style="font-size: 12px; text-align: center;">团队收益</div>
          </van-col>
          <van-col span="6">
            <div style="text-align: center; color: #f1bd01;font-size: 12px;">{{this.userdata.balance_today}}</div>
            <div style="font-size: 12px; text-align: center;">今日收益</div>
          </van-col>
        </van-row>
      </van-row>
    </van-row>
    <van-row class="home-top-acc" style="margin: 20px; border-radius: 10px; background: #f6b806; height: 100px;">
      <van-col span="12" style="color: #ffffff" @click="toTask(0)">
        <div style="text-align: center; font-size: 12px;">普通任务</div>
        <div style="text-align: center; font-size: 22px;">{{this.userdata.common_task_complete}}/{{this.userdata.common_task_num}}</div>
        <div style="text-align: center; font-size: 12px;">今日已做/今日可做</div>
      </van-col>
      <div style="position: absolute;
    left: 50%;
    width: 1px;
    height: 60px;
    background: #ffffff;
    top: 20px;"></div>
      <van-col span="12" style="color: #ffffff" @click="toTask(1)">
        <div style="text-align: center; font-size: 12px;">会员任务</div>
        <div style="text-align: center; font-size: 22px;">{{this.userdata.member_task_complete}}/{{this.userdata.member_task_num}}</div>
        <div style="text-align: center; font-size: 12px;">今日已做/今日可做</div>
      </van-col>
    </van-row>
    <div class="user_module">
      <van-cell-group>
        <van-cell icon="shoucang" title="提现记录" to="/withdraw" isLink/>
        <van-cell icon="dingwei" title="资金明细" to="/fundDetail" isLink/>
        <van-cell icon="kefu" title="我的邀请码" to="/myInvitation" isLink/>
        <van-cell icon="kefu" title="我的团队" to="/myTeam" isLink/>
      </van-cell-group>
    </div>
    <div class="user_module" style="margin: 10px 0;">
      <van-cell-group>
        <van-cell icon="shoucang" title="我的任务" to="/myTask" isLink/>
        <van-cell icon="dingwei" title="开通会员" to="/member" isLink/>
        <van-cell icon="kefu" title="联系客服" to="/conttactCustomer" isLink/>
      </van-cell-group>
    </div>
  </div>
</template>

<script>
import { Tab, Tabs, Panel, Card, List, Tag, Row, Col, Image, Divider, Button } from 'vant'
import { grtUser } from '@/api/loginapi'
import { getLocalStorage } from '@/utils/local-storage'

export default {
    name: 'user',
    components: {
      [Tab.name]: Tab,
      [Tabs.name]: Tabs,
      [Panel.name]: Panel,
      [Card.name]: Card,
      [List.name]: List,
      [Tag.name]: Tag,
      [Row.name]: Row,
      [Col.name]: Col,
      [Image.name]: Image,
      [Divider.name]: Divider,
      [Button.name]: Button
    },
  data () {
    return {
      userdata: []
    }
  },
  created () {
    let data = {
      user: getLocalStorage(['username']).username
    }
    console.log(getLocalStorage('username'))
    grtUser(data).then(res => {
      console.log(res)
      this.userdata = res.data[0]
    })
  },
    methods: {
      // 进入任务页面
      toTask (val) {
        this.$router.push({
          name: 'getTask',
          query: {
            activeIndex: val
          }
        })
      }
    }
}
</script>

<style scoped>
  .home-top {
    padding: 30px 20px;
    overflow: hidden;
    border-bottom-left-radius: 500px 50px;
    border-bottom-right-radius: 500px 50px;
    background: #ffffff;
    position: relative;
    z-index: 1;
    height: 200px;
  }
  .home-top-base {
    position: relative;
    overflow: hidden;
    margin-bottom: 20px;
    padding: 0 15px;
  }
  .home-top-base >.base-logo {
    width: 50px;
    height: 50px;
    background: url(../../assets/images/defaultLogo.png);
    background-size: 100% 100%;
    float: left;
  }
  .home-top-base >.base-nick {
    font-size: 14px;
  }
  .home-top-base >.base-nick {
    float: left;
    padding-left: 15px;
    margin-top: 8px;
  }
  .base-edit {
    position: absolute;
    right: 54px;
    font-size: 24px;
    top: 10px;
    padding: 0 6px;
  }
  .base-set {
    position: absolute;
    right: 9px;
    font-size: 24px;
    top: 10px;
    padding: 0 6px;
  }
  .home-top-acc {
    background: #e4ede3;
    padding: 20px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    position: relative;
    height: 130px;
  }
  .acc-list {
    display: flex;
    margin-top: 15px;
  }
  .acc-list a {
    display: block;
    flex: auto;
    text-align: center;
    font-size: 12px;
  }
  .acc-list a span {
    display: block;
    font-size: 18px;
    color: #F37B1D;
  }
  .user_module {
    background-color: #fff;
  }
  .van-icon {
    font-size: 20px;
  }
</style>
