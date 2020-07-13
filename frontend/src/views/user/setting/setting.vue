<template>
  <div style="margin-top: 44px;">
    <van-cell-group style="margin-top: 10px;">
<!--      <van-cell icon="shoucang" title="修改支付密码" is-link @click="isPayPassword = true" />-->
      <van-cell icon="dingwei" title="修改收款支付宝账号" is-link @click="changePayAccount = true"/>
<!--      <van-cell icon="kefu" title="重置支付密码" is-link @click="findPayAccount = true"/>-->
      <van-cell icon="kefu" title="修改密码" is-link @click="changePassWord = true"/>
      <van-cell icon="kefu" title="退出登录" @click="isExit"/>
    </van-cell-group>
<!--    <van-popup-->
<!--      v-model="isPayPassword"-->
<!--      closeable-->
<!--      position="bottom"-->
<!--      :style="{ height: '40%' }"-->
<!--    >-->
<!--      <van-form @submit="submitPayPassword">-->
<!--        <van-field-->
<!--          v-model="oldPayPassword"-->
<!--          type="password"-->
<!--          name="oldPayPassword"-->
<!--          placeholder="请输入原支付密码"-->
<!--          :rules="[{ required: true, message: '请输入原支付密码' }]"-->
<!--        />-->
<!--        <van-field-->
<!--          v-model="newPayPassword"-->
<!--          type="password"-->
<!--          name="newPayPassword"-->
<!--          placeholder="请输入新支付密码"-->
<!--          :rules="[{ required: true, message: '请输入新支付密码' }]"-->
<!--        />-->
<!--        <van-field-->
<!--          v-model="aginPayPassword"-->
<!--          type="password"-->
<!--          name="aginPayPassword"-->
<!--          placeholder="请再次输入新支付密码"-->
<!--          :rules="[{ required: true, message: '请再次输入新支付密码' }]"-->
<!--        />-->
<!--        <div style="margin: 16px;">-->
<!--          <van-button block type="info" native-type="submit">-->
<!--            确定修改-->
<!--          </van-button>-->
<!--        </div>-->
<!--      </van-form>-->
<!--    </van-popup>-->
    <van-popup
      v-model="changePayAccount"
      closeable
      position="bottom"
      :style="{ height: '50%' }"
    >
      <van-form @submit="submitAccount">
<!--        <van-field-->
<!--          v-model="payPassword"-->
<!--          name="payPassword"-->
<!--          placeholder="请输入支付密码"-->
<!--          :rules="[{ required: true, message: '请输入支付密码' }]"-->
<!--        />-->
        <van-field
          v-model="accountName"
          name="accountName"
          placeholder="请输入新的收款支付宝真实姓名"
          :rules="[{ required: true, message: '请输入新的收款支付宝真实姓名' }]"
        />
        <van-field
          v-model="newAccount"
          name="newAccount"
          placeholder="请输入新的收款支付宝账号"
          :rules="[{ required: true, message: '请输入新的收款支付宝账号' }]"
        />
        <van-field
          v-model="aginAccount"
          name="aginAccount"
          placeholder="请再次输入支付宝账号"
          :rules="[{ required: true, message: '请再次输入支付宝账号' }]"
        />
        <div style="margin: 16px;">
          <van-button block type="info" native-type="submit">
            确定修改
          </van-button>
        </div>
      </van-form>
    </van-popup>
    <!--<van-popup
      v-model="findPayAccount"
      closeable
      position="bottom"
      :style="{ height: '40%' }"
    >
      <van-form @submit="submitFunPayPassword">
        <van-field
          v-model="loginPassword"
          type="password"
          name="loginPassword"
          placeholder="请输入账号登录密码"
          :rules="[{ required: true, message: '请输入账号登录密码' }]"
        />
        <van-field
          v-model="newPayPassword"
          type="password"
          name="newPayPassword"
          placeholder="请输入新支付密码"
          :rules="[{ required: true, message: '请输入新支付密码' }]"
        />
        <van-field
          v-model="aginPayPassword"
          type="password"
          name="aginPayPassword"
          placeholder="请再次输入新支付密码"
          :rules="[{ required: true, message: '请再次输入新支付密码' }]"
        />
        <div style="margin: 16px;">
          <van-button block type="info" native-type="submit">
            确定修改
          </van-button>
        </div>
      </van-form>
    </van-popup>-->
    <van-popup
      v-model="changePassWord"
      closeable
      position="bottom"
      :style="{ height: '40%' }"
    >
      <van-form @submit="changePassword">
        <van-field
          v-model="loginPassword"
          type="password"
          name="loginPassword"
          placeholder="请输入原密码"
          :rules="[{ required: true, message: '请输入原密码' }]"
        />
        <van-field
          v-model="newPassword"
          type="password"
          name="newPassword"
          placeholder="请输入新密码"
          :rules="[{ required: true, message: '请输入新支付密码' }]"
        />
        <van-field
          v-model="aginPassword"
          type="password"
          name="aginPassword"
          placeholder="请再次新密码"
          :rules="[{ required: true, message: '请再次新密码' }]"
        />
        <div style="margin: 16px;">
          <van-button block type="info" native-type="submit">
            确定修改
          </van-button>
        </div>
      </van-form>
    </van-popup>
  </div>
