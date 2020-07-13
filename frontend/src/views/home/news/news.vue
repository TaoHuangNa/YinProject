<template>
  <van-pull-refresh
    style="overflow: auto; margin-top: 44px;"
    success-text="刷新成功"
    v-model="isLoading"
    @refresh="onRefresh">
    <van-list
      v-model="loading"
      :finished="finished"
      finished-text="没有更多了"
      @load="onLoad">
     <van-cell-group v-for="(item, i) in list" :key="i" style="margin: 5px;"  @click="toDetail(item.new_id)">
        <van-cell :title="item.new_title" style="font-size: 20px;font-weight: 700;" isLink>
        </van-cell>
        <div style="font-size: 12px;font-weight: 100;padding: 10px;margin-left: 5px;">&emsp;&emsp;{{ item.new_content }}</div>
      </van-cell-group>
    </van-list>
  </van-pull-refresh>
</template>

<script>
import { Row, Col, PullRefresh, List } from 'vant'
import { getNews } from '@/api/loginapi'
export default {
    name: 'news',
    data () {
    return {
      order: [],
      isLoading: false,
      list: [],
      loading: false,
      finished: false,
      page: 0,
      limit: 10
    }
  },
  methods: {
    toDetail (val) {
      this.$router.push({ name: 'newsDetail', params: { id: val } })
    },
    onRefresh () {
      setTimeout(() => {
        this.isLoading = false
        this.count++
      }, 1000)
    },
    onLoad () {
      this.page++
      let data = {
        page: this.page,
        pageSize: this.limit
      }
      getNews(data).then(res => {
        // if (this.taskList.length === 0) {
        //   this.taskList = res.data.results
        // } else {
        //   this.taskList.push(res.data.results)
        // }
        // this.taskList.push(res.data.results)
        // this.taskList = JSON.parse(JSON.stringify(this.taskList))
        this.list = [...this.list, ...res.data.results]
        this.loading = false
        if (res.data.next === null) {
          this.finished = true
        } else {
          this.finished = false
        }
      })
    }
  },
    components: {
    [Row.name]: Row,
    [Col.name]: Col,
    [PullRefresh.name]: PullRefresh,
    [List.name]: List
    }
}
</script>

<style scoped lang="scss">
  @import '../../../assets/scss/mixin';
  .order_status {
    background-color: #fff;
    text-align: center;
    padding: 10px 0;
    font-size: 12px;

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
        color: #000;
      }
    }
  }
</style>
