<template>
  <div class="order_list" style="margin-top: 44px;">
    <van-tabs v-model="activeIndex"
              :swipe-threshold="5"
              @click="handleTabClick">
      <van-tab v-for="(tabTitle, index) in tabTitles"
               fixed
               :title="tabTitle"
               :key="index">
        <van-list v-model="loading"
                  :finished="finished"
                  :immediate-check="false"
                  finished-text="没有更多了"
                  @load="getOrderList">
          <van-row class="taskRow"
                   v-for="(task, i) in taskList"
                   :key="i"
          >
            <van-row style="background: #FFFFFF; font-size: 18px; height: 5vh; line-height: 5vh; font-weight: 700; padding: 0 10px;">
              提现金额: <span style="color: #db3d3c;">￥{{ task.money }}</span>
            </van-row>
            <van-divider style="margin: 6px 0;" />
            <van-row style="background: #FFFFFF; height: 9vh; padding: 0 10px;">
              <!--<van-col span="10">-->
              <div style="display: flex;">
                <div style="display: flex; flex-direction: column;margin-left: 8px; justify-content: center;">
                  <span style="font-size: 14px;">提交日期: {{ task.add_time }}</span>
                  <span style="font-size: 14px; color: #07c160;">审核状态: {{ tabTitle }}</span>
                </div>
              </div>
            </van-row>
          </van-row>
        </van-list>
      </van-tab>
    </van-tabs>
  </div>
</template>

<script>
import { Tab, Tabs, Panel, Card, List, Tag, Row, Col, Image, Divider, Button } from 'vant'
import { getMoneyRecord } from '@/api/loginapi'
import { getLocalStorage } from '@/utils/local-storage'
export default {
  name: 'withdraw',

  props: {
    active: {
      type: [String, Number],
      default: 0
    }
  },
  created () {
    this.init()
  },
  data () {
    return {
      activeIndex: Number(this.active),
      tabTitles: ['待放款', '已放款', '已驳回'],
      taskList: [],
      page: 0,
      limit: 10,
      loading: false,
      finished: false
    }
  },

  methods: {
    init () {
      this.page = 0
      this.taskList = []
      this.getOrderList()
    },
    getOrderList () {
      this.page++
      let data = {
        page: this.page,
        pageSize: this.limit,
        state: this.activeIndex,
        user: getLocalStorage(['username']).username
      }
      getMoneyRecord(data).then(res => {
        this.taskList = [...this.taskList, ...res.data.results]
        this.loading = false
        if (res.data.next === null) {
          this.finished = true
        } else {
          this.finished = false
        }
      })
    },
    confirmOrder (id) {
    },
    commentOrder (id) {},
    toPay (id) {
      this.$router.push({ name: 'payment', params: { orderId: id } })
    },
    handleTabClick () {
      this.page = 0
      this.taskList = []
      this.getOrderList()
    }
  },
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
  }
}
</script>

<style lang="scss" scoped>
  .order_list {
    .van-panel {
      margin-top: 20px;
    }

    .van-card {
      background-color: #fff;
    }

    .total {
      text-align: right;
      padding: 10px;
    }

    .footer_btn {
      text-align: right;
      .van-button {
        margin-left: 10px;
      }
    }
  }
  .taskRow {
    background: #ffffff;
    font-size: 18px;
    margin-top: 10px;
  }
  .title {
    margin-left: 10px;
    display: inline-block;
    border: 1px solid #f55315;
    color: #f55315;
    font-weight: 100;
    padding: 0 5px;
    font-size: 12px;
    line-height: 16px;
  }
  .title1 {
    margin-left: 10px;
    display: inline-block;
    border: 1px solid #d9dc0b;
    color: #d9dc0b;
    font-weight: 100;
    padding: 0 5px;
    font-size: 12px;
    line-height: 16px;
  }
</style>
