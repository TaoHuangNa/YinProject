<template>
  <div class="order_list" style="margin-top: 44px;">
    <van-list v-model="loading"
              :finished="finished"
              :immediate-check="false"
              finished-text="没有更多了"
              @load="getTeamList">
      <van-row class="taskRow"
               v-for="(team, i) in teamList"
               :key="i"
      >
        <van-row style="background: #FFFFFF; font-size: 18px; height: 5vh; line-height: 5vh; font-weight: 500; padding: 0 10px; margin-top: 10px;">
          <van-col span="18">
            {{ team.name }}
          </van-col>
          <van-col span="6" style="text-align: end;">
            <span style="color: red;">{{ team.member_level }}</span>
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
</template>

<script>
import { Tab, Tabs, Panel, Card, List, Tag, Row, Col, Image, Divider, Button } from 'vant'
import { myTeam } from '@/api/loginapi'
export default {
  name: 'myTeam',
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
      teamList: [],
      page: 0,
      limit: 10,
      loading: false,
      finished: false
    }
  },
  created () {
    this.teamList = []
    this.loading = false
    this.finished = true
    this.page++
    let data = {
      page: this.page,
      pageSize: this.limit
    }
    myTeam(data).then(res => {
      console.log(res)
      this.teamList = [...this.teamList, ...res.data.results]
      this.loading = false
      if (res.data.next === null) {
        this.finished = true
      } else {
        this.finished = false
      }
    })
  },
  methods: {
    // getTeamList () {
    //   this.loading = false
    //   this.finished = true
    //   this.page++
    //   let data = {
    //     page: this.page,
    //     pageSize: this.limit
    //   }
    //   myTeam(data).then(res => {
    //     this.teamList = [...this.teamList, ...res.data.results]
    //     this.loading = false
    //     if (res.next === null) {
    //       this.finished = true
    //     } else {
    //       this.finished = false
    //     }
    //   })
    // }
  }
}
</script>

<style scoped>

</style>
