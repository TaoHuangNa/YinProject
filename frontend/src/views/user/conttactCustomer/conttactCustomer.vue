<template>
    <div style="margin-top: 44px">
      <van-row style="margin: 5px;">
        <van-field
          v-model="content"
          rows="5"
          autosize
          type="textarea"
          placeholder="请输入您的问题或建议,字数4-300间"
        />
      </van-row>
      <van-row style="text-align: center; margin-top: 10px;">
        <van-button type="info" @click="submit" style="width: 90%;">确定提交</van-button>
      </van-row>
      <van-list v-model="loading"
                :finished="finished"
                :immediate-check="false"
                finished-text="没有更多了"
                style="padding: 5px; padding-right: 10px;"
                @load="getContentList">
        <van-row class="taskRow"
                 v-for="(content, i) in contentList"
                 :key="i"
        >
          <van-row style="background: #FFFFFF; padding: 5px; margin-top: 10px;">
            <div>{{ content.time }} &emsp; 我留言:</div>
            <div>{{ content.content }}</div>
            <van-divider style="margin: 6px 0;" />
            <van-row style="background: #FFFFFF; padding: 5px;">
              <span v-if="content.reply == '' || content.reply == null" style="color: #ff0000;">等待客服回复</span>
              <span v-else>回复：{{ content.reply }}</span>
            </van-row>
          </van-row>
        </van-row>
      </van-list>
    </div>
</template>

<script>
import { Field, Button, Tab, Tabs, Panel, Card, List, Tag, Row, Col, Divider, Dialog, Notify } from 'vant'
export default {
    name: 'conttactCustomer',
    components: {
      [Field.name]: Field,
      [Button.name]: Button,
      [Tab.name]: Tab,
      [Tabs.name]: Tabs,
      [Panel.name]: Panel,
      [Card.name]: Card,
      [List.name]: List,
      [Tag.name]: Tag,
      [Row.name]: Row,
      [Col.name]: Col,
      [Divider.name]: Divider,
      Dialog,
      Notify
    },
    data () {
      return {
        content: '',
        contentList: [],
        page: 0,
        limit: 10,
        loading: false,
        finished: false
      }
    },
    created () {
      this.contentList = [{
        time: '2020-07-01 11:30',
        content: '我靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠酷酷酷酷酷酷酷酷酷酷喀什酱豆腐就是领导了离开洒家的看法斯科拉大家分厘卡时间附件',
        reply: '您好，绿卡就是的附件两款手机了咖啡碱撒的开发靠捡垃圾的法律框架撒旦看风景啊十大科技绿卡觉得分厘卡收到发'
      }, {
        time: '2020-07-01 11:30',
        content: '我靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠靠酷酷酷酷酷酷酷酷酷酷喀什酱豆腐就是领导了离开洒家的看法斯科拉大家分厘卡时间附件',
        reply: ''
      }]
    },
    methods: {
      // 提交按钮
      submit () {
        if (this.content === '') {
          Notify({ type: 'warning', message: '请输入您的问题或建议' })
          return
        } else if (this.content.length < 4) {
          Notify({ type: 'warning', message: '输入内容过少' })
          return
        }
        Dialog.alert({
          message: '提交成功，请耐心等待客服回复'
        }).then(() => {
          this.content = ''
        })
      },
      // 获取留言信息数据
      getContentList () {
        this.page++
        this.finished = true
        // let data = {
        //   page: this.page,
        //   pageSize: this.limit
        // }
        // getMoneyRecord(data).then(res => {
        //   this.taskList = [...this.taskList, ...res.data.results]
        //   this.loading = false
        //   if (res.data.next === null) {
        //     this.finished = true
        //   } else {
        //     this.finished = false
        //   }
        // })
      }
    }
}
</script>

<style scoped>

</style>
