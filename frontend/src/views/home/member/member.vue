<template>
    <div class="order_list" style="margin-top: 44px;">
        <van-row class="taskRow"
                 v-for="(member, i) in memberList"
                 :key="i"
        >
          <van-row style="background: #FFFFFF; font-size: 18px; height: 5vh; line-height: 5vh; font-weight: 700; padding: 0 10px;">
            <van-col span="18">
             {{ member.memberName }}
            </van-col>
            <van-col span="6" style="text-align: end;">
              <span style="color: red;">￥{{ member.cost}}</span>
            </van-col>
          </van-row>
          <van-divider style="margin: 6px 0;" />
          <van-row style="background: #FFFFFF; height: 9vh; padding: 0 10px;">
            <van-col span="18">
              <div style="display: flex;">
                <div style="display: flex; flex-direction: column;margin-left: 8px; justify-content: center;">
                  <span style="font-size: 14px;">开通期限: 12个月</span>
                  <span style="font-size: 14px; color: red;">每日可做任务: {{ member.number }}次</span>
                </div>
              </div>
            </van-col>
            <van-col span="6" style="text-align: end; margin-top: 7px;">
              <van-button type="primary" size="small" @click="getMember(member)">开通会员</van-button>
            </van-col>
          </van-row>
        </van-row>
    </div>
</template>

<script>
import { Tab, Tabs, Panel, Card, List, Tag, Row, Col, Image, Divider, Button, Dialog } from 'vant'
export default {
  name: 'member',
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
      memberList: [],
      page: 0,
      limit: 10,
      loading: false,
      finished: false
    }
  },
  created () {
    this.memberList = [{
      memberName: '青铜',
      cost: '200',
      time: '12个月',
      number: '2'
    }, {
      memberName: '白金',
      cost: '400',
      time: '12个月',
      number: '4'
    }, {
      memberName: '砖石',
      cost: '600',
      time: '12个月',
      number: '6'
    }]
  },
  methods: {
    // 获取会员信息
    getMemberList () {
    },
    // 开通会员
    getMember (values) {
      Dialog.confirm({
        title: '温馨提示',
        message: '是否开通会员'
      })
        .then(() => {
          // on confirm
        })
        .catch(() => {
          // on cancel
        })
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

