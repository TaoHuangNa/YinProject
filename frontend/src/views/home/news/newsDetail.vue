<template>
  <van-cell-group
    style="margin-top: 44px; background: #FFFFFF; height: 100%;">
    <div style="text-align: center; font-size: 22px; font-weight: 700; padding: 10px;">
      {{ this.new.new_title }}
    </div>
    <van-divider />
    <div style="padding: 10px;">&emsp;&emsp;{{ this.new.new_content }}</div>
  </van-cell-group>
</template>

<script>
import { Cell, CellGroup, Divider } from 'vant'
import { getNewsDetails } from '@/api/loginapi'
export default {
    name: 'newsDetail',
    data () {
      return {
        new: {}
      }
    },
    created () {
      console.log(this.$route.params.id)
      this.page++
      let data = {
        id: this.$route.params.id
      }
      getNewsDetails(data).then(res => {
        // if (this.taskList.length === 0) {
        //   this.taskList = res.data.results
        // } else {
        //   this.taskList.push(res.data.results)
        // }
        // this.taskList.push(res.data.results)
        // this.taskList = JSON.parse(JSON.stringify(this.taskList))
        this.new = res.data
      })
    },
  components: {
    [Cell.name]: Cell,
    [CellGroup.name]: CellGroup,
    [Divider.name]: Divider
  }
}
</script>

<style scoped>

</style>
