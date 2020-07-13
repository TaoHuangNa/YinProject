<template>
  <div class="order_list">
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
                  finished-text="没有更多了(系统将自动删除上个月数据)"
                  @load="getOrderList">
          <van-row class="taskRow"
                   v-for="(task, i) in taskList"
                   :key="i"
          >
            <van-row style="background: #FFFFFF; font-size: 18px; height: 5vh; line-height: 5vh; font-weight: 700; padding: 0 10px;">
              <van-col span="18">
                编号: {{ task.execute_id }} <span class="title" v-show="task.tasks_id.type !== '0'">会员任务</span>
              </van-col>
              <van-col span="6" style="text-align: end;">
                <span style="color: red;">￥{{ task.price }}</span>
              </van-col>
            </van-row>
            <van-divider style="margin: 6px 0;" />
            <van-row style="background: #FFFFFF; height: 9vh; padding: 0 10px;">
              <!--<van-col span="10">-->
                <div style="display: flex;">
                  <van-image :src="require('../../assets/images/dy.png')" />
                  <div style="display: flex; flex-direction: column;margin-left: 8px; justify-content: center;">
                    <span style="font-size: 14px;">要求: {{ task.tasks_id.tasks_name }}</span>
                    <span style="font-size: 14px; color: #07c160;">状态: {{ tabTitle }}</span>
                  </div>
                </div>
              <!--</van-col>-->
              <!--<van-col span="14" style="text-align: end; margin-top: 7px;">-->
                <!--<van-button type="primary" size="small" @click="toOrderDetail(task.tasks_id)">领取</van-button>-->
                <!--<span class="title1">审核时间28分钟前</span>-->
              <!--</van-col>-->
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
import { getTasksSelfComplete } from '@/api/loginapi'
import { getLocalStorage } from '@/utils/local-storage'
export default {
  name: 'task',

  props: {
    active: {
      type: [String, Number],
      default: 0
    }
  },
  created () {
    // this.activeIndex = this.$route.query.activeIndex
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
      tabTitles: ['待审核', '已驳回', '已完成'],
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
        state: this.activeIndex,
        complete_user: getLocalStorage(['username']).username
      }
      console.log(getLocalStorage('username'))
      getTasksSelfComplete(data).then(res => {
        // if (this.taskList.length === 0) {
        //   this.taskList = res.data.results
        // } else {
        //   this.taskList.push(res.data.results)
        // }
        // this.taskList.push(res.data.results)
        // this.taskList = JSON.parse(JSON.stringify(this.taskList))
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
