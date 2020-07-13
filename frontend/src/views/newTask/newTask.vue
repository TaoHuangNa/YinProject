<template>
  <div style="margin-top: 50px;">
    <van-form @submit="onSubmit">
      <van-field
        v-model="url"
        rows="5"
        autosize
        label="视频地址"
        type="textarea"
        placeholder="复制需要做任务的视频链接黏贴此处"
        show-word-limit
        :rules="[{ required: true, message: '请输入链接' }]"
      />
      <van-field
        readonly
        v-model="target_times"
        label="目标次数"
        type="text"
        placeholder="请选择"
        @click="showPicker = true"
        :rules="[{ required: true, message: '选择目标次数' }]"
      />
      <van-field
        v-model="type"
        label="任务要求"
        placeholder="请输入"
        :rules="[{ required: true, message: '请选择任务要求' }]"
      />
      <van-field
        v-model="price"
        label="出价"
        placeholder="请输入"
        @keyup.native="priveChange"
        :rules="[{ required: true, message: '请输入单条价格' }]"
      />
      <van-field
        readonly
        v-model="total_cost"
        autosize
        label="费用总计"
        placeholder="自动计算"
        show-word-limit
      />
      <div style="margin: 16px;">
        <van-button block type="info" native-type="submit">
          确定提交
        </van-button>
      </div>
    </van-form>
    <van-popup v-model="showPicker" position="bottom">
      <van-picker
        show-toolbar
        :columns="columns"
        value-key="text"
        @confirm="onConfirm"
        @cancel="showPicker = false"
      />
    </van-popup>
    <van-popup v-model="showPicker1" position="bottom">
      <van-picker
        show-toolbar
        :columns="columns1"
        value-key="type"
        @confirm="onConfirm1"
        @cancel="showPicker1 = false"
      />
    </van-popup>
  </div>
</template>

<script>
import { Form, Field, Picker, Popup, Button } from 'vant'
import field from '@/components/field/'
import fieldGroup from '@/components/field-group/'
import { sumbitTasks } from '@/api/loginapi'
export default {
    name: 'newTask',
    data () {
      return {
        url: '',
        target_times: '',
        total_cost: '',
        price: '',
        type: '',
        num: 0,
        complete_price: '',
        columns: [{
          num: 10,
          text: '10次'
        }, {
          num: 500,
          text: '500次'
        }, {
          num: 1000,
          text: '1000次'
        }, {
          num: 2000,
          text: '2000次'
        }, {
          num: 5000,
          text: '5000次'
        }],
        columns1: [],
        showPicker: false,
        showPicker1: false
      }
    },
  // created () {
  //   getTasksType().then(res => {
  //     this.columns1 = res.data.results
  //   })
  // },
    methods: {
      onConfirm (value) {
        this.target_times = value.text
        this.num = Number(value.num)
        this.showPicker = false
        this.costSum()
      },
      priveChange () {
        if (this.num !== 0 && this.price !== '') {
          this.total_cost = this.num * Number(this.price)
        }
      },
      costSum () {
        if (this.num !== 0 && this.price !== '') {
          this.total_cost = this.num * Number(this.price)
        }
      },
      onSubmit () {
        let data = {
          url: this.url,
          target_times: parseInt(this.target_times),
          // target_times:this.target_times,
          total_cost: this.total_cost,
          tasks_name: this.type,
          cost: this.price,
          complete_cost: this.price * 0.5
        }
        sumbitTasks(data).then(res => {
          this.$router.push({
            name: 'payMent',
            query: {
              tasks_id: res.data.tasks_id,
              total_cost: this.total_cost
            }
          })
        })
      }
    },
    components: {
      [Form.name]: Form,
      [Field.name]: Field,
      [field.name]: field,
      [fieldGroup.name]: fieldGroup,
      [Picker.name]: Picker,
      [Popup.name]: Popup,
      [Button.name]: Button
    }
}
</script>

<style scoped>

</style>
