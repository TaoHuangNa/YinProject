<template>
  <div>
    <van-nav-bar title="我的任务" left-text="返回" left-arrow @click-left="goBack" right-text="新增" @click-right="handleAdd" fixed />
      <!--<template #right>-->
        <!--<div @click="handleAdd"><van-icon name="add" size="18" /></div>-->
      <!--</template>-->
    <!--</van-nav-bar>-->
    <div class="order_list" style="margin-top: 44px;">
      <van-list v-model="loading"
                :finished="finished"
                :immediate-check="false"
                finished-text="没有更多了"
                @load="getTaskList">
        <van-row class="taskRow"
                 v-for="(task, i) in taskList"
                 :key="i"
        >
          <van-row style="background: #FFFFFF; font-size: 18px; height: 5vh; line-height: 5vh; font-weight: 700; padding: 0 10px;">
            <van-col span="18">
              编号: {{ task.tasks_id }} <span style="color: red;">&emsp;￥{{ task.total_cost }}</span>
            </van-col>
            <van-col span="6" style="text-align: end;">
              <span style="color: #07c160;">{{ task.state }}</span>
            </van-col>
          </van-row>
          <van-divider style="margin: 6px 0;" />
          <van-row style="background: #FFFFFF; height: 9vh; padding: 0 10px;">
            <van-col span="18">
              <div style="display: flex;">
                <van-image :src="require('../../../assets/images/dy.png')" />
                <div style="display: flex; flex-direction: column;margin-left: 8px; justify-content: center;">
                  <span style="font-size: 14px;">要求: {{ task.tasks_name }}</span>
                  <span style="font-size: 14px; color: red;">目标: {{ task.target_times }} &emsp;剩余: {{ task.target_times - task.completed_times }}</span>
                </div>
              </div>
            </van-col>
            <van-col span="6" style="text-align: end;">
              <van-button type="primary" size="small" style="height: 20px;" v-show="task.state == '未支付'" @click="handlePay(task)">支付</van-button>
<!--              <van-button type="primary" size="small" style="height: 20px;" v-show="task.state == '未支付'" @click="handleDelete(task)">删除</van-button>-->
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
    </div>
  </div>
</template>

<script>
import { Tab, Tabs, Panel, Card, List, Tag, Row, Col, Image, Divider, Button, NavBar, Dialog } from 'vant'
import { myTasks, deleteMyTasks } from '@/api/loginapi'
export default {
  name: 'myTask',
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
    [Button.name]: Button,
    [NavBar.name]: NavBar,
    Dialog
  },
  data () {
    return {
      page: 0,
      limit: 10,
      loading: false,
      finished: false,
      taskList: []
    }
  },
  created () {
    this.taskList = [
    ]
    this.loading = false
    this.finished = true
    this.page++
    let data = {
      page: this.page,
      pageSize: this.limit
    }
    myTasks(data).then(res => {
      console.log(res)
      this.taskList = [...this.taskList, ...res.data.results]
      this.loading = false
      if (res.data.next === null) {
        this.finished = true
      } else {
        this.finished = false
      }
    })
  },
  methods: {
    goBack () {
      this.$router.back(-1)
    },
    // 跳转到新增页面
    handleAdd () {
      this.$router.push({name: 'newTask'})
    },
    getTaskList () {
      this.page++
      this.finished = true
    },
    // 删除任务
    handleDelete (values) {
      console.log(values)
      Dialog.confirm({
        title: '温馨提示',
        message: '删除后将无法恢复，确定要执行吗'
      })
      let data = {
        tasks_id: values.tasks_id,
        state: '5'
      }
      deleteMyTasks(data).then(() => {
          // on confirm
        })
        .catch(() => {
          // on cancel
        })
    },
    // 付钱
    handlePay (values) {
      this.$router.push({
        name: 'payMent',
        query: {
          tasks_id: values.tasks_id,
          total_cost: values.total_cost
        }
      })
      console.log(values)
    }
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
</style>
