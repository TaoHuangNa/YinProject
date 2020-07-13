<template>
  <div class="order_list" style="margin-top: 44px;">
    <van-tabs v-model="activeIndex"
              :swipe-threshold="5"
              @click="handleTabClick">
      <van-tab v-for="(tabTitle, index) in tabTitles"
               fixed
               :title="tabTitle"
               :key="index">
        <!--<template #title> <van-icon class="iconfont icon-chepai"/>&emsp;{{ tabTitle }} </template>-->
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
             <van-col span="18">
               编号: {{ task.tasks_id }} <span class="title" v-show="isShow">会员任务</span>
             </van-col>
             <van-col span="6" style="text-align: end;">
               <span style="color: red;">￥{{ task.complete_cost}}</span>
             </van-col>
           </van-row>
            <van-divider style="margin: 6px 0;" />
            <van-row style="background: #FFFFFF; height: 9vh; padding: 0 10px;">
              <van-col span="18">
                <div style="display: flex;">
                  <van-image :src="require('../../../assets/images/dy.png')" />
                  <div style="display: flex; flex-direction: column;margin-left: 8px; justify-content: center;">
                    <span style="font-size: 14px;">要求: {{ task.tasks_name }}</span>
                    <span style="font-size: 14px; color: red;">剩余: {{ task.target_times-task.completed_times }}</span>
                  </div>
                </div>
              </van-col>
              <van-col span="6" style="text-align: end; margin-top: 7px;">
                <van-button type="primary" size="small" @click="toOrderDetail(task)">领取</van-button>
              </van-col>
            </van-row>
          </van-row>
          <!--<van-panel v-for="(task, i) in taskList"-->
                     <!--:key="i"-->
                     <!--:title="'编号: ' + task.num"-->
                     <!--:status="task.yuan"-->
                     <!--@click.native="toOrderDetail(task.id)">-->
          <!--</van-panel>-->
        </van-list>
      </van-tab>
    </van-tabs>
  </div>
</template>

<script>
import { Tab, Tabs, Panel, Card, List, Tag, Row, Col, Image, Divider, Button } from 'vant'
import { getTasks } from '@/api/loginapi'
export default {
  name: 'getTask',

  props: {
    active: {
      type: [String, Number],
      default: 0
    }
  },
  created () {
    this.activeIndex = this.$route.query.activeIndex
    if (this.activeIndex === 0) {
      this.isShow = false
    } else {
      this.isShow = true
    }
    this.init()
  },
  data () {
    return {
      activeIndex: Number(this.active),
      tabTitles: ['普通任务', '会员任务'],
      taskList: [],
      page: 0,
      limit: 10,
      loading: false,
      finished: false,
      isShow: false
    }
  },

  methods: {
    init () {
      this.page = 0
      this.taskList = []
      this.getOrderList()
    },
    getOrderList () {
      if (this.activeIndex === 0) {
        this.isShow = false
      } else {
        this.isShow = true
      }
      this.page++
      let data = {
        page: this.page,
        pageSize: this.limit,
        type: this.activeIndex
      }
      getTasks(data).then(res => {
        this.taskList = [...this.taskList, ...res.data.results]
        this.loading = false
        if (res.data.next === null) {
          this.finished = true
        } else {
          this.finished = false
        }
      })
      // orderList({
      //   showType: this.activeIndex,
      //   page: this.page,
      //   limit: this.limit
      // }).then(res => {
      //   this.orderList.push(...res.data.data.list);
      //   this.loading = false;
      //   this.finished = res.data.data.page >= res.data.data.pages;
      // });
    },
    confirmOrder (id) {
      // this.$dialog
      //   .confirm({
      //     message: '请确认收到货物, 确认收货后无法撤销!'
      //   })
      //   .then(() => {
      //     orderConfirm({ orderId: id }).then(() => {
      //       this.init();
      //       this.$toast('已确认收货');
      //     });
      //   })
      //   .catch(() => {});
    },
    commentOrder (id) {},
    toPay (id) {
      this.$router.push({ name: 'payment', params: { orderId: id } })
    },
    handleTabClick () {
      this.page = 0
      this.taskList = []
      this.getOrderList()
    },
    // 领取请求
    toOrderDetail (task) {
      this.$router.replace({
        name: 'pickTask',
        query: {
          task: task
        }
      })
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
</style>