</template>

<script>
import { Form, Field, Popup, Button, Dialog, Notify } from 'vant'
import { updatePassword, updateZFB } from '@/api/loginapi'
import { getLocalStorage } from '@/utils/local-storage'
export default {
    name: 'setting',
    components: {
      [Form.name]: Form,
      [Field.name]: Field,
      [Popup.name]: Popup,
      [Button.name]: Button,
      Dialog,
      Notify
    },
    data () {
      return {
        isPayPassword: false,
        changePayAccount: false,
        findPayAccount: false,
        changePassWord: false,
        oldPayPassword: '',
        newPayPassword: '',
        aginPayPassword: '',
        payPassword: '',
        accountName: '',
        newAccount: '',
        aginAccount: '',
        loginPassword: '',
        newPassword: '',
        aginPassword: ''
      }
    },
    methods: {
      // 修改支付密码
      submitPayPassword (values) {
        if (values.newPayPassword !== values.aginPayPassword) {
          Notify({ type: 'warning', message: '两次输入的密码不一致，请修改' })
          return
        }
        console.log((values))
        this.newPayPassword = ''
        this.aginPayPassword = ''
        this.oldPayPassword = ''
      },
      // 修改收款支付宝账号
      submitAccount (values) {
        if (values.newAccount !== values.aginAccount) {
          Notify({ type: 'warning', message: '两次输入的支付宝账号不一致，请修改' })
          return
        }
        console.log(values)
        let data = {
          username: getLocalStorage(['username']).username,
          ZFB_account: values.newAccount,
          // target_times:this.target_times,
          ZFB_name: values.accountName
        }
        updateZFB(data).then(res => {
          console.log(res)
        })
        this.newAccount = ''
        this.aginAccount = ''
        this.payPassword = ''
        this.accountName = ''
      },
      // 找回支付密码
      submitFunPayPassword (values) {
        if (values.newPayPassword !== values.aginPayPassword) {
          Notify({ type: 'warning', message: '两次输入了支付密码不一致，请修改' })
          return
        }
        console.log(values)
        this.loginPassword = ''
        this.newPayPassword = ''
        this.aginPayPassword = ''
      },
      // 修改登录密码
      changePassword (values) {
        if (values.newPassword !== values.aginPassword) {
          Notify({ type: 'warning', message: '两次输入了支付密码不一致，请修改' })
          return
        }
        console.log(values)
        let data = {
          username: getLocalStorage(['username']).username,
          old_password: values.loginPassword,
          // target_times:this.target_times,
          password: values.newPassword
        }
        updatePassword(data).then(res => {
          console.log(res)
        })
        this.loginPassword = ''
        this.newPassword = ''
        this.aginPassword = ''
      },
      // 退出登录
      isExit () {
        Dialog.confirm({
          title: '温馨提示',
          message: '是否退出登录'
        })
          .then(() => {
            window.localStorage.removeItem('Authorization')
            window.localStorage.removeItem('username')
            this.$router.push({ name: 'home' })
          })
          .catch(() => {
            // on cancel
          })
      }
    }
}
</script>

<style scoped>

</style>
