<template>
    <div style="margin-top: 44px;">
      <van-form style="margin-top: 20px; margin: 10px;">
        <van-field
          readonly
          label="收款方账号"
          v-model="account"
          name="account"
        />
        <van-field
          readonly
          label="收款方姓名"
          v-model="accountName"
          name="accountName"
        />
        <van-field
          readonly
          label="转账金额"
          v-model="muchMoney"
          name="muchMoney"
        />
        <van-field
          v-model="payAccount"
          name="payAccount"
          label="付款账号"
          placeholder="请输入付款账号"
        />
        <van-field
          v-model="payName"
          name="payName"
          label="付款人姓名"
          placeholder="请输入付款人姓名"
        />
      </van-form>
      <div style="margin: 10px;">转账凭证(请使用支付宝转账)</div>
      <div style="margin: 10px; background: #FFFFFF; padding-bottom: 10px;">
        <van-uploader upload-icon="camera_full"
                      accept="image/png, image/jpeg"
                      :max-size="3 * 1024 * 1024"
                      :after-read="afterRead"
                      v-model="fileList"
                      multiple
                      :max-count="3"
                      style="margin: 10px 0 0 10px;"
        />
      </div>
      <div style="margin: 16px;">
        <van-button block type="info" @click="copy" style="margin-top: 10px;">
          复制收款账号
        </van-button>
        <van-button block type="info" @click="handleSumbit" style="margin-top: 10px;">
          确定提交
        </van-button>
      </div>
    </div>
</template>

<script>
import { Form, Field, Popup, Button, Dialog, Notify, Uploader, Toast } from 'vant'
import { submitImage, Transfer } from '@/api/loginapi'
export default {
  name: 'payMent',
  components: {
    [Form.name]: Form,
    [Field.name]: Field,
    [Popup.name]: Popup,
    [Uploader.name]: Uploader,
    [Button.name]: Button,
    Dialog,
    Notify
  },
  data () {
    return {
      account: '18179768000',
      accountName: '邱斌',
      muchMoney: '',
      payAccount: '',
      tasks_id: '',
      payName: '',
      payType: '',
      fileList: [],
      imageList: []
    }
  },
  created () {
    console.log(this.$route.query)
    this.muchMoney = this.$route.query.total_cost
    this.tasks_id = this.$route.query.tasks_id
  },
  methods: {
    handleSumbit () {
      let data = {
        money: this.muchMoney,
        cheques_account: this.account,
        cheques_name: this.accountName,
        payment_account: this.payAccount,
        payment_name: this.payName,
        tasks_id: this.tasks_id,
        image: this.imageList
      }
      Transfer(data).then(res => {
        console.log(res)
      })
      Dialog.alert({
        title: '提交成功',
        message: '您的转账已经成功提交，请等待工作人员的审核'
      })
    },
    afterRead (file) {
      // const param = new FormData()
      // param.append('url', file.file)
      // console.log(param)
      const param = new FormData()
      param.append('url', file.file)
      console.log(param)
      console.log(222)
      submitImage(param).then(res => {
        this.imageList.push(res.data.id)
        this.$router.push({name: 'home'})
      })
    },
    copy () {
      let onInput = document.createElement('input')
      onInput.value = this.account
      document.body.appendChild(onInput)
      onInput.select()
      document.execCommand('Copy')
      Toast.success('复制成功')
      onInput.remove()
    }
  }
}
</script>

<style scoped>

</style>
